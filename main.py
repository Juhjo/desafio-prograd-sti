from aluno import Aluno
from curso import Curso
import csv


def coluna_do_csv(arquivo, coluna):
    with open(arquivo) as fluxo:
        reader = csv.DictReader(fluxo)
        for linha in reader:
            yield linha[coluna]


def importar_dados(vetor, coluna, arquivo):
    for name in coluna_do_csv(arquivo, coluna):
        vetor.append(int(name))


def salvacabecalho(arquivo, vetor):
    with open(arquivo, 'r') as arquivocsv:
        primeira_linha = arquivocsv.readline().rstrip().split(",")
        for header in primeira_linha:
            vetor.append(header)


def remover_repeticoes(vetor):
    organizado = []
    for number in range(len(vetor)):
        encontrou = False
        a = vetor[number]

        for j in range(len(organizado)):
            if a == organizado[j]:
                encontrou = True
                break

        if not encontrou:
            organizado.append(a)

    organizado.sort()

    return organizado



def ajeitar_dados(vetor_final, coluna1, coluna2, csvfile):
    vetor_lido = []
    vetor_referencia = []
    cabecalho = []

    salvacabecalho(csvfile, cabecalho)
    cabecalho.pop(1)
    cabecalho.pop(4)

    
    importar_dados(vetor_referencia, cabecalho[coluna1], csvfile)
    importar_dados(vetor_lido, cabecalho[coluna2], csvfile)

    
    vetor_organizado = remover_repeticoes(vetor_referencia)

    for numero in vetor_organizado:
        org = []

        for j in range(len(vetor_lido)):

            if vetor_referencia[j] == numero:
                org.append(vetor_lido[j])

        vetor_final.append(org)


csvarq = 'notas.csv'


matricula = []
codigo = []
nota_matricula = []
nota_curso = []
carga_horaria_matricula = []
carga_horaria_curso = []
temp = []

salvacabecalho(csvarq, temp)

del (temp[1])
del (temp[4])


importar_dados(matricula, temp[0], csvarq)
importar_dados(codigo, temp[1], csvarq)
matricula = remover_repeticoes(matricula)
codigo = remover_repeticoes(codigo)


temp.clear()


ajeitar_dados(nota_matricula, 0, 2, csvarq)
ajeitar_dados(nota_curso, 1, 2, csvarq)
ajeitar_dados(carga_horaria_matricula, 0, 3, csvarq)
ajeitar_dados(carga_horaria_curso, 1, 3, csvarq)



print("-" * 7, " O CR dos alunos é: ", "-" * 8, '\n')

for i in range(len(matricula)):
    aluno = Aluno(matricula[i], nota_matricula[i], carga_horaria_matricula[i], None)

    aluno.setcr()

    print("{} - {:.2f}\n".format(aluno.matricula, aluno.cr))

print("-" * 37, '\n')

print("-" * 5, " Média de CR dos cursos ", "-" * 6, '\n')

for i in range(len(codigo)):
    curso = Curso(nota_curso[i], carga_horaria_curso[i], codigo[i])

    curso.setcr()

    print("{} - {:.2f}\n".format(curso.codigo_curso, curso.cr))

print("-" * 37, '\n')
