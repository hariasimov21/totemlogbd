import psycopg2



#logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')


def get_db_connection():   
    try:
        # Produccion con datos QA
        #conn = psycopg2.connect(host="172.20.4.209",
        # QA con datos productivos
        conn = psycopg2.connect(host="172.20.6.238",
        database="totemlog",
        user="totemlog",
        #password="totemlog.,2022",)
        password="totemlog.,2023",)
        conn.autocommit = True
        return conn 
    
    except Exception as e:
            print("Error al conectar: %s", e)

def getParametros():
    conn = None
    cur = None
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("select * from config c order by id_config ")
    
   
    desc = cur.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
            for row in cur.fetchall()]


    cur.close()
    conn.close()

    return data



def obtenerDatosTotem(id_totem):
    conn = None
    cur = None
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("select totem_id , a.agendescripcion, a.responsable ,a.email_responsable  from totem t left join agencia a on t.sucursal = a.agencodigo where totem_id = (%s)" , [id_totem])
       
    desc = cur.description 
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
            for row in cur.fetchall()] 

    cur.close()
    conn.close()

    return data