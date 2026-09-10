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
                ans.append(s[ind: ind + curr_num])
                curr_num, ind = 0, ind + curr_num
            elif s[ind].isdigit():
                curr_num = curr_num * 10 + int(s[ind])
                ind += 1
            else:
                raise ValueError("malformed input at {ind}".format(ind))
        return ans
