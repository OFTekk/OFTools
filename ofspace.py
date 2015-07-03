#
# coding:utf-8;

from math import *
import hashlib


class Point(object):
    def __init__(self, x=0.0, y=0.0, z=0.0, space=0):
        if not isinstance(x, (int, long, float)):
            raise TypeError
        if not isinstance(y, (int, long, float)):
            raise TypeError
        if not isinstance(z, (int, long, float)):
            raise TypeError
        self.x = x
        self.y = y
        self.z = z
        if space != 0:
            if isinstance(space, Space):
                self.space = space
            else:
                self.space = 0
        else:
            self.space = 0
        self.name = self.calculatehash()

    def __getitem__(self, key):
        if key == 0 or key == 'x' or key == 'X' or key == 'u' or key == 'U' or key == 'r' or key == 'R':
            return self.x
        if key == 1 or key == 'y' or key == 'Y' or key == 'v' or key == 'V' or key == 'g' or key == 'G':
            return self.y
        if key == 2 or key == 'z' or key == 'Z' or key == 'w' or key == 'W' or key == 'b' or key == 'B':
            return self.z
        raise TypeError

    def __setitem__(self, key, value):
        if not isinstance(value, (int, long, float)):
            raise TypeError
        if key == 0 or key == 'x' or key == 'X' or key == 'u' or key == 'U' or key == 'r' or key == 'R':
            self.x = value
            return
        if key == 1 or key == 'y' or key == 'Y' or key == 'v' or key == 'V' or key == 'g' or key == 'G':
            self.y = value
            return
        if key == 2 or key == 'z' or key == 'Z' or key == 'w' or key == 'W' or key == 'b' or key == 'B':
            self.z = value
            return
        raise TypeError

    def calculatehash(self):
        m = hashlib.md5()
        m.update(str(self.x))
        m.update(str(self.y))
        m.update(str(self.z))
        return m.hexdigest()

    def setx(self, v):
        if not isinstance(v, (int, long, float)):
            raise TypeError
        self.x = v

    def sety(self, v):
        if not isinstance(v, (int, long, float)):
            raise TypeError
        self.y = v

    def setz(self, v):
        if not isinstance(v, (int, long, float)):
            raise TypeError
        self.z = v

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getz(self):
        return self.z

    def xside(self, v):
        if isinstance(v, Point):
            if self.x < v.x:
                return -1
            if self.x == v.x:
                return 0
            if self.x > v.x:
                return 1
        if isinstance(v, (int, long, float)):
            if self.x < v:
                return -1
            if self.x == v:
                return 0
            if self.x > v:
                return 1
        raise TypeError

    def yside(self, v):
        if isinstance(v, Point):
            if self.y < v.y:
                return -1
            if self.y == v.y:
                return 0
            if self.y > v.y:
                return 1
        if isinstance(v, (int, long, float)):
            if self.y < v:
                return -1
            if self.y == v:
                return 0
            if self.y > v:
                return 1
        raise TypeError

    def zside(self, v):
        if isinstance(v, Point):
            if self.z < v.z:
                return -1
            if self.z == v.z:
                return 0
            if self.z > v.z:
                return 1
        if isinstance(v, (int, long, float)):
            if self.z < v:
                return -1
            if self.z == v:
                return 0
            if self.z > v:
                return 1
        raise TypeError

    def side(self, v):
        if isinstance(v, Point):
            return [self.xside(v), self.yside(v), self.zside(v)]
        raise TypeError

    def setname(self, n):
        self.name = n

    def getname(self):
        return self.name

    def __add__(self, v):
        if isinstance(v, Point):
            return Point(self.x + v.x, self.y + v.y, self.z + v.z)
        if isinstance(v, (int, long, float)):
            return Point(self.x + v, self.y + v, self.z + v)
        raise TypeError

    def __sub__(self, v):
        if isinstance(v, Point):
            return Point(self.x - v.x, self.y - v.y, self.z - v.z)
        if isinstance(v, (int, long, float)):
            return Point(self.x - v, self.y - v, self.z - v)
        raise TypeError

    def __mul__(self, v):
        if isinstance(v, Point):
            return Point()
        if isinstance(v, (int, long, float)):
            return Point(self.x * v, self.y * v, self.z * v)
        raise TypeError

    def __div__(self, v):
        if isinstance(v, Point):
            return Point()
        if isinstance(v, (int, long, float)):
            if v == 0:
                raise ZeroDivisionError
            return Point(self.x / v, self.y / v, self.z / v)
        raise TypeError

    def __eq__(self, v):
        if isinstance(v, Point):
            return self.x == v.x and self.y == v.y and self.z == v.z
        raise TypeError

    def __ne__(self, v):
        if isinstance(v, Point):
            return self.x != v.x or self.y != v.y or self.z != v.z
        raise TypeError

    def __str__(self):
        return "(" + str(self.name) + "@[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "])"

    def abs(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)


