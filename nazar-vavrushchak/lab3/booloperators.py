# average_score = 85
# has_failed_exams = False
#
# if average_score >= 85 and not has_failed_exams:
#     print("You get scholarship")
# else:
#     print("Try to do better next year")

average_score = 85
has_debts = False
is_olympiad_winner = False

if (average_score >= 85 and not has_debts) or is_olympiad_winner:
    print("Great job")
else:
    print("Try to do better next year")