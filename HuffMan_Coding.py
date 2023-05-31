#!/usr/bin/env python
# coding: utf-8

# In[39]:


string = input("Enter ANY string")


# In[40]:


class NodeTree(object):
    def __init__(self,left = None, right = None):
        self.left = left
        self.right = right
        
    def children(self):
        return(self.left,self.right)


# In[41]:


## Calculating Frequency

freq = {}
for c in string: 
    if c in freq:
        freq[c] = freq[c]+1
    
    else:
        freq[c] = 1
        
freq = sorted(freq.items(),key = lambda x: x[1],reverse = True)

nodes = freq


# In[42]:


while len(nodes)>1:
    (key1,c1) = nodes[-1]
    (key2,c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1,key2)
    nodes.append((node,c1+c2))
    
    nodes = sorted(nodes,key = lambda x : x[1] , reverse = True)


# In[43]:


def huffman_code_tree(node,left = True , binString=''):
    if type(node) == str:
        return {node : binString}
    (l,r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l,True,binString + '0'))
    d.update(huffman_code_tree(r,False,binString + '1'))
    return d


# In[44]:


huffmanCode = huffman_code_tree(nodes[0][0])
for(char,frequency) in freq:
    print(" %-4r | %12s" %(char,huffmanCode[char]))


# In[ ]:




