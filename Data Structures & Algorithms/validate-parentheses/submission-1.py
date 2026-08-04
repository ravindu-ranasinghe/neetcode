class Solution:
    def isValid(self, s: str) -> bool:
        map = {'(':')', '[':']', '{':'}'}
        #initialize stack
        stack = []

        #add opening characters to stack
        for x in s:
            if x in map:
                stack.append(x)
            #edge case
            elif x in map.values():
                if len(stack) == 0:
                    return False
                #get opening char
                last = stack.pop()

                # check if closing char (value) = to opening char (key)
                if map[last] != x:
                    return False


        # stack will be empty if all pairs are valid
        return len(stack) == 0


        