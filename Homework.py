import json
import xml.etree.ElementTree as ET
import os

def common_list_json_function(document):
    """
    Возврашает общий список с повторяющимися переменными из файла .json
    """
    with open(document, encoding='utf-8') as f:
        data = json.load(f)
        common_list = list()
        for item in data['rss']['channel']['items']:
            description = item['description'].split(' ')
            for element in description:
                if len(element) >= 6 and type(element) != int():
                    common_list.append(element)
        return common_list


def common_list_xml_function(document):
    """
    Возврашает общий список с повторяющимися переменными из файла .xml
    """
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(document, parser)
    root = tree.getroot()
    common_list = list()
    for item in root.findall('channel/item'):
        description = item.find('description').text.split(' ')
        for element in description:
            if len(element) >= 6 and type(element) != int():
                common_list.append(element)
    return common_list


def quantity_dict_function(common_list):
    """
    Возврашает словарь ключ-элемент common_list, значение-количество повторений
    """
    quantity_dict = dict()
    for element in common_list:
        quantity_dict[element] = quantity_dict.get(element, 0) + 1
    return quantity_dict


def top_word(quantity_dict, quantity):
    """
    Возвращает список топ слов из словаря
    """
    number_list_top = list()
    for number in quantity_dict.values():
        number_list_top.append(number)
    number_list_top.sort(reverse=True)
    words_list_top = list()
    for number_top in number_list_top[:quantity]:
        for word, number in quantity_dict.items():
            if number_top == number:
                while len(words_list_top) < quantity  + 1:
                    words_list_top.append(word)
                    break
    return words_list_top


def main(document, quantity):
    file_extension = os.path.splitext(document)
    common_list = list()
    if '.json' in file_extension:
        common_list = common_list_json_function(document)
    elif '.xml' in file_extension:
        common_list = common_list_xml_function(document)
    else:
        print('Такого расширения пока нет')
    quantity_dict = quantity_dict_function(common_list)
    top = top_word(quantity_dict, quantity)
    print(top)

main('newsafr.json', 15)
main('newsafr.xml', 14)