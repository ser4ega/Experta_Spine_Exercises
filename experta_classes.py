from experta import *

# Определяем факты
class Person(Fact):
    # возраст
    age = Field(int)
    # вес
    weight = Field(int)
    # рост
    height = Field(int)
    # уровень подготовки
    level = Field(str)
    # заболевание тренировок
    desease = Field(str)

class Exercise(Fact):
    # название упражнения
    exercise_name = Field(str, mandatory=False)
    # описание упражнения
    description = Field(str, mandatory=False)
    # подходящий возрастной период "a;b"
    exercise_age = Field(str, mandatory=False)
    # подходящий рост "a;b"
    exercise_height = Field(str, mandatory=False)
    # необходимое оборудование
    equipments = Field(str, mandatory=False)
    # вес, используемый при выполнении упражнения
    exercise_weight = Field(str, mandatory=False)
    # уровень сложности
    exercise_level = Field(str, mandatory=False)
    # ID упражнения
    exercise_id = Field(int, mandatory=False)
    



# # Определяем правила
class HealthExpertSystem(KnowledgeEngine):
    Common_recommends = []
    # def __init__(self):
    #     self.Common_recommends = []

    @Rule(Person(age=P(lambda x: x < 18)))
    def too_young(self):
        recom = "Вы слишком молоды для тренировок с весами. Если вы все же хотите заниматься с железом - проконсультируйтесь с врачом"
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)

    @Rule(Person(desease='Остеохондроз шейного отдела'))
    def rule1(self):
        recom = "С вашим заболеванием  следует выполнять упражнения на растяжение и расслабление мышц шеи, повороты и наклоны головы, массаж шейно-воротниковой зоны."
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Шейный спондилоз'))
    def rule2(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на укрепление мышц шеи и верхней части спины, избегать резких движений головой, использовать ортопедический валик или подушку.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Шейный радикулит'))
    def rule3(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на снятие воспаления и боли в шее, применять компрессы или обезболивающие мази, избегать физического перенапряжения.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Шейный миозит'))
    def rule4(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на согревание и расслабление мышц шеи, избегать сквозняков и переохлаждения, носить теплый шарф или воротник.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Остеохондроз грудного отдела'))
    def rule5(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на развитие гибкости и подвижности позвоночника, повороты и наклоны туловища, упражнения для дыхательной системы.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Грудной спондилоз'))
    def rule6(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на укрепление мышц спины и грудной клетки, избегать нагрузок на позвоночник, использовать корсет или пояс.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Грудной радикулит'))
    def rule7(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на снятие воспаления и боли в спине, применять компрессы или обезболивающие мази, избегать физического перенапряжения.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Грудной миозит'))
    def rule8(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на согревание и расслабление мышц спины и груди, носить теплую одежду, избегать сквозняков и переохлаждения.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Остеохондроз поясничного отдела'))
    def rule9(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на растяжение и расслабление мышц поясницы, прогибы и противопрогибы туловища, массаж пояснично-крестцовой зоны.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Поясничный спондилоз'))
    def rule10(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на укрепление мышц поясницы и живота, избегать нагрузок на позвоночник, использовать корсет или пояс.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Поясничный радикулит'))
    def rule11(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на снятие воспаления и боли в пояснице, применять компрессы или обезболивающие мази, избегать физического перенапряжения")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Поясничный миозит'))
    def rule12(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на согревание и расслабление мышц поясницы, носить теплую одежду, избегать сквозняков и переохлаждения.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Артроз крестцово-подвздошного сустава'))
    def rule13(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на развитие подвижности и гибкости сустава, круговые движения тазом, наклоны в стороны и вперед-назад.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Воспаление крестцово-подвздошного сустава'))
    def rule14(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на снятие воспаления и боли в суставе, применять компрессы или противовоспалительные мази, избегать нагрузок на сустав.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Травма крестцово-подвздошного сустава'))
    def rule15(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на восстановление функции сустава, применять иммобилизацию или фиксацию сустава, обратиться к врачу.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Сакролиит'))
    def rule16(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на укрепление мышц спины и таза, избегать нагрузок на позвоночник, использовать антибактериальную терапию.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Боли в сакральной области, вызванные мышечным напряжением или дисбалансом мышц'))
    def rule17(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на расслабление и растяжение мышц таза и поясницы, применять массаж или акупунктуру, корректировать осанку и позу.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Слабость мышц в сакральной области, связанная с дегенеративными изменениями или травмами'))
    def rule18(self):
        recom = ("С вашим заболеванием следует выполнять упражнения на укрепление и стимуляцию мышц таза и поясницы, применять физиотерапию или электростимуляцию, использовать ортопедические приспособления.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Профилактика болезней позвоночника и суставов'))
    def rule19(self):
        recom = ("Следует выполнять комплекс обще-развивающих упражнений для всех частей тела, чередовать упражнения скоростно-силового, силового, гибкостного и выносливостного характера, заканчивать комплекс упражнениями на расслабление.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease='Не указана'))
    def rule20(self):
        recom = ("Нужно подбирать упражнения индивидуально в зависимости от диагноза и стадии заболевания, согласовывать комплекс с лечащим врачом.")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)
    @Rule(Person(desease=MATCH.desease))
    def rule0(self,desease):
        if desease == "Отсутствует":
            recom = ('Вы хотите заняться профилактикой заболеваний позвоночника.')    
        elif desease == 'Не указана':
            recom = ('Ваша болезнь неизвестна. Пожалуйста, не занимайтесь самолечением.')
        else:
            recom = (f"У вас заболевание {desease}")
        if recom not in self.Common_recommends:
            self.Common_recommends.append(recom)
        print(recom)

    @Rule(Person(height=MATCH.height),
          Exercise(exercise_age=MATCH.exercise_age,
                   exercise_name=MATCH.exercise_name,
                   description = MATCH.description,
                    exercise_height = MATCH.exercise_height,
                    equipments = MATCH.equipments,
                    exercise_weight = MATCH.exercise_weight,
                    exercise_level = MATCH.exercise_level,
                    exercise_id = MATCH.exercise_id                   
                   ))
    def delete_exercise_from_height(self, height, exercise_age,exercise_name,description,exercise_height,equipments,exercise_weight,exercise_level,exercise_id):
        if not is_height_in_range(height, exercise_height):
            fact_to_remove = Exercise(exercise_name=exercise_name,
                                        exercise_age=exercise_age,                         
                                        description = description,
                                        exercise_height = exercise_height,
                                        equipments = equipments,
                                        exercise_weight = exercise_weight,
                                        exercise_level = exercise_level,
                                        exercise_id = exercise_id
                                      )
            # all_facts = [f[1] for f in self.facts.items()]
            i=0
            mutated = True            
            while mutated:
                mutated = False
                for l_fact in self.facts.items():
                    if isinstance(l_fact[1], Exercise):
                        if is_exes_eq(fact_to_remove,l_fact[1]):
                            # print('До удаления:')
                            # show_exercises(self)
                            self.facts.pop(i)
                            print('\n\n')
                            print(f"Удалено упражнение с возрастным интервалом: {exercise_age}")
                            mutated = True
                            break
                            # print('После удаления:')
                            # show_exercises(self)
                    i=i+1



    @Rule(Person(weight=MATCH.weight),
          Exercise(exercise_age=MATCH.exercise_age,
                   exercise_name=MATCH.exercise_name,
                   description = MATCH.description,
                    exercise_height = MATCH.exercise_height,
                    equipments = MATCH.equipments,
                    exercise_weight = MATCH.exercise_weight,
                    exercise_level = MATCH.exercise_level,
                    exercise_id = MATCH.exercise_id                   
                   ))
    def delete_exercise_from_weight(self, weight, exercise_age,exercise_name,description,exercise_height,equipments,exercise_weight,exercise_level,exercise_id):
        if not is_weight_in_range(weight, exercise_weight):
            fact_to_remove = Exercise(exercise_name=exercise_name,
                                        exercise_age=exercise_age,                         
                                        description = description,
                                        exercise_height = exercise_height,
                                        equipments = equipments,
                                        exercise_weight = exercise_weight,
                                        exercise_level = exercise_level,
                                        exercise_id = exercise_id
                                      )
            # all_facts = [f[1] for f in self.facts.items()]
            i=0
            mutated = True            
            while mutated:
                mutated = False
                for l_fact in self.facts.items():
                    if isinstance(l_fact[1], Exercise):
                        if is_exes_eq(fact_to_remove,l_fact[1]):
                            # print('До удаления:')
                            # show_exercises(self)
                            self.facts.pop(i)
                            print('\n\n')
                            print(f"Удалено упражнение с возрастным интервалом: {exercise_age}")
                            mutated = True
                            break
                            # print('После удаления:')
                            # show_exercises(self)
                    i=i+1


    @Rule(Person(level=MATCH.level),
          Exercise(exercise_age=MATCH.exercise_age,
                   exercise_name=MATCH.exercise_name,
                   description = MATCH.description,
                    exercise_height = MATCH.exercise_height,
                    equipments = MATCH.equipments,
                    exercise_weight = MATCH.exercise_weight,
                    exercise_level = MATCH.exercise_level,
                    exercise_id = MATCH.exercise_id                   
                   ))
    def delete_exercise_from_level(self, level, exercise_age,exercise_name,description,exercise_height,equipments,exercise_weight,exercise_level,exercise_id):
        if not is_level_in_range(level, exercise_level):
            fact_to_remove = Exercise(exercise_name=exercise_name,
                                        exercise_age=exercise_age,                         
                                        description = description,
                                        exercise_height = exercise_height,
                                        equipments = equipments,
                                        exercise_weight = exercise_weight,
                                        exercise_level = exercise_level,
                                        exercise_id = exercise_id
                                      )
            # all_facts = [f[1] for f in self.facts.items()]
            i=0
            mutated = True            
            while mutated:
                mutated = False
                for l_fact in self.facts.items():
                    if isinstance(l_fact[1], Exercise):
                        if is_exes_eq(fact_to_remove,l_fact[1]):
                            # print('До удаления:')
                            # show_exercises(self)
                            self.facts.pop(i)
                            print('\n\n')
                            print(f"Удалено упражнение с возрастным интервалом: {exercise_age}")
                            mutated = True
                            break
                            # print('После удаления:')
                            # show_exercises(self)
                    i=i+1



# class MyExpertSystem(KnowledgeEngine):
    @Rule(Person(age=MATCH.age),
          Exercise(exercise_age=MATCH.exercise_age,
                   exercise_name=MATCH.exercise_name,
                   description = MATCH.description,
                    exercise_height = MATCH.exercise_height,
                    equipments = MATCH.equipments,
                    exercise_weight = MATCH.exercise_weight,
                    exercise_level = MATCH.exercise_level,
                    exercise_id = MATCH.exercise_id                   
                   ))
    def delete_exercise(self, age, exercise_age,exercise_name,description,exercise_height,equipments,exercise_weight,exercise_level,exercise_id):
        if not is_age_in_range(age, exercise_age):
            fact_to_remove = Exercise(exercise_name=exercise_name,
                                        exercise_age=exercise_age,                         
                                        description = description,
                                        exercise_height = exercise_height,
                                        equipments = equipments,
                                        exercise_weight = exercise_weight,
                                        exercise_level = exercise_level,
                                        exercise_id = exercise_id
                                      )
            # all_facts = [f[1] for f in self.facts.items()]
            i=0
            mutated = True            
            while mutated:
                mutated = False
                for l_fact in self.facts.items():
                    if isinstance(l_fact[1], Exercise):
                        if is_exes_eq(fact_to_remove,l_fact[1]):
                            # print('До удаления:')
                            # show_exercises(self)
                            self.facts.pop(i)
                            print('\n\n')
                            print(f"Удалено упражнение с возрастным интервалом: {exercise_age}")
                            mutated = True
                            break
                            # print('После удаления:')
                            # show_exercises(self)
                    i=i+1

           

def is_age_in_range(age, age_range):
    min_age, max_age = map(int, age_range.split(';'))
    return min_age <= age <= max_age

def is_weight_in_range(weight, weight_range):
    min_weight, max_weight = map(int, weight_range.split(';'))
    return min_weight <= weight <= max_weight

def is_height_in_range(height, height_range):
    min_height, max_height = map(int, height_range.split(';'))
    return min_height <= height <= max_height

def is_level_in_range(level, exercise_level):
    if level == 'Начальный':
        return  (level in exercise_level.split(' '))
    if level == 'Средний':
        return  ((level in exercise_level.split(' ')) or ('Начальный' in exercise_level.split(' ')))
    if level == 'Высокий':
        return True

def is_exes_eq(self, other):
        if isinstance(other, Exercise) and isinstance(self, Exercise):
            for  field_value in self:#zip(self.__dict__.items(),other.__dict__.items()):
                if field_value in other:
                    # print(f"self[{field_value}]:{self[field_value]}??other[{field_value}]:{other[field_value]}")
                    if self[field_value]!=other[field_value]:
                        # print(f"self[{field_value}]:{self[field_value]}!=other[{field_value}]:{other[field_value]}")
                        return False
                    
            return True


# engine = HealthExpertSystem()
# engine.reset()
# engine.declare(Person(age=25))
# engine.declare(Exercise(exercise_name='Упражнение 1',
#                          exercise_age='18;30',                         
#                         description = "qweqweqwe",
#                         exercise_height = "0;9000",
#                         equipments = '0',
#                         # exercise_weight = 0,
#                         exercise_level = 'Начинающий',
#                         exercise_id = 1
#                          ))
# engine.declare(Exercise(exercise_name='Упражнение 2', 
#                         exercise_age='40;50',
#                         description = "qweqweqwe",
#                         exercise_height = "0;9000",
#                         equipments = '0',
#                         exercise_weight = 0,
#                         exercise_level = 'Начинающий',
#                         exercise_id = 2
#                         ))



def show_exercises(engine):
    # Выводим список упражнений и их атрибутов
    exercises = engine.facts
    # print('Число фактов:',len(exercises))
    # for exercise in [f[1] for f in exercises.items()]:
        
        # if isinstance(exercise, Exercise) :
                # print('-------------------------------------------')
                # for  field_value in exercise:
                        # print(f"self[{field_value}]:{exercise[field_value]}")
# engine.run()


# print('end')