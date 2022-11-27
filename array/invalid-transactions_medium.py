"https://leetcode.com/problems/invalid-transactions/description/"

class Solution:
    def invalidTransactions(self, transactions):
        res = []
        rec = []


        for tr in transactions:
            values = tr.split(",")
            values[1] = int(values[1])
            values[2] = int(values[2])
            rec.append(values)
        
        for tr in rec:
            if tr[2] > 1000:
                tr[1] = str(tr[1])
                tr[2] = str(tr[2])
                res.append(",".join(tr))
                continue
            for x in rec:
                if tr[0] == x[0] and abs(int(tr[1]) - int(x[1])) <= 60 and tr[3] != x[3]:
                    tr[1] = str(tr[1])
                    tr[2] = str(tr[2])
                    res.append(",".join(tr))
                    break
        return res





                


                
