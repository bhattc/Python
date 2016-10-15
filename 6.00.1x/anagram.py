def anagram():
    
    #abc = "abcdefghijklmnopqrstuvwxyz"
    #givenstr = "abcdefghijklmnoPqrstuvwxyz"

    abc = "aaa";
    givenstr = "abc";
    new = givenstr.lower()
    n = 0
    print new;
    for i in abc:
        print i;
        if i not in new:
            print "not anagram"
            break
        else:
            n += 1

    if n == 3:
        print "anagram"
    else:
        print "not anagram";


def is_anagram(s1, s2):
     if s1.lower() == s2.lower():
         return False
     print sorted(s1.lower()) == sorted(s2.lower())

#anagram();
is_anagram("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmonPqrstuvwxyz");


