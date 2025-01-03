from collections import deque

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []  
        in_block = False  
        buffer = []  

        for line in source:
            i = 0
            while i < len(line):
                if not in_block:
                    if line[i:i + 2] == '//':
                        break
                    elif line[i:i + 2] == '/*':
                        in_block = True
                        i += 1
                    else:
                        buffer.append(line[i])
                else:
                    if line[i:i + 2] == '*/':
                        in_block = False
                        i += 1
                i += 1
            
            if not in_block and buffer:
                res.append(''.join(buffer))
                buffer = []

        return res