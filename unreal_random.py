class unreal_random:
    def __init__(self, l, r, nesting):
        self.l = l
        self.r = r
        self.nesting = nesting
    def un_random(self):
        from random import randint as rand
        randoms = []
        for i in range(self.nesting):
            randoms.append(self.un_random_recursion())
        return randoms[rand(0, len(randoms) - 1)]

    def un_random_recursion(self):
        from random import randint as rand
        from random import uniform as unif
        randoms = []
        for i in range(rand(1, rand(2, 100000))):
            if(rand(0, 1) == 0):
                randoms.append(rand(self.l, self.r))
            else:
                s = str(unif(self.l, self.r))
                randoms.append(s[rand(1, abs(s.find('.') - len(s)) - 1)])
        return randoms[rand(0, len(randoms) - 1)]

if __name__ == "__main__":
    for i in range(100):
        random = unreal_random(0, 100, 100)
        random_numb = random.un_random()
        print(random_numb)
