from curso import Curso


class Aluno(Curso):
    __matricula = 0

    def __init__(self, matricula, nota, carga_horaria, codigo_curso):
        super().__init__(nota, carga_horaria, codigo_curso)
        self.__matricula = matricula

    def setmatricula(self, matricula):
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula
