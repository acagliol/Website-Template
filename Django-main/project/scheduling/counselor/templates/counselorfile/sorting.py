from flask import Flask, render_template
import sqlite3
import random

app = Flask(__name__)

def generate_teacher_names_by_department(cursor, department_name): 
    query = f"SELECT Teacher_Name FROM TEACHERS WHERE Department_1 = '{department_name}'" 
    cursor.execute(query) 
    result = cursor.fetchall() 
    teacher_names = [row[0] for row in result] 
    return teacher_names

def fetch_course_data(cursor, table_name):
    query = f'SELECT Course_Name FROM {table_name}' 
    cursor.execute(query)
    result = cursor.fetchall()
    course_data = [row[0] for row in result]
    return course_data

def assign_courses_to_periods(course_data, num_periods, department_name):
    random.shuffle(course_data)
    num_courses = len(course_data)
    period_course_mapping = {}

    for i in range(1, num_periods + 1):
        if department_name != 'ACC' and i == 7:  
            period_course_mapping[i] = 'Conference'
        elif department_name != 'ACC' and i == 8: 
            period_course_mapping[i] = 'Collaborative'
        elif i <= num_courses:
            period_course_mapping[i] = course_data[i - 1]
        else:
            period_course_mapping[i] = ''

    return period_course_mapping

def create_mini_schedule(department_name, periods, teacher_names, period_course_mapping, course_data):
    schedule = [[department_name] + periods]
    for teacher in teacher_names:
        schedule_row = [teacher]
        
        if department_name != 'ACC':
            period_course_mapping = assign_courses_to_periods(course_data, num_periods=8, department_name=department_name)
        
        course_order = list(period_course_mapping.values())
        random.shuffle(course_order)
        schedule_row.extend(course_order)
        schedule.append(schedule_row)
    return schedule


@app.route('/')
def index():
    try:
        sqliteConnection = sqlite3.connect('scheduling/counselor/templates/counselorfile/Everything we need/DB/database (1).db')
        cursor = sqliteConnection.cursor()
        print('Connected to DataBase')

        departments = {
            'ACC': 'ACC',
            'ATH': 'ATH',
            'CTE': 'CTE',
            'MATH': 'MATH',
            'SCI': 'SCI',
            'SOCIAL_STUDIES': 'SOCIAL_STUDIES',
            'WORLD_LANG': 'WORLD_LANG',
            'ENG': 'ENG',
            'FINE_ART': 'FINE_ART',
            'SPED': 'SPED',
        }

        all_schedules = {}

        for department_name, table_name in departments.items():
            num_teachers = 8 

            teacher_names = generate_teacher_names_by_department(cursor, department_name)

            course_data = fetch_course_data(cursor, table_name)

            period_course_mapping = assign_courses_to_periods(course_data, num_periods=8, department_name=department_name)

            schedule = create_mini_schedule(department_name, [f'{i + 1}st Period' for i in range(8)], teacher_names, period_course_mapping, course_data)

            all_schedules[department_name] = schedule

        cursor.close()

    except sqlite3.Error as error:
        print('Error occurred - ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Sqlite Connection closed')

    return render_template('test.html', schedules=all_schedules)

if __name__ == '__main__':
    app.run(debug=True)