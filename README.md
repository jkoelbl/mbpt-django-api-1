# MBPT Django API
* Make Migrations
    `python manage.py makemigrations`
* Migrate
    `python manage.py migrate`
* Load Fixtures
    `python manage.py loaddata fixtures/*`
* Test
    `python manage.py test`

# API References
* `/announcement/`
    * `GET`: List all the announcement
    * Permission: `user`
    * Response:
        * 200 Successful
        * 403 Forbidden: Is your token valid?
    * Parameters
        * `Authorization`: `Bearer <access_token>`

* `/profile/<username>`
    * `GET`: Display the user profile given username.
    * Permission: `user`
    * Response:
        * 200 Successful
        * 403 Forbidden: Is your token valid?
    * Parameters
        * `Authorization`: `Bearer <access_token>`

* `/profile/`
    * `PUT`: Update the profile associated with current user.
    * Permission: `user`

