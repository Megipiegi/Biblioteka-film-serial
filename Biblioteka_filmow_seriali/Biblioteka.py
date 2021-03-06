from random import randint, randrange


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
def get_type(object_type):
    abc = []
    if type(object_type) is Film:
        for element in all_library:
            abc.append(element)
    elif type(object_type) is Serial:
        for element in all_library:
            abc.append(element)
    return abc

print('TESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSST')

test = get_type(Film)
for a in test:
    print(a)

print('TESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSST')


def get_movies():
    only_movies_def = []
    for el_movie in all_library:
        if type(el_movie) is Film:
            only_movies_def.append(el_movie)
    return only_movies_def

def get_series():
    only_series_def = []
    for el_serie in all_library:
        if type(el_serie) is Serial:
            only_series_def.append(el_serie)
    return only_series_def

# Zmienne do przechowywania filmów i seriali
only_movies = get_movies()
only_series = get_series()

# Listy posortowane wg tytułu
sorted_movies = sorted(only_movies, key=lambda x: x.tytul)
sorted_series = sorted(only_series, key=lambda x: x.tytul)

print('Posortowane Film')
for elements_in_sorted_movies in sorted_movies:
    print(elements_in_sorted_movies.tytul)
    print(elements_in_sorted_movies.rok_wydania)
    print(elements_in_sorted_movies.liczba_odtworzen)

print('Posortowane Serial')
for elements_in_sorted_series in sorted_series:
    print(elements_in_sorted_series.tytul)
    print(elements_in_sorted_series.rok_wydania)
    print(elements_in_sorted_series.liczba_odtworzen)


def search(title_name):
    result = ''
    for el_search in all_library:
        if el_search.tytul.lower() == title_name.lower():
            result = 'Tak, posiadamy taki tytuł'
            return result
        else:
            result = 'Nie, nie posiadamy tego tytułu'
    return result

def generate_views():
    random_number_list = randint(0,5)
    random_number_of_plays = randint(1,100)
    element = all_library[random_number_list]
    element.liczba_odtworzen += random_number_of_plays
    return element

def generate_views_10_times():
    for i in range(10):
        generate_views()

def top_titles(content_type):
    if content_type == 'Film':
        top_number_movies = 0
        only_movies = get_movies()
        for top_movie in only_movies:
            if top_number_movies < top_movie.liczba_odtworzen:
                top_number_movies = top_movie.liczba_odtworzen
                top_result_movies = top_movie
        return top_result_movies
    elif content_type == 'Serial':
        top_number_series = 0
        only_series = get_series()
        for top_serie in only_series:
            if top_number_series < top_serie.liczba_odtworzen:
                top_number_series = top_serie.liczba_odtworzen
                top_result_series = top_serie
        return top_result_series
   
   
# Sprawdzenie poprawności działania funkcji search
print('Sprawdzenie poprawności działania funkcji search')
test_search_positive = search('ptaki')
test_search_negative = search('abc')
print(test_search_positive)
print(test_search_negative)

# Sprawdzenie poprawności działania funkcji generate_views
generate_views_10_times()
print('Sprawdzenie poprawności działania funkcji generate_views')
gen_views = generate_views()
print(gen_views)

top_entry = top_titles('Serial')
print(f'Najczęściej oglądany był { top_entry.tytul } aż { top_entry.liczba_odtworzen } razy')

top_entry = top_titles('Film')
print(f'Najczęściej oglądany był { top_entry.tytul } aż { top_entry.liczba_odtworzen } razy')

