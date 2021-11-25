def ambil_tengah (a,b = None):
    if b == None:
        pjg = len(a)
        pembulatan = (round(pjg/2))
        return(a[pembulatan])
    else:
        pjg = len(a)
        pembulatan = (round(pjg/2))
        return (a[pembulatan+b-1])
print(ambil_tengah("abcdefg",1))
print(ambil_tengah("abcdefg",2))
print(ambil_tengah("abcd"))