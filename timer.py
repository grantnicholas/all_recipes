import time

def timeit(f):
    def timed(*args, **kw):
        start     = time.time()
        result    = f(*args, **kw)
        end       = time.time()
        print "\n__________________________________________"
        print "Function %r took: %2.4f seconds to execute  |" % (f.__name__, end-start)
        print "__________________________________________"
        return result
    return timed