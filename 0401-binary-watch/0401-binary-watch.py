class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res=[]
        def popcount(x):
            return bin(x).count('1')

        for h in range(12):
            for m in range(60):
                if popcount(h)+popcount(m) == turnedOn:
                    time_str = f'{h}:{m:02d}'
                    res.append(time_str)
        return res                    