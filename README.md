# **YZV 475E (14985)** - _Term Project_
 
**Name:** Ata Türkoğlu

**Student ID:** 150210337

## How to use

1. Install [_Python_](https://www.python.org/downloads/).
2. Make sure you are connected to internet as the data is fetched from the web (after the initial usage, a cache is created for offline usage as well).
3. Install the required packages with _pip_, using the following command:
   ```console
    pip install -r requirements.txt
   ```
4. Run the `src/main.ipynb` file.

## How it works

The `src/itu_helper.py` function is a wrapper which fetches data from [ITU Helper](https://github.com/itu-helper/data-updater) and uses the `src/data_structres/course.py` and `src/data_structres/lesson.py` to store the data it fetches. Then, from the `src/main.ipynb` _Jupyter Notebook_ file, the `ItuHelper` class is used for accesing the data and visualizing it using the [_matplotlib_](https://matplotlib.org/) library.

## Comments on the Findings
