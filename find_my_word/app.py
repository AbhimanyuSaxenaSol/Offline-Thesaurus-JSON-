import time
import json
import difflib
from difflib import get_close_matches
with open('data.jsonl', 'r') as file:    
    temp=file.read()
data= [json.loads(jline) for jline in temp.splitlines()]  #convert jsonl data to json
wordlist=[i['word'] for i in data]
index=set(wordlist)                                       #our dataset can contain multiple values for a single word this why we made an index. Making an index will also reduce the searchtimes as index is much smaller than whole of json data  
errmsg='This word was not found in the system. Are you sure you typed the correct word?'
def find(word):
    memory=[]
    if word in index:
        for i in data:
            if request == i['word']:
                memory.append(i)    
        return memory    
    else :
        return 0              
def similar(word):
    lst = get_close_matches(word,index)
    if len(lst)==0: return 0
    else: return lst

def ui(info):
    n=len(info)
    output=str(n)+' word/s found in the database\n'
    i=0 
    for value in info:
        syn='/ '.join(value['synonyms']) 
        i=i+1
       
        add=f"{i}. {value['word']} is a {value['pos']},it has synonym/s :{syn}\n"
        output=output+add
    return output

print('Hello User!....Welcome to find my word app')
time.sleep(2)
print('This app lets you find out things about your word')
time.sleep(2)
request=''

while True:
    request = input('Enter the word you want to search for: ').lower()
    if request=='/quit':
        break
    else:
        search=find(request)
        if search==0:
            match=similar(request)
            if match==0:
                print(errmsg)
            else:
                request=match[0]
                print("This word was not found in the system but was similar to:"+ ' /'.join(match))
                reply=input("Enter Y if you want find out about '"+match[0]+"' N to search for another word :")
                if reply.upper()=='Y':
                    new_list=find(match[0])
                    print(ui(new_list))
                elif reply.upper()=='N':
                    continue
                else: print('Sorry I did not understand.')   


        
        else: 
            print(ui(search))      
        
                

               
       
            
    time.sleep(1)    
