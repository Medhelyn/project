#1
people = [
	{'name' : 'jungkook', 'hobby' : 'drawing', 'eye color' : 'blue'},
	{'name' : 'jeonghan', 'hobby' : 'singing', 'eye color' : 'brown'},
	{'name' : 'hoshi', 'hobby' : 'eating', 'eye color' : 'black'}
]

for person in people:
	for key, value in person.items():
		print(f"{key}\t : {value}")
print()


#2
pet = [
	{'TypeOfPet' : 'tiger', 'PetName' : 'hoshi', 'OwnerName' : 'alin', 'Born' : '2017'},
	{'TypeOfPet' : 'bunny', 'PetName' : 'jeonghan', 'OwnerName' : 'lisa', 'Born' : '2020'},
	{'TypeOfPet' : 'otter', 'PetName' : 'chan', 'OwnerName' : 'maddie', 'Born' : '2019'},
	{'TypeOfPet' : 'cat', 'PetName' : 'wonwoo', 'OwnerName' : 'lynn', 'Born' : '2018'}
]

for pet in pet:
	for key, value in pet.items():
		print(f"{key} : {value}")
print()


#3
cities = {
    'city1' : {
        'Name' : 'Palembang',
        'Population' : '1,843 juta',
        'FunFact' : 'Memiliki Jembatan Ampera'
    },
 
    'city2' : {
        'Name' : 'Jakarta',
        'Population' : '10,56 juta',
        'FunFact' : 'Ibu kota Indonesia'        
    },
 
    'city3' : {
        'Name' : 'Bali',
        'Population' : '4,362 juta',
        'FunFact' : 'Memiliki banyak destinasi wisata'
    }
}
 
for key, val in cities.items():
 
    print(f"\nCity \t\t:{val['Name']}")
    print(f"Population \t:{val['Population']}")
    print(f"FunFact \t:{val['FunFact']}")
 
print()
    