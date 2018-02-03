
# coding: utf-8

# In[ ]:


# Главная оболочка серверного мониторинга
# Добавить запись гет запроса в файл


# In[1]:


import DataModule
import time
import csv
import os


# In[2]:


# Объявление переменных

# Время между запросами
timerequest = 600
DataFileCsv = 'data/checkpoints.csv'


# In[3]:


# Набор Функций 

# Проверка наличия базы
def CHECK_DATA():
    DataPath = os.path.exists(DataFileCsv)
    if DataPath:
        print('База данных существует!')
    else:
        print('База данных не обнаружена')
    return DataPath

# Функция получения крайнего чекпоинта 
def GET_LAST_CHECKPOINT():
    #Открыть файл
    with open(DataFileCsv, 'r') as fp:
        # Прочитать файл
        reader = csv.reader(fp)
        # Занести в массив
        data_read = [row for row in reader]
    # Получить последнее значение в списке в формате list
    last_checkpoint_list_unit = str(data_read[len(data_read)-1])
    # Конвертировать в формат целочисленного значения
    last_checkpoint= int(last_checkpoint_list_unit[2:-2])
    # Вернуть значение последнего известного чекпоинта 
    return last_checkpoint

# Функция сравнивания
def DATA_MEGERING(current_time, last_checkpoint):
    # Получить значение разницы
    CheckpointMegering = current_time - last_checkpoint
    print('Разница составляет '+str(CheckpointMegering))
    return CheckpointMegering

# Текущее время
def CURRENT_TIME():
    current_time=int(time.time())
    return current_time

# Функция записи данных в базу
def ADD_DATA(checkpoint_csv):
    # Квадратные скобки для того что бы не было ошибки. Не благодари :)
    current_checkpoint=[CURRENT_TIME()]
    with open(checkpoint_csv, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(current_checkpoint)
        print(' Чекпоинт записан!')
    MainDataFile = open('data/'+str(CURRENT_TIME())+'.txt','w')
    MainDataFile.write(str(DataModule.GETCOIN()))
    MainDataFile.close()
    # Перезапустить таймер
    CHECK_TIMER(timerequest)

# Таймер 
def CHECK_TIMER(timertime):
    # Время таймера
    timer_time = timertime
    current_time=0
    #Таймер проверки. Пока разница между текущим временем и чекпоинтом заданого времени таймера 
    while (current_time - GET_LAST_CHECKPOINT()) < timerequest :
        current_time=CURRENT_TIME()
        #print(current_time)
        print('.', end='')
        time.sleep(1)
    # Записать новый чекпоинт в базу
    ADD_DATA(DataFileCsv)
    


# In[4]:


# Основное тело программы (добавить в цикл?)

# Если база данных найдена
if CHECK_DATA():
    # Если последний чекпоинт больше нуля
    if GET_LAST_CHECKPOINT() > 0:
        # Сравнить текущее время и чекпоинт. 
        # Если меньше чем необходимый промежуток времени:
        if DATA_MEGERING(CURRENT_TIME(),GET_LAST_CHECKPOINT()) < timerequest:
            print('Время не пришло')
            # Запуск таймера с разницей
            CHECK_TIMER(DATA_MEGERING(CURRENT_TIME(),GET_LAST_CHECKPOINT()))
            print('Готово!')
        else: 
            print('Время прошло!')
            ADD_DATA(DataFileCsv)
    # Если отсутствует первый чекпоинт        
    if GET_LAST_CHECKPOINT() <= 0:
        print('Отсутствует первый чекпоинт. Записываю и запускаю таймер')
        ADD_DATA(DataFileCsv)
        
# Тут прописать создание базы данных
else:
    print('Ошибка базы данных')


# In[27]:


ADD_DATA(DataFileCsv)


# In[10]:


# Функция создания новой записи в базу csv и нового файла

# Новый чекпоинт
getcheckpoint = int(time.time())
# Файл с чепоинтами
get_checkpoint_csv = "data/checkpoints.csv"

# Функция записи данных в базу
def ADD_DATA(checkpoint, checkpoint_csv):
    current_checkpoint=[checkpoint]
    with open(checkpoint_csv, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(current_checkpoint)
    
    
    
    
ADD_DATA(getcheckpoint,get_checkpoint_csv)    


# In[31]:


# Таймер 

def CHECK_TIMER(timertime):
    # Чекпоинт из файла csv
    last_checkpoint=int(time.time())
    # Время таймера
    timer_time = timertime
    current_time=0
    #Таймер проверки. Пока разница между текущим временем и чекпоинтом заданого времени таймера 
    while (current_time - last_checkpoint) < timer_time :
        current_time=int(time.time())
        print(current_time)
        time.sleep(1)


# In[106]:


print(os.path.exists('data/checkpoints.csv'))


# In[54]:


# Проверка наличия базы

def CHECK_DATA():
    DataPath = os.path.exists('data/checkpoints.csv')
    if DataPath:
        print('База данных существует!')
    else:
        print('База данных не обнаружена')
    return DataPath


# In[100]:


# Функция получения крайнего чекпоинта 

def GET_LAST_CHECKPOINT():
    #Открыть файл
    with open('data/checkpoints.csv', 'r') as fp:
        # Прочитать файл
        reader = csv.reader(fp)
        # Занести в массив
        data_read = [row for row in reader]
    # Получить последнее значение в списке в формате list
    last_checkpoint_list_unit = str(data_read[len(data_read)-1])
    # Конвертировать в формат целочисленного значения
    last_checkpoint= int(last_checkpoint_list_unit[2:-2])
    # Вернуть значение последнего известного чекпоинта 
    return last_checkpoint
    
GET_LAST_CHECKPOINT()


# In[105]:


# Функция сравнения чекпоинта и текущего времени

current_time=int(time.time())
last_checkpoint=GET_LAST_CHECKPOINT()

def DATA_MEGERING():
    # Получить значение разницы
    CheckpointMegering = current_time - last_checkpoint
    return CheckpointMegering
    
DATA_MEGERING()


# In[42]:


open(str(CURRENT_TIME())+'.txt','w')


# In[ ]:


close()


# In[30]:


print(DataModule.GETCOIN())

