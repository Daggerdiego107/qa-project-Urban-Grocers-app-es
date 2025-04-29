import sender_stand_request
import data

def get_kit_body(kit_name):
    current_body = data.kit_body.copy()
    current_body["name"] = kit_name
    return current_body

def possitive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_kits(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json() != {}

def negative_assert_kit_name(kit_name):
    kit_body = get_kit_body(kit_name)
    response = sender_stand_request.post_new_kits(data.kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

def negative_assert_kit_body(kit_body):
    response = sender_stand_request.post_new_kits(data.kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

#Prueba 1
def test_nombre_de_kit_con_1_caracter_respuesta_exitosa():
    possitive_assert("a")

#Prueba 2
def test_nombre_de_kit_con_511_caracteres_respuesta_exitosa():
    possitive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Prueba 3
def test_nombre_de_kit_con_nombre_vacio_obtener_respuesta_error():
    kit_body = get_kit_body("")
    negative_assert_kit_name(kit_body)

#Prueba 4
def test_nombre_de_kit_con_512_caracteres_obtener_respuesta_error():
    negative_assert_kit_name("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Prueba 5
def test_nombre_de_kit_con_caracteres_especiales_respuesta_exitosa():
    possitive_assert("№%@,")

#Prueba 6
def test_nombre_de_kit_con_espacios_respuesta_exitosa():
    possitive_assert("A Aaa")

#Prueba 7
def test_nombre_de_kit_con_numeros_respuesta_exitosa():
    possitive_assert("123")

#Prueba 8
def test_cuerpo_de_kit_vacio_respuesta_error():
    kit_body = get_kit_body("")
    negative_assert_empty_kit_body(kit_body)

#Prueba 9
def test_cuerpo_de_kit_con_numeros_respuesta_error():
    kit_body = get_kit_body(123)
    negative_assert_kit_body(kit_body)