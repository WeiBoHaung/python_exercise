import pytumblr


class Python_tumblr:
    consumer_key = ""
    consumer_secret = ""
    oauth_token = ""
    oauth_secret = ""

    def __init__(self, consumer_key, consumer_secret, oauth_token, oauth_secret):
        self.consumer_key = str(consumer_key)
        self.consumer_secret = str(consumer_secret)
        self.token_key = str(oauth_token)
        self.token_secret = str(oauth_secret)
        client = pytumblr.TumblrRestClient(
            consumer_key,
            consumer_secret,
            oauth_token,
            oauth_secret,
        )
        print(client.info())  # Grabs the current user information

    def post(self, blogName, title_word, body_word):
        client = pytumblr.TumblrRestClient(self.consumer_key, self.consumer_secret, self.token_key, self.token_secret)
        # blogName = str(blogName)
        # title = str(title_word)
        # body = str(body_word)
        # client.create_text(blogName, state="published", slug="testing-text-posts", title=title, body=body)
        blogName = 'eclectickidcoffee'
        title = 'test'
        body = '<a href=“http://www.wibibi.com” target=“_blank” title=“Wibibi 網頁設計教學百科”>Wibibi 網頁設計教學百科</a>'
        client.create_text(blogName, state="published", slug="testing-text-posts", title=title, body=body,format="html")


if __name__ == '__main__':
    consumer_key = 'r5F5n3qW21xCo9RMPzBLSF9QNq7qHD8SeKNMtpGxQ4PsOfyOD2'
    consumer_secret = 'tDJwzu9J7MoB7bMoksTYVo4jXW6ObHWAW5U6DYhHMEgt1eM7vX'
    oauth_token = '1Jl5U9iTxqOL4kGwU5zV5XORP30zJUiZHXt9dvPwY33Lxrw0T6'
    oauth_secret = 'eMbkPJZcHisc9iLHuDe4jVoYuDsfsCgrTvKU8pDZPhPfHMf0la'
    user = Python_tumblr(consumer_key, consumer_secret, oauth_token, oauth_secret)
    blogName = input('輸入想發文的部落格: ').strip()
    title = input('輸入標題: ').strip()
    body = input('輸入內文: ').strip()
    user.post(blogName, title, body)
