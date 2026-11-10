# 🎓 Multiple Input Student Marks Prediction

## 📌 About the Project

This is a beginner-friendly Machine Learning project that predicts a student's final marks based on three different input features:

- Study Hours
- Attendance Percentage
- Previous Exam Marks

The model is implemented completely from scratch using Python without using Machine Learning libraries like Scikit-learn, NumPy, or TensorFlow.

It uses **Multiple Linear Regression** to learn the relationship between multiple input features and the final marks.

## ⚙️ Algorithm & Technology

- **Machine Learning Type:** Supervised Learning
- **Algorithm:** Multiple Linear Regression
- **Training Method:** Gradient Descent
- **Programming Language:** Python
- **Model Type:** Multiple Input Prediction Model

## 📊 Dataset

The model uses the following sample dataset:

| Study Hours | Attendance (%) | Previous Marks | Final Marks |
|---:|---:|---:|---:|
| 1 | 50 | 30 | 35 |
| 2 | 55 | 35 | 40 |
| 3 | 60 | 40 | 45 |
| 4 | 65 | 45 | 50 |
| 5 | 70 | 50 | 55 |
| 6 | 75 | 55 | 60 |
| 7 | 80 | 60 | 65 |
| 8 | 85 | 65 | 70 |
| 9 | 90 | 70 | 75 |
| 10 | 95 | 75 | 80 |

## 🧠 How the Model Works

1. Loads the student dataset.
2. Splits the dataset into training data.
3. Initializes three weights and one bias.
4. Starts training using Gradient Descent.
5. Calculates predictions for each training example.
6. Calculates prediction errors.
7. Computes gradients for all weights and bias.
8. Updates model parameters over multiple epochs.
9. Takes new student information as input.
10. Predicts the student's final marks.

## 🔍 Input Features

| Feature | Description |
|---|---|
| Study Hours | Number of hours spent studying |
| Attendance | Student's attendance percentage |
| Previous Marks | Marks obtained in the previous examination |

## 🚀 Features

- Multiple input-based prediction.
- Linear Regression implemented from scratch.
- Gradient Descent optimization.
- Silent model training (no training logs).
- Three independent input features.
- Input validation.
- Predicted marks limited between 0 and 100.

## ▶️ How to Run

**1. Clone the repository**

**2. Open the project folder**

**3. Run the Python file**

**4. Enter student information**

## 💻 Example Output


===== STUDENT MARKS PREDICTOR =====

Enter Study Hours: 6
Enter Attendance (%): 75
Enter Previous Marks: 55

Predicted Final Marks: 60.00 / 100


*Example output based on the sample dataset.*

## 📚 What I Learned

- Multiple Linear Regression.
- Working with multiple input features.
- Weight and Bias optimization.
- Gradient Descent.
- Training and testing data separation.
- Model prediction using Python loops.
- Input validation.

## 🔮 Future Improvements

- Implement model evaluation using MAE and MSE.
- Add more realistic student datasets.
- Improve prediction accuracy.
- Add data visualization.
- Build a graphical user interface.
- Compare Single Linear Regression and Multiple Linear Regression.

## 👨‍💻 Author

Created as part of my journey to learn Machine Learning from scratch using Python.

**Learning by building, one ML project at a time!** 🚀
