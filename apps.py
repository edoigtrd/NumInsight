import highlenium

class AppCollections :
    def __init__(self) -> None:
        self.apps = {}
    
    def register(self, app) :
        def inner(func) :
            self.apps[app] = func
            return func
        return inner
    
    def get_list(self) :
        return sorted(list(self.apps.keys()))

    def run(self) :
        apps = {}
        for i in self.apps :
            try :
                apps[i] = self.apps[i](self.params)
            except Exception as e:
                apps[i] = e
        return apps
    
    def set_params(self, params) :
        self.params = params


apps = AppCollections()

@apps.register("Amazon")
def amazon_check(params) :
    highlenium.browseto("https://www.amazon.fr/")
    highlenium.clickon("#nav-link-accountList-nav-line-1")
    highlenium.typein("#ap_email", params["number"])
    highlenium.clickon("#continue")

    if highlenium.checkfor("#auth-error-message-box") :
        return False
    else :
        return True
