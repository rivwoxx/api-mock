from behave import when, given
import requests

@given(u'I have the account')
def define_clabe(context):
    context.payload = {
        "account":"11111111111",
        "clabe":"084743111111111115",
        "name":"David Japhet Mendoza Jimenez",
        "rfc":"MEJD660606F87",
        "curp":"MEJD660606HHGNIV05",
        "sucursal":"mi6"
}
    
@when(u'I call my service')
def call_service(context):
    context.respuesta = requests.post(url = 'http://localhost:5000/api/account',
    # json={'clabe': '002073676415879463'})
    json=context.payload)
   
@then(u'the request was succesful')
def get_response(context):
    print('Account has been created')
    # print ('STATUS_CODE:' + str(context.respuesta.status_code))
    # assert context.respuesta.status_code == 200
    

    