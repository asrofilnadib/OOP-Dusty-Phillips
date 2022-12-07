import auth

auth.authenticator.add_user("joe", "joepassword")
auth.authentizor.add_permit("test program")
auth.authentizor.add_permit("change program")
auth.authentizor.permit_user("test program", "joe")


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "1": self.login,
            "2": self.test,
            "3": self.change,
            "4": self.quit
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("Input Username: ")
            password = input("Input Password: ")
            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print("Maaf, Username tidak ada")
            except auth.InvalidPassword:
                print("Maaf, Password salah")
            else:
                self.username = username

    def is_permision(self, permision):
        try:
            auth.authentizor.check_permission(permision, self.username)
        except auth.NotLoggedInError as e:
            print("{} tidak bisa login".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} tidak memiliki izin atas {}".format(e.username, permision))
            return False
        else:
            return True

    def test(self):
        if self.is_permision("test program"):
            print("Testing program now...")

    def change(self):
        if self.is_permision("change program"):
            print("Changing program now...")

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print("""
                Please enter a command:
                1. login\tLogin
                2. test\t\tTest program
                3. change\tChange program
                4. quit\t\tQuit
                """)
                answer = input("Masukan perintah: ").lower()
                try:
                    funct = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    funct()
        finally:
            print("Thanks for the testing the auth module")


Editor().menu()