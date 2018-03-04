#!/usr/bin/env python
"""
Get all function calls from a python file

The MIT License (MIT)
Copyright (c) 2016 Suhas S G <jargnar@gmail.com>
"""
import ast
from collections import deque


class FuncCallVisitor(ast.NodeVisitor):
    def __init__(self):
        self._name = deque()

    @property
    def name(self):
        return '.'.join(self._name)

    @name.deleter
    def name(self):
        self._name.clear()

    def visit_Name(self, node):
        self._name.appendleft(node.id)

    def visit_Attribute(self, node):
        try:
            self._name.appendleft(node.attr)
            self._name.appendleft(node.value.id)
        except AttributeError:
            self.generic_visit(node)


def get_func_calls(tree):
    func_calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            callvisitor = FuncCallVisitor()
            callvisitor.visit(node.func)
            func_calls.append(callvisitor.name)

    return func_calls

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input .py file', required=True)
    args = parser.parse_args()
    tree = ast.parse(open(args.input).read())
    # Print just the method names, not the full namespace
    for call in get_func_calls(tree):
        print(call.split('.')[-1])
