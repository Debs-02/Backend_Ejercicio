from models import Articulo
from conexionDB import conexionSQLServer
import pyodbc
from fastapi import HTTPException, status

class ArticuloController:
    def Create(element:Articulo):
            try:    
                conexion=conexionSQLServer()
                conexion.conectar()
                cursor=conexion.obtener_conexion().cursor()
                
                sql="SET NOCOUNT ON exec  SP_CreateArticulo ?,?,?,?"
                
                cursor.execute(sql,(element.sku.upper(),element.nombre,element.marca,element.cantidad))
                
                row = cursor.fetchone()
                cursor.commit()
                if row:
                    element=Articulo(Codigo=row[0],
                                        sku=row[1],
                                        nombre=row[2],
                                        marca=row[3],
                                        cantidad=row[4],
                                        fecha_creacion=row[5].strftime('%Y-%m-%d %H:%M:%S'))
                return element
                

            except pyodbc.Error as ex:
                raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY,detail=ex.args[1])   
            except Exception as exc :
                raise exc   
            finally:
                cursor.close()


    def Read():
            try:
                articulos=[]
                conexion = conexionSQLServer()
                conexion.conectar()
                cursor = conexion.obtener_conexion().cursor()
                cursor.execute("SET NOCOUNT ON exec SP_ReadAllArticulos")
                rows = cursor.fetchall()
                cursor.commit()

                for row in rows:
                    element=Articulo(Codigo=row[0],
                                        sku=row[1],
                                        nombre=row[2],
                                        marca=row[3],
                                        cantidad=row[4],
                                        fecha_creacion=row[5].strftime('%Y-%m-%d %H:%M:%S')
                                        )
                    articulos.append(element)
                
                if len(articulos) == 0:
                    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="No se pudo obtener informacion de la base de datos")
                            
                return articulos  
            except pyodbc.Error as ex:
                raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY,detail=ex.args[1])   
            except Exception as exc :
                raise exc       
            finally:
                cursor.close()


    def ReadArticuloBySku(sku: str):
        try:
            articulos = []
            conexion = conexionSQLServer()
            conexion.conectar()
            cursor = conexion.obtener_conexion().cursor()
            
            sql = "SET NOCOUNT ON exec SP_ReadArticulosBySku ?"
            
            # Pasa el parámetro como una tupla (sku,)
            cursor.execute(sql, (sku.upper(),))  # Asegúrate de pasarlo como una tupla
        
            row = cursor.fetchone()
            cursor.commit()
            
            if row:
                element = Articulo(
                    Codigo=row[0],
                    sku=row[1],
                    nombre=row[2],
                    marca=row[3],
                    cantidad=row[4],
                    fecha_creacion=row[5].strftime('%Y-%m-%d %H:%M:%S')
                )
                return element
            
        except pyodbc.Error as ex:
            raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail=ex.args[1])   
        except Exception as exc:
            raise exc       
        finally:
            cursor.close()




    
    def Update(element:Articulo):
        try:

            conexion=conexionSQLServer()
            conexion.conectar()
            cursor =conexion.obtener_conexion().cursor()
            
            sql="SET NOCOUNT ON exec SP_UpdateArticulo ?,?,?,?,?"
            cursor.execute(sql,(element.Codigo,
                                element.sku,
                                element.nombre,
                                element.marca,
                                element.cantidad
                            ))
           
            cursor.commit()
            return element
        except pyodbc.Error as ex:
            raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY,detail=ex.args[1])   

        finally:
            cursor.close()    


    def Delete(codigo:int):
        try:

            conexion=conexionSQLServer()
            conexion.conectar()
            cursor =conexion.obtener_conexion().cursor()
            
            sql="SET NOCOUNT ON exec SP_DeleteArticulo ?"
            cursor.execute(sql,(codigo))
           
            cursor.commit()
        except pyodbc.Error as ex:
            raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY,detail=ex.args[1])   

        finally:
            cursor.close()    



