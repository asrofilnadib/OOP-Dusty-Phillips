import hashlib


class User:
    def __init__(self, username, password):
        """bikin objek baru dengan nama users.
        Passwordnya bakal di enkripsi sebelum distoring"""
        self.username = username
        self.password = self._encryption_pw(password)
        self.is_logged_in = False

    def _encryption_pw(self, password):
        """enkripsi password dengan username dan
        balikin secure hash algorithm"""
        hash_string = (self.username + password)
        hash_string = hash_string.encode(encoding='utf-8')
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """return jika password bener, False buat
         sebaliknya"""
        encrypted = self._encryption_pw(password)
        return encrypted == self.password


class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = {}


class UsernameIsAlreadyExist(AuthException):
    pass


class PasswordToShort(AuthException):
    pass


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


class Authenticator:
    def __init__(self):
        """class ini dibuat untuk memanajemenkan
        user login or logout"""
        self.users = {}

    def add_user(self, username, password):
        """sebelum nambahin user perlu dicek 2 kondisi,
        panjang password dan user sebelumnya sudah ada"""
        if username in self.users:
            raise UsernameIsAlreadyExist(username)
        if len(password) < 6:
            raise PasswordToShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except:
            raise InvalidUsername

        if not user.check_password(password):
            raise InvalidPassword

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False


authenticator = Authenticator()


class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permission = {}

    def add_permit(self, perm_name):
        """make a new permission that users
        can be added to"""
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            self.permission[perm_name] = set()
        else:
            raise PermissionError("Permission Exist")

    def permit_user(self, perm_name, username):
        """ngasih ijin ke user"""
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            raise PermissionError("Permission dose not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True


class NotLoggedInError(AuthException):
    pass


class NotPermittedError(AuthException):
    pass


authentizor = Authorizor(authenticator)
