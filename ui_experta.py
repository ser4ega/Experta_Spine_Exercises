from tkinter import *
from tkinter.ttk import Combobox
import sqlite3
from ExportFromExcel import refresh_bd_from_excel
from experta_classes import Person, Exercise, HealthExpertSystem,is_age_in_range,is_exes_eq,show_exercises








# обновим БД из эксель-файла
refresh_bd_from_excel()

# получим список болезней
conn = sqlite3.connect('exercises.db')
cursor = conn.cursor()
cursor.execute("SELECT desease FROM spine_deseases")
deseases=tuple(des[0] for des in cursor.fetchall())
conn.commit()
conn.close()

buttons = []
recom_labels = []
root = Tk()

# root.geometry('400x200')
root.title('Экспертная система')

age_label = Label(root, text="Возраст в годах:")
age_label.grid(row=0)
age_entry = Entry(root)
age_entry.grid(row=0, column=1)

weight_label = Label(root, text="Вес в кг:")
weight_label.grid(row=1)
weight_entry = Entry(root)
weight_entry.grid(row=1, column=1)

height_label = Label(root, text="Рост в см:")
height_label.grid(row=2)
height_entry = Entry(root)
height_entry.grid(row=2, column=1)

level_label = Label(root, text="Уровень подготовки:")
level_label.grid(row=3)
level_combo = Combobox(root)
level_combo['values'] =['Начальный','Средний','Высокий']
level_combo.current(0)
level_combo.grid(row=3, column=1)


desease_label = Label(root, text="Заболевание позвоночника:")
desease_label.grid(row=4)
combo = Combobox(root)
combo['values'] =deseases
combo.current(0)
combo.grid(row=4, column=1)

def submit():
    age = age_entry.get()
    weight = weight_entry.get()
    height = height_entry.get()
    desease = combo.get()
    level = level_combo.get()


    conn = sqlite3.connect('exercises.db')
    cursor = conn.cursor()
    cursor.execute(f'select id, id_section, recommends from spine_deseases where desease = "{desease}"')
    rows = cursor.fetchall()
    des_id, id_section, recommends = rows[0]
    # id_section = cursor.fetchall()[0][1]
    # recommends = cursor.fetchall()[0][2]
    cursor.execute(f'select id_effect from rel_deseases_effects where id_desease = {des_id}')
    effect_ids = cursor.fetchall()
    exercise_ids = []
    exercise_names = []
    descriptions = []
    effect_ids_row=''
    for effect_id in effect_ids:
        effect_ids_row=effect_ids_row   + '"'+  str(effect_id[0])+'", '
    effect_ids_row = effect_ids_row[:-2]
    # выбираем упражнения подходящие по области воздействия и оказываемому эффекту, либо те, что рекомендовал эксперт
    query = f'''select distinct
                        exercise_id, 
                        exercise_name, 
                        description 
                        from exercises_rel_deseases 
                        where 
                        spine_section_id = "{id_section}"
                        AND effect_id in ({effect_ids_row})
                        OR desease_id = "{des_id}"
                        '''
    # print(query)
    cursor.execute(query)
    
    rows = cursor.fetchall()
    for row in rows:
        exercise_id, exercise_name, description = row
        exercise_ids.append(exercise_id)
        exercise_names.append(exercise_name)
        descriptions.append(description)

        # print(exercise_id, exercise_name)
    # Собран список упражнений по заболеванию
    # Осталось применить правила по аттрибутам пользователя:
        
    #     Вес
    #     Возраст
    #     Рост
    #     Уровень подготовки   
    # А также сообщить о необходимом оборудовании оборудования

    # Выберем из БД ограничения:
    exercises_ids_row=''
    for exercise_id in exercise_ids:
        exercises_ids_row=exercises_ids_row   +  str(int(exercise_id))+', '
    exercises_ids_row = exercises_ids_row[:-2]
    query = f'''select 
                         
                        weight, 
                        age,
                        height,
                        level,
                        equipment
                        from exercises_attr 
                        where id in ({exercises_ids_row})
                        '''
    # print(query)
    cursor.execute(query)
    rows = cursor.fetchall()
    exercise_weights = [] #массивы совпадают по индексации с exercise_ids,  exercise_names,  descriptions
    exercise_ages = []
    exercise_heights = []
    exercise_levels = []
    exercise_equipments = []
    for row in rows:
        exercise_weight, exercise_age, exercise_height, exercise_level, exercise_equipment = row
        exercise_weights.append(exercise_weight)
        exercise_ages.append(exercise_age)
        exercise_heights.append(exercise_height)
        exercise_levels.append(exercise_level)
        exercise_equipments.append(exercise_equipment)


    # Также сообщить о необходимом оборудовании оборудования
    engine = HealthExpertSystem()
    engine.Common_recommends = []
    engine.reset()
    if age == '':
        age = 0
    if weight == '':
        weight = 200
    if height == '':
        height = 250
    if desease == '':
        desease = 'Не указана'

    engine.declare(Person(age=int(age),
                          weight = int(weight),
                          height = int(height),
                          level = level,
                          desease = desease
                          ))
    for i in range(len(exercise_names)):
        engine.declare(Exercise(exercise_name=exercise_names[i],
                                exercise_age=exercise_ages[i],                         
                                description = descriptions[i],
                                exercise_height = exercise_heights[i],
                                equipments = exercise_equipments[i],
                                exercise_weight = exercise_weights[i],
                                exercise_level = exercise_levels[i],
                                exercise_id = exercise_ids[i]
                                ))
    engine.run()
    show_exercises(engine)

    print(f"Ваш возраст: {age}, ваш вес: {weight}, ваш рост: {height}, заболевание позвоночника: {desease}")
    # print('qqqqqqqqqqqqqqqqq',engine.Common_recommends)
    start_row = 9
    orig_start_row = start_row

    if len(recom_labels)>0:
        for rec_lbl in recom_labels:
            rec_lbl.destroy()

            # recom_labels.pop()
        recom_labels.clear()

    for recom in engine.Common_recommends:
        recom_labels.append(Label(root, text= recom, anchor = 'w', wraplength=500, font=("Arial", 14)))
        recom_labels[start_row-orig_start_row].grid(row=start_row, column=0,columnspan=2, sticky="w")
        start_row=start_row+1
    
    form_exs_list_exercises(engine,start_row+2)

