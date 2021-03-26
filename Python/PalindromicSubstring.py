s="fffacdefgfedcabb"
if (s is None):
    print(None)
else:   
    length = len(s)
    print("lenth is {}".format(length))  

    if (s == s[::-1]):
        print(s)
    else:
        found = False
        i=0
        while (i<=int(length/2) and not found):
            tmp1 = s[:length-i]
            tmp2 = s[i:length]
            tmp3 = s[i:length-i]
            print("{}, {}, {}".format(tmp1, tmp2, tmp3))
            
            if (tmp1 == tmp1[::-1]):
                print(tmp1 + "!!!")
                found=True

            if (tmp2 == tmp2[::-1] and not found):
                print(tmp2+ "!!!")
                found=True
                
            if (tmp3 == tmp3[::-1] and not found):
                print(tmp3+ "!!!")
                found=True

            i=i+1
            print(i)
            print('------------------------')