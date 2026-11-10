#Project: STUDENT MARKS PREDICTION SIMPLE MODEL
#MACHINE: LEARNING FORM SCRATCH
#ALGORITHM: LINEAR REGRESSION


#STEP-1: Training Daatset

study_hours = [1,2,3,4,5,6]

actual_marks = [15,25,35,45,55,65]

#STEP-2: Initialize Model Parameters

weight = 0.0

bias = 0.0


#STEP-3: Traning Configuaratuon

learning_rate = 0.01

epochs = 5000

n =len(study_hours)


#STEP-4: Start Model Traning



for epoch in range(epochs):

    total_error_weight = 0
    total_error_bias = 0

    #process every traning example
    for i in range(n):

        x = study_hours[i]
        actual = actual_marks[i]

        #prediction

        predicted = weight * x + bias
        error = predicted - actual

        # Calculate Gradients

        total_error_weight += error * x
        total_error_bias += error


# Average Gradients

    dw = (2 / n) * total_error_weight

    db = (2 / n) * total_error_bias


    # Update Model Parameters

    weight = weight - learning_rate * dw
    bias = bias - learning_rate * db



# STEP 5: Take User Input
print("\n\n---STUDENT MARKS PREDICTION---\n")

hours = float(input("Enter Study Hours: "))

if hours<0:
    print("Invalid Input! Study Hours cannot be negative.")
    exit()
else:
    prediction = weight * hours + bias

    #limit the prediction to a maximum of 100 marks
    prediction = max(0, min(100, prediction))

print("\nPredicted Marks:", round(prediction, 2))
