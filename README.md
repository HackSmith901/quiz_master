Here is an updated README file incorporating the provided Python code:

# Random Quiz Generator

## Description

This application generates random US state capitals quizzes. It creates 35 unique quizzes with 50 questions each. The states and answers are randomly shuffled in each quiz.

## Features

- Generates 35 unique quizzes 
- Each quiz has 50 multiple choice questions
- Questions are randomly ordered
- Answer options are randomly ordered 
- Quiz and answer key files created for each quiz

## Code Overview

- `random_quiz.py` - Main quiz generation logic
  - `capitals` dictionary contains states and capitals
  - Loops to generate 35 quizzes
  - Shuffles state order and answer options for each quiz
  - Writes quiz questions and answer key to text files
- Quiz files named `Quiz1.txt`, `Quiz2.txt`, etc
- Answer key files named `Answer1.txt`, `Answer2.txt`, etc

## Running the Code

```
python random_quiz.py
```

This will generate the 35 quiz and answer key files in the current directory.

## Improvements

- Add a CLI or GUI for quiz configuration
- Support more question types (multiple choice, true/false)
- Expand to other subjects besides capitals
- Add quiz solution after completion

