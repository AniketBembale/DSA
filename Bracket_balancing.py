def isBalanced(s):
    brackets = {')':'(','}':'{',']':'['}


    stack = []

    for brac in s:

        if brac in brackets.values():
            stack.append(brac)

        elif brac in brackets.keys():
            
            if stack and stack[-1] ==brackets[brac]:
                stack.pop()
            
            else:
                return "No"
        else:
            return "No"
            
    return "Yes" if not stack else "No"


s = "{[()]}"

print(isBalanced(s))





def is_balanced(s):
    brackets = {"}":"{","]":"[",")":"("}

    stack = []

    for brack in s:
        if brack in brackets.values():
            stack.append(brack)
        elif brack in brackets.keys():
            if stack and stack[-1] == brackets[brack]:
                stack.pop()
            else:
                return "No"
        else:
            return "No"
    return "yes" if not stack else "NO"

print(is_balanced(s))




def is_balanced(s):

    brackets  =   {"}":"{","]":"[",")":"("}
    stack  = []

    for brac in s:
        if brac in brackets.values():
            stack.append(brac)
        elif brac  in brackets.keys():
            if stack and stack[-1] == brackets[brac]:
                stack.pop()
            else:
                return "No"
        else:
            return"No"
    return "Yes" if not stack else "No"



print(is_balanced(s))