class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = {}
        index = 0
        for c in order:
            pos[c] = index
            index += 1

        current = words[0]
        for i in range(1, len(words)):
            for j in range(min(len(current), len(words[i]))):
                if pos.get(current[j]) < pos.get(words[i][j]):
                    break
                elif pos.get(current[j]) > pos.get(words[i][j]):
                    return False
                else:
                    if j == len(words[i]) - 1:
                        return False
            current = words[i]
        return True

