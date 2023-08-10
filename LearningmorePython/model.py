class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def give_like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    def __str__(self):
        return f'{self.name} - {self.year} - {self.likes} Likes'


class Movie(Program):
    def __init__(self, name, year, time):
        super().__init__(name, year)
        self.time = time

    def __str__(self):
        return f'{self.name} - {self.year} - {self.time} min - {self.likes} Likes'


class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self.name} - {self.year} - {self.seasons} seasons - {self.likes} Likes'


class Playlist:
    def __init__(self, name, program):
        self.name = name
        self.__program = program

    def __getitem__(self, item):
        var = self.__program[item]

    @property
    def listing(self):
        return self.__program


    def __len__(self):
        return len(self.__program)


breaking_bad = Serie("Breaking Bad", 2008, 5)
tbbt = Serie("The Big Bang Theory", 2007, 12)
interstellar = Movie("Interstellar", 2014, 169)
The_Oficce = Serie("The Oficce", 2005, 9)

interstellar.give_like()
interstellar.give_like()
interstellar.give_like()
interstellar.give_like()
interstellar.give_like()
interstellar.give_like()
tbbt.give_like()
tbbt.give_like()
tbbt.give_like()
tbbt.give_like()
tbbt.give_like()
breaking_bad.give_like()
breaking_bad.give_like()
breaking_bad.give_like()
breaking_bad.give_like()
breaking_bad.give_like()
breaking_bad.give_like()
breaking_bad.give_like()
breaking_bad.give_like()
The_Oficce.give_like()
The_Oficce.give_like()
The_Oficce.give_like()
The_Oficce.give_like()
The_Oficce.give_like()

movies_and_series = [interstellar, The_Oficce, tbbt, breaking_bad]
weekend = Playlist("Weekend", movies_and_series)

print(f'Playlist size: {len(weekend.listing)}')

len(weekend)
for program in weekend.listing:
    print(program)