import streamlit as st
from PIL import Image

# Configuración básica de la página
st.set_page_config(page_title="Auditor de Sesgos de Género", page_icon="🔍", layout="centered")
try:
    icono_poc = Image.open("poc.png")
except:
    icono_poc = "🔍"

st.set_page_config(
    page_title="Auditor de Sesgos de Género", 
    layout="wide", 
    page_icon=icono_poc
)

estilo_css = """
<style>
    /* Fondo principal morado oscuro con un ligero degradado */
    .stApp {
        background-color: #582479;
        background-image: linear-gradient(180deg, #582479 0%, #3a1352 100%);
    }

    /* Forzar que todos los textos principales sean blancos */
    h1, h2, h3, p, span, label, div {
        color: #FFFFFF !important;
    }

    /* Color de fondo del título del acordeón */
    [data-testid="stExpander"] summary {
        background-color: #976AA8 !important; /* Fondo lila */
        border-radius: 10px !important;
    }

    /* Color del texto del título en estado normal */
    [data-testid="stExpander"] summary p,
    [data-testid="stExpander"] summary span {
        color: #FFFFFF !important; /* Texto blanco */
        font-weight: bold !important;
    }

    /* Color de la flechita del acordeón en estado normal */
    [data-testid="stExpander"] summary svg {
        fill: #FFFFFF !important;
    }

    /* Estilo al pasar el ratón (hover) o al hacer clic (focus) */
    [data-testid="stExpander"] summary:hover,
    [data-testid="stExpander"] summary:focus {
        background-color: #E6C875 !important; /* Fondo se vuelve dorado */
    }

    /* Color del texto al pasar el ratón o hacer clic */
    [data-testid="stExpander"] summary:hover p,
    [data-testid="stExpander"] summary:hover span,
    [data-testid="stExpander"] summary:focus p,
    [data-testid="stExpander"] summary:focus span {
        color: #582479 !important; /* Texto morado oscuro para que contraste */
    }

    /* Color de la flechita al pasar el ratón */
    [data-testid="stExpander"] summary:hover svg,
    [data-testid="stExpander"] summary:focus svg {
        fill: #582479 !important;
    }
    
    /* Estilo del formulario */
    [data-testid="stForm"] {
        background-color: rgba(151, 106, 168, 0.3); /* Lila transparente */
        border: 2px solid #E6C875; /* Línea dorada simulando las ondas */
        border-radius: 20px;
        padding: 25px;
    }

    /* Estilo del botón principal */
    [data-testid="stForm"] button {
        background-color: #976AA8 !important;
        border: 2px solid #E6C875 !important;
        border-radius: 25px !important;
        transition: all 0.3s ease !important;
    }

    /* Color del texto en estado normal */
    [data-testid="stForm"] button p {
        color: #000000 !important; /* <-- Texto negro aquí */
        font-weight: bold !important;
    }

    /* Estilo al pasar el mouse (Hover) */
    [data-testid="stForm"] button:hover {
        background-color: #E6C875 !important; /* Se vuelve dorado */
        border: 2px solid #E6C875 !important;
    }

    /* Color del texto al pasar el mouse */
    [data-testid="stForm"] button:hover p {
        color: #582479 !important; /* Texto morado oscuro para que resalte */
    }

    /* Evitar el color blanco por defecto de Streamlit al hacer clic (Focus) */
    [data-testid="stForm"] button:focus,
    [data-testid="stForm"] button:active {
        background-color: #976AA8 !important;   
        border: 2px solid #E6C875 !important;
    }
    
    [data-testid="stForm"] button:focus p,
    [data-testid="stForm"] button:active p {
        color: #000000 !important; /* <-- Texto negro también al hacer clic */
    }

    header[data-testid="stHeader"] {
        display: none !important;
        height: 0px !important;
        opacity: 0 !important;
    }
</style>
"""
st.markdown(estilo_css, unsafe_allow_html=True)
st.title("🔍 Auditor de Sesgos en la Investigación")
st.markdown("Evalúa tu proyecto o investigación para detectar posibles sesgos androcéntricos o sexistas.")

