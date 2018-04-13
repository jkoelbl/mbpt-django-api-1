mysql -u $DATABASE_USER -h $DATABASE_HOST -P $DATABASE_PORT -p$DATABASE_PASSWORD < mysql/create_db.sql
py manage.py makemigrations
py manage.py migrate
py manage.py loaddata fixtures/default_user.json
py manage.py loaddata fixtures/default_client.json
py manage.py loaddata fixtures/mock_data/announcements.json
py manage.py loaddata fixtures/mock_data/challenges.json
py manage.py loaddata fixtures/mock_data/discussions.json