#!/usr/bin/env python3

from tables._表 import 表 as _表
import re

class 表(_表):

	def parse(self, fs):
		name = str(self)
		hz = ""
		yb = ""
		ipa = ""
		js = ""
		if name in ("汝城", "瑞安東山", "新界客家話", "長壽", "宜章巖泉","郴州","樂昌皈塘","尤溪","晉江", "龍門路溪", "詔安", "道縣官話", "重慶", "樂昌三溪", "南安"):
			hz, yb, js = fs[:3]
		elif name in ("通州金沙",):
			yb, hz, js = fs[:3]
		elif name in ("江陰", "江陰新橋", "江陰申港"):
			_, hz, js, yb = fs[:4]
		elif name in ("東方八所",):
			_, hz, sy, sd, js = fs[:5]
			yb = sy + sd
		elif name in ("龍游",):
			_, hz, sm, ym, dz, _, js = fs[:7]
			ipa = sm + ym + dz
		elif name in ("1900梅惠",):
			hz,_,_,yb = fs[:4]
		elif name in ("劍川金華",):
			hz, sy, sd, js = fs[:4]
			yb = sy + sd
		elif name in ("1926綜合",):
			hz,yb,_,_,_,js = fs[:6]
		elif name in ("蒼南錢庫",):
			sm,ym,sd,hz,js = fs[:5]
			if sd == "轻声": sd = "0"
			yb = sm + ym + sd
		elif name in ("1890會城",):
			hz,_,_,sm,ym,js = fs[:6]
			yb = sm + ym
		elif name in ("貴陽",):
			hz, _, _, ipa, js = fs[:6]
		elif name in ("樂淸"):
			_, sm, ym, sd, hz, js = fs[:6]
			yb = sm + ym + sd
		elif name in ("淸末溫州",):
			_,hz,sy,_,_,sd,js = fs[:7]
			yb = sy + sd
		elif name in ("眞如南",):
			_, _, hz, js, sm, ym, sd = fs[:7]
			yb = sm + ym + sd
		#ipa
		elif name in ("五峯", "恩平恩城","台山台城"):
			hz, ipa = fs[:2]
		elif name in ("華安髙安","五華"):
			ipa, hz, js = fs[:3]
		elif name in ("惠來隆江",):
			hz, ipa, js = fs[:3]
		elif name in ("壽寧平溪"):
			hz, yb, js = fs[:3]
			hz = hz.replace("", "□")
		elif name in ("新會會城",):
			hz, _, _, ipa = fs[:4]
		elif name in ("廈門","漳州","饒平", "遵義", "犍爲玉津", "綦江古南", "桐梓婁山關"):
			hz, _, ipa, js = fs[:4]
		elif name in ("遂昌","五華橫陂","蔡家話"):
			hz, sy, sd, js = fs[:4]
			ipa = sy + sd
		elif name in ("開化",):
			hz, js, sm, ym, sd = fs[:5]
			yb = sm + ym + sd.strip("[]")
			if re.match(r"（.*?）", js): js = js[1:-1]
		elif name in ("富陽東梓關","新登城陽"):
			_, hz, js, ipa = fs[:4]
		elif name in ("新登下港",):
			hz, ipa, js = fs[0], fs[6], fs[8]
		elif name in ("嘉善", "上海"):
			hz, sm, ym, sd, js = fs[:5]
			yb = sm + ym + sd
			if hz.endswith("-"):
				hz = hz[:-1]
				yb = yb + "-"
		elif name in ("臨海", "泰順羅陽", "雲和", "仙居"):
			hz, _, sy, sd, js = fs[:5]
			ipa = sy + sd
		elif name in ("松陽",):
			hz, _, sy, sd = fs[:4]
			ipa = sy + sd
		elif name in ("珠海唐家",):
			hz, sm, ym, sd, js = fs[7], fs[12], fs[13], fs[14], fs[18]
			ipa = sm + ym + sd
		elif name in ("江門",):
			hz, sm, ym, sd, jso, js = fs[7], fs[25], fs[26], fs[27], fs[11], fs[12]
			ipa = sm + ym + sd
			if jso: js = jso + "。" + js
			js = js.strip("。")
		elif name in ("江門墟頂","江門白沙","江門水南","江門沙仔尾","江門紫萊"):
			hz, sm, ym, sd, js = fs[0], fs[6], fs[7], fs[4], fs[9]
			yb = sm + ym + sd
		elif name in ("江門禮樂","江門潮連"):
			hz, sm, ym, sd, js = fs[:5]
			ipa = sm + ym + sd
		elif name in ("瑞安湖嶺",):
			_, hz, ipa, _, js = fs[:5]
		elif name in ("湖州",):
			hz, _, ipa, _, js = fs[:5]
		elif name in ("武義",):
			_, hz, _, ipa, js = fs[:5]
		elif name in ("鳳凰-新豐",):
			hz, py, _, ipa, js = fs[:5]
		elif name in ("潮州","汕頭"):
			hz, _, _, ipa, js = fs[:5]
		elif name in ("汕頭市郊"):
			hz, _, _, ipa, js = fs[:5]
		elif name in ("雷州",):
			hz, _, _, _, _, ipa = fs[:6]
			ipa = ipa.replace("˨˨˩", "˨˩")
		elif name in ("長泰",):
			_, sm, ym, sd, hz, js = fs[:6]
			ipa = sm + ym + sd
		elif name in ("普寧",):
			hz,_,js,sm,ym,sd = fs[:6]
			ipa = sm + ym + sd
		elif name in ("中山三鄕",):
			hz,sm,ym,sd, _, js = fs[:6]
			ipa = sm + ym + sd
		elif name in ("深圳南頭",):
			hz, _, _, _, ipa, js = fs[:6]
		elif name in ("通東餘東",):
			hz, _, _, sy, _, sd, js = fs[:7]
			sy = sy.lstrip("ʔ")
			ipa = sy + sd
		elif name in ("南寧", "南寧亭子"):
			_, hz, _, ipa, _, js, c = fs[:7]
			js = c + js
		elif name in ("蒼南蒲門",):
			hz, sy, sd, _, _, _, js = fs[:7]
			ipa = sy + sd
		elif name in ("鶴山雅瑤",):
			hz, sm, ym, sd, _, _, _, js = fs[:8]
			ipa = sm + ym + sd
		elif name in ("開平護龍",):
			hz, sm, ym, sd, js = fs[:5]
			ipa = sm + ym + sd
			yb = self.dz2dl(ipa)
		elif name in ("揭陽",):
			hz, _, _, _, _, ipa, yd, js = fs[:8]
			yb = self.dz2dl(ipa)
			ipa = ""
			yd = yd.strip("(读)")
			if yd == "文": yb+="="
			elif yd == "白": yb+="-"
		elif name in ("台山斗山墟",):
			hz, ipa, js = fs[0], fs[12], fs[13]
		elif name in ("新會天湖",):
			hz, sm, ym, sd, js = fs[0], fs[11], fs[12], fs[13], fs[14]
			ipa = sm + ym + sd
		elif name in ("鶴山沙坪",):
			hz, sm, jy, ym, sd, js = fs[0], fs[8], fs[9], fs[10], fs[11], fs[14]
			l = list()
			for i in ym.split("，"):
				ipa = sm + jy + i + sd
				yb = self.dz2dl(ipa)
				l.append((hz, yb, js))
			return l
		elif name in ("縉雲",):
			hz, _, _, _, _, js, _, ipa = fs[:8]
		elif name in ("深圳西鄕","深圳沙井"):
			hz, _, _, _, _, _, _, ipa, js = fs[:9]
		elif name in ("新晃凳寨",):
			hz,ipa,js = fs[0], fs[9], fs[10]
		elif name in ("如東豐利",):
			hz,_,sy,_,_,_,sd,_,_,js = fs[:10]
			yb = sy + sd
		elif name in ("如東大豫",):
			hz,_,_,_,sd,js,sm,ym,_ = fs[:9]
			yb = sm + ym + sd
		elif name in ("詔安白葉","詔安霞葛"):
			hz, yb, js = fs[:3]
			if " " in yb:
				l = list()
				for y,j in zip(yb.split(" "), js.split(" ")):
					l.append((hz, y, j))
				return l
		elif name in ("陽春河口",):
			hz, sm, ym, sd, js = fs[9], fs[6], fs[7], fs[4].split("\\")[0], fs[10]
			yb = sm + ym + sd
		elif name in ("中山石岐",):
			hz, sm, ym, sd, js = fs[7], fs[12], fs[13], fs[14], fs[18]
			ipa = sm + ym + sd
		elif name in ("上饒沙溪",):
			hz, yb, _, js = fs[:4]
		elif name in ("1818漳州",):
			hz, yb = fs[0], fs[4]
		elif name in ("榮縣",):
			hz,_,_,js,sm,ym,sd = fs[:7]
			if sm in "ø": sm = ""
			l = list()
			for sd in sd.split("或"):
				yb = self.dz2dl(sm + ym, sd)
				l.append((hz, yb, js))
			return l
		elif name in ("鄭張",):
			self.ybTrimSpace = False
			self.isYb = False
			hz = fs[0]
			js = fs[16]
			yb = ("%s%s (%s%s切 %s聲 %s%s)"%(fs[12], f"/{fs[13]}" if fs[13] else "", fs[7],fs[8],fs[9],fs[10],fs[11]))
		elif name in ("白-沙",):
			self.isYb = False
			hz, yb = fs[0], fs[4]
		elif name in ("中唐",):
			self.isYb = False
			hz, yb, js = fs[:3]
		elif name in ("中世朝鮮"):
			self.isYb = False
			hz = fs[0]
			yb = "".join(fs[1:4])
		elif name in ("溫州",):
			toneValues = {'阳入':8,'阴上':3,'阳平':2,'阴入':7,'阳去':6,'阴平':1,'阴去':5,'阳上':4}
			_,hz,_,sy,_,_,sd,js = fs[:8]
			yb = sy + str(toneValues[sd])
		elif name in ("瑞安陶山",):
			hz, sm, ym, sd, js, bz = fs[:6]
			sd = sd.strip("[]")
			yb = sm + ym + sd
			js = (js + " " +bz).strip()
		elif name in ("宜章梅田",):
			hz,sm,ym,sd,js = fs[:5]
			yb = sm + ym + sd
		elif name in ("蒼南宜山",):
			sm,ym,sd,hz,js = fs[:5]
			sd = sd.strip("[]")
			yb = sm + ym + sd
			js = js.strip("{}")
		elif name in ("南通", ):
			hz = fs[1]
			yb = fs[-6] + fs[-4]
			js = fs[-7].strip()
			if len(hz) > 1 and len(js) == 0:
				js = hz[1:].strip()
				hz = hz[0]
		elif name in ("寧德",):
			hz,_,yb,sd,js = fs
			yb += self.dz2dl(sd.split("|")[0])
		elif name in ("江門荷塘(上)","江門荷塘(下)"):
			hz, ipa, js = fs[:3]
		elif name in ("汝城延壽",):
			hz, yb, js = fs[:3]
		elif name in ("建陽連墩",):
			hz, yb, js = fs[:3]
		elif self._file.startswith("粤西闽语方言字表"):
			if len(fs) < 6: return
			hz = fs[0]
			ybs = fs[self.ybIndex]
			ybs = ybs.replace("／", "/")
			if not ybs or ybs.startswith("—"): return
			_js = hz[1:] if len(hz)>1 else ""
			_js = _js.strip("（）")
			hz = hz[0]
			l = list()
			for _yb in ybs.split("/"):
				_yb = _yb.strip()
				c = ""
				if "（" in _yb:
					n = _yb.index("（")
					c = _yb[n:]
					_yb = _yb[:n]
				yb = self.dz2dl(_yb)
				js = c + _js
				if js.startswith("（") and js.endswith("）"):
					js = js[1:-1]
				l.append((hz, yb, js))
			return l
		elif self._file.startswith("鄉話"):
			index = self.ybIndex
			hz, js = fs[:2]
			yb = "".join(fs[index:index+3])
		elif self._file.startswith("丹陽（雲陽訪仙河陽埤城）"):
			hz = fs[0][0]
			if hz.startswith("["): return
			js = fs[0][1:].strip("()（）")
			yb = fs[self.ybIndex]
			yb = self.dz2dl(yb)
		elif self._file.startswith("广西富川富阳方言21点"):
			if not fs[0]: return
			hz = fs[0][0]
			js = fs[0][1:].strip("()（）")
			yb = self.dz2dl(fs[self.ybIndex])
		elif len(fs) >= 4:
			hz, _, ipa, js = fs[:4]
		elif len(fs) == 2:
			hz, yb = fs[:2]
		else:
			hz, yb, js = fs[:3]
		if hz:
			if ipa:
				yb = self.dz2dl(ipa)
			if len(hz) != 1 or not yb: return
			yb = self.normYb(yb)
			if hz in "?？�": hz = "□"
			return hz, yb, js
		return
