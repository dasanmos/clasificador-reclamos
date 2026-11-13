"""Genera el dataset SINTETICO de mensajes de clientes (ficticio, sin datos reales)."""
import random, csv, re, sys
random.seed(42)

C = {
"pagos": [
("Me cobraron dos veces el mismo pedido y necesito que me devuelvan uno de los cobros hoy", 1),
("Pagué con tarjeta pero la página me dice que el pago no fue aprobado y ya me descontaron la plata", 1),
("¿Por qué el valor que me cobraron es mayor al que aparecía en el carrito?", 0),
("Quiero pagar con PSE pero me sale un error al elegir mi banco", 0),
("Hice la transferencia hace tres días y el pedido sigue en estado pendiente de pago", 1),
("No me llegó la factura electrónica de mi compra, ¿me la pueden reenviar?", 0),
("Me aplicaron un cobro que no reconozco en mi extracto, creo que fue de su tienda", 1),
("El cupón de descuento no se aplicó al momento de pagar, ¿qué hago?", 0),
("Quiero cambiar el medio de pago de un pedido que aún no se ha enviado", 0),
("La tarjeta me la rechaza siempre en su página pero en otras tiendas sí funciona", 0),
("Cancelé el pedido y todavía no me reembolsan el dinero, ya pasaron dos semanas", 1),
("¿Se puede pagar en cuotas sin interés con tarjeta de crédito?", 0),
("Me salió un cargo duplicado en la cuenta de ahorros por una sola compra", 1),
("Pagué contra entrega y el domiciliario me dijo que el valor era distinto al de la orden", 0),
("Necesito el comprobante de pago para presentarlo en mi empresa", 0),
("Me cobraron el envío aunque la promoción decía envío gratis", 0),
("El reembolso me llegó incompleto, faltan 25 mil pesos", 1),
("Intenté pagar con Nequi y la app se queda cargando sin confirmar", 0),
("Ya pagué y no me llegó ningún correo de confirmación, no sé si quedó registrado", 0),
("Me hicieron un cobro después de devolver el producto, esto es un abuso", 1),
("¿Por qué me aparece el pago como rechazado si mi banco dice que fue aprobado?", 0),
("Necesito corregir los datos de facturación, puse mal el NIT", 0),
("Pagué un pedido y ahora me aparece que lo debo, ¿está bien?", 1),
("El saldo a favor de mi devolución no aparece en mi cuenta", 0),
("Me estan cobrando una suscripcion que nunca pedi, quiero que la cancelen ya", 1),
],
"envios": [
("Mi pedido debía llegar el lunes y todavía no aparece, necesito saber dónde está", 0),
("El paquete llegó con la caja rota y el producto estaba golpeado", 0),
("La guía de rastreo lleva cinco días sin actualizarse", 0),
("Me entregaron un pedido que no es el mío, venía otro producto", 0),
("¿Pueden cambiar la dirección de entrega? Me equivoqué de barrio", 1),
("El domiciliario nunca llegó y la plataforma dice que ya me entregaron", 1),
("¿Cuánto se demora el envío a Cali?", 0),
("Faltó un artículo en mi pedido, solo llegaron dos de los tres productos", 0),
("Necesito que el pedido llegue antes del viernes porque es un regalo", 1),
("La transportadora dice que no encontró mi dirección, pero la puse bien", 0),
("¿Hacen envíos a zonas rurales o solo a ciudades principales?", 0),
("Me llegó el pedido y la talla no corresponde a la que compré", 0),
("Hace dos semanas hice el pedido y sigue diciendo preparando envío", 0),
("Quiero reprogramar la entrega porque no voy a estar en casa", 0),
("El paquete fue devuelto al remitente sin avisarme", 1),
("¿Puedo recoger mi pedido en una tienda física en vez de recibirlo?", 0),
("Pedí un medicamento de venta libre y necesito que llegue hoy, ¿es posible?", 1),
("Me dieron un número de guía que no funciona en la página de la transportadora", 0),
("Recibí el producto con el empaque abierto, parece usado", 0),
("El repartidor dejó el paquete con un vecino que no conozco", 0),
("¿Por qué me cobran el envío por separado si compré dos productos?", 0),
("Mi pedido salió de la bodega hace una semana y no ha pasado de la misma ciudad", 0),
("La entrega estaba programada para hoy y nadie ha llamado", 1),
("quiero saber el estado de mi envio, el numero de pedido es 48213", 0),
("El producto llegó roto y lo necesitaba para un evento mañana", 1),
],
"cuenta": [
("No puedo iniciar sesión, me dice que mi contraseña es incorrecta", 0),
("Olvidé mi contraseña y el correo de recuperación nunca llega", 0),
("Alguien entró a mi cuenta y hizo compras que yo no hice", 1),
("Quiero cambiar el correo electrónico asociado a mi cuenta", 0),
("Me bloquearon la cuenta sin explicación y tengo un pedido pendiente", 1),
("¿Cómo elimino mi cuenta y mis datos personales de la tienda?", 0),
("El código de verificación por mensaje de texto no me llega", 0),
("Quiero actualizar mi número de celular en el perfil", 0),
("No me deja registrarme, dice que el correo ya existe pero nunca he comprado", 0),
("Mi cuenta aparece con el nombre de otra persona", 0),
("Recibí un correo diciendo que cambiaron mi contraseña y yo no fui", 1),
("¿Cómo activo la verificación en dos pasos?", 0),
("La aplicación me cierra la sesión cada vez que la abro", 0),
("No puedo ver mi historial de pedidos, la sección sale vacía", 0),
("Necesito cambiar la dirección guardada en mi perfil", 0),
("Me sale un error al intentar entrar con mi cuenta de Google", 0),
("Me llegan correos de la tienda y nunca me suscribí, quiero darme de baja", 0),
("No recuerdo con qué correo me registré, ¿me pueden ayudar a encontrarlo?", 0),
("Mi cuenta fue suspendida por actividad sospechosa, pero yo solo compré una vez", 1),
("El enlace para restablecer la contraseña dice que ya expiró", 0),
("No puedo guardar mi tarjeta en el perfil, la página se queda en blanco", 0),
("Quiero unificar mis dos cuentas porque creé una por error", 0),
("me sale que mi usuario esta bloqueado por intentos fallidos, ayuda", 0),
("Alguien más tiene acceso a mi cuenta, veo pedidos que no reconozco", 1),
("¿Cómo cambio el nombre que aparece en mi perfil?", 0),
],
"otro": [
("¿Cuál es el horario de atención de sus tiendas los domingos?", 0),
("Quería felicitarlos, el pedido llegó rápido y el producto es excelente", 0),
("¿Tienen este modelo de zapatos en color negro y talla 40?", 0),
("Me gustaría que agregaran más opciones de productos para mascotas", 0),
("¿Venden al por mayor? Tengo un negocio pequeño y quiero cotizar", 0),
("¿Cómo funciona la garantía de los electrodomésticos?", 0),
("Quiero trabajar con ustedes, ¿dónde envío mi hoja de vida?", 0),
("La página se ve muy lenta en mi celular, sería bueno que la mejoren", 0),
("¿Cuándo vuelve a estar disponible el audífono que agotaron?", 0),
("¿Tienen programa de puntos o descuentos para clientes frecuentes?", 0),
("Gracias por la atención, la asesora fue muy amable", 0),
("¿Pueden recomendarme un portátil para estudiar ingeniería con presupuesto de dos millones?", 0),
("¿Cómo devuelvo un producto que no me gustó? Aún está sellado", 0),
("Sugiero que pongan fotos reales de los productos y no solo las del fabricante", 0),
("¿Esta chaqueta es impermeable o solo resistente al agua?", 0),
("¿Tienen alguna tienda en Barranquilla?", 0),
("Quisiera saber si ofrecen servicio de instalación para los televisores", 0),
("¿Van a hacer descuentos en el Día sin IVA?", 0),
("Les escribo para proponer una alianza con mi marca de ropa", 0),
("¿Cuáles son las medidas exactas de este escritorio?", 0),
("No encuentro la categoría de libros en el menú, ¿sigue existiendo?", 0),
("Excelente servicio, seguiré comprando con ustedes", 0),
("¿Los productos de esta marca son originales?", 0),
("¿Me pueden enviar el catálogo de la nueva temporada?", 0),
("Tengo una duda: ¿la tienda tiene política de cambios por talla?", 0),
],
}
SALUDOS = ["Buenas tardes, ", "Hola, ", "Buen día, ", "Hola equipo, ", "Estimados, ", ""]
CIERRES = [" Gracias.", " Quedo atento.", " Muchas gracias por su ayuda.", " Espero su respuesta.", " Por favor respondan pronto.", ""]

def sin_tildes(t):
    return t.translate(str.maketrans("áéíóúÁÉÍÓÚñ¿¡","aeiouAEIOUn  ")).strip().lower()

def variantes(txt):
    cuerpo = txt[0].lower() + txt[1:]
    v1 = txt
    v2 = random.choice(SALUDOS) + (cuerpo if random.random() < .8 else txt) + random.choice(CIERRES)
    v3 = sin_tildes(txt).replace(",", "")
    return [v1, v2, v3]

filas, vistos, g = [], set(), 0
for cat, lista in C.items():
    for txt, urg in lista:
        g += 1  # grupo = mensaje base; sus variantes deben quedar juntas al dividir train/test
        for m in variantes(txt):
            m = re.sub(r"\s+", " ", m).strip()
            if m in vistos: continue
            vistos.add(m)
            filas.append({"mensaje": m, "categoria": cat, "urgente": "si" if urg else "no",
                          "origen": "sintetico", "grupo": g})
random.shuffle(filas)
for i, f in enumerate(filas, 1):
    f["id"] = i
with open(sys.argv[1], "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=["id", "mensaje", "categoria", "urgente", "origen", "grupo"])
    w.writeheader(); w.writerows(filas)
print(len(filas), "filas")
