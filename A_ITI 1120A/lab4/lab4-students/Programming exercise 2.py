def mess(text):
    result = ""
    last_alpha = ("r,s,t,v,w,x,y,z")
    for char in text:
        if char.lower() in last_alpha:
            result += char.upper()
        elif char == " ":
            result += "-"
        else:
            result += char
    return result
