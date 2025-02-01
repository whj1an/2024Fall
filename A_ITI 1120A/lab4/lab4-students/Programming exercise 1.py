def is_eligible():
    '''
    name -> String
    age -> intage
    citizenship -> String
    prison -> string, only has no will come out True
    '''
    name= input("Please enter your name: ")
    age = int(input("Please enter you age: "))
    citizenship = input("Please enter you citizneship: ").replace(" ","").lower()
    prison = input("Have you ever lived in prison? ").replace(" ","").lower()
    if (age>=18) and (citizenship=="canada" or citizenship=="canadian") and (prison=="no"):
          print(name, ", you are eligible to vote")
    else:
          print(name, ", you are ineligible to vote")
    return
