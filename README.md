# NumPy & Pandas Practice 🐍📊

Small, beginner-friendly Python scripts for learning **NumPy** and **pandas** by building small real-life projects: a step tracker, a student grade report, an expense tracker and more.

Each script is short and runs on its own, so you can read it, run it and change it in a few minutes.

## 📂 What's inside

| File | Topic | What it does |
|------|-------|--------------|
| [`pandas1.py`](pandas1.py) | Step tracker | Makes 5 weeks of random step data and works out distance (km), calories and whether each day's goal was met, using `np.where` and `describe()` |
| [`1_project.py`](1_project.py) | Student grade report | Works out total, average, pass/fail and rank for each student, then exports the result to `grade.xlsx` |
| [`1.py`](1.py) | Expense DataFrame | Builds a DataFrame, filters rows with boolean masks and sorts by amount |
| [`claude1.py`](claude1.py) | NumPy basics | Covers `np.where`, sorting in descending order and `np.unique` |
| [`perdonal_tracker.py`](perdonal_tracker.py) | Expense tracker (input) | Interactive CLI that records daily expenses into `expense.csv` |
| [`personal_tracker.py`](personal_tracker.py) | Expense tracker (analysis) | Reads `expense.csv` and adds running total, average, max spend and a high/low label |

## 🧠 Concepts covered

- Creating arrays and DataFrames
- Vectorized math (`np.sum`, `np.mean`, `np.round`)
- Conditional logic with `np.where`
- Filtering, sorting and ranking DataFrames
- Summary statistics with `describe()`
- Reading and writing CSV and Excel files
- Classes and simple input handling in Python

## 🚀 Getting started

```bash
git clone https://github.com/piratewave32/numpy-and-pandas.git
cd numpy-and-pandas
pip install -r requirements.txt
python pandas1.py
```

Replace `pandas1.py` with any other script to run it.

## 🤝 Contributing

New practice problems, fixes and improvements are welcome. Fork the repo, make your change and open a pull request.

## ⭐ Support

If this helped you learn NumPy or pandas, please give the repo a **star** so other learners can find it!

## 📄 License

[MIT](LICENSE)
