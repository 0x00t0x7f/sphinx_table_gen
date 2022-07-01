# -*- coding:utf-8 -*-

from distutils.core import setup

from setuptools import find_packages

long_desc = \
    """
    # generator_table
    reStructuredText sample table generator

    # Usage
    >>> from sphinx_table_gen import gen
    >>> tables = '''
    ... 名称    类型     描述
    ... token   string  授权访问令牌
    ... '''
    >>> gen(tabels, leftoffset=True)

    使用sphinx api生成的文档中需要内嵌表格时，此脚本就是帮助你生成简单样式表格的工具，希望它对你有用！

    clone项目，编辑 gen_tool.py文件替换其中的tables换成你的制表字符串并执行脚本。

    ps: 每列之间至少需一个制表符或两个空格。
    """

setup(
    name="sphinx_table_gen",
    version="0.0.2",
    description="reStructuredText sample table generator for sphinx.",
    long_description=long_desc,
    author="kuing",
    author_email="samleeforme@gmail.com",
    license="BSD 2-Clause License",
    url="https://github.com/0x00t0x7f/sphinx_table_gen",
    platforms=["any"],
    packages=find_packages(),
    keywords=["Python sphinx", "sphinx", "sphinx table generator", "reStructuredText table generator"]
)
