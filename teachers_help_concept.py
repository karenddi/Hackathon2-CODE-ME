names = ["Anna", "Tom"]  # get and process input for a list of names
tasks = [2, 3]  # get and process input for a list of the number of tasks
grades = [4, 3]  # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} tasks left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for names, tasks, grades in zip(names, tasks, grades):
    print(message.format(names, tasks, grades, int(grades) + 1))







# write a for loop that iterates through each set of names, tasks, and grades to print each student's message
# use functions to keep everything clear