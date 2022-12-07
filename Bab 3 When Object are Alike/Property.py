class Property:
    def __init__(self, bedroom='', bathroom='', meter_persegi='', **kwargs):
        self.bedroom = bedroom
        self.bathroom = bathroom
        self.meter_persegi = meter_persegi

    def display(self):
        print("\n\nPROPERTY DETAILS")
        print(16 * '=')
        print("Meter Persegi {}".format(self.meter_persegi))
        print("Bedroom {}".format(self.bedroom))
        print("Bathroom {}".format(self.bathroom))

    def prompt_init():
        return dict(meter_persegi=input("Masukan meter persegi: "),
                    beds=input("Masukan jumlah tempat tidur: "),
                    bath=input("Masukan jumlah kamar mandi: "))

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    input_string += " ({}) ".format(", ".join(valid_options))
    respon = input(input_string)
    while respon.lower() not in valid_options:
        respon = input(input_string)
    return respon


class Apartment(Property):
    valid_balkon = ("coin", "ensuite", "none")
    valid_laundri = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def diplay(self):
        super().display()
        print("\nDETAIL APARTMENT")
        print("Laundri: %s" % self.laundry)
        print("Berapa Balkon: %s" % self.balcony)

    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input("Fasilitas Laundri ", Apartment.valid_laundri)
        balkon = get_valid_input("Ada berapa Balkon", Apartment.valid_balkon)
        parent_init.update({
            "laundri": laundry,
            "balkon": balkon
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    valid_garasi = ("attached", "detached", "none")
    valid_pagar = ("yes", "no")

    def __init__(self, num_lantai='', garasi='', pagar='', **kwargs):
        super().__init__(**kwargs)
        self.num_lantai = num_lantai
        self.pagar = pagar
        self.garasi = garasi

    def display(self):
        super().display()
        print("\nDETAIL RUMAH")
        print("Jumlah Lantai: {}".format(self.num_lantai))
        print("Pagar: {}".format(self.pagar))
        print("Garasi: {}".format(self.garasi))

    def prompt_init():
        parent_init = Property.prompt_init()
        pagar = get_valid_input("Apakah dihalamannya memiliki pagar? ", House.valid_pagar)
        garasi = get_valid_input("Apakah ada garasi? ", House.valid_garasi)
        lantai = input("Berapa banyak lantai? ")
        parent_init.update({
            "pagar": pagar,
            "garasi": garasi,
            "num_lantai": lantai
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    def __init__(self, harga='', pajak='', **kwargs):
        super().__init__(**kwargs)
        self.pajak = pajak
        self.harga = harga

    def display(self):
        super().display()
        print("\nDETAIL HARGA")
        print("Harga jual: {}".format(self.harga))
        print("Estimasi pajak: {}".format(self.pajak))

    def prompt_init():
        return dict(
            harga=input("Berapa harga jual? "),
            pajak=input("Berapa estimasi pajak? ")
        )

    prompt_init = staticmethod(prompt_init)


class Rental:
    def __init__(self, utilities='', sewa='', furnitur='', **kwargs):
        super().__init__(**kwargs)
        self.sewa = sewa
        self.furnitur = furnitur
        self.lama_sewa = utilities

    def display(self):
        super().display()
        print("\nDETAIL SEWA")
        print("Sewa: {}".format(self.sewa))
        print("Furnitur: {}".format(self.furnitur))
        print("Lama Sewa: {}".format(self.lama_sewa))

    def prompt_init():
        return dict(
            sewa=input("Berapa harga sewa per bulan? "),
            lama_sewa=input("Menyewa untuk berapa lama? "),
            furnitur=get_valid_input("Apakah Properti memiliki perabotan", ("yes", "no"))
        )

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Apartment, Rental):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(House, Purchase):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Apartment, Purchase):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    def __init__(self):
        self.properti_list = []

    def display_property(self):
        for properti in self.properti_list:
            properti.display()

    type_map = {
        ("rumah", "sewa"): HouseRental,
        ("rumah", "beli"): HousePurchase,
        ("apartment", "sewa"): ApartmentRental,
        ("apartment", "beli"): ApartmentPurchase
    }

    def add_properti(self):
        jenis_properti = get_valid_input("Jenis Properti? ", ("apartment", "rumah")).lower()
        jenis_pembayaran = get_valid_input("Jenis Pembayaran? ", ("sewa", "beli")).lower()

        PropertyClass = self.type_map[
            (jenis_properti, jenis_pembayaran)]
        init_args = PropertyClass.prompt_init()
        self.properti_list.append(PropertyClass(**init_args))


agent = Agent()
agent.add_properti()
agent.display_property()
