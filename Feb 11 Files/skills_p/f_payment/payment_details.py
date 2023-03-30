import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from f_course import course_details

def a_payment():
    print("this is my payment details")

course_details.a_course()