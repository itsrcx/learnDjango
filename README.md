# learnDjango

1) add your .cnf file for adding <b>mysql</b> as <b>database</b>
2) cnf file format :

<code>[client]
database = DB_NAME
host = localhost
user = DB_USER
password = DB_PASSWORD
default-character-set = utf8</code>

3) <b>update</b> the <b>settings.py</b> with <b>path</b> to .cnf file:

<code>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}</code>


<h3>for security purposes we need .cnf file not to directly hardcode the personal info.</h3>
