from dao import conectar

# Espaço da Lara
def get_hospedes():
    
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(id) AS total_hospedes FROM hospedes")
    dados= cursor.fetchone()

    cursor.close()
    conn.close()

    return dados

def get_quartos():
    
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(id) AS total_quartos FROM quartos")
    dados= cursor.fetchone()

    cursor.close()
    conn.close()

    return dados

def get_reservas_ativas():
    
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT COUNT(id) AS total_reservas
        FROM reservas
    """)

    dados = cursor.fetchone()

    cursor.close()
    conn.close()

    return dados


# visualizar reserva por id
def consulta_reserva_id(id):

    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            reservas.id,
            hospedes.nome AS hospede,
            quartos.numero AS quarto,
            quartos.tipo,
            quartos.valor_diaria,
            reservas.data_entrada,
            reservas.data_saida
        FROM reservas
        INNER JOIN hospedes 
            ON reservas.id_hospede = hospedes.id
        INNER JOIN quartos 
            ON reservas.id_quarto = quartos.id
        WHERE reservas.id = %s
    """, (id,))

    dados = cursor.fetchone()

    cursor.close()
    conn.close()

    return dados

# ====_Mostrar_Todos_os_Hospedes_====
def consulta_hospedes():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM hospedes")
    dados = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return dados

# ====_Mostrar_Hospede_Especifico_====
def consulta_hospede_id(id):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM hospedes WHERE id = %s",(id,))
    dados= cursor.fetchone()

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
    dados= conn.commit()

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

    conn.commit()

    cursor.close()
    conn.close()

def delete_hospede(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM hospedes WHERE id = %s", (id,))

    conn.commit()

    cursor.close()
    conn.close()






    

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

#Espaço lara  


# CONSULTAR RESERVAS

def consulta_reservas():

    conn = conectar()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            reservas.id,
            hospedes.nome AS hospede,
            quartos.numero AS quarto,
            reservas.data_checkin,
            reservas.data_checkout,
            reservas.valor_total
           
        FROM reservas
        INNER JOIN hospedes
            ON reservas.hospede_id = hospedes.id
        INNER JOIN quartos
            ON reservas.quarto_id = quartos.id
    """)

    reservas = cursor.fetchall()

    cursor.close()
    conn.close()

    return reservas


# CONSULTAR RESERVA POR ID

def consulta_reserva_id(id):

    conn = conectar()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            reservas.*,
            hospedes.nome AS hospede_nome,
            hospedes.email,
            hospedes.telefone,
            quartos.numero,
            quartos.tipo,
            quartos.valor_diaria
        FROM reservas
        INNER JOIN hospedes
            ON reservas.hospede_id = hospedes.id
        INNER JOIN quartos
            ON reservas.quarto_id = quartos.id
        WHERE reservas.id = %s
    """, (id,))

    reserva = cursor.fetchone()

    cursor.close()
    conn.close()

    return reserva


# ADICIONAR RESERVA

def add_reserva(hospede_id, quarto_id, data_entrada, data_saida):

    conn = conectar()

    cursor = conn.cursor(dictionary=True)

    # pegar valor da diária
    cursor.execute("""
        SELECT valor_diaria
        FROM quartos
        WHERE id = %s
    """, (quarto_id,))

    quarto = cursor.fetchone()

    valor_diaria = quarto["valor_diaria"]

    # calcular quantidade de dias
    from datetime import datetime

    entrada = datetime.strptime(data_entrada, "%Y-%m-%d")
    saida = datetime.strptime(data_saida, "%Y-%m-%d")

    dias = (saida - entrada).days

    valor_total = dias * float(valor_diaria)

    cursor.execute("""
        INSERT INTO reservas (
            hospede_id,
            quarto_id,
            data_checkin,
            data_checkout,
            valor_total
          
        )
        VALUES ( %s, %s, %s, %s, %s)
    """, (
        hospede_id,
        quarto_id,
        data_entrada,
        data_saida,
        valor_total
        
    ))

    conn.commit()

    cursor.close()
    conn.close()


# ATUALIZAR RESERVA

def update_reserva(id, hospede_id, quarto_id, data_entrada, data_saida):

    conn = conectar()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT valor_diaria
        FROM quartos
        WHERE id = %s
    """, (quarto_id,))

    quarto = cursor.fetchone()

    valor_diaria = quarto["valor_diaria"]

    from datetime import datetime

    entrada = datetime.strptime(data_entrada, "%Y-%m-%d")
    saida = datetime.strptime(data_saida, "%Y-%m-%d")

    dias = (saida - entrada).days

    valor_total = dias * float(valor_diaria)

    cursor.execute("""
        UPDATE reservas
        SET
            hospede_id = %s,
            quarto_id = %s,
            data_checkin = %s,
            data_checkout = %s,
            valor_total = %s
        WHERE id = %s
    """, (
        hospede_id,
        quarto_id,
        data_entrada,
        data_saida,
        valor_total,
        id
    ))

    conn.commit()

    cursor.close()
    conn.close()


# EXCLUIR RESERVA


def delete_reserva(id):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM reservas
        WHERE id = %s
    """, (id,))

    conn.commit()

    cursor.close()
    conn.close()