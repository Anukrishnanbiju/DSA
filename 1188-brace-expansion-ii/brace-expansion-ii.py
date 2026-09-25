class Solution:
    def braceExpansionII(self, expression):
        def parse(s):
            res = [set()]
            cur = {""}
            i = 0

            while i < len(s):
                if s[i] == '{':
                    j = i + 1
                    count = 1

                    while count:
                        if s[j] == '{':
                            count += 1
                        elif s[j] == '}':
                            count -= 1
                        j += 1

                    part = parse(s[i + 1:j - 1])
                    cur = {a + b for a in cur for b in part}
                    i = j

                elif s[i] == ',':
                    res.append(cur)
                    cur = {""}
                    i += 1

                else:
                    cur = {x + s[i] for x in cur}
                    i += 1

            res.append(cur)

            ans = set()
            for x in res:
                ans |= x

            return ans

        return sorted(parse(expression))