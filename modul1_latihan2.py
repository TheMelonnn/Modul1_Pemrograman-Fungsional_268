#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Inisiasi penyimpanan
temp_data_float = []
data_string = []
data_int = {'satuan' : [], 'puluhan' : [], 'ratusan' : []}

def checkdata (input_list) :
    random_list = input_list
    for data in random_list:
        if type(data) == float:
            temp_data_float.append(data)
        
        elif type(data) == str:
            data_string.append(data)
        
        elif type(data) == int:
            if data / 10 < 1:
                data_int['satuan'].append(data)
            elif data / 100 < 1:
                data_int['puluhan'].append(data)
            elif data /1000 < 1:
                data_int['ratusan'].append(data)
            else:
                print(data, " : Data invalid")
        
        else:
            print(data, " : data invalid")
    
    #Konversi tipe data
    data_float = tuple(temp_data_float)
    
    print("Hasil pemisahan data :")
    print("Data Float : ", (data_float), " dengan tipe data ",type(data_float))
    print("Data String : ", data_string, " dengan tipe data ",type(data_string))
    print("Data Integer : ", data_int,  " dengan tipe data ",type(data_int))


# In[ ]:


random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]
checkdata(random_list)

