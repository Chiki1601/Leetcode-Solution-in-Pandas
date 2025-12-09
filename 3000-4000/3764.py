import pandas as pd

def topLearnerCourseTransitions(courses: pd.DataFrame) -> pd.DataFrame:

    courses = courses.fillna(4)
    courses['ave'] = courses.groupby('user_id')['course_rating'].transform('mean')
    courses['cnt'] = courses.groupby('user_id')['course_rating'].transform('count')
    courses.sort_values(['user_id', 'completion_date'], inplace = True)
    courses['second_course'] = courses.course_name.shift(-1)

    courses = (courses.loc[(courses.ave >= 4) & (courses.cnt >= 5)]
                      .loc[courses.user_id == courses.user_id.shift(-1)]
                      .rename(columns = {'course_name':'first_course'})
                      .groupby(['first_course', 'second_course'])
                      .size().reset_index(name = 'transition_count'))

    courses['lower1'] = courses.first_course.str.lower()
    courses['lower2'] = courses.second_course.str.lower()

    return (courses.sort_values(['transition_count', 'lower1', 'lower2'],
                                    ascending = [0,1,1]).iloc[:,[0,1,2]])
