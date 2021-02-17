# Next time: https://flask.palletsprojects.com/en/1.1.x/testing/#the-application
def inc(x):
    return x + 1

def test_answer():
    assert inc(4) == 5
