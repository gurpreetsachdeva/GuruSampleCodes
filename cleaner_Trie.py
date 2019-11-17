#Problem Solving : For a bunch words print bad set if anyone is a prefix of anyone
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
array_length=input()
words=[]
output=["BAD SET","GOOD SET"]
for i in range(len(array_length)):
    words.append(input())

class Node:
    def __init__(self):
        self.character_map={}
        self.leaf_node=False
class Trie:
    def __init__(self):
        self.root=Node()
    def insertWord(self,word):
        top_node=self.root
        for ch in word:
            #character not already there, then add , otherwise just iterate
            if(top_node.character_map.get(ch,None)==None):
                top_node.character_map[ch]=Node()
            top_node=top_node.character_map[ch]
        top_node.leaf_node=True
    def insertWords(self,words):
        for w in words:
            self.insertWord(w)
    def prefixString(self,search_word):
        #Returns the count of strings with prefix as search_word
        ##Reach the node where iteration needs to be done 
        top_node=self.root
        ans=[]
        for ch in search_word:
            #character not already there, then add , otherwise just iterate
            if(top_node.character_map.get(ch,None)==None):
                return 0 #directly return zero or len([]) 
            top_node=top_node.character_map[ch]
        ans=self.subtree_iterate(top_node,search_word)
        return len(ans) ## or In Java ans.size() ;)
    def subtree_iterate(self,level_node,search_word):
        ans=[]
        if(level_node.leaf_node==True):
            ans.append(search_word)
        for key,value in level_node.character_map.items():
            ans.extend(self.subtree_iterate(value,search_word+key))
        return ans #Return all the prefix matches , auto_completion ;)
if __name__=='__main__':   
    trie=Trie()

    print(words)
    for word in words:
        print("Starting for word"+word)
        print(trie.prefixString(''))
        print(word +"Searching word"+str(trie.prefixString(word)>0))
        if(trie.prefixString(word)>0):
            print (output[0])
            print(word)
            sys.exit(0)
        trie.insertWord(word)
        
    print(output[1])


