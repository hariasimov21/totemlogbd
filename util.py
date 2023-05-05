import parametros 
import psycopg2



TIMEOUT=20000
#logging.basicConfig(filename='log.log', format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

PARAMETROS = parametros.getParametros()
# print(PARAMETROS)
URL_PORTAL_SMS = PARAMETROS[0]['value']
MAIL_SUBJECT = PARAMETROS[3]['value']
MAIL_MESSAGE_TERMICA_PAPER = PARAMETROS[4]['value']

conn = psycopg2.connect(host="172.20.6.238",
        database="totemlog",
        user="totemlog",
        #password="totemlog.,2022",)
        password="totemlog.,2023",)
cur = conn.cursor()
cur.execute("SELECT value FROM config WHERE key='CORREO_ALERTA_TERMICA_PAPER'")
result = cur.fetchone()
PLANTILLA_CORREO = result[0]


class Utiles:

    def enviaMail(id_totem):
        print('pasa por aca')
        data= parametros.obtenerDatosTotem(id_totem)
        print("datos totem: ", data)

        AGENCIA = data[0]['agendescripcion']
        RESPONSABLE = data[0]['responsable']
        EMAIL_RESPOSANBLE= data[0]['email_responsable']

        message= PLANTILLA_CORREO
        message = message.replace("$TITULO", MAIL_SUBJECT)
        message = message.replace("$RESPONSABLE", RESPONSABLE)
        message = message.replace("$TOTEM", id_totem)
        message = message.replace("$AGENCIA", AGENCIA)

        """message =  MAIL_MESSAGE_TERMICA_PAPER.replace("1",RESPONSABLE)
        message= message.replace("2",id_totem )
        message= message.replace("3",AGENCIA ) """

        print(message)

        payload = [
            {
                'to' : EMAIL_RESPOSANBLE,
                'subject' : MAIL_SUBJECT,
                'type' : 'EMAIL',
                'origin' : 'Monitoreo Totem',
                'message' : message,  
                'content_type': 'text/html'           
            }
        ]
       
        headers = {
            'Content-Type' : 'application/json'
        }
        """response = requests.post(URL_PORTAL_SMS, json=payload, headers=headers, timeout=TIMEOUT)
        if response.status_code == 200:
            print('Correo alerta etiqueta enviado')
            return response.content
        else:
            return response.content"""
