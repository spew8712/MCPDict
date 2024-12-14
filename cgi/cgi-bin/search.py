#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys, re, os
reload(sys)
sys.setdefaultencoding('utf-8')

import xml.etree.ElementTree as ET
cur = os.path.abspath(os.path.dirname(__file__))
xmlname = os.path.join(cur, "strings.xml")
tree = ET.parse(xmlname)
root = tree.getroot()
def getStrings(name):
	l = root.findall("string-array[@name='%s']/*" % name)
	return [i.text for i in l]

def getString(name):
	l = root.findall("string[@name='%s']" % name)[0]
	return l.text

HZ = "漢字"

import sqlite3
dbname = os.path.join(cur, 'mcpdict.db')
conn = sqlite3.connect(dbname)
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute("SELECT * FROM info")
result = c.fetchall()
#SEARCH_AS_NAMES,COLORS,DICT_NAMES,DICT_LINKS,INTROS,TONE_NAMES = map(dict, result)
KEYS = [i["簡稱"].encode() for i in result]
KEYS_READING = [i["簡稱"].encode() for i in result if i["音節數"]]
KEYS_Y = ("說文", "康熙", "漢大", "匯纂")

LANGUAGES = {i["簡稱"].encode():i["語言"] for i in result}
COLORS = {i["簡稱"].encode():i["地圖集二顏色"] for i in result}

def formatIntro(i):
	s = ""
	if i["簡稱"].encode() == HZ:
		for k in ("版本","字數","說明"):
			if i[k]:
				s += "%s：%s<br/>" % (k, i[k])
		# if s: s += "<br/>"
		# if i["說明"]:
		# 	s += i["說明"]	
	else:
		for k in ("地點","經緯度", "作者", "錄入人", "維護人","來源", "參考文獻","文件名","版本","字數","□數", "音節數","不帶調音節數"):
			if i[k]:
				s += "%s：%s<br/>" % (k, i[k])
		if s: s += "<br/>"
		if i["說明"]:
			s += i["說明"]
	return s

INTROS = {i["簡稱"].encode():formatIntro(i) for i in result}

import cgitb
cgitb.enable()

import cgi
print("Content-type: text/html; charset=UTF-8\n")
form = cgi.FieldStorage()
lang = form.getvalue("lang", HZ)
orgLang = lang
charset = form.getvalue("charset", HZ)
variant = form.getvalue("variant", False)
filter = form.getvalue("filter", "顯示全部")
tone = form.getvalue("tone", 0)
hzs = form.getvalue(HZ, sys.argv[1] if len(sys.argv) == 2 else "")

print("""<html lang=ko>
<head>
	<title>%s</title>
	<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=1">
	<style>
		@font-face {
			font-family: ipa;
			src: url(/ipa.ttf);
		}
		div {
			display:inline-block;
			align: left;
		}
		.place {
			border: 1px black solid;
			padding: 0 3px;
			border-radius: 5px;
			text-align: center;
			vertical-align: top;
			transform-origin: right;
			font-size: 80%%;
		}
		body {
			font-family: ipa, sans;
		}
		.ipa {
			padding: 0 5px;
		}
		.desc {
			font-size: 70%%;
		}
		.hz {
			font-size: 300%%;
			color: #9D261D;
		}
		.variant {
			color: #808080;
		}
		.y {
			color: #1E90FF;
			margin: 0 5px;
		}
		p {
			margin: 0.2em 0;
		}
		td {
			vertical-align: top;
			align: left;
		}
		ul {
			margin: 1px;
			padding: 0px 6px;
		}
	</style>
</head><body>
"""%getString("app_name"))

def rich(r, k):
	s = r[k]
	if k == "白-沙": return s
	s = s.replace(" ", "")
	s = re.sub(", ?", ", ", s)
	s = s.replace("\n", "<br>")
	s = re.sub("\{(.*?)\}", "<div class=desc>\\1</div>", s)
	s = re.sub("\|(.*?)\|", "<font color='#808080'>\\1</font>", s)
	s = re.sub("\*(.*?)\*", "<b>\\1</b>", s)
	return s

def isHZ(c):
	uni = ord(c[0])
	return (uni >= 0x4E00 and uni <= 0x9FFF)\
		 or uni == 0x25A1\
		 or uni == 0x3007\
		 or (uni >= 0x3400 and uni <= 0x4DBF)\
		 or (uni >= 0x20000 and uni <= 0x2A6DF)\
		 or (uni >= 0x2A700 and uni <= 0x2B73F)\
		 or (uni >= 0x2B740 and uni <= 0x2B81F)\
		 or (uni >= 0x2B820 and uni <= 0x2CEAF)\
		 or (uni >= 0x2CEB0 and uni <= 0x2EBEF)\
		 or (uni >= 0x30000 and uni <= 0x3134F)\
		 or (uni >= 0x31350 and uni <= 0x323AF)\
		 or (uni >= 0x2EBF0 and uni <= 0x2EE5F)\
		 or (uni >= 0xF900 and uni <= 0xFAFF)\
		 or (uni >= 0x2F800 and uni <= 0x2FA1F)

