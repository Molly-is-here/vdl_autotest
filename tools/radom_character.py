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
                input_character = '测试發_' + radom_character
                
            return input_character