# 1. Apartado de Información (Estilo acordeón / Expander)
with st.expander("📚 ¿Qué es el Análisis de Género y cuáles son los sesgos comunes?"):
    st.markdown("""
    **Análisis Integral de las Herramientas para el Análisis de Género en el Desarrollo Social**
    
    El análisis de género no es solo revisar datos sobre mujeres y hombres; es un proceso relacional para desentrañar estructuras de poder. Permite ver "lo invisible" en proyectos que se asumen neutrales.
    
    ---
    
    **Los 7 Sesgos Sexistas en la Investigación:**
    
    * **Ginopía (Invisibilidad de las mujeres):** Se produce cuando las mujeres son directamente omitidas en la investigación. Cualquier indicador social incurre en ginopía si no está desagregado en función del sexo. Es una variante del androcentrismo, donde se reconstruye la realidad desde una perspectiva masculina ignorando o minusvalorando las experiencias de las mujeres.
    * **Sobregeneralización:** Se presenta cuando se realizan investigaciones tomando como referencia a un sexo (usualmente el masculino) y se generalizan sus resultados como si fueran aplicables a ambos sexos.
    * **Insensibilidad de género:** Consiste en ignorar que el sexo y/o el género es una variable socialmente relevante en las investigaciones. Esto lleva a la descontextualización, al no reconocer que una misma situación puede tener significados e implicaciones distintas para mujeres y hombres.
    * **Familismo:** Es una manifestación exacerbada de insensibilidad de género. Consiste en tratar a la familia o al hogar como una unidad de análisis, presuponiendo que a todos sus integrantes les afectan del mismo modo los eventos estudiados e ignorando las diferencias y posiciones de poder intrafamiliares.
    * **Doble rasero:** Se produce al analizar, tratar, medir o evaluar conductas o situaciones idénticas para ambos sexos con criterios diferentes.
    * **«Propio de su sexo»:** Consiste en naturalizar, o dar por sentado, que hay cosas, acciones y/o actitudes más apropiadas para un sexo que para otro. Una forma común es asumir la tradicional división sexual del trabajo (como delegar el cuidado del hogar exclusivamente a las mujeres) como algo no problemático.
    * **Dicotomía sexual:** Consiste en tratar a los dos sexos como categorías separadas y segregadas, sobreexagerando las diferencias de género en lugar de considerar que existen muchas características coincidentes. Se da cuando un atributo humano se identifica en exclusiva con uno u otro sexo (por ejemplo, asociar liderazgo solo a hombres y sensibilidad solo a mujeres).
    
    """)

st.divider()

# 2. Formulario del Auditor
st.subheader("📝 Cuestionario de Evaluación")

with st.form("formulario_auditor"):
    st.markdown("Responde **Sí** o **No** a las siguientes preguntas sobre tu metodología:")
    
    q1 = st.radio("1. ¿Tus indicadores sociales o datos recolectados carecen de separación en función del sexo?", ("No", "Sí"), horizontal=True)
    q2 = st.radio("2. ¿Tomaste como referencia la experiencia o datos de un solo sexo y generalizaste los resultados para toda la población?", ("No", "Sí"), horizontal=True)
    q3 = st.radio("3. ¿Ignoras el sexo o el género como una variable socialmente relevante para explicar el problema que estás estudiando?", ("No", "Sí"), horizontal=True)
    q4 = st.radio("4. ¿Analizas a la familia como una sola unidad económica, presumiendo que los ingresos y gastos afectan por igual a todos sus miembros?", ("No", "Sí"), horizontal=True)
    q5 = st.radio("5. ¿Evalúas o mides conductas idénticas con criterios diferentes dependiendo de si las realiza un hombre o una mujer?", ("No", "Sí"), horizontal=True)
    q6 = st.radio("6. ¿Asumes en tu diseño de investigación la división sexual tradicional del trabajo (ej. cuidado para ellas, proveeduría para ellos) como algo 'natural' o dado?", ("No", "Sí"), horizontal=True)
    q7 = st.radio("7. ¿Asocias un atributo humano en exclusiva con uno u otro sexo (ej. liderazgo a los varones, sensibilidad a las mujeres)?", ("No", "Sí"), horizontal=True)
    
    # Botón de envío
    submitted = st.form_submit_button("Auditar Proyecto 🚀")

