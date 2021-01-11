"""
Function: 
Coding: utf-8
Author: Sun Yuexin
Date:
"""
match_num = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
have_result = False
match_summary = int(input("Please input a number: "))
for i in match_num:
    for j in match_num:
        for k in match_num:
            if i + j == k:
                if match_num[i] + match_num[j] + match_num[k] + 4 == match_summary:
                    print("%d + %d = %d" % (i, j, k))
                    have_result = True
if not have_result:
    print("No result for %d" % match_summary)