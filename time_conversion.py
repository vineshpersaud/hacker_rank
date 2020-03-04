def timeConversion(s):
    if s[8:] == 'PM' and int(s[:2]) < 12 :
        return(str(int(s[0:2])+12)+s[2:-2])
    elif s[:2] == '12' and s[8:] != 'PM' :
        return ('00'+s[2:-2])
    else :
        return(s[0:-2])