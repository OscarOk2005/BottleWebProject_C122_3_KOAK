import json
from datetime import datetime


def createhistory(methodname, data):
    """
    Записывает историю вычислений алгоритмов в файл "calchistory.json".
    """

    try:
        # Пытаемся открыть файл "calchistory.json" для чтения
        with open('calchistory.json', 'r') as read_json:
            # Загружаем данные из файла в словарь history
            history = json.load(read_json)
    except FileNotFoundError:
            # Если файл не найден, создаем новый словарь history с пустыми списками для каждого алгоритма    
            history = {}
            history["Prima"] = []
            history["Daykstra"] = []
            history["Floyda"] = []
            history["Kraskala"] = []
    except:
        # Если возникла неизвестная ошибка, возвращаем сообщение об ошибке
        return "Unknown error"
    
    # Получаем текущую дату и время в формате "YYYY-MM-DD HH:MM:SS"
    current_day = datetime.now()
    string = current_day.strftime('%Y-%m-%d %H:%M:%S')
    
     # Добавляем данные в историю, в зависимости от имени алгоритма
    if(methodname == "Prima"):
        # Если алгоритм Прима, то сохраняем текущую дату и время, список ребер и мст
        history["Prima"].append({"date":string, "edge_list":data[0], "mst":data[1]})
    elif(methodname == "Kraskala"):
        # Если алгоритм Краскала, то сохраняем текущую дату и время, список ребер и мст
        history["Kraskala"].append({"date":string, "edge_list":data[0], "mst":data[1]})
    elif(methodname == "Floyda"):
        # Если алгоритм Флойда, то сохраняем текущую дату и время, исходную матрицу смежности и результирующую матрицу
        history["Floyda"].append({"date":string, "original":data[0], "result":data[1]})
    elif(methodname == "Daykstra"):
        # Если алгоритм Дейкстра, то сохраняем текущую дату и время, исходную матрицу смежности и результирующую матрицу
        history["Daykstra"].append({"date":string, "original":data[0], "result":data[1]})
    
    # Записываем обновленный словарь history в файл "calchistory.json"  
    with open('calchistory.json', 'w') as outfile:
        json.dump(history, outfile, indent = 3)
        