# 3. Lógica de resultados y recomendaciones
if submitted:
    st.header("📊 Resultados de la Auditoría")
    
    sesgos_detectados = 0
    
    if q1 == "Sí":
        st.error("**Ginopía (o Androcentrismo por omisión)**")
        st.write("📌 *Problema:* Tu investigación padece de la discapacidad de percibir a las mujeres al omitirlas de los datos.")
        st.success("💡 **Recomendación:** Utiliza la herramienta de **Datos Desagregados**. Asegúrate de que todas tus encuestas, censos y métricas recojan y reporten la variable sexo/género por separado.")
        sesgos_detectados += 1
        
    if q2 == "Sí":
        st.error("**Sobregeneralización**")
        st.write("📌 *Problema:* Estás asumiendo que la experiencia (generalmente masculina) explica los fenómenos del conjunto de la sociedad.")
        st.success("💡 **Recomendación:** Delimita claramente el alcance de tu estudio. Si tu muestra es mayoritariamente de un sexo, acláralo en tus conclusiones y no extrapoles los resultados.")
        sesgos_detectados += 1
        
    if q3 == "Sí":
        st.error("**Insensibilidad de Género**")
        st.write("📌 *Problema:* Estás pasando por alto cómo un mismo contexto puede tener implicaciones muy distintas para mujeres y hombres.")
        st.success("💡 **Recomendación:** Aplica el **Marco de Harvard**. Analiza detalladamente el contexto: ¿Quién tiene acceso a los recursos del proyecto? ¿Quién toma las decisiones? Considera el género como variable cruzada desde el diseño inicial.")
        sesgos_detectados += 1
        
    if q4 == "Sí":
        st.error("**Familismo**")
        st.write("📌 *Problema:* Partes de la ficción de que el hogar se comporta como una unidad, ignorando las asimetrías de poder y recursos internas.")
        st.success("💡 **Recomendación:** Cambia tu unidad de análisis. En lugar de encuestar al 'jefe de familia', recopila información de los individuos dentro del hogar para notar diferencias en consumo y tiempo.")
        sesgos_detectados += 1
        
    if q5 == "Sí":
        st.error("**Doble Rasero**")
        st.write("📌 *Problema:* Existe un trato metodológico discriminatorio e inequitativo en los criterios de evaluación.")
        st.success("💡 **Recomendación:** Estandariza tus métricas. Verifica que las preguntas, pruebas de usabilidad o criterios de éxito de tu proyecto apliquen exactamente igual sin importar el sexo del usuario.")
        sesgos_detectados += 1
        
    if q6 == "Sí":
        st.error("**«Propio de su sexo»**")
        st.write("📌 *Problema:* Aceptas acríticamente que ciertos roles son inherentes a un sexo sin plantearlo como una pregunta de investigación.")
        st.success("💡 **Recomendación:** Usa el **Marco de Moser** y la herramienta del **Reloj de 24 horas**. Reconoce la triple jornada y cuestiona si tu proyecto está asumiendo que las mujeres tendrán tiempo libre sin considerar sus labores de cuidado.")
        sesgos_detectados += 1
        
    if q7 == "Sí":
        st.error("**Dicotomía Sexual**")
        st.write("📌 *Problema:* Tratas a los sexos como categorías opuestas segregadas, exagerando las diferencias y minimizando las similitudes.")
        st.success("💡 **Recomendación:** Evita el determinismo biológico. Analiza los atributos humanos como un espectro y asegúrate de que tu interfaz, algoritmo o estudio no fuerce a los usuarios a encajar en estereotipos rígidos.")
        sesgos_detectados += 1

    if sesgos_detectados == 0:
        st.balloons()
        st.success("🎉 ¡Felicidades! Según tus respuestas, el diseño metodológico de tu proyecto parece tener una sólida perspectiva de género y está libre de los sesgos tipificados más comunes.")
    else:
        st.warning(f"⚠️ Se han detectado **{sesgos_detectados}** áreas de oportunidad metodológica. Revisa las recomendaciones para ajustar tu proyecto.")
