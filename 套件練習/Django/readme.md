# Django 練習筆記



| 環境 |  | 
| -------- | -------- |
| Pycharm     | Pofessional    | 
| Python     | 3.7.3     | 
| Django     | 3.0.4     | 

 

簡介
---
先來認識一下 Django 的設計模式，也就是 MTV，


* Model : 定義一些資料庫的東西 ( ORM )，這層通常是直接和資料有關。

* Template : 使用者基本上就是看到這層，也就是最後所呈現的 Template ( html )。

* View : 可以將這層看做是中間層，它主要負責 Model 和 Template 之間的業務邏輯。


介紹了 Django 的設計模式，接下來你一定會問，那這有什麼好處 ❓

最直接的好處就是，我們可以很明確且很快速的知道問題在哪裡，例如，今天可能頁面出了問題，
這樣我們就會知道要先去 template 中找問題，而如果是關於資料庫的問題，則可能就要先去 Model

中找，總之，就是不會像一隻無頭蒼蠅一樣不知道要去哪裡找問題☺️

最後簡單將 Django 的 MTV 和 ASP.NET 中的 MVC 比較一下，


| MTV | MVC |
| -------- | -------- |
| Model     | Model     | 
| Template     | View     | 
| View     | Controller     | 


其實可以將 MTV 想成算是 MVC 的變形 😏


教學
---
1. 建立專案Django Project

    建議直接安裝 PyCharm Pofessional，然後新增一個 Django Project
    
    ![](https://i.imgur.com/nW1QDBR.png)
    
    用 PyCharm Pofessional 建立 project 還有一個好處，就是一些設定會先幚你設定好，不用全部重新自己動手設設定。
    
    但是只有 PyCharm Professional 才有這個功能，如果你是安裝一般的 PyCharm Community Edition，則沒有這個選項。

    可以使用以下方法：
    
    在Terminal輸入指令建立專案

        django-admin startproject django_tutorial
    執行Django
    
        python manage.py runserver
2.  建立Django App

    在 Django 中，通常我們會依照 功能 去建議一個 App ， 例如範例的 musics ，代表他是 管理音樂 的部份。

    **請在你的Terminal底下輸入**
    
            python manage.py startapp musics
    執行後，會發現專案底下會先增新資料夾
    ![](https://i.imgur.com/fAH3HQr.png)
    
    **建立完成後在App加入設定檔**
    
    請在settings.py裡面INSTALLED_APPS加入剛剛的APP
    ![](https://i.imgur.com/9wEVWAQ.png)
    
    **在templates新增View**
    
    flask會先到專案資料夾『templates』去尋找相對應的html文件，因此，你需要先做的就是在專案底下建置一個資料夾，並且命名為『templates』。
    ![](https://i.imgur.com/O6VdPDL.png)
    
    請先在 templates 裡面新增一個 hello_django.html，並在裡面輸入下方程式碼：
    ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        {{data}}
    </body>
    ```
    hello_django.html 裡面的{{data}}，只是透過 views.py 傳值過來而已。

    接著我們將views.py裡面新增以下程式碼：
    ```
    from django.shortcuts import render

    # 新增你的view.
    def hello_view(request):
        return render(request,'hello_django.html',{
                'data':"Hello Django",
            })

    ```
    透過flask的render函數渲染模板，因此它需要一個『模板』來提供渲染的格式，flask會先到專案資料夾『templates』去尋找相對應的html文件。
    
    成果如下圖：
    ![](https://i.imgur.com/0bc1hch.png)

    **新增Router**
    
    在 urls.py 裡面增加一上對應路由，如下：
    ![](https://i.imgur.com/a36Vgbt.png)
    
    ```
    from django.contrib import admin
    from django.urls import path
    from musics.views import hello_view

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('hello/',hello_view),
    ]

    ```
    **from musics.views import hello_viewr**將musics資料夾底下的views.py引入
    
    在urlpatterns list中新增路徑path('hello/',hello_view)
    
    

    

