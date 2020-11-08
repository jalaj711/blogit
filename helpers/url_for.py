_url_database = {
    "views.user": "/u/<username>",
    "views.tags": "/t/<tagname>",
    "views.auth.login": "/auth/login",
    "views.auth.signup": "/auth/signup",
    "api.auth.signup.validate": "/api/auth/signup/validate/",
    "api.auth.login": "/api/auth/login",
    "api.uploader": "/api/uploader",
    "api.renderer": "/api/render",
    "storage": "/storage/<uuid>"
}


def url_for(name: str) -> str:
    try:
        return _url_database[name]
    except KeyError:
        return None
