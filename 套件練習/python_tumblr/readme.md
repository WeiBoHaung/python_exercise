# python串連tumblr貼文

###### tags: `python` `tumlr`

## 取得OAuth key

1. 你需要創立一個應用程式到此[連結](https://www.tumblr.com/oauth/apps)

    ![](https://i.imgur.com/9LQer1U.png)

1. 先輸入以下幾項
    *    應用程式名稱: firstApp
    *    應用程式網站: https://firstApp.tumblr.com
    *    應用程式敘述: 隨便打
    *    系統管理聯絡電子郵件: 你的帳號信箱就可以了
    *    預設回傳 URL: https://firstApp.tumblr.com

    ![](https://i.imgur.com/EU4aXMx.png)

1. 點擊下方註冊後就會產生一個APP
![](https://i.imgur.com/8p1bmAT.png)

## 建立python連接應用程式


        
1. 取得ＫＥＹ
    
    這個時後點開剛剛創好的應用程式設定
    ![](https://i.imgur.com/0x1rqDp.png)
    進到編輯設定畫面
    右邊有兩組key:OAuth消費者金鑰，OAuth消費者密碼（需要點show才會出現）
    將OAuth消費者金鑰、OAuth消費者密碼複製
    
    ![](https://i.imgur.com/oIEsBN2.png)
    
    到這個連結[https://api.tumblr.com/console](https://api.tumblr.com/console)先登入你要貼文的帳號，會看到這個畫面
    ![](https://i.imgur.com/ygDwRKm.png)
    分別填入剛剛複製的OAuth消費者金鑰、OAuth消費者密碼後按下Authenticate
    ![](https://i.imgur.com/VRSmzeY.png)
    系統會詢問是否同意，你剛剛的Ａpp來操作你的帳號
    ![](https://i.imgur.com/uvgXrej.png)
    選擇python你會看到四組字串
    * consumer_key
    * consumer_secret
    * oauth_token
    * oauth_secret
    ![](https://i.imgur.com/zLHPKFP.png)
    

1. 安裝PyTumblr
    
        pip install pytumblr       

1.  使用範例
    ```
    consumer_key ='輸入自己的'
    consumer_secret = '輸入自己的'
    oauth_token = '輸入自己的'
    oauth_secret = '輸入自己的'
    user=Python_tumblr(consumer_key,consumer_secret,oauth_token,oauth_secret)
    blogName = input('輸入想發文的部落格: ').strip()
    title = input('輸入標題: ').strip()
    body = input('輸入內文: ').strip()
    user.post(blogName,title,body)
    ```
1. 如果多帳號使用

    換帳號後重複到到這個連結[https://api.tumblr.com/console](https://api.tumblr.com/console)取得您的key
    