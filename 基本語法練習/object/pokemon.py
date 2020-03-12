class Pokemon():
    count=0
    def __init__(self,level,):
        Pokemon.count+=1
        self.level=level
if __name__ == '__main__':
    p1=Pokemon(10)
    p2=Pokemon(100)
    print('pokemon_1_level=%d' % p1.level)
    print('pokemon_2_level=%d' % p2.level)
    print('共有%d隻pokemon' % Pokemon.count)

