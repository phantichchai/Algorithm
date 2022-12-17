class Solution:
    # 150. Evaluate Reverse Polish Notation
    def evalRPN(self, tokens: List[str]) -> int:
        # check the token has a valid expession
        if len(tokens) < 3:
            return int(tokens[0])

        # create the stack for contain the first term and secound term for wait to operation
        stack = []

        # iterate thourgh the tokens
        for token in tokens:
            # check if token is a opertors then do operation of the value that store in the two top of the stack
            if token in "+-*/":
                # pop value from stack then store in first term
                first = stack.pop()
                # pop value from stack then store in secound term
                secound = stack.pop()
                # create result varible for store result when operation process
                result = 0
                # Do operation addition when token is a '+'
                if token == "+":
                    result = secound + first
                # Do operation subtract when token is a '-'
                elif token == "-":
                    result = secound - first
                # Do operation multiply when token is a '*'
                elif token == "*":
                    result = secound * first
                # Do operation divide when token is a '/'
                elif token == "/":
                    result = secound / first
                # then push the result of the operation to the top of stacl
                stack.append(int(result))
            else:
                # if token is a number then push it on top of the stack
                stack.append(int(token))
        # return the final result
        return stack.pop()