class PointList(object):
    def __init__(self):
        self.pointsx = []
        self.pointsy = []
        self.pointsz = []

    def append(self, p):
        if not isinstance(p, Point):
            raise TypeError
        self.pointsx.append(p.x)
        self.pointsy.append(p.y)
        self.pointsz.append(p.z)

    def __len__(self):
        return len(self.pointsx)

    def __str__(self):
        s = "("
        for i in range(0, len(self.pointsx)):
            s = s + "'" + str(Point(self.pointsx[i], self.pointsy[i], self.pointsz[i])) + "'"
            if i < len(self.pointsx) - 1:
                s += ","
        return s + ")"

    def sort(self, axis=2):
        if axis > 2 or axis < 0:
            raise ValueError
        for i in range(0, len(self.pointsx)):
            for j in range(i + 1, len(self.pointsx)):
                p1 = Point(self.pointsx[j], self.pointsy[j], self.pointsz[j])
                p2 = Point(self.pointsx[i], self.pointsy[i], self.pointsz[i])
                cmps = p1.side(p2)
                if cmps[axis] == 1:
                    tmp = self.pointsx[i]
                    self.pointsx[i] = self.pointsx[j]
                    self.pointsx[j] = tmp
                    tmp = self.pointsy[i]
                    self.pointsy[i] = self.pointsy[j]
                    self.pointsy[j] = tmp
                    tmp = self.pointsz[i]
                    self.pointsz[i] = self.pointsz[j]
                    self.pointsz[j] = tmp
                    break

    def __getitem__(self, key):
        if not isinstance(key, (int, long)):
            raise TypeError
        if key < 0 or key > len(self.pointsx) - 1:
            raise ValueError
        return Point(self.pointsx[key], self.pointsy[key], self.pointsz[key])

    def __setitem__(self, key, value):
        if not isinstance(value, Point) or not isinstance(key, (int, long)):
            raise TypeError
        if key < 0 or key > len(self.pointsx) - 1:
            if key != len(self.pointsx):
                raise ValueError
            else:
                self.pointsx.append(value[0])
                self.pointsy.append(value[1])
                self.pointsz.append(value[2])
        self.pointsx[key] = value[0]
        self.pointsy[key] = value[1]
        self.pointsz[key] = value[2]


