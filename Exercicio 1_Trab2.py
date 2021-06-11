from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png



name="Exercicio 1 - Trab2"
ESCAPE = '\033'
window = 0
xrot = yrot = zrot = 0.0
dx = 0.1
dy = 0
dz = 0




def LoadTextures():
    global texture
    texture = glGenTextures(2)
    reader = png.Reader(filename='dado.png')
    w, h, pixels, metadata = reader.read_flat()
    if (metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


def desenha():
    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glTranslatef(0.0, 0.0, -10.0)
    glRotatef(1, 1.0, 0.0, 0.0)


    # figure creation
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_QUADS)

    # ---Front Face----
    glTexCoord2f(2 / 3, 1 / 2);glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1, 1 / 2);glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1, 0);glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(2 / 3, 0);glVertex3f(-1.0, 1.0, 1.0)

    # ---Back Face---
    glTexCoord2f(0, 1 / 2);glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1 / 3, 1 / 2);glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(1 / 3, 1);glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(0, 1);glVertex3f(1.0, -1.0, -1.0)

    # ---Top Face---
    glTexCoord2f(1 / 3, 1 / 2);glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(2 / 3, 1 / 2);glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(2 / 3, 0);glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1 / 3, 0);glVertex3f(1.0, 1.0, -1.0)

    # ---Bottom Face---
    glTexCoord2f(1 / 3, 1 / 2);glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(2 / 3, 1 / 2);glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(2 / 3, 1);glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1 / 3, 1);glVertex3f(-1.0, -1.0, 1.0)

    # ---Right face---
    glTexCoord2f(2 / 3, 1 / 2);glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1, 1 / 2);glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(1, 1);glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(2 / 3, 1);glVertex3f(1.0, -1.0, 1.0)

    # ---Left Face---
    glTexCoord2f(0, 1 / 2);glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1 / 3, 1 / 2);glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1 / 3, 0);glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(0, 0);glVertex3f(-1.0, 1.0, -1.0)

    glEnd()
    glutSwapBuffers()

def init(Width, Height):
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(500, 500)
    glutCreateWindow(name)
    glutDisplayFunc(desenha)
    init(2,2)
    glClearColor(0, 0, 0, 1)
    gluPerspective(10, 8 / 3, 0.1, 90)
    glutTimerFunc(10, timer, 1)
    glutMainLoop()
if __name__ == "__main__":
    main()
