def prompt_user_passwd(self, host, realm):
    """Override this in a GUI environment!"""
    import getpass
    try:
        user = input("Enter username for %s at %s: " % (realm,
                                                            host))
        passwd = getpass.getpass("Enter password for %s in %s at %s: " %
            (user, realm, host))
        return user, passwd
    except KeyboardInterrupt:
        print()
        return None, None
