class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0, 0, 0]
        for bill in bills:
            if bill == 5:
                change[0] += 1
            else:
                if bill == 10:
                    change[1] += 1
                else:
                    change[2] += 1
                amtDue = bill - 5
                while amtDue >= 20 and change[2] > 0:
                    amtDue -= 20
                    change[2] -= 1
                while amtDue >= 10 and change[1] > 0:
                    amtDue -= 10
                    change[1] -= 1
                while amtDue >= 5 and change[0] > 0:
                    amtDue -= 5
                    change[0] -= 1
                if amtDue > 0:
                    return False
                

        return True