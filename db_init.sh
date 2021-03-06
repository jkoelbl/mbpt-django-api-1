mysql -u $DATABASE_USER -h $DATABASE_HOST -P $DATABASE_PORT -p$DATABASE_PASSWORD < mysql/create_db.sql
find . -path "./api/*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "./api/migrations/*.py" -not -name "__init__.py" -delete
find . -path "./api/*/migrations/*.pyc"  -delete
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/mock_data/tiers.json
python manage.py loaddata fixtures/default_language.json
python manage.py loaddata fixtures/mock_data/tags.json
python manage.py loaddata fixtures/default_user.json
python manage.py loaddata fixtures/default_client.json
python manage.py loaddata fixtures/default_todo.json
python manage.py loaddata fixtures/default_profile.json
python manage.py loaddata fixtures/mock_data/announcements.json
python manage.py loaddata fixtures/mock_data/tags.json
python manage.py loaddata fixtures/mock_data/challenges.json
python manage.py loaddata fixtures/mock_data/discussions.json
python manage.py loaddata fixtures/mock_data/comments.json
python manage.py loaddata fixtures/mock_data/submissionstatus.json
python manage.py loaddata fixtures/mock_data/submissions.json