def form_exs_list_exercises(engine,start_row):
        
        global buttons
        orig_start_row = start_row
        # Выводим список упражнений и их атрибутов
        exercises = engine.facts
        # print('Число фактов:',len(exercises))
        
        if len(buttons)>0:
             for butn in buttons:
                  butn.grid_forget()
        buttons = []
        exercise_dict = {}
        for exercise in [f[1] for f in exercises.items()]:
            if isinstance(exercise, Exercise):
                    exercise_dict[exercise['exercise_name']] = exercise
                    # buttons.append(Button(root, text=exercise['exercise_name'], command=lambda: open_window(exercise)))
                    buttons.append(Button(root, text=exercise['exercise_name']))
                    buttons[start_row-orig_start_row].grid(row=start_row, column=0, columnspan=2, sticky="nsew")
                    buttons[start_row-orig_start_row].bind("<Button-1>", lambda event: my_function(event, exercise_dict))
                    start_row = start_row +1   
                    # for  field_value in exercise:
                        

                            # print(f"self[{field_value}]:{exercise[field_value]}")

        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)

def my_function(event,exercise_dict):
    # print(event.widget["text"])
    open_window(exercise_dict[event.widget["text"]])

def open_window(exercise):
    # info = button.grid_info()
    # row = info["row"]
    new_window = Toplevel(root)
    # root.maxsize(600, 800)
    new_window.title(exercise['exercise_name'])
    # new_window.geometry("200x200")
    start_row = 3
    # print(exercise)
    for  field_value in exercise:
        Label(new_window, text= str(field_value).replace("None", "")+' : '+str(exercise[field_value]).replace("None", ""), anchor = 'w', wraplength=500).grid(row=start_row, column=0, sticky="w")
        start_row=start_row+1

    

    new_window.mainloop()


Button(root, text='Подтвердить данные', command=submit).grid(row=5, column=0, pady=4)
# Button(root, text='Выход', command=root.quit).grid(row=4, column=1)

root.mainloop()