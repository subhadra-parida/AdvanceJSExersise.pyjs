def reverse(str):
    if len(str)==0:
        return ""
    else:
        return (str[len(str)-1])+reverse(str[0:len(str)-1])
str="Subha"
print(reverse(str))




