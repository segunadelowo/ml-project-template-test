"""This DAG has the goal to simulate a ML Training pipeline
Follow the instruction in the README.md to complete the DAG.
"""
from datetime import timedelta

from airflow import DAG
from airflow.hooks.sqlite_hook import SqliteHook
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from src.models.train_pipeline import data_preprocessing, split_data, fit_and_save_model, \
    predict_test, measure_model_performance


TRAINING_TABLE = 'training' # Variable.get("training_table")


# default_args when passed to a DAG, it will apply to any of its operators
default_args = {
                "start_date": "2019-8-5",
                "email": ["airflow_notification@thisisadummydomain.com"],
                "email_on_failure": False,
                "email_on_retry": False,
                "retries": 2,
                "retry_delay": timedelta(minutes=5)
                }


dag = DAG("training_pipeline",
          description="Project-ML Training Pipeline",
          # train every first day of the month
          schedule_interval="@monthly",
          default_args=default_args,
          dagrun_timeout=timedelta(minutes=60*10),
          catchup=False
          )


def save_model_accuracy(**kwargs):
    # Tasks can pass parameters to downstream tasks through the XCom space.
    # XCom (cross-communication) allows communication between task instances.
    # In this example the current task `save_model_accuracy` takes the output
    # of the previous task `measure_accuracy` "pulling" it from the XCom space
    ti = kwargs['ti']
    accuracy = ti.xcom_pull(task_ids='measure_accuracy')

    sql_insert = f"""INSERT INTO {TRAINING_TABLE} 
                            (mape_test, rmse_test, days_in_test)
                     VALUES({accuracy['mape_test']}, 
                            {accuracy['rmse_test']},
                            {accuracy['days_in_test']})
                    ;
                  """
    # Hooks are interface to external platforms (e.g. Amazon S3)
    # and DBs (e.g. SQLite DB, PostgreSQL)
    conn_host = SqliteHook(sqlite_conn_id='sqlite_ml').get_conn()
    conn_host.execute(sql_insert)
    conn_host.commit()


with dag:
    # Instantiating a PythonOperator class results in the creation of
    # a task object, which ultimately becomes a node in DAG objects.
    task_1_preprocess = PythonOperator(task_id="data_preprocessing",
                                       python_callable=data_preprocessing
                                       )

    # Add here
    task_2_split = PythonOperator(task_id="split_data",
                                  python_callable=split_data
                                  )

    task_3_fit_and_save = PythonOperator(task_id="fit_and_save_model",
                                         python_callable=fit_and_save_model
                                         )

    task_4_make_prediction = PythonOperator(task_id="predict_test",
                                            python_callable=predict_test
                                            )

    task_5_accuracy = PythonOperator(task_id="measure_model_performance",
                                     python_callable=measure_model_performance
                                     )

    task_6_save = PythonOperator(task_id="save_model_accuracy",
                                 python_callable=save_model_accuracy,
                                 provide_context= True
                                 )

    # TODO Uncomment and Complete with the tasks order execution
    task_1_preprocess >> task_2_split >> task_3_fit_and_save >> task_4_make_prediction >> task_5_accuracy >> task_6_save
