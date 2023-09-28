#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Fungsi Penjumlahan
def add (input1, input2) :
    if type(input1) == tuple and type(input2) == tuple:
        return tree(input1) + tree(input2)
    else:
        return input1 + input2


# In[ ]:


#Fungsi Pengurangan
def minus (input1, input2) :
    if type(input1) == tuple and type(input2) == tuple:
        return tree(input1) - tree(input2)
    else:
        return input1 - input2


# In[ ]:


#Fungsi Perkalian
def mult(input1, input2):
    if type(input1) == tuple and type(input2) == tuple:
        return tree(input1) * tree(input2)
    else:
        return input1 * input2


# In[ ]:


#Fungsi Pembagian
def div (input1, input2) :
    if type(input1) == tuple and type(input2) == tuple:
        return tree(input1) / tree(input2)
        return result1 / result2
    else:
        return input1 / input2


# In[ ]:


def tree(node) :
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator =='+':
            return add(left_operand, right_operand)
        elif operator =='-':
            return minus(left_operand, right_operand)
        elif operator =='*':
            return mult(left_operand, right_operand)
        elif operator =='/':
            return div(left_operand, right_operand)


# In[ ]:


#Pohon Ekspresi = (2 + 3) * (5 - 1)
expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))
result = tree(expression_tree)


# In[ ]:


print("Hasil evaluasi pohon ekspresi = ", result)

