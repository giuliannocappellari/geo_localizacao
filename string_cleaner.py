"""
#Explicando a URL
URL'https://maps.googleapis.com/maps/api/geocode/json?address={number}+{street},+{city},+{state}&key=AIzaSyCpMCAkuN89MgGDQAxVJfBGcbGA8bosKZQ'
"""


class Cleaner:
    def __init__(self):
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json?address=1+2,+3,+4&key=AIzaSyCpMCAkuN89MgGDQAxVJfBGcbGA8bosKZQ'
        self.url_base = None
        self.url_parametros = None
        self.parametros = {
            1 : "number",
            2 : "street",
            3 : "city",
            4 : "state"
        }
        
    #get only base url
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        self.url_base = self.url[:indice_interrogacao]
        return self.url_base

    #get only url's params
    def get_url_params(self):
        index_equal = self.url.find('=')
        index_e_comerce = self.url.find('&')
        self.url_parametros = self.url[index_equal + 1 : index_e_comerce]
        return self.url_parametros

    #set user's params
    def user_params(self):
        self.url_parametros = self.get_url_params()
        self.parametros["number"] = int(input("Number: "))
        self.parametros["street"] = str(input("Street: ")).title()
        self.parametros["city"] = str(input("City  : ")).title()
        self.parametros["state"] = str(input("State : ")).upper()
        return self.parametros

    #fix user's params
    def str_cleaner(self):
        self.parametros = self.user_params()
        self.parametros["street"] = self.parametros["street"].replace(" ","+")
        self.parametros["city"] = self.parametros["city"].replace(" ","+")
        return self.parametros

    #set url params from user's params
    def set_url_params(self):
        self.url_parametros = self.get_url_params()
        self.parametros = self.str_cleaner()
        self.url = self.url.replace("1", str(self.parametros["number"]))
        self.url = self.url.replace("2", str(self.parametros["street"]))
        self.url = self.url.replace("3", str(self.parametros["city"]))
        self.url = self.url.replace("4", str(self.parametros["state"]))
        print(self.url)
        return self.url

    #search only one param
    def get_valor_parametro(self, parametro_busca):
        index_param = self.get_url_parametros().find(parametro_busca)
        index_value = index_param + len(parametro_busca) + 1
        index_coma = self.get_url_parametros().find(',', index_value)
        if index_coma == -1:
            valor = self.get_url_parametros()[index_value:]
        else:
            valor = self.get_url_parametros()[index_value:index_coma]
        return valor

    #return the number of letters in the string
    def __len__(self):
        return len(self.url)

    #return the url
    def __str__(self):
        return self.url 

    def __eq__(self, other):
        return self.url == other.url

"""c = Cleaner()
c.set_url_params()"""  