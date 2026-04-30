def conv_ton_kg(ton):
    return ton * 1000


def calc_pre_carga(cod_carga, kg):
    if cod_carga in range(10, 21):
        return kg * 100

    elif cod_carga in range(21, 31):
        return kg * 250

    return kg * 340


def calc_imposto(pre_carga, estado):
    impostos = [0.35, 0.25, 0.15, 0.05, 0]

    return (impostos[estado - 1] * pre_carga)


def main():
    codigo_estado = int(input("Digite o codigo do estado de origem (1 a 5): "))
    peso_carga_ton = float(input("Digite o peso da carga em toneladas: "))
    codigo_carga = int(input("Digite o codigo da carga (10 a 40): "))

    peso_carga_kg = conv_ton_kg(peso_carga_ton)
    preco_carga = calc_pre_carga(codigo_carga, peso_carga_kg)
    imposto = calc_imposto(preco_carga, codigo_estado)
    valor_total = preco_carga + imposto

    print(f"Peso convertido em KG: {peso_carga_kg}")
    print(f"Preco da carga: R${preco_carga}")
    print(f"Valor imposto: R${imposto}")
    print(f"Valor total: R${valor_total}")


if __name__ == "__main__":
    main()