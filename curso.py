class Curso:
    
    __codigo_curso = 0
    __nota = []
    __carga_horaria = []
    _cr = 0

    
    def __init__(self, nota, carga_horaria, codigo_curso):
        self.__nota = nota
        self.__carga_horaria = carga_horaria
        self.__codigo_curso = codigo_curso

    def setcodigo_curso(self, codigo_curso):
        self.__codigo_curso = codigo_curso

    @property
    def codigo_curso(self):
        return self.__codigo_curso

    def setnota(self, nota):
        self.__nota.append(nota)

    @property
    def nota(self):
        return self.__nota

    def setcarga_horaria(self, carga_horaria):
        self.__carga_horaria.append(carga_horaria)

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    def setcr(self):
        nota_total = 0
        carga_total = 0

        for i in range(len(self.__nota)):
            nota_total += (self.__nota[i] * self.__carga_horaria[i])
            carga_total += self.__carga_horaria[i]

        self._cr = nota_total / carga_total

    @property
    def cr(self):
        return self._cr
