from datetime import datetime
import time
 
start_time = datetime.now()  # время начала выполнения
 
time.sleep(3)
 
end_time = datetime.now()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения
 
print(f"Время выполнения программы: {execution_time} секунд")