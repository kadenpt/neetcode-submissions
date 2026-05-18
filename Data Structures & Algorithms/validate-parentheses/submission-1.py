class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in "([{":
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                match p:
                    case "}":
                        if stack[-1] == "{":
                            stack.pop()
                        else:
                            return False
                    case ")":
                        if stack[-1] == "(":
                            stack.pop()
                        else:
                            return False
                    case "]":
                        if stack[-1] == "[":
                            stack.pop()
                        else:
                            return False

        return len(stack) == 0
        