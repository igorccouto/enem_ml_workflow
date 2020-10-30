![GitHub](https://img.shields.io/github/license/igorccouto/enem_ml_workflow)

# ENEM

Complete Machine Learning Workflow to predict the ENEM (National High School Exam in Portuguese) essay score based on social-economic questions.

The entire workflow was designed here. From download script to deploy process. Data Scientists can attach your model to make better predictions.

## Workflow steps

Each step is made by a specific Bash/Python script. For instance, if you want to execute manually each step to ENEM 2018:

1. Download
```console
$ bash download_data.sh 2018
```
2. Extract
```console
$ bash extract_data.sh 2018
```
3. Process
```console
$ python process_data.py 2018
```
4. Model
5. Test
6. Deploy

The whole process is orchestrated by a dockerized Apache Airflow instance.

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    ├── notebooks          <- Jupyter notebooks.
    ├── requirements.txt   <- The requirements file .
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── data           <- Scripts to download or generate data
        ├── features       <- Scripts to turn raw data into features for modeling
        ├── models         <- Scripts to train models and then use trained models to make
        └── visualization  <- Scripts to create exploratory and results oriented visualizations


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>