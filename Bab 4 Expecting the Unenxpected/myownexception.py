class InvalidWithdrawal(Exception):
    def __init__(self, amount, balance):
        super().__init__("Account doesn't have {}".format(amount,))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance


class Inventory:
    def lock(self, item_type):
        '''Pilih item mana yang ingin diubah.
        metode ini akan mengunci inventory
        jadi ngga sembarangan orang bisa punya
        akses ke metode ini sampe di returned'''
        pass

    def unlock(self):
        '''Membuka kunci inventory agar customer
        dapat mengaksesnya'''
        pass

    def purchase(self, item_type):
        '''kalo item yang dipilih gak terkunci,
        munculin eksepsi. Kalo item gada, munculin
        eksepsi. Kalo itemnya out of stock, munculin
        eksepsi. kalo item ada maka keluarin item
        dan return jumlah item yang tersisa'''
        pass