#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:21:34 2022

@author: romainplt
"""


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


gp=[
["\u16A0",'F','','2'],
["\u16A2",'U','V','3'],
["\u16A6",'TH','','5'],
["\u16A9",'O','','7'],
["\u16B1",'R','','11'],
["\u16B3",'C','K','13'],
["\u16B7",'G','','17'],
["\u16B9",'W','','19'],
["\u16BB",'H','','23'],
["\u16BE",'N','','29'],
["\u16C1",'I','','31'],
["\u16C4",'J','','37'],
["\u16C7",'EO','','41'],
["\u16C8",'P','','43'],
["\u16C9",'X','','47'],
["\u16CB",'S','Z','53'],
["\u16CF",'T','','59'],
["\u16D2",'B','','61'],
["\u16D6",'E','','67'],
["\u16D7",'M','','71'],
["\u16DA",'L','','73'],
["\u16DD",'NG','ING','79'],
["\u16DF",'OE','','83'],
["\u16DE",'D','','89'],
["\u16AA",'A','','97'],
["\u16AB",'AE','','101'],
["\u16A3",'Y','','103'],
["\u16E1",'IA','IO','107'],
["\u16E0",'EA','','109']
]


def encrypt_with_numbers(txt):
    ct = ""
    for i in range(len(txt)):
        if txt[i] not in alphabet and txt[i] not in alphabet.lower():
            pass
        else : 
            for j in gp:
                if txt[i].upper() in j:
                    ct += " " + j[3] + " "
    return ct

def encrypt_with_runes(txt):
    ct = ""
    for i in range(len(txt)):
        if txt[i] not in alphabet and txt[i] not in alphabet.lower():
            ct += " " + txt[i] + " "
        else : 
            for j in gp:
                if txt[i].upper() in j:
                    ct += j[0]
    return ct

def decrypt_numbers(ct):
    pt = ""
    ct = ct.split(" ")
    print(ct)
    for i in range(len(ct)):
        if ct[i] == "":
            pass
        else :
            for j in gp:
                if int(ct[i]) == int(j[3]):
                    pt += j[1]
    return pt






    