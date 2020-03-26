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
        blogName = str(blogName)
        title = str(title_word)
        body = str(body_word)
        client.create_text(blogName, state="published", slug="testing-text-posts", title=title, body=body)


if __name__ == '__main__':
    consumer_key = ''
    consumer_secret = ''
    oauth_token = ''
    oauth_secret = ''
    user = Python_tumblr(consumer_key, consumer_secret, oauth_token, oauth_secret)
    blogName = input('輸入想發文的部落格: ').strip()
    title = input('輸入標題: ').strip()
    body = input('輸入內文: ').strip()
    user.post(blogName, title, body)
