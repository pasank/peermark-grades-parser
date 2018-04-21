from bs4 import BeautifulSoup
import csv
from time import strftime, localtime

current_time = strftime("%Y-%m-%d-%H-%M-%S", localtime())

root_dir = "C:\\Users\\pkarunaratne\\PycharmProjects\\parse_peer_mark\\"
all_html_file_names = ["frame_1.txt", "frame_2.txt", "frame_3.txt", "frame_4.txt", "frame_5.txt", "frame_6.txt",
                       "frame_7.txt", "frame_8.txt", "frame_9.txt", "frame_10.txt"]
output_file = "peer_review_marks" + "_" + current_time + ".csv"


def parse(html_file):
    html = open(html_file, encoding='utf8').read()
    soup = BeautifulSoup(html, 'html.parser')

    student_names = [student_name.get_text().strip() for student_name in soup.find_all('span', {'class': 'student-name'})]
    total_grades = [total_grade.get_text() for total_grade in soup.find_all('span', {'class': 'total-grade'})]

    student_grades = list(zip(student_names, total_grades))
    print(student_grades)

    with open(output_file, 'a') as f:
        wr = csv.writer(f)

        for student_grade in student_grades:
            wr.writerow(student_grade)


def parse_all_files():
    for html_file_name in all_html_file_names:
        parse(root_dir + html_file_name)

if __name__ == '__main__':
    parse_all_files()