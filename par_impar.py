def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
resultado = verificar_par_impar(7)
print(f"O número 7 é {resultado}")