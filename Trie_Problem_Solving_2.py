#To figure the number of matches , you don't have to iterate, you can keep a value at every node 
# this program supports two operations with Trie 
# Written by Gurpreet
# find abc
# add abc
#!/bin/python3

import os
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
                return 0 #directly return zero or topNode.value
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


#
# Complete the contacts function below.
#
def contacts(queries):
    trie=Trie()
    result=[]
    for q in queries:
        if(q[0]=='add'):
            trie.insertWord(q[1])
        else:
            ans=trie.prefixString(q[1])
            #ans=len(ans)
            result.append(ans)
    return result
    #
    # Write your code here.
    #

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())
    #queries=[['add','guru'],['add','gurpreet'],['find','gur'],['find','guru']]
    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())
    queries=[['add','guru'],['add','gurpreet'],['find','gur'],['find','gurud']]

    result = contacts(queries)

    print('\n'.join(map(str, result)))
    print('\n')

    

