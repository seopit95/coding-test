class SignIn:
    registered_user_id = ['joonas', 'baekjoon']

    def __init__(self, id):
        self.id = id

    def validateCheck(self):
        for user_id in self.registered_user_id:
            if self.id == user_id:
                print(self.id + '??!')

signIn = SignIn('joonas')

signIn.validateCheck()
# joonas??!