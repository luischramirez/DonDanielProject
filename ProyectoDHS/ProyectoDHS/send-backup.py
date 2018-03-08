import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

print("**** Enviar email con Gmail ***")
"""
user = input("Cuenta de gmail:")
password = getpass.getpass("Password: ")
"""
user = "lchajo115@gmail.com"
password = "Pa$$w0rdorsurus"


#Para la cabecera del email
remitente = "Admin <lchajo115@gmail.com>"
destinatario = "Luis <ldchavezr@uqvirtual.edu.co>"
asunto = "Envío de Backup de la aplicación DHS"
mensaje = "<h1> Este correo contiene el Backup generado por la aplicación del Centro Canino de Servicios Integrales DHS</h1> "
archivo = "C:\SW3\BackupDHS.backup"

#Host y puerto SMTP de gmail
gmail = smtplib.SMTP('smtp.gmail.com',587)

#protocolo de cifrado de datos utilizado por gmail
gmail.starttls()

#credenciales
gmail.login(user,password)

#muestra la depuracion de la operacion de envio 1=true
gmail.set_debuglevel(1)

header = MIMEMultipart()
header['Subject'] = asunto
header['From'] = remitente
header['To'] = destinatario

mensaje = MIMEText(mensaje, 'html') #Content-type:text/html
header.attach(mensaje)

if (os.path.isfile(archivo)):
    adjunto = MIMEBase('application', 'octet-stream')
    adjunto.set_payload(open(archivo, "rb").read())
    encode_base64(adjunto)
    adjunto.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(archivo))
    header.attach(adjunto)

#Enviar email
gmail.sendmail(remitente, destinatario, header.as_string())

#Cerrar la conexion SMTP
gmail.quit()