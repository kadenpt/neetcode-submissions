class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [0]

        for asteroid in asteroids:
            mag = abs(asteroid)
            while True:
                if stack[-1] > 0 and asteroid < 0:
                    if abs(stack[-1]) < mag:
                        stack.pop()
                    elif abs(stack[-1]) == mag:
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(asteroid)
                    break

        return stack[1:]