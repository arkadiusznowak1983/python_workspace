from datetime import datetime


class Json:
    def __init__(self, entity):
        self.entity = entity

    def __str__(self):
        return f"{str(self.entity)}"


class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{{'{str(self.key)}': {str(self.value)}}}"


class Element:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"'{str(self.value)}'"


class Array:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        return f"[{','.join([str(x) for x in self.array])}]"


json_arr_element = Json(KeyValue('created_date', Element(datetime.now().strftime("%Y-%m-%d"))))

elements = Array([Element('value1'), Element('value2'), Element('value3'), json_arr_element])
json_entity = KeyValue('elements array', elements)
json = Json(json_entity)

print(str(json))
