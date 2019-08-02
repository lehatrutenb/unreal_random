class unreal_random:
    def __init__(self, l, r, nesting):
        self.l = l
        self.r = r
        self.nesting = nesting
        from random import randint as rand
    def un_random(self):
        from random import randint as rand
        randoms = []
        for i in range(self.nesting):
            randoms.append(self.un_random_recursion())
        return randoms[rand(0, len(randoms) - 1)]

    def un_random_recursion(self):
        from random import randint as rand
        randoms = []
        for i in range(rand(1, rand(2, 100000))):
            randoms.append(rand(self.l, self.r))
        return randoms[rand(0, len(randoms) - 1)]

if __name__ == "__main__":
    for i in range(100):
        random = unreal_random(0, 100, 25)
        random_numb = random.un_random()
        print(random_numb)