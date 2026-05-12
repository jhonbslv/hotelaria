from dao import conectar

# Espaço da Lara
def get_posts():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM hotelaria")
    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados

# Espaço da Sophia
# ====_Mostrar_Todos_os_Hospedes_====
def consulta_hospedes():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    sql= "SELECT * FROM hospedes"

    cursor.execute(sql)
    dados = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return dados

# ====_Mostrar_Hospede_Especifico_====
def consulta_hospede_id(id):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    sql= "SELECT * FROM posts WHERE id = %s"

    cursor.execute(sql,(id,))
    dados= cursor.fetchone

    cursor.close()
    conn.close()

    return dados


# ===_Cadastrar_Hospede_====
def add_hospede(nome, email, telefone, cpf):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    valores = (nome, email, telefone, cpf)

    cursor.execute(
        '''
        INSERT INTO 
            hospedes 
            (nome, email, telefone, cpf) 
        VALUES 
            (%s, %s, %s, %s)
        ''', valores)
    dados= cursor.commit()

    cursor.close()
    conn.close()

    return dados
    

# Espaço da Katrina quarto

# ===_Cadastrar_Quartos_====
#listar os quartos
def consulta_quartos():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM quartos")
    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados

# consulta dos quartos por id
def consulta_quarto_id(id):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)


    cursor.execute(("SELECT * FROM quartos WHERE id = %s", id,))
    dados = cursor.fetchone()

    conn.close()

    return dados

# inserir quarto 
def add_quarto(numero, tipo, valor_diaria, status):

    conn = conectar()
    cursor = conn.cursor()

    valores = (numero, tipo, valor_diaria, status)

    cursor.execute("""
    INSERT INTO quartos(
        numero,
        tipo,
        valor_diaria,
        status
    )

    VALUES(%s, %s, %s, %s)
    """, valores)

    conn.commit()
    conn.close()

#update edit de quartos
def update_quarto(id, numero, tipo, valor_diaria, status):

    conn = conectar()
    cursor = conn.cursor()


    valores = (id, numero, tipo, valor_diaria, status)

    cursor.execute("""
    UPDATE quartos
    SET numero=%s,
        tipo=%s,
        valor_diaria=%s,
        status=%s
    WHERE id=%s
    """, valores)

    conn.commit()
    conn.close()


# deletar quarto
def delete_quarto(id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM quartos WHERE id=%s", (id,))

    conn.commit()
    conn.close()


# Espaço do Jonatan


# Espaço da Laura