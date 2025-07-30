"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    return [round(score) for score in student_scores]

def count_failed_students(student_scores):
    #return len([score for score in student_scores if score <= 40])
    count = 0
    for i in student_scores:
        if i <= 40:
            count += 1
    return count
def above_threshold(student_scores, threshold):
    return [score for score in student_scores if score >= threshold]

def letter_grades(highest):
    interval = (highest - 40) // 4
    thresholds = []
    for i in range(4):
        score = 41 + i * interval
        thresholds.append(score)
    return thresholds

def student_ranking(student_scores, student_names):
    ranking = []
    for index, (name, score) in enumerate(zip(student_names, student_scores), start=1):
        ranking.append(f"{index}. {name}: {score}")
    return ranking


def perfect_score(student_info):
    for student in student_info:
        name, score = student
        if score == 100:
            return [name, score]
    return []
