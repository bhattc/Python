def findNewLine():
    global wordArray;
    wordArray = [];
    wordArray = open("D:/Python/6.00.1x/LineTest.txt").read().splitlines()
    print wordArray;
    findWhite();


def findWhite():
    global wordWhite;
    wordWhite = [];
    for i in wordArray:
        numberWhite = len(i) - len(i.lstrip(' '));
        wordWhite.append(numberWhite);

    print wordWhite;

def findPath():
    path = "";
    total = 0;
    #ext = [".jpeg", ".gif", ".png"];
    for x in range(0,len(wordArray)):
        if(x < (len(wordArray)-1) ):
            
            if (wordWhite[x+1]) > wordWhite[x]:
                path += "/"+wordArray[x].lstrip(' ');
                print path;
                print "here";
                if( ".jpeg" in wordArray[x+1]  or ".gif" in wordArray[x+1] ):
                    print path;
                    total += len(path); 
                    print "substring Found";
                    #print wordArray[x];
                    #print total;
            elif (wordWhite[x+1] < wordWhite[x]):
                diff = wordWhite[x] - wordWhite[x+1];
                #print diff;
                print "Less"
                path = path.rsplit('/', diff)[0];
                print path;
                
                

findNewLine();
findPath();
