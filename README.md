# learnDjango

add your .cnf file for adding <b>mysql</b>as <b>database</b> 
& <b>update</b> the <b>settings.py</b> with:

<code>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}</code>

& update the <b>path</b> to the /path/my.cnf file

cnf file format :

<code>[client]
database = DB_NAME
host = localhost
user = DB_USER
password = DB_PASSWORD
default-character-set = utf8</code>
