from arcutils.settings import make_prefixed_get_setting


DEFAULTS = {
    'auto_create_user': True,

    # Base URL for the CAS server; it should end with a slash.
    'base_url': 'https://sso.pdx.edu/idp/profile/cas/',

    # These will be joined to CAS.base_url to form the login & logout URLs.
    # An absolute path can be used to override the base_url path prefix.
    'login_path': 'login',
    'logout_path': '/idp/profile/Logout',
    'validate_path': 'serviceValidate',

    # This specifies whether users should be redirected to the CAS logout
    # page to log them out of CAS. If this is false, users will only be
    # logged out of Django, which isn't very useful, since they can log
    # directly back in without having to enter their credentials.
    'logout_completely': True,


    # Set this to force redirection back to a specific URL instead of to the
    # referring page.
    'redirect_url': None,

    # These callbacks are called when CAS login is successful. The CAS XML
    # response is parsed into a dictionary of user attributes, which is
    # passed to each callback in turn. The default callback constructs a
    # standard User object from those attributes if the user doesn't already
    # exist.
    'response_callbacks': ['arcutils.cas.callbacks.default_response_callback'],

    'session_key': {
        'redirect_to': 'CAS.redirect_to',
    },
}


get_setting = make_prefixed_get_setting('CAS', DEFAULTS)
