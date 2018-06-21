# A jobs website #

This is a simple job-posting website written using Django and Bootstrap.  Its
neatest feature is that it automatically Tweets jobs when they're approved,
and readers can sign up to spread the word by automatically re-tweeting those
tweets.

It's made public under an MIT License.

## Configuration ##

Check out the source, then create four files in the jobsboard subdirectory (next
to `settings.py`):

`sitename_settings.py`:

    JOBS_BOARD_TITLE = "Jimbo's site for Python jobs"
    JOB_TYPE_DESCRIPTION = "Python Jobs"
    FOOTER_TEXT = "Some text to go at the bottom of every page"

    ALLOWED_HOSTS = ["www.yoursite.com"]


`email_settings.py`:

    EMAIL_SUBJECT_PREFIX = "[Some Kind Of Jobs] "
    EMAIL_SITE_ADDRESS = "email_address_for_receving_stuff_from_readers@somewhere.com"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = "something@gmail.com"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_PASSWORD = "some kind of password"

`db_settings.py`:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'jobsboard_db',
            'USER': 'jobsboard_user',
            'PASSWORD': 'a password',
            'HOST': 'a mysql server',
            'PORT': '',
        }
    }

`twitter_settings.py`:

    # For the job-tweeting Twitter app
    APP_CONSUMER_KEY = 'blah blah'
    APP_CONSUMER_SECRET = 'blah blah'

    # For your job board's own twitter account
    OWN_TWITTER_ACCOUNT_ID = "myjobsboardtwitterid"
    OWN_TWITTER_ACCOUNT_ACCESS_KEY = 'blah blah'
    OWN_TWITTER_ACCOUNT_ACCESS_SECRET = 'blah blah'

    TWITTER_HASHTAGS = "#somekind #job"

Next, add a file called `main/templates/google_analytics.html`; this can contain
with the Google Analytics code if you want, or should otherwise be empty.

You can also add a file to configure Akismet, which will filter job posts for
spam:

`akismet_settings.py`:

    USE_AKISMET = True
    AKISMET_KEY = 'an akismet key'
    AKISMET_SITE = "https://www.yoursite.com/"


Next, sync the DB and migrate it to bring it up to date:

    19:03 ~/jobsboard (master)$ ./manage.py syncdb
    19:11 ~/jobsboard (master)$ ./manage.py migrate


## Dependencies ##

See requirements.txt
