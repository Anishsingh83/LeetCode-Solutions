class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        curr_line = []
        curr_len = 0
        
        for word in words:
            if curr_len + len(word) + len(curr_line) > maxWidth:
                spaces = maxWidth - curr_len
                if len(curr_line) == 1:
                    res.append(curr_line[0] + " " * spaces)
                else:
                    gaps = len(curr_line) - 1
                    space_per_gap = spaces // gaps
                    extra_spaces = spaces % gaps
                    
                    line_str = ""
                    for i in range(gaps):
                        line_str += curr_line[i] + " " * (space_per_gap + (1 if i < extra_spaces else 0))
                    line_str += curr_line[-1]
                    res.append(line_str)
                
                curr_line = []
                curr_len = 0
            
            curr_line.append(word)
            curr_len += len(word)
        
        last_line = " ".join(curr_line)
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res