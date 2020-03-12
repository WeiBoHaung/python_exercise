import win32com.client

if __name__ == '__main__':
    dm = win32com.client.Dispatch('dm.dmsoft')  # 调用大漠插件
    print(dm.ver())  # 输出版本号
