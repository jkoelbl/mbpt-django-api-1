py manage.py dumpdata auth.user > fixtures/default_user.json
py manage.py dumpdata profiles.profile > fixtures/default_profile.json
py manage.py dumpdata announcements.announcement > fixtures/mock_data/announcements.json
py manage.py dumpdata challenges.challenge > fixtures/mock_data/challenges.json
py manage.py dumpdata discussions.discussion > fixtures/mock_data/discussions.json
py manage.py dumpdata discussions.comment > fixtures/mock_data/comments.json
