from numpy.ma.extras import average


def evaluate_performance(punctuality,task_completion,teamwork,innovation):
    score=0

    # step1: punctuality
    if punctuality=='excellent':
        score+=3
    elif punctuality=='good':
        score+=2
    elif punctuality=='Average':
        score+=1


    # step 2:task_completion
    if task_completion>=90:
        score+=3
    elif task_completion>=75:
        score+=2
    elif task_completion>=50:
        score+=1

    # step 3: teamwork
    if teamwork=='excellent':
        score+=3
    elif teamwork=='good':
        score+=2
    elif teamwork=='Average':
        score+=1

    #step4:Innovation
    if innovation=='high':
        score+=3
    elif innovation=='medium':
        score+=2
    elif innovation=='low':
        score+=1

    #Final Evaluation
    if score>=10:
        return "Outstanding Performance"

    elif score>=7:
        return "Average Performance"
    elif score>=4:
        return "Below Average Performance"
    else:
        "Needs Improvement"

# Example
print("Employee Performance evaluation system")
punctuality=input("Enter punctuality(excellent/good/average)").lower()
task_completion=int(input("Enter task completion percentage"))
teamwork=input("Enter teamwork(excellent/good/average)").lower()
innovation=input("Enter innovation(high/medium/low)").lower()

result=evaluate_performance(punctuality,task_completion, teamwork,innovation)
print(f"Final Evaluation:{result}")

