#!/usr/bin/env python3

from tables._表 import 表 as _表
import re

class 表(_表):
	def __init__(self):
		self.hzs_to_skip = 'ˉˊˇˋ˙·'
		self.hz_repls = {
			'⿱宀⿰⿱土示又': '㝮',
			'〈忄柬〉': '𱞫',
		}
		self.py_repls = [
			('·(.*)', '\g<1>0'),  # 輕聲
			('ˊ', '2'), ('ˇ', '3'), ('ˋ', '4'), ('˙', '5'),
			('(?<![0-5])$', '1'),

			('(?<=[ㄓㄔㄕㄖ])(?=[0-5]|$)', 'ʅ'),
			('(?<=[ㄗㄘㄙ])(?=[0-5]|$)', 'ɿ'),

			('ㄅ', 'p'), ('ㄆ', 'pʰ'), ('ㄇ', 'm'), ('ㄈ', 'f'), ('ㄪ', 'ʋ'),
			('ㄉ', 't'), ('ㄊ', 'tʰ'), ('ㄋ', 'n'), ('ㄌ', 'l'),
			('ㄍ', 'k'), ('ㄎ', 'kʰ'), ('ㄫ', 'ŋ'), ('ㄏ', 'x'),
			('ㄐ', 'tɕ'), ('ㄑ', 'tɕʰ'), ('ㄬ', 'ȵ'), ('ㄒ', 'ɕ'),
			('ㄓ', 'tʂ'), ('ㄔ', 'tʂʰ'), ('ㄕ', 'ʂ'), ('ㄖ', 'ɻ'),
			('ㄗ', 'ts'), ('ㄘ', 'tsʰ'), ('ㄙ', 's'),

			('ㄧ', 'i'), ('ㄨ', 'u'), ('ㄩ', 'y'), ('ㄦ', 'ɚ'),
			('ㄝ', 'e'), ('ㄜ', 'ə'), ('ㄛ', 'o'),
			('ㄚ', 'a'),
			('ㄟ', 'əi'), ('ㄡ', 'əu'), ('ㄣ', 'ən'), ('ㄥ', 'əŋ'),
			('ㄞ', 'ai'), ('ㄠ', 'au'), ('ㄢ', 'an'), ('ㄤ', 'aŋ'),
			('(?<=[iuy])ə(?=[nŋ])', ''), ('uŋ', 'oŋ'), ('yŋ', 'ioŋ'),
			('(?<=[iy])a(?=n)', 'ɛ'), ('iai', 'iæi'),

			('0', ''),  # 輕聲
		]

	def parse(self, fs):
		if len(fs) < 2: return
		hz, py = fs[:2]
		if hz in self.hzs_to_skip: return
		hz = self.hz_repls.get(hz, hz)
		for pattern, repl in self.py_repls:
			py = re.sub(pattern, repl, py)
		return hz, py
