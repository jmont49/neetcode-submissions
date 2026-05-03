class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        seen = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token not in operators:
                seen.append(int(token))

            else:
                right = seen[-1]
                seen.pop()
                left = seen[-1]
                seen.pop()

                result = 0

                if token == '+':
                   result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left * right
                else:
                    result = int( left / right)

                seen.append(result)
        
        return seen[0]


            
            


        