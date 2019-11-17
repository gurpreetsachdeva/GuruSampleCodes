#Problem Solving : For a bunch words print bad set if anyone is a prefix of anyone
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


class Node:
    def __init__(self):
        self.character_map={}
        self.leaf_node=False
        self.value=0
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
            top_node.value+=1
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
        ans=top_node.value
        return ans ## or In Java ans.size() ;)
    def subtree_iterate(self,level_node,search_word):
        ans=[]
        if(level_node.leaf_node==True):
            ans.append(search_word)
        for key,value in level_node.character_map.items():
            ans.extend(self.subtree_iterate(value,search_word+key))
        return ans #Return all the prefix matches , auto_completion ;)
if __name__=='__main__':
    array_length=int(input())
    #print("Array length"+str(array_length))
    words=[]
    output=["BAD SET","GOOD SET"]
    for i in range(array_length):
        words.append(input().rstrip())   
    trie=Trie()
    #words=['aab','aac','aacghgh','aabghgh']
    #print(words)
    for i in range(0,len(words)):
        #print("Inserting "+words[i])
        trie.insertWord(words[i])
        for j in range(0,i+1):
            if trie.prefixString(words[j])>1:
                print(output[0])
                #print("never in break")
                print(words[i])
                sys.exit(0)
                
        
        
    print(output[1])


