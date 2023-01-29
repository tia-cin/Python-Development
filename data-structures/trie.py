class Trie:
    def __init__(self):
        self.dic = {}

    def insert(self, word):
        curr = self.dic

        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]

        curr['end'] = {}

    def search(self, word):
        curr = self.dic
        for ch in word:
            if ch in curr:
                curr = curr[ch]
            else: 
                return False
        if 'end' in curr:
            return True
        return False
    
    def start_with(self, prefix):
        curr = self.dic

        for ch in prefix:
            if ch in curr:
                cur = curr[ch]

            else:
                return False
        return True


if __name__ == '__main__':
    obj = Trie() 
    obj.insert("hello") 
    obj.insert("hi") 
    obj.insert("hey") 
    print(obj.dic)
    print(obj.search("hi")) 
    print(obj.start_with("he"))
    print(obj.start_with("heyy")) 