def detectar_base(numero):
    if numero.startswith("0b"):
        return 2
    elif numero.startswith("0o"):
        return 8
    elif numero.startswith("0x"):
        return 16
    else:
        return 10

def binari_decimal(num):
    digits = num[2:]
    for d in digits:
        if d not in "01":
            return None
    valor = 0
    for d in digits:
        valor = valor * 2 + int(d)
    return valor

def octal_decimal(num):
    digits = num[2:]
    for d in digits:
        if d not in "01234567":
            return None
    valor = 0
    for d in digits:
        valor = valor * 8 + int(d)
    return valor

def hexa_decimal(num):
    digits = num[2:]
    valid = "0123456789ABCDEF"
    digits = digits.upper()

    hex_map = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    for d in digits:
        if d not in valid:
            return None

    valor = 0
    for d in digits:
        if d.isdigit():
            valor = valor * 16 + int(d)
        else:
            valor = valor * 16 + hex_map[d]
    return valor

def decimal_binari(n):
    if n == 0:
        return "0b0"
    digits = ""
    while n > 0:
        digits = str(n % 2) + digits
        n //= 2
    return "0b" + digits

def decimal_octal(n):
    if n == 0:
        return "0o0"
    digits = ""
    while n > 0:
        digits = str(n % 8) + digits
        n //= 8
    return "0o" + digits



def decimal_hexadecimal(n):
    if n == 0:
        return "0x0"
    digits = ""
    hex_chars = "0123456789ABCDEF"
    while n > 0:
        digits = hex_chars[n % 16] + digits
        n //= 16
    return "0x" + digits    

def main():
    while True:
        try:
            numero = input("Introdueix un número (o  sortir): ")

            if numero.lower()  == "sortir":
                print("Programa finalitzat .")
                break

            base = detectar_base(numero)

            match base:
                case 2:
                    decimal = binari_decimal(numero)
                case 8:
                    decimal = octal_decimal(numero)
                case 16:
                    decimal = hexa_decimal(numero)
                case 10:
                    if not numero.isdigit():
                        print("ERROR: El número decimal només pot contenir dígits 0-9.")
                        continue
                    decimal = int(numero)
                case _:
                    print("ERROR: Base desconeguda.")
                    continue

            print(f"Decimal: {decimal}")
            print(f"Binari : {decimal_binari(decimal)}")
            print(f"Octal  : {decimal_octal(decimal)}")
            print(f"Hex    : {decimal_hexadecimal(decimal)}")

        except ValueError:
            print("ERROR: S'ha produït un error inesperat.")

if __name__ == "__main__":
    main()
