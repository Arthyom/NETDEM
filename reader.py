import xml.dom.minidom as dm
import os

### get all files from the current directory and then filterring only xml files
archivosFromDir = [ f for f in os.listdir(os.getcwd()) if os.path.isfile( os.path.join(os.getcwd(), f ) ) ]
archivosXML = [ fi for fi in archivosFromDir if "xml" in fi ]
totalHostsRes = open('totalHostsRes.txt','w')
hostAgrupados = { }

for xmlFile in archivosXML:
    ### parse xml file
    archivoXml = xmlFile
    archivoLst = open(archivoXml.replace('xml', 'txt'), 'a')
    archivoFrc = open(archivoXml.split('.')[0]+'Frc.txt', 'a')
    d = dm.parse(archivoXml)

    ### get host and address tag
    etiquetas = d.getElementsByTagName('address')

    ### declare local variables 
    t = []; ip = 0; mac = 0; ven = 0; i = 0; up = 0; total = 0; hostXArchivo = {}
    total = d.getElementsByTagName('hosts')[0].getAttribute('total')
        

    for ti in etiquetas:
        if i%2 != 0:
            mac = str(ti.getAttribute('addr'))
            ven = str(ti.getAttribute('vendor'))
            t.append( [ip,mac,ven] )
        else:
            ip = str(ti.getAttribute('addr'))
        i+= 1

    ### group and count host frecuency
    for li in t:
        archivoLst.writelines(li[0] + ', ' + li[1] +', '+ li[2])
        archivoLst.write('\n')
        ##open(archivoLst, 'a').write(li)
        if li[2] not in hostAgrupados.keys():
            hostAgrupados[li[2]] = 1
        else :
            hostAgrupados[li[2]] += 1

        if li[2] not in hostXArchivo.keys():
            hostXArchivo[li[2]] = 1
        else :
            hostXArchivo[li[2]] += 1
    
    ### print grouped information 
    for di in hostXArchivo:
        archivoFrc.writelines(di+", "+ str(hostXArchivo[di]))
        archivoFrc.write('\n')
        print( di, hostXArchivo[di] )
    archivoLst.writelines("Up: " + str(len(t)) +' , All: '+ str(total))



 

### print grouped information 
for di in hostAgrupados:
    totalHostsRes.writelines(di+", "+ str(hostAgrupados[di]))
    totalHostsRes.writelines('\n')
