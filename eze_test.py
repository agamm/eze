import flick as f

# This has to be in the global scope for the multiprocessing.map
def _slow_func(x): 
    import time
    time.sleep(0.5)

def test_together():
    t0 = f.get_time(lambda: [_slow_func(x) for x in ['a','b']])
    t1 = f.get_time(lambda: f.together(_slow_func, ['a','b'], {}))
    assert t1 < t0