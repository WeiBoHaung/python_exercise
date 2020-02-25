class Student():#類別名稱必須大寫()內為父類別
    def __init__(self):#稱之為建構子產生物件時一定會執行
        self.name=''
        self.age=0
        self.chinese=0
if __name__ == '__main__':
    s1=Student();#產生物件
    s1.name='weibo'
    s1.age=50
    s1.chinese=100
print('name=%s ,age=%d chinese=%d' % (s1.name , s1.age ,s1.chinese))