class Line(object):
    def __init__(self, p1=Point(), p2=Point()):
        if not isinstance(p1, Point):
            raise TypeError
        if not isinstance(p2, Point):
            raise TypeError
        self.plist = PointList()
        self.plist.append(p1)
        self.plist.append(p2)
        for i in range(0, 2):
            self.plist.sort(i)

    def __getitem__(self, key):
        return self.plist[key]

    def __setitem__(self, key, value):
        if not isinstance(value, Point) or not isinstance(key, (int, long)):
            raise TypeError
        if key < 0 or key > 1:
            raise ValueError
        self.plist[key] = value
        for i in range(0, 2):
            self.plist.sort(i)

    def __eq__(self, l):
        if not isinstance(l, Line):
            raise TypeError
        return self[0] == l[0] and self[1] == l[1]

    def __ne__(self, l):
        if not isinstance(l, Line):
            raise TypeError
        return self[0] != l[0] or self[1] != l[1]

    def __div__(self, l):
        if isinstance(l, Line):
            xr = self.plist[0][0]
            yr = self.plist[0][1]
            xa = self.plist[1][0] - xr
            ya = self.plist[1][1] - yr
            xs = l.plist[0][0]
            ys = l.plist[0][1]
            xb = l.plist[1][0] - xs
            yb = l.plist[1][1] - ys
            divisor = xb * ya - xa * yb
            if divisor == 0:
                return None
            ysmr = ys - yr
            xrms = xr - xs
            lmbda = (xb * ysmr + yb * xrms) / divisor
            xi = (xa * ysmr + ya * xrms) / divisor
            if lmbda < 0.0 or lmbda > 1.0 or xi < 0.0 or xi > 1.0:
                return False
            zr = self.plist[0][2]
            za = self.plist[1][2] - zr
            zs = l.plist[0][2]
            zb = l.plist[1][2] - zs
            xp = xr + lmbda * xa
            yp = yr + lmbda * ya
            zp = zr + lmbda * za
            xq = xs + xi * xb
            yq = ys + xi * yb
            zq = zs + xi * zb
            if xp == xq and yp == yq and zp == zq:
                return Point(xp, yp, zp)
            return False
        if isinstance(l, Point):
            return True
        raise TypeError


class Triangle(object):
    def __init__(self, p1=Point(), p2=Point(), p3=Point()):
        if not isinstance(p1, Point):
            raise TypeError
        if not isinstance(p2, Point):
            raise TypeError
        if not isinstance(p3, Point):
            raise TypeError
        self.plist = PointList()
        self.plist.append(p1)
        self.plist.append(p2)
        self.plist.append(p3)
        for i in range(0, 2):
            self.plist.sort(i)

    def __getitem__(self, key):
        return self.plist[key]

    def __setitem__(self, key, value):
        if not isinstance(value, Point) or not isinstance(key, (int, long)):
            raise TypeError
        if key < 0 or key > 2:
            raise ValueError
        self.plist[key] = value
        for i in range(0, 2):
            self.plist.sort(i)

    def __eq__(self, t):
        if not isinstance(t, Triangle):
            raise TypeError
        return self[0] == t[0] and self[1] == t[1] and self[2] == t[2]

    def __ne__(self, t):
        if not isinstance(t, Triangle):
            raise TypeError
        return self[0] != t[0] or self[1] != t[1] or self[2] != t[2]


class Rectangle(object):
    def __init__(self, lt=Point(), rt=Point(), lb=Point(), rb=Point()):
        if not isinstance(lt, Point):
            raise TypeError
        if not isinstance(rt, Point):
            raise TypeError
        if not isinstance(lb, Point):
            raise TypeError
        if not isinstance(rb, Point):
            raise TypeError
        self.plist = PointList()
        self.plist.append(lt)
        self.plist.append(rt)
        self.plist.append(lb)
        self.plist.append(rb)
        for i in range(0, 2):
            self.plist.sort(i)

    def __getitem__(self, key):
        return self.plist[key]

    def __setitem__(self, key, value):
        if not isinstance(value, Point) or not isinstance(key, (int, long)):
            raise TypeError
        if key < 0 or key > 3:
            raise ValueError
        self.plist[key] = value
        for i in range(0, 2):
            self.plist.sort(i)

    def __eq__(self, r):
        if not isinstance(r, Rectangle):
            raise TypeError
        return self[0] == r[0] and self[1] == r[1] and self[2] == r[2] and self[3] == r[3]

    def __ne__(self, r):
        if not isinstance(r, Rectangle):
            raise TypeError
        return self[0] != r[0] or self[1] != r[1] or self[2] != r[2] or self[3] != r[3]


class Space(object):
    def __init__(self, origin=Point()):
        if not isinstance(origin, Point):
            raise TypeError
        self.origin = origin
        self.items = []
