import xml.dom.minidom as dm

### parse xml file
archivoXml = 's11.xml'
archivoLst = open(archivoXml.replace('xml', 'txt'), 'a')
archivoFrc = open(archivoXml.split('.')[0]+'Frc.txt', 'a')
d = dm.parse(archivoXml)

### get host and address tag
host = d.getElementsByTagName('hosts')
etiquetas = d.getElementsByTagName('address')

### declare local variables 
t = []; ip = 0; mac = 0; ven = 0; i = 0; hostAgrupados = { }
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

### print grouped information 
for di in hostAgrupados:
    archivoFrc.writelines(di+", "+ str(hostAgrupados[di]))
    archivoFrc.write('\n')
    print( di, hostAgrupados[di] )

### print total, up and readed hosts
for h in host:
    ups = h.getAttribute('up')
    alls = h.getAttribute('total')
    print ( 'Total ' + str(alls), ' ups '+ str(ups) , ' leidos '+ str(len(t) +1) )
 
