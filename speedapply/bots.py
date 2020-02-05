class ApplyBot:
    def __init__(self, site, auth):
        self.site = site
        self.auth = auth

    def __call__(self, settings):
        return self.site(self.auth, settings)
