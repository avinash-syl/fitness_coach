class AuthService():
    def getUsernameFromEmailAddr(self, emailAddr):
        return emailAddr.split('@')[0]
