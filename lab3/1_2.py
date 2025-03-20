def function(x, y = None):
    if y is None:
        y=[]
    y.append(x)
    print(y)
    return y

function(1)
function(2)
function(3)

