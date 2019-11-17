class Node:
    def __init__(self):
            # Two Choices here , keep an arraylist for 26 chars(which is a natural map a> 0 , b> 1 etc or make it a generic using a map or dict. You can use any character other than alphabet.
            # In Java Terms Map<Character,Node>
            self.children={} #can call it map as well
            self.leaf_node=False

class Trie:
    def __init__(self):
        self.root=Node()
    
    def insert(self,word):
        top_node=self.root
        for i in range(len(word)):
            #if node is not there , insert a new node
            if(top_node.children.get(word[i],None)==None):
                top_node.children[word[i]]=Node()
            top_node=top_node.children[word[i]]
        
        top_node.leaf_node=True
        #print("setting leaf_node =true")
            
    def find(self,word):
        top_node=self.root
        for ch in word:
            if(top_node.children.get(ch,None)==None):
                return False
            else:
                top_node=top_node.children.get(ch,None)
        if top_node!=None and top_node.leaf_node==True:
            return True
    def iterate_subtree(self,trie,current_word):
        ans=[]
        if(trie.leaf_node==True):
            ans.append(current_word+"")
        #print(ans)
        for key,value in trie.children.items():
            ans.extend(self.iterate_subtree(value,current_word+key))
        return ans
    #AutoCompletion or prefixStringSearch, Corrected now #2 commit
    def prefixString(self,word):
        top_node=self.root
        for ch in word:
            if(top_node.children.get(ch,None)==None):
                return []
            else:
                top_node=top_node.children.get(ch,None)
        ans=self.iterate_subtree(top_node,word)
        return ans
           

            
if __name__=='__main__':     
    trie=Trie()      
    words=['abc','efg','abcd']
    for w in words:
        trie.insert(w)

    print(trie.find('abc'))
    print(trie.find('abcde'))
