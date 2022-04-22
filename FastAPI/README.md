Source of all this information:
https://www.youtube.com/watch?v=0sOvCWFmrtA&t=3533

# Virtual Env in Windows
In terminaL `py -3 -m venv venv`

# Virtual env in MacOS
In terminal `python3 -m venv venv`
Choose interpreter
then `source venv/bin/activate`

# Make directly a requirements.txt based on your freeze
pip freeze > requirements.txt

# Test API 
To test APIs you can use the program postman. 

# CRUD
Create -> post => /posts
Read -> get => /posts or /posts:id
Update -> put/patch => /posts/:id
Delete -> delete => /posts/:id