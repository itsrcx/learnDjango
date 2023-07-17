# learnDjango

<nobr>add your .cnf file for adding <h2>mysql</h2>as <h2>database</h2></nobr> 
<nobr>& <h3>update</h3> the <h3>settings.py</h3> with:
<code>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}
</code>
& update the <b>path</b> to the .cnf file

cnf file format :
<code>
[client]
database = DB_NAME
host = localhost
user = DB_USER
password = DB_PASSWORD
default-character-set = utf8
</code>
