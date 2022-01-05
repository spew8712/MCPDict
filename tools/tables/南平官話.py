#!/usr/bin/env python3

from tables._縣志 import 字表 as 表

class 字表(表):
	key = "cmn_fyd_npgh"
	note = "更新：2021-10-04<br>來源：<u>清竮塵</u>整理自蘇華《福建南平方言同音字彙》"
	tones = "44 1 1a 陰平 ꜀,21 2 1b 陽平 ꜁,353 3 2 上 ꜂,,35 5 3 去 ꜄,,2 7 4 入 ꜆"
	_file = "南平官话同音字表*.tsv"
	_color = "#FF0000,#FF6600"
	simplified = 2
