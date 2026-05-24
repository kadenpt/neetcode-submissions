class MyHashMap:

    def __init__(self):
        self.values = {}

    def put(self, key: int, value: int) -> None:
        if self.values.get(key) != value:
            self.values[key] = value

    def get(self, key: int) -> int:
        if key in self.values:
            return self.values[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        self.values.pop(key, None)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)