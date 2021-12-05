# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:41:20 2018

@author: wave-top
"""

import re

with open ("original_msg.txt", "r") as email:
#    emailStr=myEmail.readlines()
    emailList = email.read()
    emailList = re.sub('[^0-9a-zA-Z]+', ' ', emailList)
    emailList = emailList.split()
    email.close()

    
# emailList = re.sub("[^\w]", " ",  emailStr).split()

print(emailList)
    
list = ['--f403043c4d48e839a20564502461--']
"""
lista = ['1']
listb = ['1', '2', '3', '4', '5', '1']
mergeList = set(lista)&set(listb)
print(len(mergeList))
"""
# p = set(emailStr)&set(list)
# print(len(p))