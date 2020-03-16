#THIS IS ONLY FOR TESTING AND EXPERIMENT PURPOSES
import json

with open ('dat.json','r') as f:
    # conts = f.readlines()
    ca = json.load(f)
    c = ca['data']
    # c = ca
# print(c)

# pop = [{'account':'42441124012', 'clabe':'013436424411240122','name':'Augusto Carlos Rivera Gomez','rfc':'RIGA9701127D0','curp':'RIGA970112HDFVMG05','sucursal':'m05'},
# {'account':'95867742349','clabe':'009385958677423493','name':'Pedro Martinez de la Rosa','rfc':'MARP710224UXA','curp':'MADP710224HMCRLD04','sucursal':'fb1'}]
# print(c)
c1 = list(c)
# print (c1)
# # print(c1[0]['name'])
# print(c1[3]['account'])
cuenta = {}
a = 0
for x in c1:
    c2 = c1[a]['account']
    # pepe = str(c1[a])
    cuenta[c2] = x
    a = a + 1
print(cuenta)
# print(cuenta[key])

# PEOPLE = {}
# a = 0
# for x in c1:
#     c2 = c1[a]['account']
#     # pepe = str(c1[a])
#     PEOPLE[c2] = x
#     a = a + 1
# print(PEOPLE)

# print(PEOPLE['data'])
# def filly(pop):

#     if(pop in c1):
#         return True
#     else:
#         return False

# fil = filter(filly, pop)

# # # # def getpepe():
# # # #     for x in c1:
# # # #         print(x)


# print('\nsomething something: \n')
# for i in fil:
#     print(i)

# getpepe()
