import random
import time

class radom_Name():
    character = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','x','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    #获得随机数
    def get_character(length):
            
            radom_character = ''
            random.seed(time.time())
            for i in range(length): 
                radom_character += random.choice(radom_Name.character)
                input_character = '測試方案_' + radom_character
                
            return input_character
    
    def get_params(list1,list2,list3=None):
        combined_list = []
        if list3 == None:
            count = min(len(list1),len(list2))
            for i in range(count):
                param_A = random.choice(list1)
                param_B = random.choice(list2)
                
                combined_list.append((param_A,param_B))
                list1.remove(param_A)
                list2.remove(param_B)
            return combined_list
        else:    
            count = min(len(list1),len(list2),len(list3))
            for i in range(count):
                param_A = random.choice(list1)
                param_B = random.choice(list2)
                param_C = random.choice(list3)
                combined_list.append((param_A,param_B,param_C))
                list1.remove(param_A)
                list2.remove(param_B)
                list3.remove(param_C)
            return combined_list
