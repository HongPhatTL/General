s1 = "abbaaabba"
s2 = "aabbabb"

def longest_common(s1,s2):
    list1 = list(s1)
    list2 = list(s2)
    common =[]
    temp = 0
    #temp_list = []
    # if len(list1) < len(list2): 
    #     temp_list = list2
    #     list2 = list1
    #     list1 = temp_list
    # print(list1,list2)
    for j in range(len(list1)):
        temp_value = list1[j]
        print("j is",j)
        for i in range(temp,len(list2)) :
            if list2[i] == temp_value:
                common.append(temp_value)
                temp = i+1
                print("temp is",temp)
                break
    return common

aa = longest_common(s1,s2)
print(aa)
