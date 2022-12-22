# from flask import Flask
# app = Flask(__name__)

import db
from models import Result

# @app.route('/')
def ini(numQ):
    db.Base.metadata.create_all(db.engine)
    res,it = [], 0
    for solution in queens(numQ, 0, [], [], []):
        it= it+1
        res.append(solution)
        guardaenBD(solution)
    res.append(it)
    print(it)
    imprimedeBD()
    return 'Total: ' + str(it)

def queens(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a

def guardaenBD(texto):
    resStr = ','.join(map(str,texto))
    registro = Result(resStr)
    db.session.add(registro)
    db.session.commit()

def imprimedeBD():
    productos = db.session.query(Result).all()
    for row in productos:
        print(row.result)

print(ini(8))