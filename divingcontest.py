def calculate_score(judge_scores):
    return judge_scores[0] + judge_scores[1] + judge_scores[2]

judge_scores = (10, 10, 10)
print (calculate_score(judge_scores))