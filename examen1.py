aprobado=0
reprobado=0
promocionado=0
x=1
n=int(input("cantidad de examen:"))
while x<=n:
    valor=int(input("puntaje:"))
    if valor>1 and valor<=29:
        reprobado=reprobado+1
        print("reprobo")
    else:
           if valor>30 and valor<=47:
            reprobado=reprobado+1
            print("reprobo")
           else:
              if valor>48 and valor<=59:
                reprobado=reprobado+1
              print("reprobo con 3:")
              if valor>60 and valor<=65:
                  reprobado=reprobado+1
                  print("reprobado:")
              else:
                  if valor<=66 and valor<=71:
                      reprobado=reprobado+1
                      print("aprobado")
                      if valor>72 and valor<=77:
                          aprobado=aprobado+1
                          print("aprobado")
                      else:
                          if valor>78 and valor<=83:
                              aprobado=aprobado+1
                          else:
                              if valor>84 and valor<=89:
                                  print("promocionado")
                              else:
                                  if valor>90 and valor<=95:
                                      print("promocionado")
                                  else:
                                      if valor>96 and valor<=100:
                                          print("promocionado")
    x=x+1
promedio_reprobado=(reprobado*100)/10
promedio_aprobado=(aprobado*100)/10
promedio_promocionado=(promocionado*100)/10
promedio_total=(reprobado+aprobado+promocionado)/10
print("aprobados",promedio_aprobado)
print("reprobados",promedio_reprobado)
print("promocionado",promedio_promocionado)
print("promedio total",promedio_total)