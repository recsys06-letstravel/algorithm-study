class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(int)

    def put(self, key: int, value: int) -> None:
        self.table[key] = value

    def get(self, key: int) -> int:
        if key in self.table:
            return self.table[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.table:
            self.table.pop(key)
        return -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)