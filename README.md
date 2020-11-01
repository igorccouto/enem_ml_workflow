![GitHub](https://img.shields.io/github/license/igorccouto/enem_ml_workflow)
![](https://img.shields.io/badge/OS-Linux-blue)

# ENEM - Machine Learning Workflow

An orchestrated Machine Learning Workflow (Pipeline) to manage data from ENEM (National High School Exam in Portuguese). Data Analysts/Scientists can download the application to analyze data and/or create models to predict scores from students in ENEM exams.

The entire workflow was designed here. From download data to deploy process. All workflow (Bash and Python scripts) is orchestrated by Apache Airflow. All resources are dockerized to be easily installed. 

Install, download data from a chosen year, analyzes and creates a model for your own purposes.

## 1. Installation

By Makefile, you can manage the application:
- *make up* - Builds and starts the application.
    - After, you can access the main page of the pipeline at [http://localhost:8080/](http://localhost:8080)
    - You can use detachable mode with *make up_d*.
    - If you have problems with permissions in docker folders, runs with superuser privileges, like *sudo make up*.
- *make stop* - Stops the containers.
- *make down* - Removes the containers.
- *make restart* - Restarts.

## 2. Workflow steps

Each step is made by a specific Bash/Python script. In general, Apache Airflow controls and manage all these steps. However, you can run it manually. For instance, if you want to execute manually each step to manipulate data from ENEM 2018:

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

## 3. Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    ├── docker             <- Files and sources for dockerized application.
    ├── docker-compose.yml <- Defines a multi-container Docker application.
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