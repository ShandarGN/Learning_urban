import pprint
import inspect

class test_obj:
    cls_int_atr = 0
    cls_float_atr = 0.1
    cls_bool_atr = False
    cls_str_atr = 'Class'
    cls_tuple_atr = (0, 1, 2)
    cls_lst_atr = [3, 4, 5]
    cls_dict_atr = {'six' : 6, 'seven' : 7}

    def __init__(self):
        self.obj_int_atr = 1
        self.obj_float_atr = 1.0
        self.obj_bool_atr = True
        self.obj_str_atr = 'Object'
        self.obj_tuple_atr = (10, 11, 12)
        self.obj_lst_atr = [13, 14, 15]
        self.obj_dict_atr = {'sixteen' : 16, 'seventeen' : 17}

    def test_method(self):
        print('Тестовый метод')

HW_obj = test_obj()

"""
    inf - строковый параметр определающий тип выдаваемой информации, список:
        type - тип объекта
        attr - атрибуты объекта и их тип
        attr_z - значения атрибутов объекта
        meth0 - немагические методы объекта
        meth1 - все методы объекта
        m_meth - магические методы объекта
        m_n_m - элементы определенные через __, но не являющиеся методами
        modul - модуль в котором определен объект
        call -  вызываемость элементов объекта
        all - все данные об объекте (по умолчанию)    
"""

def introspection_info(obj, inf = 'all'):
    if inf in ('type', 'attr', 'meth0', 'meth1', 'm_meth', 'm_n_m', 'modul', 'call', 'func', 'attr_z', 'all'):
        if inf == 'type':
            return 'Тип:', type(obj)
        elif inf == 'attr':
            return 'Атрибуты:', {i : type(getattr(obj, i)) for i in dir(obj) if i[0:2] != '__' and 'method' not in
                    str(type(getattr(obj, i)))}
        elif inf == 'attr_z':
            return 'Значения атрибутов:', {i: getattr(obj, i) for i in dir(obj) if i[0:2] != '__' and 'method' not in
                                 str(type(getattr(obj, i)))}
        elif inf == 'meth0':
            return 'Немагические методы:', {i: type(getattr(obj, i)) for i in dir(obj) if i[0:2] != '__' and
                    'method' in str(type(getattr(obj, i)))}
        elif inf == 'meth1':
            return 'Все методы:', {i : i for i in dir(obj) if inspect.ismethod(getattr(obj, i))}
        elif inf == 'm_meth':
            return 'Магические методы:', {i: type(getattr(obj, i)) for i in dir(obj) if i[0:2] == '__' and 'method'
                    in str(type(getattr(obj, i)))}
        elif inf == 'm_n_m':
            return 'Не методы, но есть __', {i: type(getattr(obj, i)) for i in dir(obj) if i[0:2] == '__' and 'method'
                    not in str(type(getattr(obj, i)))}
        elif inf == 'modul':
            return 'Модуль объекта', inspect.getmodule(obj)
        elif inf == 'call':
            return 'Вызываемость элементов', {i : callable(getattr(obj, i)) for i in dir(obj)}
        elif inf == 'func':
            return 'Функции:', {i: i for i in dir(obj) if inspect.isfunction(getattr(obj, i))}
        else:
            return {i : (type(getattr(obj, i)), getattr(obj, i)) for i in dir(obj)}, inspect.getmodule(obj)
    else:
        return 'Передан неопознанный параметр'

pprint.pprint(introspection_info(HW_obj))









