class Solution:
    def makeLargestSpecial(self, s: str) -> str:

        substrings = []
        start = 0
        height = 0
        for index,value in enumerate(s):
            if value =="1":
                height+=1
            else:
                height-=1
            if height == 0:
                substrings.append(f"1{self.makeLargestSpecial(s[start + 1 :index])}0")
                start = index +1
        substrings.sort(reverse = True)
        return "".join(substrings)             
        