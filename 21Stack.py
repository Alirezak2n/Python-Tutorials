
def solution(a): 
    
    stack = []
    valid = True    
    for c in a:
        if c == "[" or c == "{" or c=="(":
            stack.append(c)
            print(stack)
        elif c == ")":
             valid = False if not stack or stack.pop() != "(" else valid
             #age stack khali bashe ya pop mokhalef un braket bashe false mishe
             print(stack)
        elif c == "}":
            valid = False if not stack or stack.pop() != "{" else valid
            print(stack)
                 
        elif c == "]":
            valid = False if not stack or stack.pop() != "[" else valid
            print(stack)
                 
            
    return 1 if valid and not stack else 0
print(solution("{{([])}}()[]{}()"))       
print(solution("()]]"))       
    