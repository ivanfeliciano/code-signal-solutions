import json

class Node(object):
    def __init__(self, is_a_complete_word=False):
        self.is_a_complete_word = is_a_complete_word
        self.value = None
        self.references = [None for i in range(52)]
class Trie(object):
    def __init__(self):
        self.root = Node()
        self.alphabet = {
            'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25, 'A' : 26, 'B' : 27, 'C' : 28, 'D' : 29, 'E' : 30, 'F' : 31, 'G' : 32, 'H' : 33, 'I' : 34, 'J' : 35, 'K' : 36, 'L' : 37, 'M' : 38, 'N' : 39, 'O' : 40, 'P' : 41, 'Q' : 42, 'R' : 43, 'S' : 44, 'T' : 45, 'U' : 46, 'V' : 47, 'W' : 48, 'X' : 49, 'Y' : 50, 'Z' : 51
        }
    def is_in_the_trie(self, word):
        current_node = self.root
        n = len(word)
        i = 0
        while current_node != None and i < n:
            char_idx = self.alphabet[word[i]]
            if current_node.references[char_idx] == None:
                return False, None
            if current_node.references[char_idx].is_a_complete_word\
                and i == n - 1:
                return True, current_node.references[char_idx].value
            current_node = current_node.references[char_idx]
            i += 1
        return True, -1
    def add_word(self, word):
        is_a_key, _ = self.is_in_the_trie(word)
        if is_a_key and _ != -1:
            return False
        current_node = self.root
        n = len(word)
        i = 0
        while current_node != None and i < n:
            char_idx = self.alphabet[word[i]]
            if current_node.references[char_idx] == None:
                current_node.references[char_idx] = Node()
            if i == n - 1:
                current_node.references[char_idx].is_a_complete_word = True
                current_node.references[char_idx].value = word
            current_node = current_node.references[char_idx]
            i += 1

def findSubstrings(words, parts):
    ans = []
    mi_trie = Trie()
    for part in parts:
        mi_trie.add_word(part)
    for word in words:
        best_idx = len(word)
        best_part = ""
        i = 0
        start_pos = 0
        last_end_pos = 0
        while i < len(word) and start_pos < len(word):
            is_key, part = mi_trie.is_in_the_trie(word[start_pos: i + 1])
            if not is_key:
                start_pos += 1
                i = start_pos
                continue
            if is_key and part != -1 and len(best_part) < len(part):
                best_idx = start_pos
                #start_pos += 1
                best_part = part
            i += 1
            if part == -1 and i == len(word):
                start_pos += 1
                i = start_pos

        if best_part != "":
            ans.append(word[:best_idx] + "[" + word[best_idx:best_idx + len(best_part)] + "]" + word[best_idx + len(best_part):])
        else:
            ans.append(word)
    return ans

if __name__ == '__main__':
    with open('test-17.json') as json_file:
        data = json.load(json_file)
    words = data['input']['words']
    parts = data['input']['parts']
    ans = findSubstrings(words, parts)
    out = data['output']
    print(ans)
    if ans == data['output']: print("CORRECT")
    for i in range(len(ans)):
        if ans[i] != out[i]: print("{} {}".format(ans[i], out[i]))
