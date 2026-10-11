#1- Multiplicacion Rusa (sin operador)
def multiplicacion_rusa(a, b):
    if b == 0:
        return 0
    
    # Llamada recursiva duplicando 'a' y halando 'b'
    res = multiplicacion_rusa(a + a, b // 2)
    
    # Si b es impar, sumamos 'a' extra
    if b % 2 != 0:
        res += a
        
    return res
