from dao import conectar

# Espaço da Lara
def get_hospedes():
    
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(id) AS total_hospedes FROM hospedes")
    dados= cursor.fetchone

    cursor.close()
    conn.close()

    return dados

def get_quartos():
    
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(id) AS total_quartos FROM quartos")
    dados= cursor.fetchone

    cursor.close()
    conn.close()

    return dados

def get_reservas_ativas():
    
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(id) AS total_hospedes FROM hospedes")
    dados= cursor.fetchone

    cursor.close()
    conn.close()

    return dados




# ==================================== HOSPEDES ==================================
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

    cursor.execute("SELECT * FROM posts WHERE id = %s",(id,))
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

# ===_Atulizar_Hospede_====
def update_hospede(id,nome, email, telefone, cpf):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    valores = (nome, email, telefone, cpf, id)

    cursor.execute("""
        UPDATE hospedes
        SET nome = %s,
            email = %s,
            telefone = %s,
            cpf = %s
        WHERE id = %s
    """,valores)

    cursor.close()
    conn.close()

def delete_hospede(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM hospedes WHERE id = %s", (id,))

    conn.commit()

    cursor.close()
    conn.close()

#==============================================================================




    

# Espaço da Katrina quarto

# ===_Cadastrar_Quartos_====
# listar quartos
def consulta_quartos():

    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM quartos")

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados


# buscar quarto por id
def consulta_quarto_id(id):

    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM quartos WHERE id = %s",(id,))

    dados = cursor.fetchone()

    cursor.close()
    conn.close()

    return dados


# add quarto
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

    cursor.close()
    conn.close()


# edit quarto
def update_quarto(id, numero, tipo, valor_diaria, status):

    conn = conectar()
    cursor = conn.cursor()

    valores = (numero, tipo, valor_diaria, status, id)

    cursor.execute("""
        UPDATE quartos
        SET numero = %s,
            tipo = %s,
            valor_diaria = %s,
            status = %s
        WHERE id = %s
    """, valores)

    conn.commit()

    cursor.close()
    conn.close()


# delete quarto
def delete_quarto(id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM quartos WHERE id = %s",(id,))

    conn.commit()

    cursor.close()
    conn.close()


# Espaço do Jonatan


# Espaço da Laura