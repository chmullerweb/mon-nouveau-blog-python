#def make_tea(cup, teabag, water):
    
def hi(name):
        if name =='Ola':
                print('Hi Ola!')
        elif name =='Sonja':
                print('Hi Sonja!')
        else: 
            print('Hi anonymous !')
        
hi('Paul')

def myname(fullname):
        print('Hi '+ fullname + '!')

myname('Arthur')

girls = ['Elise', 'Monica', 'Charline', 'Lola']

for name in girls:
    print('hi ' + name)
    
person = {
    'name' : "Ola",
    'height' : 155,
    'fav_meal' : 'lasagna',
}

for element in person:
    print(element)
    
for element in person.values():
    print(element)
    
for element in person.items():
    print(element)
    
for key, value in person.items():
    print('La personne ' + str(key) + ' est ' + str(value))
