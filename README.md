
# Assessment Collector - Backend

This is the backend repository for the Assessment Collector application


## Run application

Clone the project

```bash
  git clone https://github.com/Phil-Hary/assessment_collector_backend.git
```

Go to the project directory

```bash
  cd assessment_collector_backend
```

Install dependencies

```bash
  # create env
  python3 -m venv env

  # activate env
  # windows
  env\Scripts\activate

  # mac
  source myenv/bin/activate
  
```

Run migrations

This will setup the sqlite database and the tables for you

```bash
  # run migrations
  python manage.py migrate
```

Start the application

```bash
  python manage.py runserver
``` 