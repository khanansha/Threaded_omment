# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:01:17 2021

@author: Anjum Khan
"""


import re

def formulaExpand(d, text):
    d_key = [*d]
    dict2 = {}
    for key, value in d.items():
        dict2[key] = value
        for dk in d_key:
            if value.find(dk) > -1:
                dict2[key] = value.replace(dk, d[dk])
        rep = dict2
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    return text

d = {"a": "b + 10", "b": "20", "c": "30"} # output: 20 + 10 + 20 + 30 + 42
# Inputs
# d = {"a": "10", "b": "a + 20", "c": "30"} # output: 10 + 10 + 20 + 30 + 42
# d = {"a": "c + 10", "b": "20", "c": "30"} # output: 30 + 10 + 20 + 30 + 42
text = "a + b + c + 42"

formula_get = formulaExpand(d, text)
print(formula_get)