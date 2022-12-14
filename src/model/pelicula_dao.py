from re import T
from .conexion_db import conexionBD
from tkinter import messagebox

def crear_tabla():

	conexion = conexionBD()

	sql = """ 
		CREATE TABLE peliculas(
			id_pelicula INTEGER,
			nombre VARCHAR(100),
			duracion VARCHAR(10),
			genero VARCHAR(100),
			PRIMARY KEY(id_pelicula AUTOINCREMENT)
		)
	"""

	try:
		conexion.cursor.execute(sql)
		conexion.cerrar()
		titulo = "Crear registro"
		mensaje = "Se creó la tabla en la base de datos"
		messagebox.showinfo(titulo, mensaje)
	except:
		titulo = "Crear registro"
		mensaje = "La tabla ya está creada en la base de datos"
		messagebox.showwarning(titulo, mensaje)
		

def borrar_tabla():
	conexion = conexionBD()

	sql = """ 
		DROP TABLE peliculas
	"""

	try:
		conexion.cursor.execute(sql)
		conexion.cerrar()
		titulo = "Borrar registro"
		mensaje = "Se borró la tabla en la base de datos"
		messagebox.showinfo(titulo, mensaje)
	except:
		titulo = "Borrar registro"
		mensaje = "No hay tabla en la base de datos"
		messagebox.showerror(titulo, mensaje)

class Pelicula:
	def __init__(self, nombre, duracion, genero):
		
		self.id_pelicula = None
		self.nombre = nombre
		self.duracion = duracion
		self.genero = genero
	
	def __str__(self) -> str:
		return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'

def guardar(pelicula):
	conexion = conexionBD()

	sql = f""" INSERT INTO peliculas(nombre, duracion, genero)
	VALUES('{pelicula.nombre}', '{pelicula.duracion}','{pelicula.genero}') """

	try:
		conexion.cursor.execute(sql)
		conexion.cerrar()

	except:
		titulo = "Conexión al registro"
		mensaje = "La tabla peliculas no está creada en la base de datos"
		messagebox.showerror(titulo, mensaje)

def listar():
	conexion = conexionBD()

	lista_peliculas = []

	sql = 'SELECT * FROM peliculas'

	try:
		conexion.cursor.execute(sql)
		lista_peliculas = conexion.cursor.fetchall()
		conexion.cerrar()
	except:
		titulo = "Coneccion al registro"
		mensaje = "Crea la tabla en la base de datos"
		messagebox.showwarning(titulo, mensaje)

	return lista_peliculas

def editar(pelicula, id_pelicula):
	conexion = conexionBD()

	sql = f""" UPDATE peliculas
	SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}', genero = '{pelicula.genero}' WHERE id_pelicula =  {id_pelicula} """

	try:
		conexion.cursor.execute(sql)
		conexion.cerrar()
	except:
		titulo = "Edición de datos"
		mensaje = "No se ha editato este registro	"
		messagebox.showerror(titulo, mensaje)

def eliminar(id_pelicula):
	conexion = conexionBD()

	sql = f""" DELETE FROM peliculas WHERE id_pelicula= {id_pelicula} """

	try:
		conexion.cursor.execute(sql)
		conexion.cerrar()
	except:
		titulo = "Eliminar datos"
		mensaje = "No se ha eliminado este registro	"
		messagebox.showerror(titulo, mensaje)