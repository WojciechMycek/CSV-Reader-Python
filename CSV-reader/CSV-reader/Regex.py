import re
#\d - dowolna cyfra od 0 do 9
#\D - dowolny znak z wylaczeniem cyfr od 0 do 9
#\w - dowolna litera, cyfra lub znak podkreslenia
#\W - dowolny znak, ktory nie jest litera, cyfra lub znakiem podkreslenia
#\s - dowolna spacja, tabulator, znak nowego wiersza
#\S - dowolny znak, ktory nie jest spacja, tabulatorem, lub znakiem nowego miejsca
#[0-5.] - dopasowanie od 0 do 5 wlacznie z kropka
#[^0-5] - negatywna klasa znakow, zostana dopasowane wszystkie znaki oprocz wymienionych
#r'^Witaj' - dopasowanie wzorca zaczynajacego sie od Witaj
#r'\d$' - dopasuje wzorzec konczacy sie dowolna liczba
#r'^\d+$' - dopasowuje wzorzec ktory zarowna zaczyna sie i konczy jedna lub wieloma liczbami
#r'.ba' - . dopasowuje jeden znak przed wyrazeniem ba
#(.*) - dopasuj wszystko i nic metoda zachlanna
#newlineRegex = re.compile('.*', re.DOTALL) - dopasuje wszystkie znaki wraz z wyrazaniami nowego wiersza
#(?) - zero wystapien lub jedno wystapienie
#(*) - zero wystapien lub wiecej
#(+) - jedno wystapienie lub wiecej
#{n} - dopasowanie poprzedzajacego go grupy n razy
#{n,} - od n do nieskonczonosci
#{n,m} - od n do m
#{n,m}? - niezachlanne dopasowanie 
#robocop = re.compile(r'robocop', re.I) - ignorowanie wielkosci znakow
class Automate():

    def find_all_phones_number(self,records_lists_to_search):

        phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
        for i in range(len(records_lists_to_search)):
            mo = phoneNumRegex.findall(records_lists_to_search[i])
            if mo == None:
                return None
            else:
                print(mo)

    def find_area_code_number(self,records_lists_to_search):

        phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
        for i in range(len(records_lists_to_search)):
            mo = phoneNumRegex.findall(records_lists_to_search[i])
            if mo == None:
                return None
            else:
                print(mo)

    def find_groups(self,records_lists_to_search):
        namesRegex = re.compile(r'Brian| Wojciech')
        for i in range(len(records_lists_to_search)):
            mo=namesRegex.search(records_lists_to_search[i])
            if mo == None:
                return None
            else:
                print(mo.group())

    def maybe_find_this(self,records_lists_to_search):
        namesRegex = re.compile(r'Brian| Wojciech')
        for i in range(len(records_lists_to_search)):
            mo=namesRegex.search(records_lists_to_search[i])
            if mo == None:
                return None
            else:
                print(mo.group())

    def optional_find_this(self,records_lists_to_search):
        namesRegex = re.compile(r'(\n)?Woj(ci)?ech')
        for i in range(len(records_lists_to_search)):
            mo=namesRegex.search(records_lists_to_search[i])
            if mo == None:
                return None
            else:
                print(mo.group())

    def optional_find_this_star(self,records_lists_to_search):
        namesRegex = re.compile(r'Woj(ci)*ech')
        for i in range(len(records_lists_to_search)):
            mo=namesRegex.search(records_lists_to_search[i])
            if mo == None:
                return None
            else:
                print("star" + mo.group())

    def optional_find_this_plus(self,records_lists_to_search):
        namesRegex = re.compile(r'Woj(ci)+ech')
        for i in range(len(records_lists_to_search)):
            mo=namesRegex.findall(records_lists_to_search[i])
            if mo == None:
                return None
            else:
                print(mo)

    def repeat_regex(self,records_lists_to_search):
        namesRegex = re.compile(r'Woj(ci){4}ech')
        for i in range(len(records_lists_to_search)):
            mo=namesRegex.search(records_lists_to_search[i])
            if mo == None:
                return None
            else:
                print(mo.group())

    def you_own_class_znak(self, records_lists_to_search):
        regexnu = re.compile(r'[aeiouAEIOU]')
        for i in range(len(records_lists_to_search)):
            mo=regexnu.findall(records_lists_to_search[i])
            if mo == None:
                return None
            else:
                print(mo)

    def sub_method(self):
        namesRegex = re.compile(r"Agent \w+")
        namesRegex.sub('Ocenzurowane', "Agen Alicja przekazala dla Agent Beata")