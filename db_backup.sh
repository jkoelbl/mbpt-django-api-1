python manage.py dumpdata auth.user > fixtures/default_user.json
python manage.py dumpdata profiles.profile > fixtures/default_profile.json
python manage.py dumpdata announcements.announcement > fixtures/mock_data/announcements.json
python manage.py dumpdata challenges.challenge > fixtures/mock_data/challenges.json
python manage.py dumpdata challenges.submissionstatus > fixtures/mock_data/submissionstatus.json
python manage.py dumpdata challenges.submission > fixtures/mock_data/submissions.json
python manage.py dumpdata discussions.discussion > fixtures/mock_data/discussions.json
python manage.py dumpdata discussions.comment > fixtures/mock_data/comments.json
