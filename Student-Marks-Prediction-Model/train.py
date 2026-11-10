
# Multiple Input Student Marks Prediction
# Silent Training Model

# Dataset
students = [
    [1, 50, 30],
    [2, 55, 35],
    [3, 60, 40],
    [4, 65, 45],
    [5, 70, 50],
    [6, 75, 55],
    [7, 80, 60],
    [8, 85, 65],
    [9, 90, 70],
    [10, 95, 75]
]

final_marks = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

# Training Data
train_x = students[:8]
train_y = final_marks[:8]

# Model Parameters
weights = [0.0, 0.0, 0.0]
bias = 0.0

learning_rate = 0.00001
epochs = 10000
n = len(train_x)

# Silent Training
for epoch in range(epochs):

    dw = [0.0, 0.0, 0.0]
    db = 0.0

    for i in range(n):

        prediction = bias

        for j in range(3):
            prediction += weights[j] * train_x[i][j]

        error = prediction - train_y[i]

        for j in range(3):
            dw[j] += error * train_x[i][j]

        db += error

    for j in range(3):
        dw[j] = (2 / n) * dw[j]
        weights[j] -= learning_rate * dw[j]

    db = (2 / n) * db
    bias -= learning_rate * db


# User Input
print("\n===== STUDENT MARKS PREDICTOR =====")

hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance (%): "))
previous_marks = float(input("Enter Previous Marks: "))

if hours < 0 or not 0 <= attendance <= 100 or not 0 <= previous_marks <= 100:
    print("Invalid Input!")

else:
    new_student = [hours, attendance, previous_marks]

    prediction = bias

    for j in range(3):
        prediction += weights[j] * new_student[j]

    prediction = max(0, min(100, prediction))

    print("\nPredicted Final Marks:", round(prediction, 2), "/ 100")
