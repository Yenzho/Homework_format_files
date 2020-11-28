def common_list_json_function(document):
    '''
    Возврашает общий список с повторяющимися переменными из файла .json
    '''
    pass

def common_list_xml_function(document):
    '''
    Возврашает общий список с повторяющимися переменными из файла .xml
    '''
    pass

def quantity_dict_function(common_list):
    '''
    Возврашает словарь ключ-элемент common_list, значение-количество повторений
    '''
    pass

def top_10_word(quantity_dict):
    '''
    Возвращает список топ-10 слов из словаря
    '''
    quantity_dict = quantity_dict_function
    pass

def main():
    common_list_json = common_list_json_function('newsafr.json')
    common_list_xml = common_list_xml_function('newsafr.xml')
    quantity_dict_json = quantity_dict_function(common_list_json)
    quantity_dict_xml = quantity_dict_function(common_list_xml)
    top_10_word_json  = top_10_word(quantity_dict_json)
    top_10_word_xml = top_10_word(quantity_dict_xml)
    print(top_10_word_json)
    print(top_10_word_xml)
main()