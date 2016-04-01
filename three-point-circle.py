import string
import numpy
import math
def checkio(data):
    data = data.translate({ord('('):'',ord(')'):'',ord(','):''})
    point=[]
    for i in data:
    	point.append(int(i))
    A = numpy.array([[point[0],point[1],1],
                     [point[2],point[3],1],
                     [point[4],point[5],1]])

    A1 = numpy.array([[-(pow(point[0],2) + pow(point[1],2)),point[1],1],
    				  [-(pow(point[2],2) + pow(point[3],2)),point[3],1],
    				  [-(pow(point[4],2) + pow(point[5],2)),point[5],1]])

    A2 = numpy.array([[point[0],-(pow(point[0],2) + pow(point[1],2)),1],
    				  [point[2],-(pow(point[2],2) + pow(point[3],2)),1],
    				  [point[4],-(pow(point[4],2) + pow(point[5],2)),1]])

    A3 = numpy.array([[point[0],point[1],-(pow(point[0],2) + pow(point[1],2))],
    				  [point[2],point[3],-(pow(point[2],2) + pow(point[3],2))],
    				  [point[4],point[5],-(pow(point[4],2) + pow(point[5],2))]])

    D = numpy.linalg.det(A1) / numpy.linalg.det(A)
    E = numpy.linalg.det(A2) / numpy.linalg.det(A)
    F = numpy.linalg.det(A3) / numpy.linalg.det(A)

    r = round((math.sqrt(pow(D,2)+pow(E,2)- 4*F) / 2),2)
    x0 = round(-D / 2,2)
    y0 = round(-E / 2,2)

    return ('(x-%g)^2+(y-%g)^2=%g^2'%(x0,y0,r))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"