def isUnicode(c):
	return re.match("^(U\\+)?[0-9A-Fa-f]{4,5}$", c) != None

def toUnicode(c):
	c = c.upper()
	if c.startswith("U+"): c = c[2:]
	return unichr(int(c, 16))

def getCharsetSQL():
	sql = ""
	if charset == HZ:
		pass
	elif charset in ("ltc_mc", "sw", "kx", "hd"):
		sql = "AND %s IS NOT NULL" % charset
	else:
		sql = "AND 分類 MATCH '%s'" % charset
	return sql

if hzs:
	hzs = hzs.decode("U8").strip()
else:
	print(INTROS.get(lang, INTROS[HZ]))
	conn.close()
	exit()

if not filter: filter = lang
word = "MATCH"
s = ""
if isUnicode(hzs):
	hzs = toUnicode(hzs)
if isHZ(hzs):
	lang = HZ
if lang == HZ and re.match("[a-zA-Zü]+[0-5?]?", hzs):
	lang = "cmn_"
if lang in KEYS_Y:
	if len(hzs) == 1 and isHZ(hzs):
		lang = HZ
	else:
		word = "LIKE"
		hzs = "%%%s%%" % hzs
if lang != HZ:
	if not isHZ(hzs):
		variant = False
	hzs = (hzs,)

def getKeys(key):
	keys = [key]
	if variant:
		keys.append(HZ)
		keys.append("異體字")
	elif key == "ja_any":
		keys = list(filter(lambda k: k.startswith("ja_"), KEYS))
	return keys

def getSelect(key, value):
	return 'SELECT *,offsets(mcpdict) AS vaIndex FROM mcpdict where (`%s` %s "%s") %s' % (key, word, value, getCharsetSQL())

def getVisibleColumns(filter):
	if filter == "當前語言": return [orgLang]
	if filter == "僅漢字": return []
	return KEYS_READING

regions={
	'och_':'歷史音',
	'ltc_':'歷史音',
	'cmn_':'官話',
	'cmn_xn_':'西南官話',
	'cmn_jh_':'江淮官話',
	'cmn_jil_':'冀魯官話',
	'cmn_zho_':'中原官話',
	'cmn_ly_':'蘭銀官話',
	'cmn_fyd_':'官話方言島',
	'cjy_':'晉語',
	'wuu_':'吳語',
	'czh_':'徽語',
	'gan_':'贛語',
	'hak_':'客語',
	'hsn_':'湘語',
	'yue_':'粵語',
	'csp_':'南部平話',
	'nan_':'閩南語',
	'cdo_':'閩東語',
	'mnp_':'閩北語',
	'xxx_':'土話',
	'wxa_':'鄉話',
	'vi_':'域外方音',
	'ko_':'域外方音',
	'ja_':'域外方音',
}

rks = sorted(regions.keys(),key=lambda k:-k.count('_'))

def getRegion(k):
	for i in rks:
		if k.startswith(i):
			return regions[i]
	return ""

def getRegionDiff(k, last):
	return k.count("-") - last.count("-")

def getColorName(k):
	name = k
	color = COLORS[k]
	fmt = "<font color=%s>%s</font>"
	if "," in color:
		colors = color.split(",")
		m = len(name)//2
		names = name[:m],name[m:]
		s = ""
		for i in range(2):
			s += fmt % (colors[1 - i], names[i])
		return s
	return fmt % (color, name)
for value in hzs:
	sqls = list(map(lambda x: getSelect(x, value), getKeys(lang)))
	sqls = (' UNION '.join(sqls)) + 'ORDER BY vaIndex LIMIT 10'
	for r in c.execute(sqls):
		hz = r[HZ]
		s += "<p><div class=hz>%s</div>"%(hz)
		if hz != value and variant:
			s += "<div class=variant>（%s）</div>"%(value)
		s += "<div class=y>U+%04X</div>" % (ord(hz))
		for k in KEYS_Y:
			if r[k]:
				s += "<div class=y>%s</div>" % (k)
		s += "</div>\n"
		last = ""
		for k in getVisibleColumns(filter):
			if r[k]:
				region = getRegion(k)
				if region != last:
					if last:
						diff = getRegionDiff(region, last)
						if diff <= 0:
							s += "</ul></details>\n" * (1 - diff)
						else:
							n = region.count("-")
							start = 1 if region.startswith(last) else 0
							for i in range(start, n):
								if i == 0:
									s += "</ul></details>\n"
								s += "<details open><summary>%s</summary><ul>"%region.split("-")[i]
					s +="<details open><summary>%s</summary><ul>"%region.rsplit("-", 1)[-1]
					last = region
				color = COLORS[k].split(",")[0]
				s += ("<ul><div class=place style='border:1px %s solid;'>%s</div><div class=ipa>%s</div></ul>"%(color,getColorName(k),rich(r, k)))
		s+="</ul></details>\n"
if not s:
	s = getString("no_matches")
print(s)
conn.close()