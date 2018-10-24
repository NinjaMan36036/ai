class conversation:
    def __init__(self):
        i = open('input.txt', 'rw+')
        o = open('output.txt', 'rw+')
        print('Starting...')
        while True:
            x = self.IN()
            res = self.scan(i, x)
            if res[1] == False:
                i.write(x + '\n')
                i.write('Responses -\n')
                print('Sorry, that input is not recognized.')
                i.write(input('Please input an appropriate response --> '))
            if res[1] == True:
                
            
            

    def OUT(self):
        pass

    def IN(self):
        return input('--> ')

    def parse(self, file):
        ans = []
        while True:
            temp = file.readline()
            if temp == '':
                break
            ans.append(temp)
        return ans

    def scan(self, file, phrase):
        ans = []
        contains = False
        h = self.parse(file)
        x = 0
        for i in h:
            if h[x] == phrase:
                contains = True
                ans.append(x)
        ans.append(contains)
        return ans
