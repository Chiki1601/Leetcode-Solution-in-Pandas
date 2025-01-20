import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:

            # sort scores by student_id, subject, and exam_date
    df = scores.sort_values(['student_id', 'subject', 'exam_date'])

            # Use groupby and agg to filter for score and latest score
    df = df.groupby(['student_id', 'subject']
          ).agg(first_score = ('score','first'), latest_score = ('score','last')
          ).reset_index()

            # filter for improvement
    return df[df.latest_score > df.first_score]
   
