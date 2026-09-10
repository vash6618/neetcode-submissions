import json
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + "#" + s)
        return "".join(encoded)
            

    def decode(self, s: str) -> List[str]:
        ind = 0
        ans = []
        curr_num = 0
        while ind < len(s):
            if s[ind] == "#":
                ind += 1
                cnt = 0
                int_str, chr_str = "", []
                while cnt < curr_num:
                    chr_str.append(s[ind])
                    cnt += 1
                    ind += 1
                curr_num = 0
                int_str = "".join(chr_str) if chr_str else int_str
                ans.append(int_str)
            elif s[ind].isdigit():
                curr_num = curr_num * 10 + int(s[ind])
                ind += 1
            else:
                raise Exception("malformed input")
        return ans
