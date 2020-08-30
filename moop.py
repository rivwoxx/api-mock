# from flask import make_response, abort
import json

with open ('dat.json','r') as f:
    # conts = f.readlines()
    ca = json.load(f)
    c = ca['data']
# print(c)
c1 = list(c)

cuenta = {}
a = 0
for x in c:
    c2 = c[a]['account']
    # pepe = str(c1[a])
    cuenta[c2] = x
    # print(cuenta)
    a = a + 1

# print(cuenta)
def get_dat(): 
    return [cuenta[key] for key in sorted(cuenta.keys())]


def new_ac(meh):

    account= meh.get("account", None)
    clabe = meh.get("clabe", None)
    name = meh.get("name", None)
    rfc = meh.get("rfc", None)
    curp = meh.get("curp", None)
    sucursal = meh.get("sucursal", None)

    # Does the meh exist already?
    if account not in cuenta and account is not None:
        cuenta[account] = {
            "account":account,
            "clabe":clabe,
            "name":name,
            "rfc":rfc,
            "curp":curp,
            "sucursal":sucursal
        }
        return make_response(
            "Cuenta # {account} ha sido creada".format(account=account), 201
        )
    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Cuenta # {account} ya existe".format(account=account),
        )
        

    # def filly(a):
        
#     if(a in c1):
#         return True
#     else:
#         return False

# fil = filter(filly, a)
    # print('\nsomething something: \n')
    # for i in fil:
    #     print(i)
