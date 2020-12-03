from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
engine=create_engine('sqlite:///:memory:')
Base=declarative_base(engine)

class Alumnado(Base):
    __tablename__='alumno'   
    id=Column(Integer,Sequence('alumno_seq_id'),primary_key=True)
    nombre_alumno=Column(String)
    apellido_alumno=Column(String)
    curso_id_alumno=Column(Integer,ForeignKey('curso.id'))
    cursos=relationship('Cursado',back_populates='alumnos')
    def __repr__(self):
        return'{}{}'.format(self.nombre_alumno, self.apellido_alumno)

class Cursado(Base):
    __tablename__='curso'
    id=Column(Integer, Sequence('curso_seq_id'),primary_key=True)
    nombre_curso=Column(String)
    alumnos=relationship('Alumnado',back_populates='cursos')
    hora_curso=relationship('Agenda',back_populates='curso_hora')
    def __repr__(self):
        return'{}'.format(self.nombre_curso)

class Agenda(Base):
    __tablename__='horario'
    id=Column(Integer, Sequence('horario_seq_id'),primary_key=True)
    dia=Column(String)
    hora_inicio=Column(String)
    hora_fin=Column(String)
    profesor_id=Column(Integer,ForeignKey('profesor.id'))
    curso_id=Column(Integer,ForeignKey('curso.id'))

    curso_hora=relationship('Cursado',back_populates='hora_curso')
    curso_profesor=relationship('Profesorado',back_populates='profesor_curso')

    def __repr__(self):
        return'{}{}{}'.format(self.dia,self.hora_inicio, self.hora_fin)

class Profesorado(Base):
    __tablename__='profesor'
    id=Column(Integer, Sequence('profesor_seq_id'),primary_key=True)
    nombre_profesor=Column(String)
    apellido_profesor=Column(String)

    profesor_curso=relationship('Agenda',back_populates='curso_profesor')
    def __repr__(self):
        return'{}{}'.format(self.nombre_profesor, self.apellido_profesor)


Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()

alumno1=Alumnado(nombre_alumno='Pablo', apellido_alumno=' Perez')
session.add(alumno1)

horario1=Agenda(dia='martes ',hora_inicio='9:00 ', hora_fin='10:00 ')
session.add(horario1)

horario1.curso_hora=Cursado(nombre_curso='Matematica')
horario1.curso_profesor=Profesorado(nombre_profesor='Laura',apellido_profesor=' Garcia')

print(session.query(Cursado).filter(Profesorado.profesor_curso.any()).all())
print(session.query(Agenda).filter(Profesorado.profesor_curso.any()).all())

