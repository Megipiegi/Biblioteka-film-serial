import random
from random import randint


class Film:
    def __init__ (self, tytul, rok_wydania, gatunek, liczba_odtworzen, incr: int = 1):
        self.tytul=tytul
        self.rok_wydania=rok_wydania
        self.gatunek=gatunek
        self.liczba_odtworzen = liczba_odtworzen
        self.increment = incr

    def __str__ (self):
        return f'{self.tytul} {self.rok_wydania} {self.gatunek} {self.liczba_odtworzen}'

    def increase(self):
        self.liczba_odtworzen += self.increment

    def play(self):
        self.increase()

    def tytul_rok(self):
        return f'{self.tytul} ({self.rok_wydania})'
    

id_movie_one = Film (tytul='Szczeki', rok_wydania ='1970', gatunek ='horror', liczba_odtworzen =95)
id_movie_two = Film (tytul='Ptaki', rok_wydania='1960', gatunek ='thriller', liczba_odtworzen =9)
id_movie_three = Film (tytul='Niemozliwe', rok_wydania ='2015', gatunek ='katastroficzny', liczba_odtworzen =6)
id_movie_all=[id_movie_one, id_movie_two, id_movie_three]

class Serial(Film):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka=numer_odcinka
        self.numer_sezonu=numer_sezonu

    def __str__ (self):
        return f'{self.tytul} {self.rok_wydania} {self.gatunek} {self.liczba_odtworzen} {self.numer_odcinka} {self.numer_sezonu}'

    def tytul_rok(self):
        return f'{self.tytul} S0{self.numer_sezonu}E{self.numer_odcinka}'

   
id_series_one = Serial (tytul='Little Britain', rok_wydania='1995', gatunek='serial komediowy', liczba_odtworzen=15, numer_odcinka = '12', numer_sezonu = '2')
id_series_two = Serial (tytul='Dynastia', rok_wydania='1980', gatunek='serial obyczajowy', liczba_odtworzen=20, numer_odcinka = '22', numer_sezonu = '3')
id_series_three = Serial (tytul='Sherlock Holmes', rok_wydania='1970', gatunek='serial kryminalny', liczba_odtworzen=100, numer_odcinka = '2', numer_sezonu = '1')

# pkt 6. Przechowuje Film i Serial w jednej liście.
all_library = [id_movie_one, id_movie_two,id_movie_three, id_series_one, id_series_two, id_series_three]


# sprawdzenie czy inkrementacja działa poprawnie
print('*********Funkcja PLAY***************')
print(f'Liczba odtworzeń filmu { id_movie_one.tytul } to { id_movie_one.liczba_odtworzen }')
id_movie_one.play()
print(id_movie_one.tytul_rok())
print(f'Liczba odtworzeń filmu { id_movie_one.tytul } po jednym odtworzeniu to { id_movie_one.liczba_odtworzen }')

print(f'Liczba odtworzeń serialu { id_series_one.tytul } to { id_series_one.liczba_odtworzen }')
id_series_one.play()
print(id_series_one.tytul_rok())
print(f'Liczba odtworzeń serialu { id_series_one.tytul } po jednym odtworzeniu to { id_series_one.liczba_odtworzen }')
print('*********Koniec testowania metody PLAY***************')

print('Wszystkie Film i Serial:')
for element in all_library:
    if type(element) is Film:
        print('******FILM**********')
        print(element.tytul)
        print(element.rok_wydania)
        print(element.liczba_odtworzen)
    elif type(element) is Serial:
        print('******SERIAL**********')
        print(element.tytul)
        print(element.rok_wydania)
        print(element.liczba_odtworzen)
        print(element.numer_odcinka)
        print(element.numer_sezonu)

print('*************KONIEC Wyświetlania filmów i seriali***********************')

# Funkcje
print('***********pkt7 funkcja get_movies i series************')
#7 Napisz funkcje get_movies oraz get_series:
def get_type(object_type):  
    valid_types = []
    for obj in all_library:
        if type(obj) is object_type:
            valid_types.append(obj)
    return valid_types

def get_films():
    return get_type(Film)

def get_series():
    return get_type(Serial)

print('*****Lista filmów:*****')
for f in get_films():
    print(f.tytul)

print('****Lista seriali:******') 
for s in get_series():
    print(s.tytul)


sorted_movies = sorted(get_films(), key=lambda x: x.tytul)
sorted_series = sorted(get_series(), key=lambda x: x.tytul)
print('*****sortowanie movies*******')
for sm in sorted_movies:
    print(sm.tytul)

print('*****sortowanie series*******')
for ss in sorted_series:
    print (ss.tytul)
    

print('*****pkt8 Napisz funkcję search, która wyszukuje film lub serial po jego tytule.******')

def search(search_term):
  search_term = search_term.lower()
  return [ 
    obj for obj in all_library if search_term in obj.tytul.lower()
  ]
search_library = search('dy')
for s in search_library:
    print(s.tytul)


print ('*****pkt 9 Napisz funkcję generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.******')

def generate_views():
    random_number_list = randint(0,5)
    random_number_of_plays = randint(1,100)
    element = all_library[random_number_list]
    element.liczba_odtworzen += random_number_of_plays
    return element

gen_views = generate_views()
print(gen_views)

print ("*****pkt 10 Napisz funkcję, która uruchomi generate_views 10 razy******")

def generate_views_10_times():
    for i in range (10):
        print(random.choice(all_library))
generate_views_10_times()

print ('*****pkt 11 Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki. ******')

def most_popular(count, object_type):
    valid_objects = get_type(object_type)
    return sorted(valid_objects, key=lambda a: -a.liczba_odtworzen)[:count]

print(most_popular(3, Film))
print(most_popular(3, Serial)) 
#dlaczego w replicie to się drukuje a w Visual Studio Code muszę pisać pętlę for?
exit(0)


