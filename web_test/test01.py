import re

def main():
    names=["age","1age","_age","!age","age123","2_age","#aage"]
    for name in names:
        ret=re.match(r"^[a-zA-Z_][a-zA-Z0-9]*$",name)
        if ret:
            print("变量名：%s 符合要求，，，"%name)
        else:
            print("变量名：%s 不符合要求，，，" %name)


if __name__=="__main__":
    main()