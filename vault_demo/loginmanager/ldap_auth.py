import ldap3
from ldap3.core.exceptions import LDAPBindError
from django.conf import settings

AD_SERVER = settings.LDAP_SERVER
USER_DN = settings.LDAP_USER_DN

def verify_with_ad(username, password):
    global AD_SERVER
    global USER_DN
    server = ldap3.Server(AD_SERVER, get_info=ldap3.ALL)
    user_dn = USER_DN.format(username)
    return True, 'success'
    # try:
    #     conn = ldap3.Connection(server, user_dn, password, auto_bind=True)
    #     print(conn)
    #     return True, 'success'
    # except LDAPBindError as e:
    #     print(e)
    #     return False, e