After deploy: Whenever i try to sign up and generate otp, it loads and loads before ultimately redirecting to a internal server error page --- This stems from using a local dev emil service(smtp)    [Fix it in the sign up view]


Use a script to seed users in the app for testing ---   [create_super_user.py]








Build command - pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput && python create_super_user.py


Start command -- gunicorn config.wsgi:application




DATABASE_URL=postgresql://postgres.ndgujmlrywaeetevlyyb:4dq5DiZ%2FUy%21%26nGU@aws-1-eu-west-1.pooler.supabase.com:5432/postgres
DEBUG=FALSE
DJANGO_ALLOWED_HOSTS=job-board-lpmo.onrender.com
DJANGO_SECRET_KEY="django-insecure-q6=zo84e3!v5vun-=3qpl3sd^5s6$!7mxdll6*(vh9@+prqcq!"
DJANGO_SETTINGS_MODULE=config.settings
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=password123
DJANGO_SUPERUSER_USERNAME=admin
EMAIL_HOST_PASSWORD=msdvlspamsncjqrf
EMAIL_HOST_USER=jobboard@gmail.com
SITE_URL=https://job-board.onrender.com


site url and allowed host