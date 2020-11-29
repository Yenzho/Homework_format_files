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


def top_10_word(quantity_dict):
    """
    Возвращает список топ-10 слов из словаря
    """
    number_list_top10 = list()
    for number in quantity_dict.values():
        number_list_top10.append(number)
    number_list_top10.sort(reverse=True)
    words_list_top10 = list()
    for number_10 in number_list_top10[:10]:
        for word, number in quantity_dict.items():
            if number_10 == number:
                while len(words_list_top10) < 11:
                    words_list_top10.append(word)
                    break
    return words_list_top10


def main(document):
    file_extension = os.path.splitext(document)
    common_list = list()
    if '.json' in file_extension:
        common_list = common_list_json_function(document)
    elif '.xml' in file_extension:
        common_list = common_list_xml_function(document)
    else:
        print('Такого расширения пока нет')
    quantity_dict = quantity_dict_function(common_list)
    top_10 = top_10_word(quantity_dict)
    print(top_10)

main('newsafr.json')
main('newsafr.xml')