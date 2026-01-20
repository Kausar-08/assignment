# assignmentDataset Management and Basic Analysis System



Project Overview

The Dataset Management and Basic Analysis System is a Python-based project designed to demonstrate fundamental programming concepts such as file handling, error handling, functions, loops, conditional statements, sets, and object-oriented programming (OOP).

The system reads numerical and categorical data from files, performs basic statistical analysis, and saves the results into a report file.



This project is suitable for students learning Python basics and introductory data analysis.

Project Objective

• Read numerical and categorical data from files (TXT or CSV)

• Handle common file and data errors

• Perform basic statistical calculations

• Apply Python functions, loops, and operators

• Use conditional logic for decision-making

• Extract unique categories using sets

• Implement Object-Oriented Programming (OOP)

• Save analysis results to a file



Features

• Reads numerical data such as students’ marks or sales figures

• Handles:

• Missing files

• Empty files

• Invalid (non-numeric) data

• Calculates:

• Total

• Average

• Minimum

• Maximum

• Displays performance evaluation based on a threshold

• Extracts unique categories from categorical data

• Uses a DataSet class for clean and organized code

• Saves results into a report file



Technologies Used

• Python 3

• Built-in Python modules only (no external libraries required)



File Structure

Dataset-Management-System/



├── data_numbers.txt        # Numerical data file

├── data_categories.txt     # Categorical data file

├── analysis.py             # Main Python program

├── report.txt              # Generated report file

└── README.md               # Project documentation



How the Program Works

1. Loads numerical data from a file and stores it in variables.

2. Validates the file and data using error handling.

3. Uses functions to compute total, average, minimum, and maximum.

4. Traverses the dataset using loops.

5. Applies conditional statements to evaluate performance.

6. Extracts unique categorical values using a set.

7. Uses a DataSet class to organize all operations.

8. Saves results into a report file.



Object-Oriented Design

The project uses a DataSet class with the following methods:

• load_data() – Reads and validates data from files

• calculate_statistics() – Computes total, average, minimum, and maximum

• display_results() – Displays results and performance evaluation

An object of this class is created to run the entire analysis.

Performance Evaluation

• If the calculated average is above the defined threshold, the program displays:

High Performance•



Output

• Results are displayed on the screen

• Statistics and unique category count are saved into a report file



 Learning Outcomes



By completing this project, you will understand:

• Python file handling

• Error and exception handling

• Functions and loops

• Conditional statements

• Sets for unique data extraction

• Object-Oriented Programming (OOP)

• Saving program output to files



Author



Kausara Sulaiman



