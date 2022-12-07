from myownexception import InvalidWithdrawal, Inventory


class EvenOnly(list):
    def appends(self, integer):
        if not isinstance(int, integer):
            raise TypeError("Harus memasukan bilangan")
        if integer % 2:
            raise ValueError("Hanya dapat memasukan bilangan genap")
        super().append(integer)


def no_return():
    print("Ini bakal terus di tampilin")
    raise Exception("Exception ini akan ditampilin")
    print("Ini gabakal ditampilin")
    return "Ini juga gabakal dibalikin nilainya"


def call_return():
    print("This will always being raised")
    no_return()
    print("an exception was raised...")
    print("...so this line don't run")


def try_except():
    try:
        no_return()
    except:
        print("i caught an exception")
    print("dieksekusi setelah excepsi")


def jajal_try_except(num):
    try:
        return 100 / num
    except:
        raise ZeroDivisionError("Lu gabisa bagi pecahan dengan angka 0")


def jajal_try_except2(num):
    try:
        if num == 13:
            raise ValueError("13 adalah angka sial")
        return 100 / num
    except (ZeroDivisionError, TypeError):
        return "Masukan angka selain 0"


def jajal_try_except3(num):
    try:
        if num == 13:
            raise ValueError("13 adalah angka sial")
        return 100 / num
    except ZeroDivisionError:
        return "Masukan angka selain 0"
    except TypeError:
        return "Hanya dapat memasukan bilangan"
    except ValueError:
        print("Jangan masukan angka 13 pea")
        # raise raise


def finally_else():
    import random
    some_exceptions = [ValueError, ZeroDivisionError, TypeError, IndexError, None]

    try:
        pilihan = random.choice(some_exceptions)
        print("Testing {}".format(pilihan))
        if pilihan:
            raise pilihan("ERROR")
    except ValueError:
        print("nangkep ValueError")
    except TypeError:
        print("nangkep TypeError")
    except Exception as e:
        print("nangkep error yang lain: %s" % e.__class__.__name__)
    else:
        print("kode ini muncul ketika gada exception")
    finally:
        print("ini bakal dimunculin terus dan juga bersihin kode")


def myownexception():
    try:
        raise InvalidWithdrawal(25, 50)
    except InvalidWithdrawal as e:
        print("Saya minta maaf, tetapi penarikan melebihi dari balance by {}".format(e.overage()))


def divisor_exception(pembilang, penyebut):
    try:
        print("{} / {} = {}".format(pembilang, penyebut, (pembilang / penyebut * 1.0)))
    except ZeroDivisionError as e:
        print("Penyebut tidak boleh di inisiasi oleh angka 0")


def divisor_if(pembilang, penyebut):
    if penyebut == 0:
        print("Penyebut tidak boleh di isi oleh angka 0")
    else:
        print("{} / {} = {}".format(pembilang, penyebut, (pembilang / penyebut * 1)))


class InvalidItemType:
    pass


class OutOfStock:
    pass


def inventory():
    item_type = 'jam tangan'
    inv = Inventory()
    inv.lock(item_type)
    try:
        num_left = inv.purchase(item_type)
    except InvalidItemType:
        print("Maaf, kami tidak menjual {}".format(item_type))
    except OutOfStock:
        print("Maaf, item tersebut telah habis terjual")
    else:
        print("Pembelian berhasil dengan item tersisa {} {}".format(num_left, item_type))
    finally:
        inv.unlock()


if __name__ == "__main__":
    #     # print(jajal_try_except(0))
    #     # print(jajal_try_except(5))
    #     # print(jajal_try_except("string"))
    #
    #     # for val in (0, "hello", 50.0, 13):
    #     #     print("Testing {}: ".format(val), end=' ')
    #     #     print(jajal_try_except2(val))

    # finally_else()

    # myownexception()

    inventory()
