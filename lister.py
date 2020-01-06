#!/usr/bin/env python
"""
reStructuredText 制表工具
Created by sam lee on 2019-10-31
"""

import math
import re
import string

word_int = 2  # 字间距
restructtext = True  # 是否支持结构化文本
split_line = re.compile("\n{3,}")  # 空两行分割
space_re = re.compile("\t+|\s{2,}")
results = []


def matrix_handle(filestring):
	for table in split_line.split(filestring):
		single_table = []
		if table:
			table = table.strip()
			muti_line = table.split("\n")
			for line in muti_line:
				line = line.strip()
				if line:
					rows = space_re.split(line)
					single_table.append(rows)
			results.append(single_table)
	else:
		return results


symbols = ["?", "+", "-", "_", "%", "$", "#", "@", "!", "~", "&", "^", "/", "\\", ",", ".", " ", "\"",
    "(", ")", ":", ";", "|", "“", "”"]
match_single = list(string.ascii_letters + string.digits) + symbols


def print_tabs(result, leftoffset):
	tables_string_list = []
	for table in result:
		fmt_row = ""
		fmt_row_count = []

		# 临时存储表格全部信息
		tmp_table_bucket = []

		# 预先获取每列最大宽度
		table_row_count = [[len(word) for word in line] for line in table]
		max_table_row = list(zip(*table_row_count))
		max_table_row = list(map(lambda row: max(row), max_table_row))

		for index, line in enumerate(table):
			if index == 0:
				# fmt_row = "+" + "+".join([word_int * "-" * len(words) for words in line]) + "+"
				fmt_row = "+" + "+".join([word_int * "-" * row_count for row_count in max_table_row]) + "+"
				fmt_row_count_lt = fmt_row.strip("+").split("+")
				fmt_row_count = [len(item) for item in fmt_row_count_lt]
			# print(fmt_row)  # don't delete

			# if index == 1:
			# 	tmp_table_bucket.append(fmt_row.replace("-", "="))
			# else:
			# 	tmp_table_bucket.append(fmt_row)

			tmp_table_bucket.append(fmt_row)
			real_fmt = []

			for index, words in enumerate(line):
				hans_len = len(list(filter(lambda word: word not in match_single, words)))
				# un_hans_len = len(words) - hans_len
				un_hans_len = len(words) - hans_len
				hans_width = 2 if restructtext else 1.5
				hans_len = int(hans_len * hans_width) if not leftoffset else math.ceil(hans_len * hans_width)
				space_len = fmt_row_count[index] - un_hans_len - hans_len
				real_fmt.append(words + space_len * " ")
			else:
				fmt = "|" + "|".join(real_fmt) + "|"
				# print(fmt)  # don't delete
				tmp_table_bucket.append(fmt)
		else:
			# print(fmt_row)  # don't delete
			tmp_table_bucket.append(fmt_row)
		# print(end="\n")
		tables_string_list.append("\n".join(tmp_table_bucket))
	else:
		print("\n".join(tables_string_list))


def tables_output(filestrings, leftoffset=True):
	"""
	制表函数
	支持从文件读取数据 open(file, encoding="utf-8").read()
	e.g
		表头1\t表头2\t\表头3  # 表1
		a\tb\tc\t
		1  2  3  # \t制表或至少空两个空格
		空两行
		表头1\t表头2\t\表头3  # 表2
		a\tb\tc\t
		1  2  3

		注: 每行开头不要留任何制表符和空格
	:param filestrings: 待打印表格字串
	:param leftoffset: 单元格字符数可能会导致单元格分隔符偏移, 默认左偏移
	:return: 文本样式表格
	"""
	try:
		matrix = matrix_handle(filestrings)
		print_tabs(matrix, leftoffset=leftoffset)
	except IndexError as why:
		print("请按照规定制表")


if __name__ == "__main__":
	tables = \
"""
名称    类型     描述
token   string  授权访问令牌
accesskey   string  设备合法访问的
"""
	tables_output(tables, leftoffset=True)
