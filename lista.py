import ipaddress
import datetime
import os


#meter el segmento en 1 txt llamado 'segmentos.txt'
def generar_lista_ips():
    archivo_entrada = "segmentos.txt"
    
#solo pa validar
    if not os.path.exists(archivo_entrada):
        print(f"falta el archivo con las ip")
        return

#esto tmb porque soy vago y es para hacer los resultados en un archivo txt escalable. los guarda en formato lista_ip_aaaammdd_mmss.txt
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo_salida = f"lista_ips_{timestamp}.txt"
    try:
        with open(archivo_entrada, 'r') as f_in, open(archivo_salida, 'w') as f_out:
            for linea in f_in:
                segmento = linea.strip()
                if not segmento: continue
                try:
                    red = ipaddress.ip_network(segmento, strict=False)
                    for ip in red:
                        f_out.write(str(ip) + '\n')
                except ValueError:
                    continue
#solo pongo un comentario para saber q termino
        print(f"fin en {archivo_salida}")

    except Exception as e:
        print(f"hubo un error jefe {e}")

if __name__ == '__main__':
    generar_lista_ips()
