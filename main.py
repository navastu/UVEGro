import streamlit as st
import pandas as pd

#Carga de calificaciones 
df = pd.read_csv("Calificaciones.csv")
df['CALIFICACIÓN NÚMERO'] = df['CALIFICACIÓN NÚMERO'].replace('NC',0)
df.fillna('0',inplace=True)
df['CALIFICACIÓN NÚMERO'] = df['CALIFICACIÓN NÚMERO'].astype(int)

st.header("Listado de estudiantes con calificaciones")
tipo = st.radio("Buscar por: ",['Matrícula','Nombre'], None)


if tipo == "Matrícula":
    matricula = st.text_input("Ingrese Martrícula: ")
    btn_buscar = st.button("Buscar")

    if btn_buscar:
        if matricula:
            if matricula.isdigit():
                df_alumno = df[df['MATRÍCULA']==int(matricula)]
                if not(df_alumno.empty):
                    # Aplicar estilos con pandas Styler
                    def resaltar_altos(val):
                        color = "green" if val >= 70 else "red"
                        return f"color: {color}"
                    
                    df_nom_alumno = df_alumno['NOMBRE COMPLETO'].unique()
                    nom_alumno = df_nom_alumno[0]
                    df_programaestudio = df_alumno['PROGRAMA'].unique()
                    programaestudio = df_programaestudio[0]
                    st.subheader(f"Estudiante: {nom_alumno}", divider=True)
                    st.write("Programa de estudio: ", programaestudio)
                    df_vista = df_alumno[['Unidad de Aprendizaje','CALIFICACIÓN NÚMERO','Cuatrimestre','Grupo']].sort_values('Grupo')
                    df_vista = df_vista.rename(columns={'CALIFICACIÓN NÚMERO':'CALIFICACIÓN'})
                    st.dataframe(df_vista.style.applymap(resaltar_altos, subset=["CALIFICACIÓN"]), hide_index=True, use_container_width=True)
                else:
                    st.write("Estudiante no encontrado")
            else:
                st.write("Error en matrícula, asegúerese de ingresar solo caracteres numéricos")
        else:
            st.write('Ingrese matrícula')
else:
    nombre = st.text_input("Ingrese Nombre: ")
    btn_buscarnombre = st.button("Buscar")


    if btn_buscarnombre:
        if nombre:
            if not(nombre.isdigit()):
                df_alumno = df[df['NOMBRE COMPLETO'].str.contains(nombre.upper())]
                if not(df_alumno.empty):

                    # Aplicar estilos con pandas Styler
                    def resaltar_altos(val):
                        color = "green" if val >= 70 else "red"
                        return f"color: {color}"

                    df_nombreM = df_alumno['NOMBRE COMPLETO'].unique()
                    nombreM = df_nombreM[0]
                    df_num_mat = df_alumno['MATRÍCULA'].unique()
                    num_mat = df_num_mat[0]
                    df_programaestudio = df_alumno['PROGRAMA'].unique()
                    programaestudio = df_programaestudio[0]
                    st.subheader(f"Estudiante: {nombreM}", divider=True)
                    st.write("Número de matrícula: ", str(num_mat))
                    st.write("Programa de estudios: ", str(programaestudio))
                    df_vista = df_alumno[['Unidad de Aprendizaje','CALIFICACIÓN NÚMERO','Cuatrimestre','Grupo']].sort_values('Grupo')
                    df_vista = df_vista.rename(columns={'CALIFICACIÓN NÚMERO':'CALIFICACIÓN'})
                    st.dataframe(df_vista.style.applymap(resaltar_altos, subset=["CALIFICACIÓN"]), hide_index=True, use_container_width=True)
                else:
                    st.write("Estudiante no encontrado")
            else:
                st.write("Error en nombre, asegúerese de ingresar solo caracteres de texto")
        else:
            st.write('Ingrese nombre a buscar')