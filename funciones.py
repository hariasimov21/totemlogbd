import psycopg2
import casos as cs


#logging.basicConfig(filename='log.log', format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', level=print, datefmt='%Y-%m-%d %H:%M:%S')

casos_validos = [
    "Tiempo Pantalla_Inicial",
    "Usuario",
    "Tiempo Pre-Login",
    "Recupera Pass",
    "Tiempo Login",
    "Inicio Sesion",
    "Response Authentication",
    "Response Authentication Login QR",
    "Response Authentication Login Register",
    "Response Authentication Login QR ",
    "Tiempo Login QR",
    "Response datosTotem",
    "Tiempo TyC",
    "Tiempo Pre-Emision",
    "MASIVA -  Data comprobantePDF",
    "MASIVA Response valorOFDLS",
    "Update Password",
    "Tiempo Destinatario",
    "Actualizacion Datos Usuario",
    "Tiempo Direccion",
    "Tiempo Valor_Dec-Num_Doc",
    "Tiempo Tipo_Pago",
    "Tiempo Masiva",
    "Tiempo Resumen_Destinatario",
    "Tiempo Instrucciones",
    "OF emitida",
    "Response Emision valorOFDLS",
    "Response Emision insertOfTotemPago",
    "Tiempo Medir_Cotizar",
    "Tiempo Nuevo_Envio",
    "Response pagoTotem",
    "Tiempo Resumen_Pago",
    "OF pagadas",
    "Cierre Sesion",
    "back",
    "Dropdown",
    "Out Of Service",
    "Inservice",
    "BD checkPago Request",
    "BD checkPago Response",
    "BD bultosOF Response",
    "BD checkMeasureBypackge Request",
    "BD checkMeasureBypackge Response",
    "BD recepcion Response",
    "BD Queop Eval",
    "BD Peso Sobre",
    "Cantidad OFs por Comprobante",
    "Total etiquetas impresas"
    ]

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


def desintegraData(entrada):
    conn = None
    cur = None
    try:    
        tipo = entrada["tipo"]
        data = entrada["data"]          
        
        if "BD" in tipo:
            conn = get_db_connection()
            cur = conn.cursor()
            ip = entrada["IP"]
            #sucursal = entrada["sucursal"]
            #nro_modulo = entrada["NroModulo"]
            #device_name = entrada["DeviceName"]
            fecha = entrada["datetime"]
            barra = entrada["barra"]
            dataqb = entrada["data"]
            cs.casoTipoQuickBOx(ip,tipo, barra,fecha, dataqb, cur)
        elif "Out Of Service" in str(data):
            conn = get_db_connection()
            cur = conn.cursor()
            id = entrada["id"]
            uuid = entrada["uuid"]
            time = entrada["time"]
            cs.casoTipo(id,tipo, data, cur, uuid, time) 
        elif "Inservice" in str(data):
            conn = get_db_connection()
            cur = conn.cursor()
            id = entrada["id"]
            uuid = entrada["uuid"]
            time = entrada["time"]
            cs.casoTipo(id,tipo, data, cur, uuid, time) 
        elif any(caso in tipo for caso in casos_validos) :              
            conn = get_db_connection()
            cur = conn.cursor()
            id = entrada["id"]
            uuid = entrada["uuid"]
            time = entrada["time"]
            data = entrada["data"]
            cs.casoTipo(id,tipo, data, cur, uuid, time)
        else:
            print(f"no es un caso")       
    except Exception as ex: 
        print(ex)
    finally:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()
        


    

    

 