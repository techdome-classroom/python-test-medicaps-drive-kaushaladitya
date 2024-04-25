class Solution(object):
    @staticmethod
    def isValid(s: str) -> bool:
        
        leftSymbols = []
      
        for c in s:
            
            if c in ['(', '{', '[']:
                leftSymbols.append(c)
         
            elif c == ')' and leftSymbols and leftSymbols[-1] == '(':
                leftSymbols.pop()
            elif c == '}' and leftSymbols and leftSymbols[-1] == '{':
                leftSymbols.pop()
            elif c == ']' and leftSymbols and leftSymbols[-1] == '[':
                leftSymbols.pop()
           
            else:
                return False
        return not leftSymbols
