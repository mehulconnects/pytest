# # import pytest
# #
# # @pytest.mark.parametrize("num,result",[(1,11),(2,22),(3,35),(4,44),(5,55)])
# # def calculate(num,result):
# #     assert 11*num == result
# #
# def getfinallist():
#     finallist = []
#     listleng = int(input("How long list you want? : "))
#     for i in range(0,listleng):
#         number = input("Enter the numbers : ")
#         finallist.append(int(number))
#     print("The final list is {}".format(finallist))
#     return finallist
#
# def restructurelist(finallistresult):
#     newlist = []
#     for i in range(0,len(finallistresult)):
#         maxvalue = max(finallistresult[i+1:len(finallistresult)], default=-1)
#         newlist.append(maxvalue)
#     print(newlist)
#
# finallistresult = getfinallist()
# restructurelist(finallistresult)


# Python3 code to demonstrate working of
# Words Frequency in String Shorthands
# Using dictionary comprehension + count() + split()

# OrgList = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
# x = 110
#
# strings = "masbd kakjh kjhsd oh laksd"
# print(strings.())
# print(OrgList.index(x))

a= {"a":12,"b":3,"c":4}
print(type(a))
print(*a)