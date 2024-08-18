from conexionBD import *
from usuarios.users import *
from goles.goll import *
from equipos.equip import *
from partidos.part import *
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def ventana_menu_presi(id,nombre,apellido,idEquipo):
    from equipos.equip import Equipo
    if idEquipo != None:
        ventana = Tk()
        ventana.title("Menú presidente")
        ventana.geometry("800x500")
        ventana.config(bg="#fcfcfc")
        ventana.resizable(width=0, height=0)

        def fijar_menu():
            welcome_frame.destroy()

            frame_form = Frame(ventana, bd=0, relief=SOLID, bg="#fcfcfc")
            frame_form.pack(side="right", expand=YES,fill=BOTH)

            frame_form_top = Frame(main_frame, height= 50, bd=0, relief=SOLID, bg="black")
            frame_form_top.pack(side="top", fill=X)
            title = Label(frame_form_top, text="Fija un nuevo presupuesto", font=("Times", 30), fg="black", bg="white", pady=20)
            title.pack(expand=YES, fill=BOTH)

            frame_form_fill = Frame(main_frame, height=50, bd=0, relief=SOLID, bg="#fcfcfc")
            frame_form_fill.pack(side="bottom", expand=YES, fill=BOTH)

            etiqueta_actual = Label(frame_form_fill, text="Presupuesto actual", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
            etiqueta_actual.pack(fill=X, padx=20, pady=5)
            cursor.execute("SELECT presupuesto FROM equipo WHERE presidente = %s", (id,))
            presupuesto_actual = cursor.fetchone()
            presupuesto_actual = presupuesto_actual[0]
            presupuesto_actual = Label(frame_form_fill, text=f"$ {presupuesto_actual}", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
            presupuesto_actual.pack(fill=X, padx=20, pady=5)
            
            etiqueta_presupuesto = Label(frame_form_fill, text="Presupuesto nuevo:", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
            etiqueta_presupuesto.pack(fill=X, padx=20, pady=5)
            presupuesto = Entry(frame_form_fill, font=("Times", 20))
            presupuesto.pack(fill=X, padx=20, pady=10)

            fijar_btn = Button(frame_form_fill, text="Fijar presupuesto", bg="#3a7ff6", fg="white", bd=0, font=("Bold", 15), command=lambda:fijarPresupuesto())
            fijar_btn.pack(fill=X, padx=20, pady=20)

            def fijarPresupuesto():
                if presupuesto.get():
                    resultado = messagebox.askquestion("ALERTA", "¿Deseas fijar este presupuesto?")
                    if resultado == "yes":
                        cursor.execute("UPDATE equipo SET presupuesto = %s WHERE presidente = %s", (presupuesto.get(), id))
                        conexion.commit()
                        messagebox.showinfo(message="Presupuesto fijado con éxito.",title="ALERTA")
                else:
                    messagebox.showerror(message="Por favor, rellene el campo.",title="ALERTA")

        def agendar_menu():
            welcome_frame.destroy()

            def agendarPartido(idRival):
                if idRival:
                    if idRival != idEquipo:
                        cursor.execute("SELECT id FROM equipo WHERE id = %s", (idRival,))
                        result = cursor.fetchone()
                        if result:
                            frame_form_fill.destroy()

                            frame_form_agen = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
                            frame_form_agen.pack(side="bottom", expand=YES, fill=BOTH)

                            fecha = Label(frame_form_agen, text="Fecha del partido(AAAA-MM-DD)", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                            fecha.pack(fill=X, padx=20, pady=5)
                            fecha_entry = Entry(frame_form_agen, font=("Times", 20))
                            fecha_entry.pack(fill=X, padx=20, pady=10)

                            estadio = Label(frame_form_agen, text="Estadio del partido", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                            estadio.pack(fill=X, padx=20, pady=5)
                            estadio_entry = Entry(frame_form_agen, font=("Times", 20))
                            estadio_entry.pack(fill=X, padx=20, pady=10)

                            btn = Button(frame_form_agen, text="Agendar", bg="#3a7ff6", fg="white", bd=0, font=("Bold", 15), command=lambda:agendar(fecha_entry.get(),estadio_entry.get()))
                            btn.pack(fill=X, padx=20, pady=20)

                            def agendar(fecha,estadio):
                                if fecha and estadio:
                                    resultado = messagebox.askquestion("ALERTA", "¿Deseas agendar este partido?")
                                    if resultado == "yes":
                                        new_part = Partido(idEquipo, idRival, fecha, "Pendiente", estadio)
                                        Presidente.registrarPartido(new_part)
                                        messagebox.showinfo(message="Partido agendado con éxito.",title="ALERTA")
                                else:
                                    messagebox.showerror(message="Por favor, rellene los campos.",title="ALERTA")

                        else:
                            messagebox.showerror(message="Por favor, ingrese un equipo válido.",title="ALERTA")
                    else:
                        messagebox.showerror(message="No puedes agendar un partido contigo mismo.",title="ALERTA")
                else:
                    messagebox.showerror(message="Por favor, rellene el campo.",title="ALERTA")

            frame_form = Frame(ventana, bd=0, relief=SOLID, bg="#fcfcfc")
            frame_form.pack(side="right", expand=YES,fill=BOTH)

            frame_form_top = Frame(main_frame, height= 50, bd=0, relief=SOLID, bg="black")
            frame_form_top.pack(side="top", fill=X)
            title = Label(frame_form_top, text="Agenda un nuevo partido", font=("Times", 30), fg="black", bg="white", pady=20)
            title.pack(expand=YES, fill=BOTH)

            frame_form_fill = Frame(main_frame, height=50, bd=0, relief=SOLID, bg="#fcfcfc")
            frame_form_fill.pack(side="bottom", expand=YES, fill=BOTH)

            rival = Label(frame_form_fill, text="ID del equipo rival", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
            rival.pack(fill=X, padx=20, pady=5)
            rival_entry = Entry(frame_form_fill, font=("Times", 20))
            rival_entry.pack(fill=X, padx=20, pady=10)

            btn_rival = Button(frame_form_fill, text="Continuar", bg="#3a7ff6", fg="white", bd=0, font=("Bold", 15), command=lambda:agendarPartido(rival_entry.get()))
            btn_rival.pack(fill=X, padx=20, pady=20)

            cursor.execute("SELECT id, nombre, pais FROM equipo WHERE id != %s", (idEquipo,))
            resultados = cursor.fetchall()

            if resultados:
                
                tree = ttk.Treeview(frame_form_fill, columns=("id", "nombre", "pais", "estadio"), show="headings")
                tree.heading("id", text="id")
                tree.heading("nombre", text="Nombre")
                tree.heading("pais", text="Pais")
                tree.heading("estadio", text="Estadio")
                tree.column("id",width=40)
                tree.column("nombre", width=170)
                tree.column("pais", width=170)
                tree.column("estadio", width=170)
                tree.pack(fill=BOTH, expand=YES)

                for row in resultados:
                    tree.insert("", "end", values=row)
            else:
                messagebox.showerror(message="No hay equipos disponibles para agendar.",title="ALERTA")
        
        def gestionar_menu():
            welcome_frame.destroy()

            frame_form = Frame(ventana, bd=0, relief=SOLID, bg="#fcfcfc")
            frame_form.pack(side="right", expand=YES,fill=BOTH)

            frame_form_top = Frame(main_frame, height= 50, bd=0, relief=SOLID, bg="black")
            frame_form_top.pack(side="top", fill=X)
            title = Label(frame_form_top, text="Gestión del equipo", font=("Times", 30), fg="black", bg="white", pady=20)
            title.pack(expand=YES, fill=BOTH)

            frame_form_fill = Frame(main_frame, height=50, bd=0, relief=SOLID, bg="white")
            frame_form_fill.pack(side="bottom", expand=YES, fill=BOTH)

            frame_form_fill.columnconfigure(0, weight=1)
            frame_form_fill.columnconfigure(1, weight=1)
            frame_form_fill.columnconfigure(2, weight=1)

            ckbox_ver = Radiobutton(frame_form_fill, text="Ver jugadores", font=("Times", 14), fg="#666a88", bg="white", anchor=W, command=lambda:ver())
            ckbox_ver.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
            ckbox_ver.bind("<Return>", lambda event: ver())
            ckbox_despedir = Radiobutton(frame_form_fill, text="Despedir jugador", font=("Times", 14), fg="#666a88", bg="white", anchor=W, command=lambda:despedir())
            ckbox_despedir.bind("<Return>", lambda event: despedir())
            ckbox_despedir.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
            ckbox_contratar = Radiobutton(frame_form_fill, text="Contratar jugador", font=("Times", 14), fg="#666a88", bg="white", anchor=W, command=lambda:contratar())
            ckbox_contratar.bind("<Return>", lambda event: contratar())
            ckbox_contratar.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

            def ver():
                frame_form_fill.destroy()

                frame_form_ver = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
                frame_form_ver.pack(side="bottom", expand=YES, fill=BOTH)

                pres = Label(frame_form_ver, text="Jugadores del equipo", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                pres.pack(fill=X, padx=20, pady=5)

                cursor.execute("SELECT id, nombre, apellido, nacionalidad FROM usuarios WHERE equipo_jug = %s", (idEquipo,))
                resultados = cursor.fetchall()
                if resultados:
                    tree = ttk.Treeview(frame_form_ver, columns=("id", "nombre", "apellido", "nacionalidad"), show="headings")
                    tree.heading("id", text="id")
                    tree.heading("nombre", text="Nombre")
                    tree.heading("apellido", text="Apellido")
                    tree.heading("nacionalidad", text="Nacionalidad")
                    tree.column("id",width=40)
                    tree.column("nombre", width=170)
                    tree.column("apellido", width=170)
                    tree.column("nacionalidad", width=170)
                    tree.pack(fill=BOTH, expand=YES)

                    for row in resultados:
                        tree.insert("", "end", values=row)
                else:
                    messagebox.showerror(message="No hay jugadores en el equipo.",title="ALERTA")

            def despedir():
                frame_form_fill.destroy()

                frame_form_despido = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
                frame_form_despido.pack(side="bottom", expand=YES, fill=BOTH)

                pres = Label(frame_form_despido, text="Despide a un jugador", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                pres.pack(fill=X, padx=20, pady=5)

                cursor.execute("SELECT id, nombre, apellido, nacionalidad FROM usuarios WHERE equipo_jug = %s", (idEquipo,))
                resultados = cursor.fetchall()
                if resultados:
                        
                        def despedir(idJug):
                            if idJug:
                                cursor.execute("SELECT id FROM usuarios WHERE id = %s AND equipo_jug = %s", (idJug, idEquipo))
                                result = cursor.fetchone()
                                if result:
                                    resultado = messagebox.askquestion("ALERTA", "¿Deseas despedir a este jugador?")
                                    if resultado == "yes":
                                        cursor.execute("UPDATE usuarios SET equipo_jug = 0 WHERE id = %s", (idJug,))
                                        conexion.commit()
                                        messagebox.showinfo(message="Jugador despedido con éxito.",title="ALERTA")
                                else:
                                    messagebox.showerror(message="Por favor, ingrese un jugador válido.",title="ALERTA")
                            else:
                                messagebox.showerror(message="Por favor, rellene el campo.",title="ALERTA")
    
                        labell = Label(frame_form_despido, text="Si deseas despedir a alguno, seleccione el id", font=("Times", 15), fg="#666a88",bg="#fcfcfc", anchor=W)
                        labell.pack(fill=X, padx=20, pady=5)
                        entry = Entry(frame_form_despido, font=("Times", 15))
                        entry.pack(fill=X, padx=20, pady=10)
                        btn = Button(frame_form_despido, text="Despedir", font=('Times', 15), bg="#3a7ff6", bd=0, fg="#fff", command=lambda:despedir(entry.get()))
                        btn.pack(fill=X, padx=20, pady=20)
    
                        tree = ttk.Treeview(frame_form_despido, columns=("id", "nombre", "apellido", "nacionalidad"), show="headings")
                        tree.heading("id", text="id")
                        tree.heading("nombre", text="Nombre")
                        tree.heading("apellido", text="Apellido")
                        tree.heading("nacionalidad", text="Nacionalidad")
                        tree.column("id",width=40)
                        tree.column("nombre", width=170)
                        tree.column("apellido", width=170)
                        tree.column("nacionalidad", width=170)
                        tree.pack(fill=BOTH, expand=YES)
    
                        for row in resultados:
                            tree.insert("", "end", values=row)
                else:
                    messagebox.showerror(message="No hay jugadores en el equipo.",title="ALERTA")

            def contratar():
                frame_form_fill.destroy()

                frame_form_contrato = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
                frame_form_contrato.pack(side="bottom", expand=YES, fill=BOTH)

                title= Label(frame_form_contrato, text="Contrata un nuevo jugador", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                title.pack(fill=X, padx=20, pady=5)

                cursor.execute("SELECT * FROM usuarios WHERE tipo = 'Jugador' and equipo_jug = 0")
                resultados = cursor.fetchall()
                if resultados:

                    def contratar(idJug):
                        if idJug:
                            cursor.execute("SELECT id FROM usuarios WHERE id = %s AND tipo = 'Jugador' and equipo_jug = 0", (idJug,))
                            result = cursor.fetchone()
                            if result:
                                resultado = messagebox.askquestion("ALERTA", "¿Deseas contratar a este jugador?")
                                if resultado == "yes":
                                    Presidente.contratoJugador(idJug,idEquipo)
                                    messagebox.showinfo(message="Jugador contratado con éxito.",title="ALERTA")
                            else:
                                messagebox.showerror(message="Por favor, ingrese un jugador válido.",title="ALERTA")
                        else:
                            messagebox.showerror(message="Por favor, rellene el campo.",title="ALERTA")

                    labell = Label(frame_form_contrato, text="Si deseas contratar a alguno, seleccione el id", font=("Times", 15), fg="#666a88",bg="#fcfcfc", anchor=W)
                    labell.pack(fill=X, padx=20, pady=5)
                    entry = Entry(frame_form_contrato, font=("Times", 15))
                    entry.pack(fill=X, padx=20, pady=10)
                    btn = Button(frame_form_contrato, text="Contratar", font=('Times', 15), bg="#3a7ff6", bd=0, fg="#fff", command=lambda:contratar(entry.get()))
                    btn.pack(fill=X, padx=20, pady=20)

                    tree = ttk.Treeview(frame_form_contrato, columns=("id", "nombre", "apellido", "nacionalidad"), show="headings")
                    tree.heading("id", text="id")
                    tree.heading("nombre", text="Nombre")
                    tree.heading("apellido", text="Apellido")
                    tree.heading("nacionalidad", text="Nacionalidad")
                    tree.column("id",width=40)
                    tree.column("nombre", width=170)
                    tree.column("apellido", width=170)
                    tree.column("nacionalidad", width=170)
                    tree.pack(fill=BOTH, expand=YES)

                    for row in resultados:
                        tree.insert("", "end", values=row)
                else:
                    messagebox.showerror(message="No hay jugadores disponibles para contratar.",title="ALERTA")
        
        def consultar_menu():
            welcome_frame.destroy()

            def completados():
                frame_form_fill.destroy()

                frame_form_complete = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
                frame_form_complete.pack(side="bottom", expand=YES, fill=BOTH)

                pres = Label(frame_form_complete, text="Partidos completados", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                pres.pack(fill=X, padx=20, pady=5)

                cursor.execute("SELECT id,idEq1,idEq2,fecha,estadio FROM partido WHERE (idEq1 = %s OR idEq2 = %s) AND estado = 'Completado'", (idEquipo, idEquipo))
                resultados = cursor.fetchall()
                if resultados:
                    tree = ttk.Treeview(frame_form_complete, columns=("id", "Equipo 1", "Equipo 2", "Fecha", "Estadio"), show="headings")
                    tree.heading("id", text="id")
                    tree.heading("Equipo 1", text="id Equipo 1")
                    tree.heading("Equipo 2", text="id Equipo 2")
                    tree.heading("Fecha", text="Fecha")
                    tree.heading("Estadio", text="Estadio")
                    tree.column("id",width=110)
                    tree.column("Equipo 1", width=110)
                    tree.column("Equipo 2", width=110)
                    tree.column("Fecha", width=110)
                    tree.column("Estadio", width=110)
                    tree.pack(fill=BOTH, expand=YES)

                    for row in resultados:
                        tree.insert("", "end", values=row)
                else:
                    messagebox.showerror(message="No hay partidos completados.",title="ALERTA")

            def pendientes():
                frame_form_fill.destroy()

                frame_form_complete = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
                frame_form_complete.pack(side="bottom", expand=YES, fill=BOTH)

                pres = Label(frame_form_complete, text="Partidos pendientes", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                pres.pack(fill=X, padx=20, pady=5)

                cursor.execute("SELECT id,idEq1,idEq2,fecha,estadio FROM partido WHERE (idEq1 = %s OR idEq2 = %s) AND estado = 'Pendiente'", (idEquipo, idEquipo))
                resultados = cursor.fetchall()
                if resultados:

                    def completar(idP):
                        if idP:
                            cursor.execute("SELECT id FROM partido WHERE id = %s", (idP,))
                            result = cursor.fetchone()
                            if result:
                                cursor.execute("SELECT * FROM usuarios WHERE equipo_jug = %s", (idEquipo,))
                                jugadores = cursor.fetchall()
                                if jugadores:
                                    frame_form_fill.destroy()
                                    frame_form_complete.destroy()

                                    frame_form_botones = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
                                    frame_form_botones.pack(side="bottom", expand=YES, fill=BOTH)

                                    def completarr(idd):
                                        frame_form_botones.destroy()

                                        def avanzar(gT):
                                            if gT:
                                                frame_form_llenar.destroy()
                                                global cont
                                                cont = 0
                                                def registrar(id_jug,minuto,gT):
                                                    if id and minuto:
                                                        new_gol = Goles(id_jug,idEquipo,idd,minuto,gT)
                                                        Goles.registrar_gol(new_gol)
                                                        messagebox.showinfo(message="Gol registrado con éxito.",title="ALERTA")
                                                    else:
                                                        messagebox.showerror(message="Por favor, rellene los campos.",title="ALERTA")

                                                def llamar(id_jug, min, gT):
                                                    global cont
                                                    if id_jug and min and (cont+1) < int(gT):
                                                        registrar(id_jug,min,gT)
                                                        minuto_entry.delete(0, END)
                                                        id_jug_entry.delete(0, END)
                                                        cont += 1
                                                    elif (cont+1) == int(gT):
                                                        messagebox.showinfo(message="Goles completados.\nRegistro completado",title="ALERTA")
                                                        frame_form_botones.destroy()
                                                        frame_form_final = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
                                                        frame_form_final.pack(side="bottom", expand=YES, fill=BOTH)

                                                        btn = Button(frame_form_final, text="Continuar", bg="#3a7ff6", fg="white", bd=0, font=("Bold", 15), command=lambda:finalizar())
                                                        btn.pack(fill=X, padx=20, pady=20)

                                                        def finalizar():
                                                            ele = messagebox.askquestion("ALERTA", "¿Deseas finalizar el partido?")
                                                            if ele == "yes":
                                                                cursor.execute("UPDATE partido SET estado = 'Completado' WHERE id = %s", (idd,))
                                                                conexion.commit()
                                                                messagebox.showinfo(message="Partido completado con éxito.",title="ALERTA")
                                                    else:
                                                        messagebox.showerror(message="Por favor, rellene el campo.",title="ALERTA")

                                                frame_form_botones = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
                                                frame_form_botones.pack(side="bottom", expand=YES, fill=BOTH)

                                                id_jug = Label(frame_form_botones, text="ID del jugador", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                                                id_jug.grid(row=0, column=0, padx=20, pady=5)
                                                id_jug_entry = Entry(frame_form_botones, font=("Times", 20))
                                                id_jug_entry.grid(row=1, column=1, padx=20, pady=10)
                                                
                                                minuto = Label(frame_form_botones, text="Minuto del gol", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                                                minuto.grid(row=2, column=0, padx=20, pady=5)
                                                minuto_entry = Entry(frame_form_botones, font=("Times", 20))
                                                minuto_entry.grid(row=3, column=1, padx=20, pady=10)

                                                btn = Button(frame_form_botones, text="Registrar", bg="#3a7ff6", fg="white", bd=0, font=("Bold", 15), command=lambda:llamar(id_jug_entry.get(),minuto_entry.get(),gT))
                                                btn.grid(row=4, column=1, padx=20, pady=10)
                                            else:
                                                messagebox.showerror(message="Por favor, rellene el campo.",title="ALERTA")

                                        frame_form_llenar = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
                                        frame_form_llenar.pack(side="bottom", expand=YES, fill=BOTH)

                                        golesT = Label(frame_form_llenar, text="Goles Totales", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                                        golesT.pack(fill=X, padx=20, pady=5)
                                        golesT_entry = Entry(frame_form_llenar, font=("Times", 20))
                                        golesT_entry.pack(fill=X, padx=20, pady=10)

                                        btn = Button(frame_form_llenar, text="Continuar", bg="#3a7ff6", fg="white", bd=0, font=("Bold", 15), command=lambda: avanzar(golesT_entry.get()))
                                        btn.pack(fill=X, padx=20, pady=20)
                                else:
                                    messagebox.showerror(message="No hay jugadores en el equipo.",title="ALERTA")

                                def cancelar(idd):
                                    if idd:
                                        resultado=messagebox.askquestion("ALERTA", "¿Deseas cancelar este partido?")
                                        if resultado == "yes":
                                            cursor.execute("UPDATE partido SET estado = 'Cancelado' WHERE id = %s", (idd,))
                                            conexion.commit()
                                            messagebox.showinfo(message="Partido cancelado con éxito.",title="ALERTA")
                                    else:
                                        messagebox.showerror(message="Por favor, rellene el campo.",title="ALERTA")

                                ckbox_jugador = Radiobutton(frame_form_botones, text="Completar", font=("Times", 14), fg="#666a88", bg="white", anchor=W, command=lambda: completarr(idP))
                                ckbox_jugador.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
                                ckbox_jugador.bind("<Return>", lambda event: completarr())
                                ckbox_presidente = Radiobutton(frame_form_botones, text="Cancelar", font=("Times", 14), fg="#666a88", bg="white", anchor=W, command=lambda:cancelar(idP))
                                ckbox_presidente.bind("<Return>", lambda event: cancelar())
                                ckbox_presidente.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
                            else:
                                messagebox.showerror(message="Por favor, ingrese un partido válido.",title="ALERTA")
                        else:
                            messagebox.showerror(message="Por favor, rellene el campo.",title="ALERTA")

                    labell = Label(frame_form_complete, text="Si desea completar o cancelar alguno, seleccione el id", font=("Times", 15), fg="#666a88",bg="#fcfcfc", anchor=W)
                    labell.pack(fill=X, padx=20, pady=5)
                    entry = Entry(frame_form_complete, font=("Times", 15))
                    entry.pack(fill=X, padx=20, pady=10)
                    btn = Button(frame_form_complete, text="Completar", font=('Times', 15), bg="#3a7ff6", bd=0, fg="#fff", command=lambda:completar(entry.get()))
                    btn.pack(fill=X, padx=20, pady=20)

                    tree = ttk.Treeview(frame_form_complete, columns=("id", "Equipo 1", "Equipo 2", "Fecha", "Estadio"), show="headings")
                    tree.heading("id", text="id")
                    tree.heading("Equipo 1", text="id Equipo 1")
                    tree.heading("Equipo 2", text="id Equipo 2")
                    tree.heading("Fecha", text="Fecha")
                    tree.heading("Estadio", text="Estadio")
                    tree.column("id",width=110)
                    tree.column("Equipo 1", width=110)
                    tree.column("Equipo 2", width=110)
                    tree.column("Fecha", width=110)
                    tree.column("Estadio", width=110)
                    tree.pack(fill=BOTH, expand=YES)

                    for row in resultados:
                        tree.insert("", "end", values=row)
                else:
                    messagebox.showerror(message="No hay partidos pendientes.",title="ALERTA")

            def cancelados():
                frame_form_fill.destroy()

                frame_form_complete = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
                frame_form_complete.pack(side="bottom", expand=YES, fill=BOTH)

                pres = Label(frame_form_complete, text="Partidos cancelados", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                pres.pack(fill=X, padx=20, pady=5)

                cursor.execute("SELECT id,idEq1,idEq2,fecha,estadio FROM partido WHERE (idEq1 = %s OR idEq2 = %s) AND estado = 'Cancelado'", (idEquipo, idEquipo))
                resultados = cursor.fetchall()
                if resultados:
                    tree = ttk.Treeview(frame_form_complete, columns=("id", "Equipo 1", "Equipo 2", "Fecha", "Estadio"), show="headings")
                    tree.heading("id", text="id")
                    tree.heading("Equipo 1", text="id Equipo 1")
                    tree.heading("Equipo 2", text="id Equipo 2")
                    tree.heading("Fecha", text="Fecha")
                    tree.heading("Estadio", text="Estadio")
                    tree.column("id",width=110)
                    tree.column("Equipo 1", width=110)
                    tree.column("Equipo 2", width=110)
                    tree.column("Fecha", width=110)
                    tree.column("Estadio", width=110)
                    tree.pack(fill=BOTH, expand=YES)

                    for row in resultados:
                        tree.insert("", "end", values=row)
                else:
                    messagebox.showerror(message="No hay partidos cancelados.",title="ALERTA")

            frame_form = Frame(ventana, bd=0, relief=SOLID, bg="#fcfcfc")
            frame_form.pack(side="right", expand=YES,fill=BOTH)

            frame_form_top = Frame(main_frame, height= 50, bd=0, relief=SOLID, bg="black")
            frame_form_top.pack(side="top", fill=X)
            title = Label(frame_form_top, text="Consulta los partidos del equipo", font=("Times", 30), fg="black", bg="white", pady=20)
            title.pack(expand=YES, fill=BOTH)

            frame_form_fill = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
            frame_form_fill.pack(side="bottom", expand=YES, fill=BOTH)
            frame_form_fill.columnconfigure(0, weight=1)
            frame_form_fill.columnconfigure(1, weight=1)
            frame_form_fill.columnconfigure(2, weight=1)

            ckbox_jugador = Radiobutton(frame_form_fill, text="Completados", font=("Times", 14), fg="#666a88", bg="white", anchor=W, command=lambda:completados())
            ckbox_jugador.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
            ckbox_jugador.bind("<Return>", lambda event: completados())
            ckbox_presidente = Radiobutton(frame_form_fill, text="Pendientes", font=("Times", 14), fg="#666a88", bg="white", anchor=W, command=lambda:pendientes())
            ckbox_presidente.bind("<Return>", lambda event: pendientes())
            ckbox_presidente.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
            ckbox_equipo = Radiobutton(frame_form_fill, text="Cancelados", font=("Times", 14), fg="#666a88", bg="white", anchor=W, command=lambda:cancelados())
            ckbox_equipo.bind("<Return>", lambda event: cancelados())
            ckbox_equipo.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        
        def renovar_menu():

            welcome_frame.destroy()

            def renovar(idNuevo):
                if idNuevo:
                    cursor.execute("SELECT id FROM usuarios WHERE id = %s AND tipo = 'Presidente'", (idNuevo,))
                    result = cursor.fetchone()
                    if result:
                        resultado = messagebox.askquestion("ALERTA", "¿Deseas renovar el presidente?")
                        if resultado == "yes":
                            Equipo.cambiar_presidente(idNuevo,idEquipo,id)
                            messagebox.showinfo(message="Presidente renovado con éxito.\nSe cerrará la sesión actual",title="ALERTA")
                            ventana.destroy()
                            ventana_login()
                        else:
                            messagebox.showerror(message="Error al renovar presidente.",title="ALERTA")
                    else:
                        messagebox.showerror(message="Por favor, ingrese un presidente válido.",title="ALERTA")
                else:
                    messagebox.showerror(message="Por favor, rellene el campo.",title="ALERTA")

            frame_form = Frame(ventana, bd=0, relief=SOLID, bg="#fcfcfc")
            frame_form.pack(side="right", expand=YES,fill=BOTH)

            frame_form_top = Frame(main_frame, height= 50, bd=0, relief=SOLID, bg="black")
            frame_form_top.pack(side="top", fill=X)
            title = Label(frame_form_top, text="Renovar presidente del equipo", font=("Times", 30), fg="black", bg="white", pady=20)
            title.pack(expand=YES, fill=BOTH)

            frame_form_fill = Frame(main_frame, height=50, bd=0, relief=SOLID, bg="#fcfcfc")
            frame_form_fill.pack(side="bottom", expand=YES, fill=BOTH)

            cursor.execute("SELECT id, nombre, apellido, antiguedad FROM usuarios WHERE tipo = 'Presidente' and equipo IS NULL")
            resultados = cursor.fetchall()

            if resultados:

                pres = Label(frame_form_fill, text="Presidentes disponibles", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                pres.pack(fill=X, padx=20, pady=5)
                presi = Label(frame_form_fill, text="Seleccione el ID del preisdente", font=("Times", 15), fg="#666a88",bg="#fcfcfc", anchor=W)
                presi.pack(fill=X, padx=20, pady=5)
                presi_entry = Entry(frame_form_fill, font=("Times", 15))
                presi_entry.pack(fill=X, padx=20, pady=10)
                btncont = Button(frame_form_fill, text="Continuar", font=('Times', 15), bg="#3a7ff6", bd=0, fg="#fff", command=lambda: renovar(presi_entry.get()))
                btncont.pack(fill=X, padx=20, pady=20)
                tree = ttk.Treeview(frame_form_fill, columns=("id", "nombre", "apellido", "nacionalidad"), show="headings")
                tree.heading("id", text="id")
                tree.heading("nombre", text="Nombre")
                tree.heading("apellido", text="Apellido")
                tree.heading("nacionalidad", text="Antiguedad")
                tree.column("id",width=40)
                tree.column("nombre", width=170)
                tree.column("apellido", width=170)
                tree.column("nacionalidad", width=170)
                tree.pack(fill=BOTH, expand=YES)

                for row in resultados:
                    tree.insert("", "end", values=row)
            else:
                messagebox.showinfo(message="No hay presidentes disponibles para cambio." ,title="ALERTA")

        def salir():
            welcome_frame.destroy()

            resultado = messagebox.askquestion("ALERTA", "¿Deseas salir del sistema?")
            if resultado == "yes":
                ventana.destroy()
                ventana_login()
        
        def hide():
            fijar_indicate.configure(bg="#404040")
            agendar_indicate.configure(bg="#404040")
            gestionar_indicate.configure(bg="#404040")
            consultar_indicate.configure(bg="#404040")
            renovar_indicate.configure(bg="#404040")
            salir_indicate.configure(bg="#404040")

        def borrarPages():
            for frame in main_frame.winfo_children():
                frame.destroy()

        def indicate(lb, page):
            hide()
            lb.configure(bg="#158aff")
            borrarPages()
            page()

        option_frame = Frame(ventana, bg="#404040")

        fijar_btn = Button(option_frame, text="Fijar presupuesto", bg="#404040", fg="white", bd=0, font=("Bold", 15), command=lambda: indicate(fijar_indicate, fijar_menu))
        fijar_btn.place(x=10, y=50)
        fijar_indicate = Label(option_frame, text="", bg="#404040")
        fijar_indicate.place(x=3, y=50, width=5, height=40)

        agendar_btn = Button(option_frame, text="Agendar partido", bg="#404040", fg="white", bd=0, font=("Bold", 15), command=lambda: indicate(agendar_indicate, agendar_menu))
        agendar_btn.place(x=10, y=115)
        agendar_indicate = Label(option_frame, text="", bg="#404040")
        agendar_indicate.place(x=3, y=115, width=5, height=40)

        gestionar_btn = Button(option_frame, text="Gestionar equipo", bg="#404040", fg="white", bd=0, font=("Bold", 15), command=lambda: indicate(gestionar_indicate, gestionar_menu))
        gestionar_btn.place(x=10, y=180)
        gestionar_indicate = Label(option_frame, text="", bg="#404040")
        gestionar_indicate.place(x=3, y=180, width=5, height=40)

        consultar_btn = Button(option_frame, text="Consultar partidos", bg="#404040", fg="white", bd=0, font=("Bold", 15), command=lambda: indicate(consultar_indicate, consultar_menu))
        consultar_btn.place(x=10, y=245)
        consultar_indicate = Label(option_frame, text="", bg="#404040")
        consultar_indicate.place(x=3, y=245, width=5, height=40)

        renovar_btn = Button(option_frame, text="Renovar presidente", bg="#404040", fg="white", bd=0, font=("Bold", 15), command=lambda: indicate(renovar_indicate, renovar_menu))
        renovar_btn.place(x=10, y=310)
        renovar_indicate = Label(option_frame, text="", bg="#404040")
        renovar_indicate.place(x=3, y=310, width=5, height=40)

        salir_btn = Button(option_frame, text="Salir", bg="#404040", fg="white", bd=0, font=("Bold", 15), command=lambda: indicate(salir_indicate, salir))
        salir_btn.place(x=10, y=375)
        salir_indicate = Label(option_frame, text="", bg="#404040")
        salir_indicate.place(x=3, y=375, width=5, height=40)

        option_frame.pack(side=LEFT)
        option_frame.pack_propagate(False)
        option_frame.configure(width=200, height=660)
        
        welcome_frame = Frame(ventana, bg="white")
        welcome_frame.pack(side=TOP)
        welcome_frame.pack_propagate(False)
        welcome_frame.configure(width=600, height=400)

        Label1 = Label(welcome_frame, text=f"Bienvenido presidente {nombre} {apellido}", font=("Bold", 20), fg="black", bg="white")
        Label1.pack(expand=YES, fill=BOTH)

        Label2 = Label(welcome_frame, text="\n¿Qué deseas hacer hoy?\n\nSelecciona una opción para continuar", font=("Bold", 15), fg="black", bg="white")
        Label2.pack(expand=YES, fill=BOTH)

        main_frame = Frame(ventana, bg="white")
        main_frame.pack(side=LEFT)
        main_frame.pack_propagate(False)
        main_frame.configure(width=600, height=660)

        ventana.mainloop()
    else:
        messagebox.showinfo(message="No tienes un equipo asignado.\nPor favor, añade uno para continuar.",title="ALERTA")
        ventana_login()

def ventana_menu_jugador(id,nombre,apellido,idEquipo):
    ventana = Tk()
    ventana.title("Menú Jugador")
    ventana.geometry("800x500")
    ventana.config(bg="#fcfcfc")
    ventana.resizable(width=0, height=0)
    option_frame = Frame(ventana, bg="#404040")

    def borrarPages():
        for frame in main_frame.winfo_children():
            frame.destroy()

    def hide():
        partidos_indicate.configure(bg="#404040")
        estadistica_indicate.configure(bg="#404040")
        goles_indicate.configure(bg="#404040")
        salir_indicate.configure(bg="#404040")

    def indicate(lb, page):
        hide()
        lb.configure(bg="#158aff")
        borrarPages()
        page()

    def salir():
        welcome_frame.destroy()
        resultado = messagebox.askquestion("ALERTA", "¿Deseas salir del sistema?")
        if resultado == "yes":
            ventana.destroy()
            ventana_login()

    def verPartidos():

        welcome_frame.destroy()

        def part(tipo):
            if tipo == "pendientes":
                frame_form_fill.destroy()
                cursor.execute("SELECT id,fecha,estadio,estado FROM partido WHERE (idEq1 = %s OR idEq2 = %s) and estado = 'Pendiente'", (idEquipo, idEquipo))
                resultados = cursor.fetchall()
                if resultados:
                    frame_form_ver1 = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
                    frame_form_ver1.pack(side="bottom", expand=YES, fill=BOTH)

                    pres = Label(frame_form_ver1, text="Partidos pendientes", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                    pres.pack(fill=X, padx=20, pady=5)

                    tree = ttk.Treeview(frame_form_ver1, columns=("id", "Fecha", "Estadio", "Estado"), show="headings")
                    tree.heading("id", text="id")
                    tree.heading("Fecha", text="Fecha")
                    tree.heading("Estadio", text="Estadio")
                    tree.heading("Estado", text="Estado")
                    tree.column("id",width=40)
                    tree.column("Fecha", width=170)
                    tree.column("Estadio", width=170)
                    tree.column("Estado", width=170)
                    tree.pack(fill=BOTH, expand=YES)

                    for row in resultados:
                        tree.insert("", "end", values=row)
                else:
                    messagebox.showerror(message="No hay partidos pendientes.",title="ALERTA")
            elif tipo == "completados":
                frame_form_fill.destroy()

                frame_form_ver = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
                frame_form_ver.pack(side="bottom", expand=YES, fill=BOTH)

                cursor.execute("SELECT id,fecha,estadio,estado FROM partido WHERE (idEq1 = %s OR idEq2 = %s) and estado = 'Completado'", (idEquipo, idEquipo))
                resultados = cursor.fetchall()
                if resultados:

                    pres = Label(frame_form_ver, text="Partidos completados", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                    pres.pack(fill=X, padx=20, pady=5)

                    tree = ttk.Treeview(frame_form_ver, columns=("id", "Fecha", "Estadio", "Estado"), show="headings")
                    tree.heading("id", text="id")
                    tree.heading("Fecha", text="Fecha")
                    tree.heading("Estadio", text="Estadio")
                    tree.heading("Estado", text="Estado")
                    tree.column("id",width=40)
                    tree.column("Fecha", width=170)
                    tree.column("Estadio", width=170)
                    tree.column("Estado", width=170)
                    tree.pack(fill=BOTH, expand=YES)

                    for row in resultados:
                        tree.insert("", "end", values=row)
                else:
                    messagebox.showerror(message="No hay partidos completados.",title="ALERTA")
            else:
                messagebox.showerror(message="Error al cargar partidos.",title="ALERTA")
        
        frame_form = Frame(ventana, bd=0, relief=SOLID, bg="#fcfcfc")
        frame_form.pack(side="right", expand=YES,fill=BOTH)

        frame_form_top = Frame(main_frame, height= 50, bd=0, relief=SOLID, bg="black")
        frame_form_top.pack(side="top", fill=X)
        title = Label(frame_form_top, text="Visualiza tus partidos", font=("Times", 30), fg="black", bg="white", pady=20)
        title.pack(expand=YES, fill=BOTH)

        frame_form_fill = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
        frame_form_fill.pack(side="bottom", expand=YES, fill=BOTH)
        frame_form_fill.columnconfigure(0, weight=1)
        frame_form_fill.columnconfigure(1, weight=1)
        frame_form_fill.columnconfigure(2, weight=1)

        ckbox_jugador = Radiobutton(frame_form_fill, text="Pendientes", font=("Times", 14), fg="#666a88", bg="white", anchor=W, command=lambda:part("pendientes"))
        ckbox_jugador.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        ckbox_jugador.bind("<Return>", lambda event: part("pendientes"))
        ckbox_presidente = Radiobutton(frame_form_fill, text="Completados", font=("Times", 14), fg="#666a88", bg="white", anchor=W, command=lambda:part("completados"))
        ckbox_presidente.bind("<Return>", lambda event: part("completados"))
        ckbox_presidente.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    def verEstadisticas():

        welcome_frame.destroy()

        def val(idPartdio):
            if idPartdio:
                cursor.execute("SELECT id FROM partido WHERE id = %s AND (idEq1 OR idEq2 = %s) ", (idPartdio,idEquipo))
                result = cursor.fetchone()
                if result:
                    frame_form_estadistica.destroy()
                    frame_form_top.destroy()

                    frame_form_top_est = Frame(main_frame, height= 50, bd=0, relief=SOLID, bg="black")
                    frame_form_top_est.pack(side="top", fill=X)
                    title = Label(frame_form_top_est, text="Estadísticas del partido", font=("Times", 30), fg="black", bg="white", pady=20)
                    title.pack(expand=YES, fill=BOTH)

                    frame_form_estPar = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white", pady=0)
                    frame_form_estPar.pack(fill=BOTH, expand=True)

                    cursor.execute("SELECT id_partido, minuto FROM goles WHERE id_jugador = %s and id_partido = %s", (id,idPartdio))
                    goles = cursor.fetchall()
                    if goles:
                        tree = ttk.Treeview(frame_form_estPar, columns=("id_partido", "minuto"), show="headings")
                        tree.heading("id_partido", text="Partido Id")
                        tree.heading("minuto", text="Minuto")
                        tree.column("id_partido",width=150)
                        tree.column("minuto", width=150)
                        tree.pack(fill=BOTH, expand=YES)
                        tree.pack(fill=BOTH, expand=YES)

                        for row in goles:
                            tree.insert("", "end", values=row)
                    else:
                        messagebox.showerror(message="No hay estadísticas disponibles para este partido.",title="ALERTA")
                else:
                    messagebox.showerror(message="Por favor, ingrese un partido válido.",title="ALERTA")
            else:
                messagebox.showerror(message="Por favor, rellene el campo.",title="ALERTA")

        frame_form = Frame(ventana, bd=0, relief=SOLID, bg="#fcfcfc")
        frame_form.pack(side="right", expand=YES,fill=BOTH)

        frame_form_top = Frame(main_frame, height= 50, bd=0, relief=SOLID, bg="black")
        frame_form_top.pack(side="top", fill=X)
        title = Label(frame_form_top, text="Selecciona el partido para ver tus estádisticas", font=("Times", 20), fg="black", bg="white", pady=20)
        title.pack(expand=YES, fill=BOTH)

        frame_form_estadistica = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white", pady=0)
        frame_form_estadistica.pack(fill=BOTH, expand=True)

        frame_form_estadistica.columnconfigure(0, weight=1)
        frame_form_estadistica.columnconfigure(1, weight=1)

        verest = Label(frame_form_estadistica, text="Introduce ID del partido:", font=("Times", 20), fg="#666a88",bg="white", anchor=W)
        verest.pack(fill=X, padx=20, pady=5)
        ver_entry = Entry(frame_form_estadistica, font=("Times", 15))
        ver_entry.pack(fill=X, padx=20, pady=10)

        btn = Button(frame_form_estadistica, text="Continuar", bg="#3a7ff6", fg="white", bd=0, font=("Bold", 15), command=lambda: val(ver_entry.get()))
        btn.pack(fill=X, padx=20, pady=20)

        cursor.execute("SELECT id,fecha,estadio,estado FROM partido WHERE (idEq1 = %s OR idEq2 = %s) and estado = 'Completado'", (idEquipo, idEquipo))
        resultados = cursor.fetchall()
        if resultados:
            tree = ttk.Treeview(frame_form_estadistica, columns=("id", "Fecha", "Estadio", "Estado"), show="headings")
            tree.heading("id", text="id")
            tree.heading("Fecha", text="Fecha")
            tree.heading("Estadio", text="Estadio")
            tree.heading("Estado", text="Estado")
            tree.column("id",width=40)
            tree.column("Fecha", width=170)
            tree.column("Estadio", width=170)
            tree.column("Estado", width=170)
            tree.pack(fill=BOTH, expand=YES)
            tree.pack(fill=BOTH, expand=YES)

            for row in resultados:
                tree.insert("", "end", values=row)
        else:
            messagebox.showerror(message="No hay partidos completados.",title="ALERTA")
    
    def verGoles():
        
        welcome_frame.destroy()

        frame_form = Frame(ventana, bd=0, relief=SOLID, bg="#fcfcfc")
        frame_form.pack(side="right", expand=YES,fill=BOTH)

        frame_form_top = Frame(main_frame, height= 50, bd=0, relief=SOLID, bg="black")
        frame_form_top.pack(side="top", fill=X)
        title = Label(frame_form_top, text="Visualiza tu historial de goles", font=("Times", 20), fg="black", bg="white", pady=20)
        title.pack(expand=YES, fill=BOTH)

        frame_form_gol = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white", pady=0)
        frame_form_gol.pack(fill=BOTH, expand=True)

        cursor.execute("SELECT id_partido, minuto FROM goles WHERE id_jugador = %s", (id,))
        goles = cursor.fetchall()

        if goles:
            tree = ttk.Treeview(frame_form_gol, columns=("id_partido", "minuto"), show="headings")
            tree.heading("id_partido", text="Partido Id")
            tree.heading("minuto", text="Minuto")
            tree.column("id_partido",width=150)
            tree.column("minuto", width=150)
            tree.pack(fill=BOTH, expand=YES)
            tree.pack(fill=BOTH, expand=YES)

            for row in goles:
                tree.insert("", "end", values=row)
        else:
            messagebox.showerror(message="No hay goles registrados.",title="ALERTA")

    partidos_btn = Button(option_frame, text="Ver partidos", bg="#404040", fg="white", bd=0, font=("Bold", 15), command=lambda: indicate(partidos_indicate, verPartidos))
    partidos_btn.place(x=10, y=50)
    partidos_indicate = Label(option_frame, text="", bg="#404040")
    partidos_indicate.place(x=3, y=50, width=5, height=40)

    estadistica_btn = Button(option_frame, text="Ver estadísticas", bg="#404040", fg="white", bd=0, font=("Bold", 15), command=lambda: indicate(estadistica_indicate, verEstadisticas))
    estadistica_btn.place(x=10, y=100)
    estadistica_indicate= Label(option_frame, text="", bg="#404040")
    estadistica_indicate.place(x=3, y=100, width=5, height=40)

    goles_btn = Button(option_frame, text="Ver goles", bg="#404040", fg="white", bd=0, font=("Bold", 15), command=lambda: indicate(goles_indicate, verGoles))
    goles_btn.place(x=10, y=150)
    goles_indicate = Label(option_frame, text="", bg="#404040")
    goles_indicate.place(x=3, y=150, width=5, height=40)

    salir_btn = Button(option_frame, text="Salir", bg="#404040", fg="white", bd=0, font=("Bold", 15), command=lambda: indicate(salir_indicate, salir))
    salir_btn.place(x=10, y=300)
    salir_indicate = Label(option_frame, text="", bg="#404040")
    salir_indicate.place(x=3, y=300, width=5, height=40)

    option_frame.pack(side=LEFT)
    option_frame.pack_propagate(False)
    option_frame.configure(width=200, height=660)

    welcome_frame = Frame(ventana, bg="white")
    welcome_frame.pack(side=TOP)
    welcome_frame.pack_propagate(False)
    welcome_frame.configure(width=600, height=400)

    Label1 = Label(welcome_frame, text=f"Bienvenido {nombre} {apellido}", font=("Bold", 20), fg="black", bg="white")
    Label1.pack(expand=YES, fill=BOTH)

    Label2 = Label(welcome_frame, text="\n¿Qué deseas hacer hoy?\n\nSelecciona una opción para continuar", font=("Bold", 15), fg="black", bg="white")
    Label2.pack(expand=YES, fill=BOTH)

    main_frame = Frame(ventana, bg="white")
    main_frame.pack(side=LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(width=600, height=660)

    ventana.mainloop()

def ventana_login():
    from usuarios.users import Jugador, Presidente
    ventana = Tk()
    ventana.title("Inicio de sesión")
    ventana.geometry("850x550")
    ventana.config(bg="#fcfcfc")
    ventana.resizable(width=0, height=0)

    def borrarPages():
        for frame in main_frame.winfo_children():
            frame.destroy()

    def hide():
        login_indicate.configure(bg="#404040")
        registrar_indicate.configure(bg="#404040")
        anequip_indicate.configure(bg="#404040")
        salir_indicate.configure(bg="#404040")

    def indicate(lb, page):
        hide()
        lb.configure(bg="#158aff")
        borrarPages()
        page()

    def login():
    
        def verificarlogin():
            user = usuario.get()
            pasw = contraseña.get()
            resultado = Jugador.iniciar_sesion(user, pasw)
            resultado1 = Presidente.iniciar_sesion(user, pasw )
            if resultado:
                ventana.destroy()
                ventana_menu_jugador(resultado[0],resultado[3],resultado[4],resultado[12])
            elif resultado1:
                ventana.destroy()
                ventana_menu_presi(resultado1[0],resultado1[3],resultado1[4],resultado1[10])
            else:
                messagebox.showerror(message="La contraseña o usuario is incorrecto.",title="ALERTA")

        frame_form = Frame(ventana, bd=0, relief=SOLID, bg="#fcfcfc")
        frame_form.pack(side="right", expand=YES,fill=BOTH)

        frame_form_top = Frame(main_frame, height= 50, bd=0, relief=SOLID, bg="black")
        frame_form_top.pack(side="top", fill=X)
        title = Label(frame_form_top, text="Inicio de sesión", font=("Times", 30), fg="black", bg="#fcfcfc", pady=50)
        title.pack(expand=YES, fill=BOTH)

        frame_form_fill = Frame(main_frame, height=50, bd=0, relief=SOLID, bg="#fcfcfc")
        frame_form_fill.pack(side="bottom", expand=YES, fill=BOTH)
        
        etiqueta_usuario = Label(frame_form_fill, text="Usuario", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
        etiqueta_usuario.pack(fill=X, padx=20, pady=5)
        usuario = Entry(frame_form_fill, font=("Times", 20))
        usuario.pack(fill=X, padx=20, pady=10)

        etiqueta_contraseña = Label(frame_form_fill, text="Contraseña", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
        etiqueta_contraseña.pack(fill=X, padx=20, pady=5)
        contraseña = Entry(frame_form_fill, font=("Times", 20), show="*")
        contraseña.pack(fill=X, padx=20, pady=10)

        logbtn = Button(frame_form_fill, text="Iniciar Sesión", font=('Times', 15), bg="#3a7ff6", bd=0, fg="#fff", command= verificarlogin)
        logbtn.pack(fill=X, padx=20, pady=20)
        logbtn.bind("<Return>", lambda event: verificarlogin())

    def registrar():

        def presidente():
                
                def val():
                    if user_entry.get() and passw_entry.get() and name_entry.get() and apell_entry.get() and date_entry.get() and salario_entry.get() and antiguedad_entry.get():
                        resultado = messagebox.askquestion("ALERTA", "¿Deseas añadir este usuario?")
                        if resultado == "yes":
                            new_pres = Presidente(user_entry.get(), passw_entry.get(), name_entry.get(), apell_entry.get(), date_entry.get(), salario_entry.get(), "Presidente", antiguedad_entry.get())
                            Presidente.registrarPresidente(new_pres)
                            if new_pres:
                                messagebox.showinfo(message="Usuario registrado con éxito.",title="ALERTA")
                            else:
                                messagebox.showerror(message="Error al registrar usuario.",title="ALERTA")
                    else:
                        messagebox.showerror(message="Por favor, rellene todos los campos.",title="ALERTA")

                frame_form_fill.destroy()

                frame_form_presidente = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white", pady=0)
                frame_form_presidente.pack(side="right", expand=YES, fill=BOTH)

                frame_form_presidente.columnconfigure(0, weight=1)
                frame_form_presidente.columnconfigure(1, weight=1)

                user_name = Label(frame_form_presidente, text="Nombre de usuario", font=("Times",15), fg="black", bg="white", pady=8)
                user_name.grid(row=0, column=0, padx=15, pady=5, sticky="w")
                user_entry = Entry(frame_form_presidente, text="Nombre de usuario",font=("Times", 15),width=30)
                user_entry.grid(row=1, column=0, padx=15, pady=5, sticky="w")

                passw_name = Label(frame_form_presidente,text="Contraseña", font=("Times",15), fg="black", bg="white", pady=8)
                passw_name.grid(row=2, column=0, padx=15, pady=5, sticky="w")
                passw_entry =  Entry(frame_form_presidente, text="Contraseña", font=("Times", 15),width=30)
                passw_entry.grid(row=3, column=0, padx=15, pady=5, sticky="w")

                name = Label(frame_form_presidente, text="Nombre", font=("Times",15), fg="black", bg="white", pady=8)
                name.grid(row=4, column=0, padx=15, pady=5, sticky="w")
                name_entry = Entry(frame_form_presidente, font=("Times",15),width=30)
                name_entry.grid(row=5, column=0, padx=15, pady=5, sticky="w")

                apell = Label(frame_form_presidente, text="Apellido", font=("Times",15), fg="black", bg="white", pady=8)
                apell.grid(row=0, column=1, padx=15, pady=5, sticky="w")
                apell_entry = Entry(frame_form_presidente, font=("Times",15),width=30)
                apell_entry.grid(row=1, column=1, padx=15, pady=5, sticky="w")

                date = Label(frame_form_presidente, text="Fecha nacimiento(AAAA-MM-DD)", font=("Times",15), fg="black", bg="white", pady=8)
                date.grid(row=2, column=1, padx=15, pady=5, sticky="w")
                date_entry = Entry(frame_form_presidente, font=("Times",15),width=30)
                date_entry.grid(row=3, column=1, padx=15, pady=5, sticky="w")

                salario = Label(frame_form_presidente, text="Salario", font=("Times",15), fg="black", bg="white", pady=8)
                salario.grid(row=4, column=1, padx=15, pady=5, sticky="w")
                salario_entry = Entry(frame_form_presidente, font=("Times",15),width=30)
                salario_entry.grid(row=5, column=1, padx=15, pady=5, sticky="w")

                antiguedad = Label(frame_form_presidente, text="Antiguedad", font=("Times",15), fg="black", bg="white", pady=8)
                antiguedad.grid(row=6, column=1, padx=15, pady=5, sticky="w")
                antiguedad_entry = Entry(frame_form_presidente, font=("Times",15),width=30)
                antiguedad_entry.grid(row=7, column=1, padx=15, pady=5, sticky="w")

                btn = Button(frame_form_presidente, text="Registrarse", bg="#34495e", fg="white", bd=0, font=("Bold", 15), command=lambda: val())
                btn.place(x=15, y=400)

        def jugador():

            frame_form_fill.destroy()

            def val():
                if user_entry.get() and passw_entry.get() and name_entry.get() and apell_entry.get() and date_entry.get() and salario_entry.get() and camiseta_entry.get() and nacionalidad_entry.get():
                    resultado = messagebox.askquestion("ALERTA", "¿Deseas añadir este usuario?")
                    if resultado == "yes":
                        new_plr = Jugador(user_entry.get(), passw_entry.get(), name_entry.get(), apell_entry.get(), date_entry.get(), salario_entry.get(), "Jugador", camiseta_entry.get(), nacionalidad_entry.get())
                        Jugador.registrarJugador(new_plr)
                        if new_plr:
                            messagebox.showinfo(message="Usuario registrado con éxito.",title="ALERTA")
                        else:
                            messagebox.showerror(message="Error al registrar usuario.",title="ALERTA")
                else:
                    messagebox.showerror(message="Por favor, rellene todos los campos.",title="ALERTA")

            frame_form_jugador = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white", pady=0)
            frame_form_jugador.pack(fill=BOTH, expand=True)

            frame_form_jugador.columnconfigure(0, weight=1)
            frame_form_jugador.columnconfigure(1, weight=1)

            user_name = Label(frame_form_jugador, text="Nombre de usuario", font=("Times",15), fg="black", bg="white", pady=8)
            user_name.grid(row=0, column=0, padx=15, pady=5, sticky="w")
            user_entry = Entry(frame_form_jugador, text="Nombre de usuario",font=("Times", 15),width=30)
            user_entry.grid(row=1, column=0, padx=15, pady=5, sticky="w")

            passw_name = Label(frame_form_jugador,text="Contraseña", font=("Times",15), fg="black", bg="white", pady=8)
            passw_name.grid(row=2, column=0, padx=15, pady=5, sticky="w")
            passw_entry =  Entry(frame_form_jugador, text="Contraseña", font=("Times", 15),width=30)
            passw_entry.grid(row=3, column=0, padx=15, pady=5, sticky="w")

            name = Label(frame_form_jugador, text="Nombre", font=("Times",15), fg="black", bg="white", pady=8)
            name.grid(row=4, column=0, padx=15, pady=5, sticky="w")
            name_entry = Entry(frame_form_jugador, font=("Times",15),width=30)
            name_entry.grid(row=5, column=0, padx=15, pady=5, sticky="w")

            apell = Label(frame_form_jugador, text="Apellido", font=("Times",15), fg="black", bg="white", pady=8)
            apell.grid(row=0, column=1, padx=15, pady=5, sticky="w")
            apell_entry = Entry(frame_form_jugador, font=("Times",15),width=30)
            apell_entry.grid(row=1, column=1, padx=15, pady=5, sticky="w")

            date = Label(frame_form_jugador, text="Fecha nacimiento(AAAA-MM-DD)", font=("Times",15), fg="black", bg="white", pady=8)
            date.grid(row=2, column=1, padx=15, pady=5, sticky="w")
            date_entry = Entry(frame_form_jugador, font=("Times",15),width=30)
            date_entry.grid(row=3, column=1, padx=15, pady=5, sticky="w")

            salario = Label(frame_form_jugador, text="Salario", font=("Times",15), fg="black", bg="white", pady=8)
            salario.grid(row=4, column=1, padx=15, pady=5, sticky="w")
            salario_entry = Entry(frame_form_jugador, font=("Times",15),width=30)
            salario_entry.grid(row=5, column=1, padx=15, pady=5, sticky="w")

            camiseta = Label(frame_form_jugador, text="Camiseta", font=("Times",15), fg="black", bg="white", pady=8)
            camiseta.grid(row=6, column=1, padx=15, pady=5, sticky="w")
            camiseta_entry = Entry(frame_form_jugador, font=("Times",15),width=30)
            camiseta_entry.grid(row=7, column=1, padx=15, pady=5, sticky="w")

            nacionalidad= Label(frame_form_jugador, text="Nacionalidad", font=("Times", 15), fg="black", bg="white", pady=8)
            nacionalidad.grid(row=6, column=0, padx=15, pady=5, sticky="w")
            nacionalidad_entry = Entry(frame_form_jugador, font=("Times", 15),width=30)
            nacionalidad_entry.grid(row=7, column=0, padx=15, pady=5, sticky="w")

            btn = Button(frame_form_jugador, text="Registrarse", bg="#34495e", fg="white", bd=0, font=("Bold", 15), command=lambda: val())
            btn.place(x=15, y=400)

        def equipo():
            frame_form_fill.destroy()

            def val(idPres):
                if idPres:
                    cursor.execute("SELECT id FROM usuarios WHERE id = %s and tipo='Presidente' AND equipo IS NULL", (idPres,))
                    result = cursor.fetchone()
                    if result:
                        frame_form_equipo.destroy()

                        def reg(equipoId,idPres):
                            if equipoId:
                                cursor.execute("UPDATE equipo SET presidente = %s WHERE id = %s", (idPres, equipoId))
                                conexion.commit()
                                cursor.execute("UPDATE usuarios SET equipo = %s WHERE id = %s", (equipoId, idPres))
                                conexion.commit()
                                messagebox.showinfo(message="Presidente registrado con éxito.",title="ALERTA")
                            else:
                                messagebox.showerror(message="Por favor, seleccione un equipo.",title="ALERTA")

                        frame_form_team = Frame(ventana, bd=0, relief=SOLID, bg="#fcfcfc")
                        frame_form_team.pack(side="right", expand=YES,fill=BOTH)

                        cursor.execute("SELECT id, nombre, pais, estadio FROM equipo WHERE presidente = 0")
                        resultados = cursor.fetchall()

                        if resultados:
                            pres = Label(frame_form_fill, text="Equipos disponibles", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
                            pres.pack(fill=X, padx=20, pady=5)
                            presi = Label(frame_form_fill, text="Seleccione el ID del equipo", font=("Times", 15), fg="#666a88",bg="#fcfcfc", anchor=W)
                            presi.pack(fill=X, padx=20, pady=5)
                            equipo_entry = Entry(frame_form_fill, font=("Times", 15))
                            equipo_entry.pack(fill=X, padx=20, pady=10)
                            btncont = Button(frame_form_fill, text="Continuar", font=('Times', 15), bg="#3a7ff6", bd=0, fg="#fff", command=lambda: reg(equipo_entry.get(),idPres))
                            btncont.pack(fill=X, padx=20, pady=20)
                            tree = ttk.Treeview(frame_form_fill, columns=("id", "nombre", "apellido", "nacionalidad"), show="headings")
                            tree.heading("id", text="id")
                            tree.heading("nombre", text="Nombre")
                            tree.heading("apellido", text="pais")
                            tree.heading("nacionalidad", text="estadio")
                            tree.column("id",width=40)
                            tree.column("nombre", width=170)
                            tree.column("apellido", width=170)
                            tree.column("nacionalidad", width=170)
                            tree.pack(fill=BOTH, expand=YES)

                            for row in resultados:
                                tree.insert("", "end", values=row)
                        else:
                            messagebox.showerror(message="No hay equipos disponibles.",title="ALERTA")
                    else:
                        messagebox.showerror(message="Por favor, ingrese un presidente válido.",title="ALERTA")
                else:
                            messagebox.showerror(message="Por favor, rellene el campo.",title="ALERTA")

            frame_form_equipo = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white", pady=0)
            frame_form_equipo.pack(fill=BOTH, expand=True)

            frame_form_equipo.columnconfigure(0, weight=1)
            frame_form_equipo.columnconfigure(1, weight=1)

            verPres = Label(frame_form_equipo, text="Verifica tu Id de presidente:", font=("Times", 20), fg="#666a88",bg="white", anchor=W)
            verPres.pack(fill=X, padx=20, pady=5)
            verPres_entry = Entry(frame_form_equipo, font=("Times", 15))
            verPres_entry.pack(fill=X, padx=20, pady=10)

            btn = Button(frame_form_equipo, text="Continuar", bg="#3a7ff6", fg="white", bd=0, font=("Bold", 15), command=lambda: val(verPres_entry.get()))
            btn.pack(fill=X, padx=20, pady=20)

        frame_form = Frame(ventana, bd=0, relief=SOLID, bg="#fcfcfc")
        frame_form.pack(side="right", expand=YES,fill=BOTH)

        frame_form_top = Frame(main_frame, height= 50, bd=0, relief=SOLID, bg="black")
        frame_form_top.pack(side="top", fill=X)
        title = Label(frame_form_top, text="Registro de usuario", font=("Times", 30), fg="black", bg="white", pady=20)
        title.pack(expand=YES, fill=BOTH)

        frame_form_fill = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white")
        frame_form_fill.pack(side="bottom", expand=YES, fill=BOTH)
        frame_form_fill.columnconfigure(0, weight=1)
        frame_form_fill.columnconfigure(1, weight=1)
        frame_form_fill.columnconfigure(2, weight=1)

        ckbox_jugador = Radiobutton(frame_form_fill, text="Registro como jugador", font=("Times", 14), fg="#666a88", bg="white", anchor=W, command=lambda:jugador())
        ckbox_jugador.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        ckbox_jugador.bind("<Return>", lambda event: jugador())
        ckbox_presidente = Radiobutton(frame_form_fill, text="Registro como presidente", font=("Times", 14), fg="#666a88", bg="white", anchor=W, command=lambda:presidente())
        ckbox_presidente.bind("<Return>", lambda event: presidente())
        ckbox_presidente.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        ckbox_equipo = Radiobutton(frame_form_fill, text="Registrarse a equipo", font=("Times", 14), fg="#666a88", bg="white", anchor=W, command=lambda:equipo())
        ckbox_equipo.bind("<Return>", lambda event: equipo())
        ckbox_equipo.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    def añadirEquipo():
        from equipos.equip import Equipo

        frame_form = Frame(ventana, bd=0, relief=SOLID, bg="#fcfcfc")
        frame_form.pack(side="right", expand=YES,fill=BOTH)

        frame_form_top = Frame(main_frame, height= 50, bd=0, relief=SOLID, bg="black")
        frame_form_top.pack(side="top", fill=X)
        title = Label(frame_form_top, text="Añadir equipo", font=("Times", 30), fg="black", bg="white", pady=20)
        title.pack(expand=YES, fill=BOTH)

        frame_form_fill = Frame(main_frame, height=50, bd=0, relief=SOLID, bg="#fcfcfc")
        frame_form_fill.pack(side="bottom", expand=YES, fill=BOTH)

        cursor.execute("SELECT id, nombre, apellido, antiguedad FROM usuarios WHERE tipo = 'Presidente' and equipo IS NULL")
        resultados = cursor.fetchall()

        if resultados:

            def inscripcion(idPres):
                if idPres:
                    cursor.execute("SELECT id FROM usuarios WHERE id = %s and tipo='Presidente' AND equipo IS NULL", (idPres,))
                    result = cursor.fetchone()
                    if result:
                        idSelec = idPres
                        frame_form_fill.destroy()

                        def confirmar(nombre,pais,estadio,presi,presu):
                            if nombre and pais and estadio:
                                resultado = messagebox.askquestion("ALERTA", "¿Deseas añadir este equipo?")
                                if resultado == "yes":
                                    new_team = Equipo(nombre, pais, estadio, presi,presu)
                                    Equipo.registrar_equipo(new_team)
                                    if new_team:
                                        messagebox.showinfo(message="Equipo registrado con éxito.",title="ALERTA")
                                    else:
                                        messagebox.showerror(message="Error al registrar equipo.",title="ALERTA")
                            else:
                                messagebox.showerror(message="Por favor, rellene todos los campos.",title="ALERTA")

                        frame_form_equipo = Frame(main_frame, height=10, bd=0, relief=SOLID, bg="white", pady=0)
                        frame_form_equipo.pack(side="right", expand=YES, fill=BOTH)

                        frame_form_equipo.columnconfigure(0, weight=1)
                        frame_form_equipo.columnconfigure(1, weight=1)

                        team_name = Label(frame_form_equipo, text="Nombre", font=("Times",15), fg="black", bg="white", pady=8)
                        team_name.grid(row=0, column=0, padx=15, pady=5, sticky="w")
                        team_entry = Entry(frame_form_equipo, text="Nombre",font=("Times", 15),width=30)
                        team_entry.grid(row=1, column=0, padx=15, pady=5, sticky="w")

                        pais = Label(frame_form_equipo,text="País", font=("Times",15), fg="black", bg="white", pady=8)
                        pais.grid(row=2, column=0, padx=15, pady=5, sticky="w")
                        pais_entry =  Entry(frame_form_equipo, text="Pais", font=("Times", 15),width=30)
                        pais_entry.grid(row=3, column=0, padx=15, pady=5, sticky="w")

                        estadio = Label(frame_form_equipo, text="Estadio", font=("Times",15), fg="black", bg="white", pady=8)
                        estadio.grid(row=4, column=0, padx=15, pady=5, sticky="w")
                        estadio_entry = Entry(frame_form_equipo, font=("Times",15),width=30)
                        estadio_entry.grid(row=5, column=0, padx=15, pady=5, sticky="w")

                        presupuesto = Label(frame_form_equipo, text="Presupuesto", font=("Times",15), fg="black", bg="white", pady=8)
                        presupuesto.grid(row=4, column=0, padx=15, pady=5, sticky="w")
                        pres_entry = Entry(frame_form_equipo, font=("Times",15),width=30)
                        pres_entry.grid(row=5, column=0, padx=15, pady=5, sticky="w")

                        confbtn = Button(frame_form_equipo, text="Confirmar", bg="#34495e", fg="white", bd=0, font=("Bold", 15), command=lambda: confirmar(team_entry.get(), pais_entry.get(), estadio_entry.get(), idSelec ,pres_entry.get()))
                        confbtn.place(x=15, y=400)
                    else:
                        messagebox.showerror(message="Por favor, seleccione un presidente válido.",title="ALERTA")
                else:
                    messagebox.showerror(message="Por favor, seleccione un presidente.",title="ALERTA")

            pres = Label(frame_form_fill, text="Presidentes disponibles", font=("Times", 20), fg="#666a88",bg="#fcfcfc", anchor=W)
            pres.pack(fill=X, padx=20, pady=5)
            presi = Label(frame_form_fill, text="Seleccione el ID del preisdente", font=("Times", 15), fg="#666a88",bg="#fcfcfc", anchor=W)
            presi.pack(fill=X, padx=20, pady=5)
            presi_entry = Entry(frame_form_fill, font=("Times", 15))
            presi_entry.pack(fill=X, padx=20, pady=10)
            btncont = Button(frame_form_fill, text="Continuar", font=('Times', 15), bg="#3a7ff6", bd=0, fg="#fff", command=lambda: inscripcion(presi_entry.get()))
            btncont.pack(fill=X, padx=20, pady=20)
            tree = ttk.Treeview(frame_form_fill, columns=("id", "nombre", "apellido", "nacionalidad"), show="headings")
            tree.heading("id", text="id")
            tree.heading("nombre", text="Nombre")
            tree.heading("apellido", text="Apellido")
            tree.heading("nacionalidad", text="Antiguedad")
            tree.column("id",width=40)
            tree.column("nombre", width=170)
            tree.column("apellido", width=170)
            tree.column("nacionalidad", width=170)
            tree.pack(fill=BOTH, expand=YES)

            for row in resultados:
                tree.insert("", "end", values=row)
        else:
            messagebox.showinfo(message="No hay presidentes disponibles.\nInserte uno para continuar",title="ALERTA")

    def salir():
        resultado = messagebox.askquestion("ALERTA", "¿Deseas salir del sistema?")
        if resultado == "yes":
            ventana.destroy()

    option_frame = Frame(ventana, bg="#404040")

    login_btn = Button(option_frame, text="Login", bg="#404040", fg="white", bd=0, font=("Bold", 15), command=lambda: indicate(login_indicate, login))
    login_btn.place(x=10, y=50)
    login_indicate = Label(option_frame, text="", bg="#404040")
    login_indicate.place(x=3, y=50, width=5, height=40)

    registrar_btn = Button(option_frame, text="Registrarse", bg="#404040", fg="white", bd=0, font=("Bold", 15), command=lambda: indicate(registrar_indicate, registrar))
    registrar_btn.place(x=10, y=100)
    registrar_indicate= Label(option_frame, text="", bg="#404040")
    registrar_indicate.place(x=3, y=100, width=5, height=40)

    anequip_btn = Button(option_frame, text="Añadir equipo", bg="#404040", fg="white", bd=0, font=("Bold", 15), command=lambda: indicate(anequip_indicate, añadirEquipo))
    anequip_btn.place(x=10, y=150)
    anequip_indicate = Label(option_frame, text="", bg="#404040")
    anequip_indicate.place(x=3, y=150, width=5, height=40)

    salir_btn = Button(option_frame, text="Salir", bg="#404040", fg="white", bd=0, font=("Bold", 15), command=lambda: indicate(salir_indicate, salir))
    salir_btn.place(x=10, y=300)
    salir_indicate = Label(option_frame, text="", bg="#404040")
    salir_indicate.place(x=3, y=300, width=5, height=40)

    option_frame.pack(side=LEFT)
    option_frame.pack_propagate(False)
    option_frame.configure(width=200, height=660)

    main_frame = Frame(ventana, bg="white")
    main_frame.pack(fill=BOTH, expand=True)
    main_frame.pack_propagate(False)
    main_frame.configure(width=600, height=660)

    ventana.mainloop()

ventana_login()


def inscripcion(idPresidente):
    try:
        cursor.execute("SELECT * FROM equipo WHERE presidente = 0")
        resultado = cursor.fetchall()
        if resultado:
            print("\nLista de equipos disponibles:")
            for equipo in resultado:
                print(f"\nID: {equipo[0]}")
                print(f"Nombre: {equipo[1]}")
                print(f"País: {equipo[2]}")
                print(f"Estadio: {equipo[3]}")
                print("\n-----------------------------------------")
            eleccion = input("Ingrese el ID del equipo al que desea inscribirse: ")

            cursor.execute("UPDATE equipo SET presidente = %s WHERE id = %s", (idPresidente, eleccion))
            conexion.commit()
            cursor.execute("UPDATE usuarios SET equipo = %s WHERE id = %s", (eleccion, idPresidente))
            conexion.commit()
            print("\n¡Inscripción realizada con éxito!")
        else:
            print("\nNo hay equipos disponibles.")
    except Exception as e:
        print(f"Error al mostrar equipos: {e}")

def mostrarJugadores():
    try:
        cursor.execute("SELECT * FROM usuarios WHERE tipo = 'Jugador' and equipo_jug = 0")
        resultado = cursor.fetchall()
        if resultado:
            print("\nLista de jugadores disponibles:")
            for jugador in resultado:
                print(f"\nID: {jugador[0]}")
                print(f"Nombre: {jugador[3]} {jugador[4]}")
                print(f"Salario: {jugador[6]}")
                print(f"Número de camiseta: {jugador[8]}")
                print("\n-----------------------------------------")
        else:
            print("No hay jugadores disponibles.")
    except Exception as e:
        print(f"Error al mostrar jugadores: {e}")

def borrarPantalla():
    os.system("cls")

def esperaTecla():
    input("\nPresiona una tecla para continuar...")

def menu():
    if conexion:
        while True:
            borrarPantalla()
            print("Bienvenido a la liga de futbol, ¿Que deseas hacer hoy?")
            print("\n1. Iniciar sesión")
            print("2. Registrarse")
            print("3. Añadir equipo")
            print("4. Salir")
            opcion = input("Opción: ")

            if opcion == "1":
                borrarPantalla()
                nombre_usuario = input("Nombre de usuario: ")
                contraseña = input("Contraseña: ")
                resultado = Jugador.iniciar_sesion(nombre_usuario, contraseña)
                resultado1 = Presidente.iniciar_sesion(nombre_usuario, contraseña)
                if resultado:
                    menuJugador(resultado[0],resultado[3],resultado[4],resultado[12])
                elif resultado1:
                    menuPresidente(resultado1[0],resultado1[3],resultado1[4],resultado1[10])
                else:
                    print("\nUsuario o contraseña incorrectos")
                    esperaTecla()
            elif opcion == "2":
                borrarPantalla()
                print("...:: Registro de usuario ::...")
                tipo = input("\n¿Qué clase de usuario eres?\n1. Jugador\n2. Presidente\n\nOpción: ")
                if tipo == "1":
                    borrarPantalla()
                    nombre_usuario = input("Nombre de usuario: ")
                    contraseña = input("Contraseña: ")
                    nombre = input("Nombre: ")
                    apellidos = input("Apellidos: ")
                    fecha_nac = input("Fecha de nacimiento(AAAA-MM-DD): ")
                    salario = input("Salario: ")
                    numero_camiseta = input("Número de camiseta: ")
                    nacionalidad = input("Nacionalidad: ")

                    new_plr = Jugador(nombre_usuario, contraseña, nombre, apellidos, fecha_nac, salario, "Jugador", numero_camiseta, nacionalidad)
                    Jugador.registrarJugador(new_plr)
                    esperaTecla()

                elif tipo == "2":
                    borrarPantalla()
                    nombre_usuario = input("Nombre de usuario: ")
                    contraseña = input("Contraseña: ")
                    nombre = input("Nombre: ")
                    apellidos = input("Apellidos: ")
                    fecha_nac = input("Fecha de nacimiento: ")
                    salario = input("Salario: ")
                    antiguedad = input("Años en el cargo: ")

                    new_pres = Presidente(nombre_usuario, contraseña, nombre, apellidos, fecha_nac, salario, "Presidente", antiguedad)
                    Presidente.registrarPresidente(new_pres)
                    esperaTecla()

            elif opcion == "3":
                borrarPantalla()
                
                try:
                    print("...:: Añadir equipo ::...")
                    nom = input("\nNombre del equipo: ")
                    pais = input("\nPaís: ")
                    estadio = input("\nEstadio: ")
                    cursor.execute("SELECT * FROM usuarios WHERE tipo = 'Presidente' and equipo IS NULL")
                    resultado = cursor.fetchall()

                    if resultado:
                        print("\nLista de presidentes disponibles:")
                        for presidente in resultado:
                            print(f"\nID: {presidente[0]}")
                            print(f"Nombre: {presidente[3]} {presidente[4]}")
                            print(f"Años en el cargo: {presidente[11]}")
                            print("\n-----------------------------------------")
                        
                        presidente = input("Ingrese el ID del presidente: ")
                        new_team = Equipo(nom, pais, estadio, presidente)
                        Equipo.registrar_equipo(new_team)
                    else:
                        print("No hay presidentes disponibles. Por favor, registre uno.")
                except Exception as e:
                    print(f"Error al mostrar presidente: {e}")                
                esperaTecla()

            elif opcion == "4":
                print("Gracias por usar el sistema :D. Nos vemos!")
                break
            else:
                print("opcion no válida")
                esperaTecla()

def menuPresidente(id,nombre,apellido,idEquipo):
    if idEquipo == None:
        print("\nNo perteneces a ningún equipo, por favor integrate a uno")
        inscripcion(id)
        esperaTecla()
    else:
        while True:
            borrarPantalla()
            print(f"\t ¡Bienvenido {nombre} {apellido}!")
            print(f"\nEquipo: {idEquipo}")
            opcion = input("\n¿Qué deseas hacer hoy?\n1. Fijar presupuesto\n2. Agendar partido\n3. Gestionar equipo\n4. Consultar partidos\n5. Renovar Presidente\n6. Salir\n\nOpción: ")

            if opcion == "1":
                borrarPantalla()
                print("...:: Fijar presupuesto ::...")
                presupuesto = input("Ingrese el presupuesto: ")
                Presidente.fijar_presupuesto(id,presupuesto)
                esperaTecla()
            elif opcion == "2":
                borrarPantalla()
                print("...:: Agendar partido ::...")
                try:
                    cursor.execute("SELECT * FROM equipo WHERE id != %s", (idEquipo,))
                    resultado = cursor.fetchall()
                    if resultado:
                        print("\nLista de equipos disponibles:")
                        for equipo in resultado:
                            print(f"\nID: {equipo[0]}")
                            print(f"Nombre: {equipo[1]}")
                            print(f"País: {equipo[2]}")
                            print(f"Estadio: {equipo[3]}")
                            print("\n-----------------------------------------")
                        idE2 = input("Ingrese el ID del equipo rival: ")
                        fecha = input("Ingrese la fecha del partido (AAAA-MM-DD ): ")
                        estadio = input("Ingrese el estadio: ")
                        try:
                            cursor.execute("SELECT COUNT(*) FROM partido WHERE ((idEq1 = %s AND idEq2 = %s) OR (idEq2 = %s AND idEq1 = %s)) AND fecha = %s", (idEquipo, idE2, idEquipo, idE2, fecha))
                            count = cursor.fetchone()[0]
                            if count > 0:
                                resultado = True
                            else:
                                resultado = False
                            if resultado:
                                print("\nYa existe un partido agendado entre estos equipos en esta fecha.")
                                esperaTecla()
                            else:
                                estado = "Pendiente"
                                new_part = Partido(idEquipo, idE2, fecha, estado, estadio)
                                Presidente.registrarPartido(new_part)
                                esperaTecla()
                        except Exception as e:
                            print(f"Error al agendar partido: {e}")
                            esperaTecla()
                    else:
                        print("\nNo hay equipos disponibles.")
                        esperaTecla()
                except Exception as e:
                    print(f"Error al mostrar equipos: {e}")
                    esperaTecla()
            elif opcion == "3":
                borrarPantalla()
                Presidente.gestionar_equipo(id,idEquipo)
            elif opcion == "4":
                borrarPantalla()
                print("...:: Consultar partidos ::...")
                estado = input("Ingrese el estado del partido\n1. Pendiente\n2. Completado\n3. Cancelado\nOpción: ")
                if estado == "1":
                    borrarPantalla()
                    try:
                        cursor.execute("SELECT * FROM partido WHERE (idEq1 = %s OR idEq2 = %s) AND estado = 'Pendiente'", (idEquipo, idEquipo))
                        resultado = cursor.fetchall()
                        if resultado:
                            print("\nLista de partidos:")
                            for partido in resultado:
                                print(f"\nID: {partido[0]}")
                                print(f"Equipo 1: {partido[1]}")
                                print(f"Equipo 2: {partido[2]}")
                                print(f"Fecha: {partido[3]}")
                                print(f"Estado: {partido[4]}")
                                print(f"Estadio: {partido[5]}")
                                print("\n-----------------------------------------")
                            comp = input("¿Desea completar o cancelar algún partido? (s/n): ")
                            
                            if comp == "s":
                                elPar = input("Ingrese el ID del partido: ")
                                op = input("¿Qué desea hacer con el partido?\n1. completar\n2. cancelar\nOpción: ")
                                try:
                                    cursor.execute("SELECT * FROM usuarios WHERE equipo_jug = %s", (idEquipo,))
                                    resultado = cursor.fetchall()
                                    if resultado and op == "1":
                                        op = "1"
                                    elif op == "2":
                                        op = "2"
                                    else:
                                        print("\nNo hay jugadores en el equipo. Necesitas jugadores para completar un partido.")
                                        op = "n"
                                except Exception as e:
                                    print(f"Error al recopilar la informacion: {e}")
                                if op == "1":
                                    try:
                                        cursor.execute("UPDATE partido SET estado = 'Completado' WHERE id = %s", (elPar,))
                                        conexion.commit()
                                        print("\nIngresa los goles tu equipo para completar el juego")
                                        golesT = input("\nIngresa los goles de tu equipo: ")
                                        i = 0
                                        while i < int(golesT):
                                            jugador = input("\nIngresa el ID del jugador que anotó: ")
                                            minuto = input("\nIngresa el minuto en el que anotó: ")
                                            new_gol = Goles(jugador, idEquipo, elPar, minuto, golesT)
                                            Goles.registrar_gol(new_gol)
                                            borrarPantalla()
                                            i += 1 
                                        print("\n¡ Partido completado correctamente :D !")
                                    except ValueError:
                                        print("Error: Ingrese un número válido")
                                    except Exception as e:
                                        print(f"Error al mostrar partidos: {e}")
                                elif op == "2":
                                    try:
                                        cursor.execute("UPDATE partido SET estado = 'Cancelado' WHERE id = %s", (elPar,))
                                        conexion.commit()
                                        print("\n¡ Partido cancelado correctamente :D !")
                                    except ValueError:
                                        print("Error: Ingrese un número válido")
                                    except Exception as e:
                                        print(f"Error al mostrar partidos: {e}")
                            else:
                                print("\nOperación cancelada.")
                        else:
                            print("\nNo hay partidos disponibles.")
                    except Exception as e:
                        print(f"Error al mostrar partidos: {e}")
                    esperaTecla()
                elif estado == "2":
                    borrarPantalla()
                    try:
                        cursor.execute("SELECT * FROM partido WHERE (idEq1 = %s OR idEq2 = %s) AND estado = 'Completado'", (idEquipo, idEquipo))
                        resultado = cursor.fetchall()
                        if resultado:
                            print("\nLista de partidos:")
                            for partido in resultado:
                                print(f"\nID: {partido[0]}")
                                print(f"Equipo 1: {partido[1]}")
                                print(f"Equipo 2: {partido[2]}")
                                print(f"Fecha: {partido[3]}")
                                print(f"Estado: {partido[4]}")
                                print(f"Estadio: {partido[5]}")
                                print("\n-----------------------------------------")
                            est = input("\n¿Desea ver estadísticas de algún partido? (s/n): ")
                            if est == "s":
                                elPar = input("\nIngrese el ID del partido: ")
                                Presidente.estadisticasEquipo(elPar,idEquipo,id)
                            else:
                                print("\nOperación cancelada.")
                        else:
                            print("\nNo hay partidos completados.")
                    except Exception as e:
                        print(f"Error al mostrar partidos: {e}")
                    esperaTecla()
                elif estado == "3":
                    borrarPantalla()
                    try:
                        cursor.execute("SELECT * FROM partido WHERE (idEq1 = %s OR idEq2 = %s) AND estado = 'Cancelado'", (idEquipo, idEquipo))
                        resultado = cursor.fetchall()
                        if resultado:
                            print("\nLista de partidos:")
                            for partido in resultado:
                                print(f"\nID: {partido[0]}")
                                print(f"Equipo 1: {partido[1]}")
                                print(f"Equipo 2: {partido[2]}")
                                print(f"Fecha: {partido[3]}")
                                print(f"Estado: {partido[4]}")
                                print(f"Estadio: {partido[5]}")
                                print("\n-----------------------------------------")
                        else:
                            print("\nNo hay partidos cancelado.")
                    except Exception as e:
                        print(f"Error al mostrar partidos: {e}")
                    esperaTecla()
            elif opcion == "5":
                borrarPantalla()
                try:
                    cursor.execute("SELECT * FROM usuarios WHERE tipo = 'Presidente' and equipo IS NULL")
                    resultado = cursor.fetchall()
                    if resultado:
                        print("\nLista de presidentes disponibles:")
                        for presidente in resultado:
                            print(f"\nID: {presidente[0]}")
                            print(f"Nombre: {presidente[3]} {presidente[4]}")
                            print(f"Años en el cargo: {presidente[11]}")
                            print("\n-----------------------------------------")
                        
                        ren_presidente = input("""\nIngrese el ID del nuevo presidente: 
    \nSi desea cancelar la operación, digite 0: """)
                        if ren_presidente != "0":
                            Equipo.cambiar_presidente(ren_presidente,idEquipo,id)
                            esperaTecla()
                            break
                        else:
                            print("Operación cancelada. No hay presidentes disponibles.")
                except ValueError:
                    print("Error: Ingrese un número válido")
                except Exception as e:
                    print(f"Error al mostrar presidente: {e}")
                esperaTecla()
            elif opcion == "6":
                print("Gracias por usar el sistema :D. Nos vemos!")
                esperaTecla()
                break

def menuJugador(id,nombre,apellido,idEquipo):
    while True:
        borrarPantalla()
        print(f"\t ¡Bienvenido {nombre} {apellido}!")
        opcion = input("\n¿Qué deseas hacer hoy?\n1. Ver partidos\n2. Ver estadísticas\n3. Ver goles\n4. Salir\n\nOpción: ")

        if opcion == "1":
            borrarPantalla()
            print("...:: Ver partidos ::...")
            tipo = input("¿Qué partidos deseas ver?\n1. Pendientes\n2. Jugados\nOpción: ")
            Jugador.ver_partidos(tipo,idEquipo,id)
        elif opcion == "2":
            borrarPantalla()
            print("...:: Ver estadísticas ::...")
            try:
                cursor.execute("SELECT * FROM partido WHERE (idEq1 = %s OR idEq2 = %s) and estado = 'Completado'", (idEquipo, idEquipo))
                partidos = cursor.fetchall()
                if partidos:
                    borrarPantalla()
                    print("\nLista de partidos: ")
                    for partido in partidos:
                        print(f"ID: {partido[0]}")
                        print(f"Fecha: {partido[3]}")
                        print(f"Estado: {partido[4]}")
                        print(f"Estadio: {partido[5]}")
                        print("\n-----------------------------------------")
                    eleccion = int(input("Ingrese el ID del partido para ver estadísticas: "))
                    Jugador.mostrar_estadisticas(eleccion,id)
                else:
                    print("\nNo se mostraron estadísticas.")
            except Exception as e:
                print(f"Error al mostrar estadísticas: {e}")
            esperaTecla()
        elif opcion == "3":
            borrarPantalla()
            print("...:: Ver goles ::...")
            Jugador.verGoles(id)
            esperaTecla()
        elif opcion == "4":
            print("Gracias por usar el sistema :D. Nos vemos!")
            esperaTecla()
            break

if __name__ == "__main__":
    menu()