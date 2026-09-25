class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        curr_concat = [""]
        groups = []
        
        i = 0
        while i < len(expression):
            char = expression[i]
            
            if char.isalpha():
                start = i
                while i < len(expression) and expression[i].isalpha():
                    i += 1
                word = expression[start:i]
                curr_concat = [s + word for s in curr_concat]
                continue
                
            elif char == '{':
                stack.append((groups, curr_concat))
                groups, curr_concat = [], [""]
                
            elif char == ',':
                groups.extend(curr_concat)
                curr_concat = [""]
                
            elif char == '}':
                groups.extend(curr_concat)
                group_set = set(groups)
                prev_groups, prev_concat = stack.pop()
                curr_concat = [p + s for p in prev_concat for s in group_set]
                groups = prev_groups
                
            i += 1
            
        groups.extend(curr_concat)
        return sorted(list(set(groups)))