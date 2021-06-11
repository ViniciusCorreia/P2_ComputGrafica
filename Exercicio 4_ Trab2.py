from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import sin, cos, sqrt

name="Exercicio4_Trab2"

#Caracteristicas da piramide
raio = 3
N = 5
altura = 3
angulo = (2 * 3.14) / N

alpha = 1


def tronco_piramide():
    pontos_b = []
    glPushMatrix()
    glTranslatef(0, -2, 0)
    glRotatef(90, 1.0, 0.0, 0.0)


    for i in range(0, N):
        x = raio * cos(i * angulo)
        y = raio * sin(i * angulo)
        pontos_b += [(x, y)]

    u = (pontos_b[0][0], pontos_b[0][1], 0)
    v = (pontos_b[1][0], pontos_b[1][1], 0)
    p = (pontos_b[2][0], pontos_b[2][1], 0)

    glBegin(GL_POLYGON)
    # normal
    glNormal3fv(CalculaNormal(u, v, p, True))

    for v in pontos_b:
        glVertex3f(v[0], v[1], 0)

    glEnd()

    # LATERAL
    glBegin(GL_TRIANGLES)
    for i in range(0, N):
        u = (pontos_b[i][0], pontos_b[i][1], 0.0)
        v = (pontos_b[(i + 1) % N][0], pontos_b[(i + 1) % N][1], 0.0)
        p = (0, 0, altura)
        glNormal3fv(CalculaNormal(u, v, p))
        glVertex3fv(u)
        glVertex3fv(v)
        glVertex3fv(p)

    glEnd()

    glPopMatrix()



def CalculaNormal(v0, v1, v2, Invertida=False):
    x = 0
    y = 1
    z = 2
    U = (v2[x] - v0[x], v2[y] - v0[y], v2[z] - v0[z])
    V = (v1[x] - v0[x], v1[y] - v0[y], v1[z] - v0[z])
    N = ((U[y] * V[z] - U[z] * V[y]), (U[z] * V[x] - U[x] * V[z]), (U[x] * V[y] - U[y] * V[x]))
    NLength = sqrt(N[x] * N[x] + N[y] * N[y] + N[z] * N[z])
    if Invertida:
        return (-N[x] / NLength, -N[y] / NLength, -N[z] / NLength)
    else:
        return (N[x] / NLength, N[y] / NLength, N[z] / NLength)

def desenha():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(2, 0, 1, 0)
    tronco_piramide()
    glutSwapBuffers()


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(1, timer, 1)


def init():

    Cor = (1.264)
    light_position = (10, 0, 0, 0)
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)
    glShadeModel(GL_SMOOTH)
    glMaterialfv(GL_FRONT, GL_AMBIENT, Cor)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(500, 600)
    glutCreateWindow(name)
    glutDisplayFunc(desenha)
    init()
    glClearColor(0, 0, 0, 1)
    gluPerspective(-70, 5/3, 10, 50.0)
    glTranslatef(0, 0.0, -10)
    glutTimerFunc(10, timer, 1)
    glutMainLoop()

if __name__ == '__main__':
    main()
