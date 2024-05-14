myStr = "cloudsek"
substring = "company"
output_string = ""
str_list = myStr.split(substring)
for element in str_list:
    output_string =element[0:5] + substring

print("The input string is:", myStr)
print("The substring is:", substring)
print("The output string is:", output_string)

    str1= i + str1
if(str1==str):
    print("palimdrome")
else:
    print("not palimdrome")
#


# start=0
# last=len(str);
# for start in range(0,len(str)):
#     for last in range(len(str)-1):
#         if(str[start]==str[lasest]):
#             print(str1.join(str[last]))
#             if(str1==str):
#                 print("palimdrom")
#                 break
#             else:
#                 print("not a Palimdrome")



first_str = "Cloudsek"
second_str = "company"
storing_str= ""
sub_string_list= first_str.split(second_str)
for i in sub_string_list:
    output_str = i[0:5] + second_str

print(output_str)
a=len(sub_string_list)
print(a)
print(sub_string_list)

#
# //anagram

my_list= ["cat", "at", "secure","rescue"]
dictionary = {}
for i in my_list:
    reverse_word = i[::-1]
    # print(reverse_word)
    if reverse_word in my_list:
        dictionary[i]=(my_list.pop(my_list.index(reverse_word)))
        print(dictionary)


def anagram_check(str1,str2):
    list1 = list(str1)
    list2 = list(str2)

    list1.sort()
    list2.sort()

    i =0
    match = True

    while i < len(str1) and match:
        if list1[i] == list2[i]:
            i = i+1
        else:
            match = False
    return match

print(anagram_check("secure","rescue"))



# reverse string
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = "Geeksforgeeks"
print(reverse(s))