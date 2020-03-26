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
    
    最後執行 Django ， 然後瀏覽 http://127.0.0.1:8000/hello/
    
1. Models

    定義出資料庫中的結構（schema），並且透過 Django 中的指令去建立資料庫。Django 預設是使用 SQLite ，如果想要修改為其他的資料庫，可以在 settings.py 裡面進行修改。首先，請先在 models.py 裡面增加下方程式碼:
    ```
    from django.db import models


    # Create your models here.
    class Music(models.Model):
        song = models.TextField(default="song")
        singer = models.TextField(default="AKB48")
        last_modify_date = models.DateTimeField(auto_now=True)
        created = models.DateTimeField(auto_now_add=True)

        class Meta:
            db_table = "music"
    ```
    default : 代表默認值，也就是如果你沒有指定的話會用默認值。

    auto_now_add : 新增時會幚你自動加上建立時間。

    auto_now : 資料有更新時會幚你自動加上更新的時間。

    接著在Terminal輸入
    
        python manage.py makemigrations
        python manage.py migrate
    makemigrations ： 會幚你建立一個檔案，去記錄你更新了哪些東西。
    
    migrate ： 根據 makemigrations 建立的檔案，去更新你的 DATABASE 。
    
    輸入完後在pycharm設定database顯示:
    ![](https://i.imgur.com/RbIHzH3.png)
    選擇專案底下的db.sqlite3
    ![](https://i.imgur.com/WUbtPQk.png)
    注意：如黃色匡區域有看請點擊下載缺少套件
    設定後完成如下：
    
    會出現剛剛建立的資料表
    ![](https://i.imgur.com/2uCA3dv.png)

    **Django ORM**
    
    [Django QuerySet API](https://docs.djangoproject.com/en/1.10/ref/models/querysets/) 可以讓你簡單的處理 CRUD 。
    
    直接使用 Python Console ：
   
    首先必須先 import 你的 models
            
        from musics.models import Music

    **Create**
    
        Music.objects.create(song='song1', singer='testsinger')
        
    **Read**
        
        Music.objects.all()
        or
        Music.objects.get(pk=1)
        or
        Music.objects.filter(id=1)

    **Update**

        data=Music.objects.filter(id=1)
        data.update(song='song_update')

    **Delete**

        data=Music.objects.filter(id=4)
        data.delete()
        
1. Admin Site

    Django 內建有後台管理介面。

    請先確定 settings.py 裡的 INSTALLED_APPS 裡有 django.contrib.admin    
    ![](https://i.imgur.com/FHWhb1l.png)

    設定路由
    ![](https://i.imgur.com/lxyTBx5.png)
    
    接著使用Terminal建立帳號
        
        python manage.py createsuperuser
        
    需要輸入帳號、信箱、密碼
        
    **註冊 model**
    
    我們可以註冊 model，讓後台可以操作 database
    請在 admin.py 裡面新增下方程式碼，這段程式碼只是去註冊 model 而已
    ```
    from django.contrib import admin

    # Register your models here.
    from django.contrib import admin
    from musics.models import Music

    admin.site.register(Music)
    ```
    接著執行 Django ，然後到 http://127.0.0.1:8000/admin/

    應該會看到下圖，輸入剛剛的帳號/密碼

    ![](https://i.imgur.com/9gXSZ5R.png)
    
    登入後就會發現剛剛新增的資料表了
    ![](https://i.imgur.com/H4IDZC9.png)

1. Integrating Django with a legacy database

    如果說現在我們已經有一個 db，需要建立 model 讓他 map 到 db，這時候不可能手動一個一個打
    ，好在 Django 有提供一個方法讓我們將既有的 db 轉化成 model ，我們只需要使用以下的指令：
        
        python manage.py inspectdb > models.py
        
    這時候你可以打開 models.py，你應該會看到 map 到你 db 的 model。




