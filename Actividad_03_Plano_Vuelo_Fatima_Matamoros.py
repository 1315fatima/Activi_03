# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 22:14:57 2023

@author: Gabriela Matamoros
"""

import tkinter as tk

ventana = tk.Tk()
ventana.geometry("1030x700")
ventana.config(bg="pink")

ventana.title("Calculadora de Plan de Vuelo")

#Titulo del programa
espacio1 = tk.Label(ventana, bg="pink", fg="pink")
espacio1.grid (row = 0, column = 1)

etiqueta_T = tk.Label(ventana, text='PLANIFICACIÓN DE VUELO FOTOGRAMETRICO', bg='pink', justify= 'center', font= 'Helvetica 14')
etiqueta_T.grid(row= 1, column= 1, columnspan = 8)

#Textos y cajas de textos primera fila
espacio2 = tk.Label(ventana, bg="pink", fg="pink")
espacio2.grid (row = 2, column = 1)

etiq_distfocal = tk.Label(ventana, text="Distancia Focal (mm)", bg="pink", justify= 'center', font= 'Helvetica 11')
etiq_distfocal.grid (row = 3, column = 1)

caja_distfocal = tk.Entry(ventana, font = 'Helvetica 11', justify = "center")
caja_distfocal.grid (row = 3, column = 2)

espacio3 = tk.Label(ventana, bg="pink", fg="pink")
espacio3.grid (row = 3, column = 3)

etiq_anchimage = tk.Label(ventana, text="Ancho de la Imagen (Pixel)", bg="pink", justify= 'center', font= 'Helvetica 11')
etiq_anchimage.grid (row = 3, column = 4)

caja_achimage = tk.Entry(ventana, font = 'Helvetica 11', justify = "center")
caja_achimage.grid (row = 3, column = 5)

espacio4 = tk.Label(ventana, bg="pink", fg="pink")
espacio4.grid (row = 3, column = 6)

etiq_altimage = tk.Label(ventana, text="Alto de la Imagen (Pixel)", bg="pink", justify= 'center', font= 'Helvetica 11')
etiq_altimage.grid (row = 3, column = 7)

caja_altimage = tk.Entry(ventana, font = 'Helvetica 11', justify = "center")
caja_altimage.grid (row = 3, column = 8)

#Textos y cajas de textos segunda fila
espacio5 = tk.Label(ventana, bg="pink", fg="pink")
espacio5.grid (row = 4, column = 1)

etiq_anchsensor = tk.Label(ventana, text="Ancho del Sensor (mm)", bg="pink", justify= 'center', font= 'Helvetica 11')
etiq_anchsensor.grid (row = 5, column = 1)

caja_anchsensor = tk.Entry(ventana, font = 'Helvetica 11', justify = "center")
caja_anchsensor.grid (row = 5, column = 2)

espacio6 = tk.Label(ventana, bg="pink", fg="pink")
espacio6.grid (row = 5, column = 3)

etiq_altosensor = tk.Label(ventana, text="Alto del Sensor (mm)", bg="pink", justify= 'center', font= 'Helvetica 11')
etiq_altosensor.grid (row = 5, column = 4)

caja_altosensor = tk.Entry(ventana, font = 'Helvetica 11', justify = "center")
caja_altosensor.grid (row = 5, column = 5)

espacio7 = tk.Label(ventana, bg="pink", fg="pink")
espacio7.grid (row = 5, column = 6)

etiq_altvuelo = tk.Label(ventana, text="Altura de vuelo (m)", bg="pink", justify= 'center', font= 'Helvetica 11')
etiq_altvuelo.grid (row = 5, column = 7)

caja_altvuelo = tk.Entry(ventana, font = 'Helvetica 11', justify = "center")
caja_altvuelo.grid (row = 5, column = 8)

#Textos y cajas de textos tercera fila
espacio8 = tk.Label(ventana, bg="pink", fg="pink")
espacio8.grid (row = 6, column = 1)

etiq_solongit = tk.Label(ventana, text="Solape Longitudinal (%)", bg="pink", justify= 'center', font= 'Helvetica 11')
etiq_solongit.grid (row = 7, column = 1)

caja_solongit = tk.Entry(ventana, font = 'Helvetica 11', justify = "center")
caja_solongit.grid (row = 7, column = 2)

espacio9 = tk.Label(ventana, bg="pink", fg="pink")
espacio9.grid (row = 7, column = 3)

etiq_soltrans = tk.Label(ventana, text="Solape Transversal (%)", bg="pink", justify= 'center', font= 'Helvetica 11')
etiq_soltrans.grid (row = 7, column = 4)

caja_soltrans = tk.Entry(ventana, font = 'Helvetica 11', justify = "center")
caja_soltrans.grid (row = 7, column = 5)

espacio10 = tk.Label(ventana, bg="pink", fg="pink")
espacio10.grid (row = 7, column = 6)

etiq_largparce = tk.Label(ventana, text="Largo Parcela (m)", bg="pink", justify= 'center', font= 'Helvetica 11')
etiq_largparce.grid (row = 7, column = 7)

caja_largparce = tk.Entry(ventana, font = 'Helvetica 11', justify = "center")
caja_largparce.grid (row = 7, column = 8)

#Textos y cajas de textos cuarta fila
espacio11 = tk.Label(ventana, bg="pink", fg="pink")
espacio11.grid (row = 8, column = 1)

etiq_anchparce = tk.Label(ventana, text="Ancho Parcela (m)", bg="pink", justify= 'center', font= 'Helvetica 11')
etiq_anchparce.grid (row = 9, column = 1)

caja_anchparce = tk.Entry(ventana, font = 'Helvetica 11', justify = "center")
caja_anchparce.grid (row = 9, column = 2)

espacio12 = tk.Label(ventana, bg="pink", fg="pink")
espacio12.grid (row = 9, column = 3)

etiq_velocvuelo = tk.Label(ventana, text="Velocidad de Vuelo (m/s)", bg="pink", justify= 'center', font= 'Helvetica 11')
etiq_velocvuelo.grid (row = 9, column = 4)

caja_velocvuelo = tk.Entry(ventana, font = 'Helvetica 11', justify = "center")
caja_velocvuelo.grid (row = 9, column = 5)

espacio13 = tk.Label(ventana, bg="pink", fg="pink")
espacio13.grid (row = 9, column = 6)

#Resultados de los Calculos introducidos
espacio14 = tk.Label(ventana, bg="pink", fg="pink")
espacio14.grid (row = 10, column = 1)

caja_result = tk.Text(ventana)
caja_result.grid(row = 13, column = 1, columnspan = 8)

espacio15 = tk.Label(ventana, bg="pink", fg="pink")
espacio15.grid (row = 12, column = 1)

def resultados():
    caja_result.delete(1.0, tk.END)
    distfocal = float(caja_distfocal.get())
    anchoimage = float(caja_achimage.get())
    altoimage = int(caja_altimage.get())
    anchosensor = float(caja_anchsensor.get())
    altosensor = float(caja_altosensor.get())
    RSI = anchosensor/anchoimage
    alturavuelo = float(caja_altvuelo.get())
    solaplong = float(caja_solongit.get())
    solaptrans = float(caja_soltrans.get())
    largparcela = float(caja_largparce.get())
    anchparcela = float(caja_anchparce.get())
    velocvuelo = float(caja_velocvuelo.get())
    
    #GSD
    GSD = (((alturavuelo * 100 )/ (distfocal)) * RSI)
    caja_result.insert(tk.END, f"GSD = {GSD}cm/pixel\n\n")
    
    #Escala de Vuelo
    escala_vuelo = 1/((distfocal/1000)/alturavuelo)
    caja_result.insert(tk.END, f"Escala de vuelo = {escala_vuelo}\n\n")
    
    #Ancho de la imagen
    areatomada = (anchosensor*escala_vuelo)/1000
    caja_result.insert(tk.END, f"Ancho de la Imagen Sobre el Terreno = {areatomada}m\n\n")
    
    #Alto de la imagen
    areatomada = (altosensor*escala_vuelo)/1000
    caja_result.insert(tk.END, f"Alto de la Imagen Sobre el Terreno = {areatomada}m\n\n")
    
    #Base Aérea
    base_aerea = (((anchoimage * GSD )/100)* (1-(solaplong/100)))
    caja_result.insert(tk.END, f"Base Aérea = {base_aerea}\n\n")
    
    #Distancia entre vueltas
    distvueltas = (((altoimage * GSD )/100)) * (1-(solaptrans/100))
    caja_result.insert(tk.END, f"Distancia entre vueltas = {distvueltas}m\n\n")
    
    #Tiempo entre fotos y velocidad de vuelo
    tiem_fotos = base_aerea/velocvuelo
    vel_vuelo= base_aerea/tiem_fotos
    caja_result.insert(tk.END, f"Tiempo entre fotos = {tiem_fotos}s\n\n")
    caja_result.insert(tk.END, f"Velocidad de Vuelo= {vel_vuelo}m/s\n\n")
    
    #Número de pasadas
    num_pasadas = round (anchparcela/distvueltas)
    caja_result.insert(tk.END, f"Numero de pasadas = {num_pasadas}\n\n")
    
    #Número de fotos por vueltas
    num_fotos = round (largparcela/base_aerea)+1
    caja_result.insert(tk.END, f"Numero de Fotos por vueltas = {num_fotos}\n\n")
    
    #Número de fotos por pasada
    num_vuelta= round (num_fotos)*(num_pasadas)+1
    caja_result.insert(tk.END, f"Numero de Fotos por Vuelo = {num_vuelta}\n\n")
    
    #Distancia de Vuelo
    dist_vuelo = (num_pasadas*largparcela)+anchparcela
    caja_result.insert(tk.END, f"Distancia de Vuelo = {dist_vuelo}m\n\n")
    
    #Duración de vuelo 
    tiemp_vuelo= ((num_vuelta * tiem_fotos)/60)
    caja_result.insert(tk.END, f"Duracion del Vuelo = {tiemp_vuelo}min")

#Botonde con la funcion de calcular
boton_Cal = tk.Button(ventana, text = 'Calcular', font = 'Helvetica 11', justify = "center", command = resultados)
boton_Cal.grid(row = 11, column = 4, columnspan = 3)

ventana.mainloop()