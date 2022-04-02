#!/usr/bin/env python3

from tables._表 import 表
import re

class 字表(表):
	key = "xxx_zhuang"
	_file = "壮语汉字音字表*.tsv"
	note = "說明：本字表使用Sawroeg，以武鳴壯語爲主，收集了壯語（包含方言）的漢字音，不區分層次。<br>官話層次的漢字音，去聲字派入陰平24，模仿武鳴官話的去聲24;陰平字派入陽去33，模仿武鳴官話的陰平33。"
	tones = "24 1 1a 陰平 ꜀,31 2 1b 陽平 ꜁,55 3 2a 陰上 ꜂,42 4 2b 陽上 ꜃,35 5 3a 陰去 ꜄,33 6 3b 陽去 ꜅,55 7a 4a 短陰入 ꜆,33 8 4b 陽入 ꜇,35 7b 4c 長陰入 ꜆"
	toneValues = {"24":1, "31":2, "55":3, "42":4, "35":5, "33":6}
	
	def parse(self, fs):
		hz, py, yb, js = fs[:4]
		sy = yb.strip("123450")
		sd = yb[len(sy):]
		if sd in self.toneValues:
			sd = str(self.toneValues[sd])
		else:
			sd = ""
		if sy and sy[-1] in "ptk":
			if sd == "3": sd = "7"
			elif sd == "5": sd = "9"
			elif sd == "6": sd = "8"
		yb = sy + sd
		return hz, yb, js
