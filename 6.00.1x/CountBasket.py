import json;

'''
[ 
{ "name" : "apples", 
"baskets" : [10,20,30] 
}, 
{ "name" : "bananas", 
"baskets" : [5,20,10,10] 
} 
]
'''

data =[{ "name" : "apples", "baskets" : [10,20,30] }, { "name" : "bananas", "baskets" : [5,20,10,10] }];

def printOutput(data):
    
    #parsed_data = json.loads(data);
    #print(parsed_data);
    print (data[0]);
    print ("fruit num_baskets num_fruit");
    print("-------------------------------");
    for i in range(len(data)):
        total = 0;
        #print i;
        print(data[i].get('name')),
        print(len(data[i].get('baskets'))),
        for j in range(len(data[i].get('baskets'))):
            
            total += data[i].get('baskets')[j];
        print total;
  
printOutput(data);
