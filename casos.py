import time

from decimal import Decimal
from util import Utiles


#logging.basicConfig(filename='log.log', format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')




def casoTipo(id, tipo, data, cur, uuid, tiempo):
    

    try:


        if tipo == "Tiempo Pantalla_Inicial":
            pantalla_inicial = data
            cur.execute("INSERT INTO sesion_totem(uuid) VALUES (%s)" , [uuid])
            cur.execute("INSERT INTO step(uuid, pantalla_inicial, pre_login, login, register, tyc, pre_emision, masiva, destinatario, direccion, valor_dec_num_doc, tipo_pago, resumen_destinatario, instrucciones, medir_cotizar, nuevo_envio, resumen_pago, queop) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                , [uuid, pantalla_inicial,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) 

        elif tipo == "Usuario" and "Nuevo" in data: 
            cur.execute("UPDATE sesion_totem SET nuevo_usuario = true WHERE uuid = (%s)", [uuid])

            
        elif tipo == "Cantidad OFs por Comprobante":
                  
   
            if data == 1 :
                cur.execute("update totem set termica_paper = termica_paper + 15 where totem_id = (%s)" , [id])
            else:
                largo = 15 + ((data -1) * 5 )
                cur.execute("update totem set termica_paper = termica_paper + (%s) where totem_id = (%s)" , [largo,id])


            cur.execute("SELECT termica_paper FROM totem WHERE totem_id = %s", [id])
            result = cur.fetchone()
            termica_papel = result[0]  
            print("tipo termica papel",type(termica_papel))  
            print("termica_papel: ",termica_papel)

            cur.execute("SELECT value FROM config WHERE key = 'PAPER_LIMIT_TERMICA_1'")
            result = cur.fetchone()
            limite_papel_1 = int(result[0])
    
            cur.execute("SELECT value FROM config WHERE key = 'PAPER_LIMIT_TERMICA_2'")
            result = cur.fetchone()
            limite_papel_2 = int(result[0])
    
            cur.execute("SELECT value FROM config WHERE key = 'PAPER_LIMIT_TERMICA_3'")
            result = cur.fetchone()
            limite_papel_3 = int(result[0])

            cur.execute("SELECT correo_termica_limit FROM totem where totem_id = %s", [id])
            result = cur.fetchone()
            valor_limite = int(result[0])

            if termica_papel >= limite_papel_1 and valor_limite == 0 :
                print("1 condicion")
                Utiles.enviaMail(id)
                print("limite 1 pasado")
                cur.execute("update totem set correo_termica_limit = 1 where totem_id = (%s)", [id])
            elif termica_papel >= limite_papel_1 and termica_papel < limite_papel_2 and valor_limite == 1:
                print("2 condicion")
                pass

            elif termica_papel >= limite_papel_2 and valor_limite == 1:
                print("3 condicion")
                Utiles.enviaMail(id)
                print("limite 2 pasado")
                cur.execute("update totem set correo_termica_limit = 2 where totem_id = (%s)", [id])
            elif termica_papel >= limite_papel_2 and termica_papel < limite_papel_3 and valor_limite == 2:
                print("4 condicion")
                pass

            elif termica_papel >= limite_papel_3 and valor_limite == 2:
                print("5 condicion")
                Utiles.enviaMail(id)
                print("limite 3 pasado")
                cur.execute("update totem set correo_termica_limit = 3 where totem_id = (%s)", [id])

            elif termica_papel >= limite_papel_3 and termica_papel == 3:
                print("6 condicion")
                pass

        elif tipo == "Total etiquetas impresas":
            etiquetas_totales = data["total"]

            cur.execute("update totem set ticket_paper = ticket_paper + (%s) where totem_id = (%s)" , [etiquetas_totales,id])
                #Utiles.enviaMail(id)

            cur.execute("SELECT ticket_paper FROM totem WHERE totem_id = %s", [id])
            result = cur.fetchone()
            ticket_papel = result[0]  
            print("tipo ticket papel",type(ticket_papel))  
            print("ticket_papel: ",ticket_papel)

            cur.execute("SELECT value FROM config WHERE key = 'PAPER_LIMIT_TICKET_1'")
            result = cur.fetchone()
            limite_papel_1 = int(result[0])
    
            cur.execute("SELECT value FROM config WHERE key = 'PAPER_LIMIT_TICKET_2'")
            result = cur.fetchone()
            limite_papel_2 = int(result[0])
    
            cur.execute("SELECT value FROM config WHERE key = 'PAPER_LIMIT_TICKET_3'")
            result = cur.fetchone()
            limite_papel_3 = int(result[0])

            cur.execute("SELECT correo_ticket_limit FROM totem where totem_id = %s", [id])
            result = cur.fetchone()
            valor_limite = int(result[0])

            if ticket_papel >= limite_papel_1 and valor_limite == 0 :
                print("1 condicion")
                Utiles.enviaMail(id)
                print("limite 1 pasado")
                cur.execute("update totem set correo_ticket_limit = 1 where totem_id = (%s)", [id])
            elif ticket_papel >= limite_papel_1 and ticket_papel < limite_papel_2 and valor_limite == 1:
                print("2 condicion")
                pass

            elif ticket_papel >= limite_papel_2 and valor_limite == 1:
                print("3 condicion")
                Utiles.enviaMail(id)
                print("limite 2 pasado")
                cur.execute("update totem set correo_ticket_limit = 2 where totem_id = (%s)", [id])
            elif ticket_papel >= limite_papel_2 and ticket_papel < limite_papel_3 and valor_limite == 2:
                print("4 condicion")
                pass

            elif ticket_papel >= limite_papel_3 and valor_limite == 2:
                print("5 condicion")
                Utiles.enviaMail(id)
                print("limite 3 pasado")
                cur.execute("update totem set correo_ticket_limit = 3 where totem_id = (%s)", [id])

            elif ticket_papel >= limite_papel_3 and ticket_papel == 3:
                print("6 condicion")
                pass


        elif tipo == "Tiempo Pre-Login":
            try:
                tiempo_pre_login = data
                # #print(tiempo_pre_login)
                cur.execute("UPDATE step SET pre_login = pre_login + (%s) WHERE uuid = (%s)", [tiempo_pre_login, uuid])     
                
            except Exception as e:
                print("Error al actualizar: %s", e)   

        elif tipo == "Recupera Pass":
            cur.execute("UPDATE sesion_totem SET recupera_pass = (%s) WHERE uuid = (%s)", [True, uuid])   

        elif tipo == "Tiempo Login":
            tiempo_login = data
            cur.execute("UPDATE step SET login = login + (%s) WHERE uuid = (%s)", [tiempo_login, uuid])

        elif tipo == "Inicio Sesion":
            tipoLogin = 1
            cur.execute("UPDATE sesion_totem SET id_tipo_login =(%s), fecha_inicio_sesion =(%s) WHERE uuid = (%s)", [tipoLogin,tiempo, uuid])


        elif tipo == "Response Authentication" or tipo == "Response Authentication Login QR" or tipo =="Response Authentication Login Register":
        # rut_cliente = int(data['user']["run"])
            rut = int(data['user']["run"][0: len(data['user']["run"])-1])
            digito_verificador = data['user']["run"][-1]
            #digito_verificador = a[0:a.index('back') - 1]
            nombre = data["user"]["name"] + " " + data["user"]["last_name"]
            mail = data["user"]["email"]
            telefono = data["user"]["mobile"]
            frecuencia = "#"
            antiguedad_cliente = "#"
            agencia_preferida = "#"
            idstarken = data["user"]["id"]
            cur.execute("SELECT rut_cliente FROM cliente_autoatencion WHERE rut_cliente = (%s)", [rut])
            consulta = cur.fetchone()

            if consulta is None:
                #print("-------------------------> 1 caso")
                cur.execute("INSERT INTO cliente_autoatencion(rut_cliente,dv, nombre, mail, telefono, frecuencia, antiguedad_cliente, agencia_preferida) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                [rut, digito_verificador, nombre, mail, telefono, frecuencia, antiguedad_cliente, agencia_preferida])
                cur.execute("UPDATE sesion_totem SET id_starken_pro =(%s), rut_cliente = (%s) WHERE uuid = (%s)", [idstarken, rut, uuid])    
                
            elif rut == consulta[0]:
                #print("-------------------------> 2 caso")
                cur.execute("UPDATE sesion_totem SET id_starken_pro =(%s), rut_cliente = (%s) WHERE uuid = (%s)", [idstarken, rut, uuid])       
                
            else:
                #print("-------------------------> 3 caso")
                cur.execute("INSERT INTO cliente_autoatencion(rut_cliente, dv, nombre, mail, telefono, frecuencia, antiguedad_cliente, agencia_preferida) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                [rut, digito_verificador, nombre, mail, telefono, frecuencia, antiguedad_cliente, agencia_preferida])      
        
        elif tipo == "Response Authentication Login QR ":
            rut = int(data['user']["run"][0: len(data['user']["run"])-1])
            digito_verificador = data['user']["run"][-1]
            nombre = data["user"]["name"] + " " + data["user"]["last_name"]
            mail = data["user"]["email"]
            telefono = data["user"]["phone"]
            frecuencia = "#"
            antiguedad_cliente = "#"
            agencia_preferida = "#"
            idstarken = data["user"]["id"]
            cur.execute("SELECT rut_cliente FROM cliente_autoatencion WHERE rut_cliente = (%s)", [rut])
            consulta = cur.fetchone()
        
            if consulta is None:
                #print("-------------------------> 1 caso")
                cur.execute("INSERT INTO cliente_autoatencion(rut_cliente,dv, nombre, mail, telefono, frecuencia, antiguedad_cliente, agencia_preferida) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                [rut, digito_verificador, nombre, mail, telefono, frecuencia, antiguedad_cliente, agencia_preferida])
                cur.execute("UPDATE sesion_totem SET id_starken_pro =(%s), rut_cliente = (%s) WHERE uuid = (%s)", [idstarken, rut, uuid])                
        
            elif rut == consulta[0]:
                #print("-------------------------> 2 caso")
                cur.execute("UPDATE sesion_totem SET id_starken_pro =(%s), rut_cliente = (%s) WHERE uuid = (%s)", [idstarken, rut, uuid])       
            
            else:
                #print("-------------------------> 3 caso")
                cur.execute("INSERT INTO cliente_autoatencion(rut_cliente, dv, nombre, mail, telefono, frecuencia, antiguedad_cliente, agencia_preferida) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                [rut, digito_verificador, nombre, mail, telefono, frecuencia, antiguedad_cliente, agencia_preferida])       
                
        elif tipo == "Tiempo Login QR":
            tipoLogin = 2
            tiempo_login = data
            cur.execute("UPDATE sesion_totem SET id_tipo_login =(%s) WHERE uuid = (%s)", [tipoLogin, uuid])
            cur.execute("UPDATE step SET login = login + (%s) WHERE uuid = (%s)", [ tiempo_login,uuid])     
            
        elif tipo == "Response datosTotem":
            totem_id = data["data"][0]["TOTEM_ID"]
            id_sucursal = data["data"][0]["SUCURSAL"]
            try:
                cur.execute("UPDATE sesion_totem SET totem_id = (%s), codigo_agencia = (%s) WHERE uuid = (%s)", [totem_id, id_sucursal, uuid])
            except Exception as e:
                print("Error al actualizar: %s", e)       
            
        elif tipo == "Tiempo TyC":
            tiempo_cond = data
            cur.execute("UPDATE step SET tyc = tyc + (%s) WHERE uuid = (%s)", [tiempo_cond, uuid])   

        elif tipo == "Tiempo Pre-Emision":
            tiempo_pre_emision = data
            cur.execute("UPDATE step SET pre_emision = pre_emision + (%s) WHERE uuid = (%s)", [tiempo_pre_emision, uuid]) 

        elif tipo == "MASIVA -  Data comprobantePDF":
            for encargo_orden_flete in data:
                for encargo in encargo_orden_flete["encargos"]:
                    codigo_de_barra = encargo["codigo"]
                    of_por_encargo = encargo["orden_flete"]
                    codigo_agencia_destino = encargo_orden_flete["codigo_agencia_destino"]
                    if codigo_agencia_destino is None:
                        masiva_domicilio = encargo_orden_flete["destinatario_direccion"] + " " + encargo_orden_flete["destinatario_numeracion"]
                        masiva_dest_codigo_comuna = encargo_orden_flete["destinatario_codigo_comuna"]
                        masiva_valor_declarado = encargo_orden_flete["valor_declarado"] 
                        cur.execute("INSERT INTO of_masiva(codigo_de_barra, odflcodigo,alto_masiva, ancho_masiva, largo_masiva, peso_masiva, total, descuento, valor, uuid, codigo_agencia_destino, masiva_domicilio, masiva_dest_codigo_comuna, valor_declarado) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [codigo_de_barra, of_por_encargo,0,0,0,0,0,0,0, uuid,codigo_agencia_destino,masiva_domicilio,masiva_dest_codigo_comuna,masiva_valor_declarado]) 
                        alto_masiva = encargo["alto"]
                        ancho_masiva = encargo["ancho"]
                        largo_masiva = encargo["largo"]
                        peso_masiva = encargo["kilos"]
                        cur.execute("UPDATE of_masiva SET alto_masiva = alto_masiva + (%s), ancho_masiva = ancho_masiva + (%s), largo_masiva = largo_masiva + (%s), peso_masiva = peso_masiva + (%s) where codigo_de_barra = (%s)",
                            [alto_masiva,ancho_masiva,largo_masiva,peso_masiva,codigo_de_barra])
                        
                    elif codigo_agencia_destino is not None:
                        masiva_valor_declarado = encargo_orden_flete["valor_declarado"]
                        cur.execute("INSERT INTO of_masiva(codigo_de_barra, odflcodigo,alto_masiva, ancho_masiva, largo_masiva, peso_masiva, total, descuento, valor, uuid, codigo_agencia_destino, masiva_domicilio, masiva_dest_codigo_comuna, valor_declarado) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [codigo_de_barra, of_por_encargo,0,0,0,0,0,0,0, uuid,codigo_agencia_destino,None,None,masiva_valor_declarado]) 
                        alto_masiva = encargo["alto"]
                        ancho_masiva = encargo["ancho"]
                        largo_masiva = encargo["largo"]
                        peso_masiva = encargo["kilos"]
                        cur.execute("UPDATE of_masiva SET alto_masiva = alto_masiva + (%s), ancho_masiva = ancho_masiva + (%s), largo_masiva = largo_masiva + (%s), peso_masiva = peso_masiva + (%s) where codigo_de_barra = (%s)",
                            [alto_masiva,ancho_masiva,largo_masiva,peso_masiva,codigo_de_barra])            

        elif "MASIVA Response valorOFDLS" in tipo:
            masiva_of_descuento = tipo[27:]
            #print(masiva_of_descuento)
            masiva_total = data["message"][0]["TOTAL"]
            masiva_descuento = data["message"][0]["DESCUENTO"]
            masiva_valor = data["message"][0]["VALOR"]
            cur.execute("UPDATE of_masiva SET total = total + (%s), descuento = descuento + (%s), valor = valor + (%s) WHERE odflcodigo = (%s)", [masiva_total, masiva_descuento, masiva_valor, masiva_of_descuento])
                
        elif tipo == "Update Password":
            cur.execute("UPDATE sesion_totem SET update_pass = (%s) WHERE uuid = (%s)", [True, uuid])  

        elif tipo == "Tiempo Destinatario":
            tiempo_dest = data
            cur.execute("UPDATE step SET destinatario = destinatario + (%s) WHERE uuid = (%s)", [tiempo_dest, uuid]) 

        elif tipo == "Actualizacion Datos Usuario":
            
            new_name = data["name"] + " " + data["last_name"]
            new_email = data["email"]
            new_mobile = data["mobile"]
            rut_cliente_cambio = data["rut"]
            cur.execute("UPDATE cliente_autoatencion SET nombre =(%s), mail = (%s), telefono  = (%s) WHERE rut_cliente = (%s)", [new_name, new_email, new_mobile, rut_cliente_cambio]) 
            

        elif tipo == "Tiempo Direccion":
            tiempo_emision = data
            cur.execute("UPDATE step SET direccion = direccion + (%s) WHERE uuid = (%s)", [tiempo_emision, uuid]) 
            

        elif tipo == "Tiempo Valor_Dec-Num_Doc":
            tiempo_valor_declarado = data
            cur.execute("UPDATE step SET valor_dec_num_doc = valor_dec_num_doc + (%s) WHERE uuid = (%s)", [tiempo_valor_declarado, uuid]) 
            

        elif tipo == "Tiempo Tipo_Pago":
            tiempo_tipo_pago = data
            cur.execute("UPDATE step SET tipo_pago = tipo_pago + (%s) WHERE uuid = (%s)", [tiempo_tipo_pago, uuid])

        elif tipo == "Tiempo Masiva":
            tiempo_masiva = data
            cur.execute("UPDATE step SET masiva = masiva + (%s) WHERE uuid = (%s)", [tiempo_masiva, uuid])
            

        elif tipo == "Tiempo Resumen_Destinatario":
            resumen_destinatario = data
            cur.execute("UPDATE step SET resumen_destinatario = resumen_destinatario + (%s) WHERE uuid = (%s)", [resumen_destinatario, uuid]) 

        elif tipo == "Tiempo Instrucciones":
            instrucciones = data
            cur.execute("UPDATE step SET instrucciones = instrucciones + (%s) WHERE uuid = (%s)", [instrucciones, uuid]) 

        elif tipo == "OF emitida":
            odflcodigo = data["orden_flete"]
            fecha_emision = tiempo
            of_pago_totem = tipo[19:]
            
            try:
                fecha_tipo_horario = time.strptime(tiempo[11:19], '%H:%M:%S')
            except Exception as e:
                print("Error al actualizar: %s", e)   

            hora_normal_inicio= time.strptime('08:00:00', '%H:%M:%S')
            hora_normal_fin= time.strptime('18:00:00', '%H:%M:%S')
            if fecha_tipo_horario >= hora_normal_inicio and fecha_tipo_horario <= hora_normal_fin :
                tipo_horario = 1
                #print('Horario Normal')
            else:
                tipo_horario = 2
                #print('24/7')
        
            
            
            alto_totem = data["encargos"][0]["alto"]
            ancho_totem = data["encargos"][0]["ancho"]
            largo_totem = data["encargos"][0]["largo"]
            peso_totem = float(data["kilos_total"])
            tipo_entrega =data["tipo_entrega"]["id"]
            
            if tipo_entrega == 1:
                agencia_destino = data["codigo_agencia_destino"]
                codigo_comuna = data["destinatario_codigo_comuna"]
                codigo_ciudad = data["destinatario_codigo_ciudad"]
                valor_declarado = data["valor_declarado"]
            elif tipo_entrega == 2:
                domicilio = data["destinatario_direccion"] + " " + data["destinatario_numeracion"]
                codigo_comuna = data["destinatario_codigo_comuna"]
                codigo_ciudad = data["destinatario_codigo_ciudad"]
                valor_declarado = data["valor_declarado"]

            if tipo_entrega == 1:

                cur.execute("INSERT INTO orden_de_flete(odflcodigo, fecha_emision, total, descuento, valor, tipo_horario, alto_totem, ancho_totem, largo_totem, peso_totem, uuid, tipo_pago, estado_pago, tipo_documento, tipo_entrega, agencia_destino, domicilio,codigo_comuna,codigo_ciudad, valor_declarado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)" ,
                [odflcodigo, fecha_emision, 0,0,0, tipo_horario, alto_totem, ancho_totem, largo_totem, peso_totem,  uuid, "POR PAGAR", False, "SIN EMITIR", tipo_entrega,agencia_destino,0,codigo_comuna,codigo_ciudad, valor_declarado])

            elif tipo_entrega == 2:
                cur.execute("INSERT INTO orden_de_flete(odflcodigo, fecha_emision, total, descuento, valor, tipo_horario, alto_totem, ancho_totem, largo_totem, peso_totem, uuid, tipo_pago, estado_pago, tipo_documento, tipo_entrega, agencia_destino, domicilio,codigo_comuna,codigo_ciudad, valor_declarado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)" ,
                [odflcodigo, fecha_emision, 0,0,0, tipo_horario, alto_totem, ancho_totem, largo_totem, peso_totem,  uuid, "POR PAGAR", False, "SIN EMITIR", tipo_entrega,0,domicilio,codigo_comuna,codigo_ciudad, valor_declarado])
    


        elif "Response Emision valorOFDLS" in tipo:
            of_descuento = tipo[28:]
            #print(of_descuento)
            total = data["message"][0]["TOTAL"]
            descuento = data["message"][0]["DESCUENTO"]
            valor = data["message"][0]["VALOR"]
            cur.execute("UPDATE orden_de_flete SET total = total + (%s), descuento = descuento + (%s), valor = valor + (%s) WHERE odflcodigo = (%s)", [total, descuento, valor, of_descuento])

        elif tipo == "Response Emision insertOfTotemPago":
            of_tipo_pago = data["data"]["of"]
            first_estado_pago = False
            tipo_pago = data["data"]["tipoPago"]
            cur.execute("UPDATE orden_de_flete SET (tipo_pago, estado_pago) =(%s, %s) WHERE odflcodigo = (%s)", [tipo_pago, first_estado_pago, of_tipo_pago])

        elif tipo == "Tiempo Medir_Cotizar":
            medir_cotizar = data
            cur.execute("UPDATE step SET medir_cotizar = medir_cotizar + (%s) WHERE uuid = (%s)", [medir_cotizar, uuid]) 

        elif tipo == "Tiempo Nuevo_Envio":
            nuevo_envio = data
            cur.execute("UPDATE step SET nuevo_envio = nuevo_envio + (%s) WHERE uuid = (%s)", [nuevo_envio, uuid]) 


        elif "Response pagoTotem" in tipo:
            of_pago_totem = tipo[19:]
            #print(of_pago_totem)
            tipo_documento = data["descripcionDocumento"]
            cur.execute("UPDATE orden_de_flete SET tipo_documento = (%s) WHERE odflcodigo = (%s)", [tipo_documento, of_pago_totem]) 

            

        elif tipo == "Tiempo Resumen_Pago":
            resumen_pago = data
            cur.execute("UPDATE step SET resumen_pago = resumen_pago + (%s) WHERE uuid = (%s)", [resumen_pago, uuid]) 

        elif tipo == "OF pagadas":
            of_pagadas = data
            estado_pago = True
            for of in of_pagadas:
                of =int(of)
                cur.execute("UPDATE orden_de_flete SET estado_pago = (%s) WHERE odflcodigo = (%s)", [estado_pago, of])
            

        elif tipo == "Cierre Sesion":
            tipo_cierre_sesion = data
            if tipo_cierre_sesion == "Manual":
                cur.execute("UPDATE sesion_totem SET fecha_cierre_sesion =(%s) , id_cierre_sesion =(%s) WHERE uuid = (%s)", [tiempo, 1, uuid]) 
            elif tipo_cierre_sesion == "Automatico":
                cur.execute("UPDATE sesion_totem SET fecha_cierre_sesion =(%s) , id_cierre_sesion =(%s) WHERE uuid = (%s)", [tiempo, 2, uuid]) 
            elif tipo_cierre_sesion == "Automatico - Falla Servicios":
                cur.execute("UPDATE sesion_totem SET fecha_cierre_sesion =(%s) , id_cierre_sesion =(%s) WHERE uuid = (%s)", [tiempo, 3, uuid]) 
            elif tipo_cierre_sesion == "Camara":
                cur.execute("UPDATE sesion_totem SET fecha_cierre_sesion =(%s) , id_cierre_sesion =(%s) WHERE uuid = (%s)", [tiempo, 4, uuid]) 
            elif tipo_cierre_sesion == "Balanza":
                cur.execute("UPDATE sesion_totem SET fecha_cierre_sesion =(%s) , id_cierre_sesion =(%s) WHERE uuid = (%s)", [tiempo, 5, uuid]) 
            elif tipo_cierre_sesion == "I. Etiqueta":
                cur.execute("UPDATE sesion_totem SET fecha_cierre_sesion =(%s) , id_cierre_sesion =(%s) WHERE uuid = (%s)", [tiempo, 6, uuid]) 
            elif tipo_cierre_sesion == "I. Termica":
                cur.execute("UPDATE sesion_totem SET fecha_cierre_sesion =(%s) , id_cierre_sesion =(%s) WHERE uuid = (%s)", [tiempo, 7, uuid]) 
            elif tipo_cierre_sesion == "TBK":
                cur.execute("UPDATE sesion_totem SET fecha_cierre_sesion =(%s) , id_cierre_sesion =(%s) WHERE uuid = (%s)", [tiempo, 8, uuid])

            
        elif "back" in tipo:
            a = tipo[7:]
            a= a[0:a.index('back') - 1]
            cur.execute("INSERT INTO backstep(uuid, step, tiempo) VALUES (%s, %s, %s)" , [uuid, a, data])

        elif "Dropdown" in tipo:
            tipo_drop = data
            cur.execute("INSERT INTO dropdown(uuid, tipo_dropdown) VALUES ( %s, %s)" , [uuid, tipo_drop])

        
        elif "Out Of Service" in data:
            id_totem_oos = id
            cur.execute("SELECT oos FROM totem WHERE totem_id = (%s)", [id_totem_oos])
            estado_oos = cur.fetchone()
            estado_oos = estado_oos[0]

            if  data == "Se recibe el evento Out Of Service  en ReactJS" and estado_oos == False :
                id_totem_oos = id
                cur.execute("UPDATE totem SET oos = (%s) where totem_id = (%s)", [True, id_totem_oos])
                tiempo_inicio_oos = tiempo
                #print("estado oos:", estado_oos)
                cur.execute("INSERT INTO oos(totem_id, id_dispositivo, inicio_oos) VALUES (%s, %s, %s)" , [id_totem_oos, 1, tiempo_inicio_oos])

        

        elif "Inservice" in data:
            id_totem_oos = id
            cur.execute("SELECT oos FROM totem WHERE totem_id = (%s)", [id_totem_oos])
            estado_oos = cur.fetchone()
            #print('estado_oos',estado_oos)
            estado_oos = estado_oos[0]
                
            if data == "Se recibe el evento Inservice  en ReactJS" and estado_oos == True:
                id_totem_oos = id
                #print("IN SERVICE")
                cur.execute("UPDATE totem SET oos = (%s) WHERE totem_id =(%s)", [False, id_totem_oos ])
                tiempo_fin_oos = tiempo
                #print("estado oos:", estado_oos)

                cur.execute("UPDATE oos SET fin_oos =(%s) WHERE totem_id =(%s) and fin_oos is NULL", [tiempo_fin_oos, id_totem_oos])
                cur.execute("update oos SET tiempo_oos = round(((DATE_PART('day', fin_oos::timestamp - inicio_oos::timestamp) * 24 +DATE_PART('hour', fin_oos::timestamp - inicio_oos::timestamp)) * 60 +DATE_PART('minute', fin_oos::timestamp - inicio_oos::timestamp)) * 60 +DATE_PART('second', fin_oos::timestamp - inicio_oos::timestamp)) where totem_id=(%s) and tiempo_oos is null" , [ id_totem_oos])

        

        else: 
            print("")

    except Exception as e:
            print("Error al actualizar: %s", e)   
    
    
    
def casoTipoQuickBOx(ip, tipo, barra, fecha, data, cur):
        
    try:
        if tipo == "BD checkPago Request":
            codigo_barra = barra
            orden_flete = data["of"]
            fecha_inicio = fecha
            cur.execute("INSERT INTO qbox_transaction(ip,codigo_de_barra, odflcodigo, fecha_inicio) VALUES (%s, %s, %s, %s)" , [ip, codigo_barra, orden_flete, fecha_inicio])
            

        elif tipo == "BD checkPago Response": 
            checkpago_status = data["status"]
            if checkpago_status == 200:
                cur.execute("UPDATE qbox_transaction SET check_pago = true WHERE codigo_de_barra = (%s)", [barra])
            else:
                cur.execute("UPDATE qbox_transaction SET check_pago = false WHERE codigo_de_barra = (%s)", [barra])

        elif tipo == "BD bultosOF Response":
            cur.execute("UPDATE qbox_transaction SET bultos_of = true WHERE codigo_de_barra = (%s)", [barra])

        elif tipo == "BD checkMeasureBypackge Request":
            peso = Decimal(data["peso"])
            alto = int(data["alto"])
            largo = int(data["largo"])
            ancho = int(data["ancho"])
            cur.execute("UPDATE qbox_transaction SET alto_quickbox = (%s), ancho_quickbox =(%s), largo_quickbox =(%s), peso_quickbox = (%s) WHERE codigo_de_barra = (%s)", [alto, ancho, largo, peso, barra])

        elif tipo == "BD Peso Sobre":
            peso = Decimal(data["peso"])
            alto = int(data["alto"])
            largo = int(data["largo"])
            ancho = int(data["ancho"])
            cur.execute("UPDATE qbox_transaction SET alto_quickbox = (%s), ancho_quickbox =(%s), largo_quickbox =(%s), peso_quickbox = (%s) WHERE codigo_de_barra = (%s)", [alto, ancho, largo, peso, barra])    
        
        elif tipo == "BD checkMeasureBypackge Response":
            cur.execute("UPDATE qbox_transaction SET check_measure_by_packge = true WHERE codigo_de_barra = (%s)", [barra])
        
        elif tipo == "BD recepcion Response":
            recepcion_status = data["status"]
            fecha_fin = fecha
            if recepcion_status == 200:
                cur.execute("UPDATE qbox_transaction SET recepcion_exitosa = true, fecha_fin = (%s) WHERE codigo_de_barra = (%s)", [fecha_fin, barra])
            else:
                cur.execute("UPDATE qbox_transaction SET recepcion_exitosa = false WHERE codigo_de_barra = (%s)", [barra])
        
        elif tipo == "BD Queop Eval":
            queops_valor = data
            cur.execute("UPDATE qbox_transaction SET queops_valor = (%s) WHERE codigo_de_barra = (%s)", [queops_valor, barra])
        
        else: 
            print("")

    except Exception as e:
            print("Error al actualizar: %s", e)

