"""url = 'https://maps.googleapis.com/maps/api/geocode/json?address=1+2,+3,+4&key=AIzaSyCpMCAkuN89MgGDQAxVJfBGcbGA8bosKZQ'
        
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
print(url_base)"""

class Cleanner:
    def __init__(self):
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json?address=1+2,+3,+4&key=AIzaSyCpMCAkuN89MgGDQAxVJfBGcbGA8bosKZQ'
        self.url_base = None
        self.url_parametros = None
        self.parametros = {
            "number" : 1,
            "street" : 2,
            "city"   : 3,
            "state"  : 4
        }

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        self.url_base = self.url[:indice_interrogacao]
        return self.url_base

    def get_url_params(self):
        index_equal = self.url.find('=')
        index_e_comerce = self.url.find('&')
        self.url_parametros = self.url[index_equal + 1 : index_e_comerce]
        return self.url_parametros

    def user_params(self):
        self.parametros["number"] = int(input("Number: "))
        self.parametros["street"] = str(input("Street: ")).title()
        self.parametros["city"] = str(input("City  : ")).title()
        self.parametros["state"] = str(input("State : ")).upper()
        return self.parametros

    def str_cleaner(self):
        self.parametros = self.user_params()
        self.parametros["street"] = self.parametros["street"].replace(" ","+")
        self.parametros["city"] = self.parametros["city"].replace(" ","+")
        return self.parametros


    def set_url_params(self):
        self.url_parametros = self.get_url_params()
        self.parametros = self.str_cleaner()
        self.url = self.url.replace("1", str(self.parametros["number"]))
        self.url = self.url.replace("2", str(self.parametros["street"]))
        self.url = self.url.replace("3", str(self.parametros["city"]))
        self.url = self.url.replace("4", str(self.parametros["state"]))
        print(self.url)
        return self.url


c = Cleanner()
#print(c.get_url_base())
#print(c.user_params())
c.set_url_params()
print(c.parametros)
print(c.url)