from functools import wraps

def autoInitiator(*decArgs):
    def _wrapper(func):
        @wraps(func)
        def _wrapped(*args,**kwargs):
            super(args[0].__class__,args[0]).__init__(*args,**kwargs)
            return func(*args,**kwargs)
        return _wrapped
    return _wrapper
