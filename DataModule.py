
# coding: utf-8

# In[2]:



# coding: utf-8

# Задания по модулю:
# 
# 0. Решить проблему графической оболочки
# 
# 1.Нужен цикл, для мониторинга и записи в отдельные файлы всего запроса с именем EPOCH ровными промежутками времени для сбора базы данных, на случай необходимости подбора архитектуры модуля AI (получить доступ к серверу для автономии, вести мониторинг две недели?) Какими промежутками?
# 
# 2. Решить проблему автономной работы в принципе
#     Таймер? В модуле AI? Переписать цикл в функцию возвращающую массив и вызывать ее по таймеру в модуле AI?
# 3. Начать работу 
# 

# In[20]:


# Модуль получения данных.

# Импорт дополнений

import CoinDataDictonary
import urllib.request, json 
import time


# In[21]:


# Объявление функций



# Гет запрос получения всех данным по всем валютам
def GETCOIN():
    with urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=0") as url:
        # Все монеты (Гет запрос)
        data = json.loads(url.read().decode())
        # Если нужно получить данные первой монеты: sdata = data[0]
        #print("1 SUCCESS!" + str(data))
        return data

# Получить данные монеты 
def GET_NAME_ID(count, data):
    data_part = data[count]
    Currency_name = data_part['name']
    #print('Присваиваю монете из запроса имя'+str(Currency_name))
    return Currency_name

    
# Получить данные монеты 
def GET_PERCENT(count, data):
    data_part = data[count]
    Currency_percent = data_part['percent_change_1h']
    return Currency_percent

# Получить порядковый номер в базе по ключевому слове
def DATABASE_ID(getname):
    if CoinDataDictonary.CoinDictonary.get(getname) != None:
        Currency_database_number = CoinDataDictonary.CoinDictonary[getname]
        return Currency_database_number

# Получить массив процентного изменения валют за 1 час.
def GET_DATA_ARRAY():
    # Сделать запрос данных и занести в переменную
    Main_data=GETCOIN()

    #Инициализация массива
    Percent_array = [0.0]*1495
    #Запись эпохи в нулевую ячейку
    Percent_array[0]=int(time.time())

    # Цикл заполнения массива значениями процентного изменения 

    for i in range(0,len(Main_data)):
        #Получает имя монеты из запроса
        Name = GET_NAME_ID(i, Main_data)
        #Получает изменение процента
        Percent = GET_PERCENT(i, Main_data)
        #Получает порядковый номер монеты в базе данных
        Database_id = DATABASE_ID(Name)
                
        #if Database_id == None:
			#None
            #print('Не могу найти в базе данное имя, пропускаю')
        if Database_id != None:
        #Записывает значение процентного изменения в ячейку отностельно порядкового номера монеты
            if Percent == None:
                Percent_array[int(Database_id)] = 0.0
                #print('Обнаружен None в ячейке'+Name)
                #print("Заношу "+Name+" в ячейку номер "+Database_id+' как 0')
                

            else:
                Percent_array[int(Database_id)] = Percent
                #print("Заношу "+Name+" в ячейку номер "+Database_id+' как' + Percent)
                #print("Порядковый номер для монеты "+str(Name)+" равен "+Database_id)
    
    return Percent_array


# In[22]:


#Получить данные

#Percent_data_array = GET_DATA_ARRAY()



# In[1]:


#Data_coin_array = GET_DATA_ARRAY()
#print(Data_coin_array)

