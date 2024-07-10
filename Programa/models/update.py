from main import cursor


def update(nova_quantidade, codigo):
    comma = \
            f"""
            UPDATE PRODUTOS_SERGEL
            SET qtd = {nova_quantidade}
            WHERE codigo = {codigo}
            """
    cursor.execute(comma)
    cursor.commit()