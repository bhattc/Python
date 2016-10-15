import operator

def goog(test):
    print test;
    final = [];
    maxi = "";
    a = 0;
    b = 0;
    c = 0;
    a = test.count('a');
    b = test.count('b');
    c = test.count('c');
    
    dict = {'a' : a, 'b' : b, 'c' : c};
    print dict
    for i in dict:
        print i;
        '''
        maxi = max(dict.iteritems(), key = operator.itemgetter(1))[0];
        print maxi;
        final.append(maxi);
        print final
        '''
        dict = {key: value -1 for key, value in dict.item()};
        print dict;
    

goog(['a','a','a', 'b', 'c', 'c']);
