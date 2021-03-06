from functools import wraps
from flask import request, session, redirect

def login_required(f):
    @wraps(f)
    def func(*args, **kwargs):
        if 'user' in session:
            return f(*args,**kwargs)
        return redirect('/login')    
    return func

def is_admin(f):
    @wraps(f)
    def func(*args, **kwargs):
        if 'user' in session and session['user']['role'] == 'admin':
            return f(*args, **kwargs)

        return redirect('/problems')
    return func    
