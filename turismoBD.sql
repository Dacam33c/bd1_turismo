use turismo;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS Pessoa;
DROP TABLE IF EXISTS Hotel;
DROP TABLE IF EXISTS Destino;
DROP TABLE IF EXISTS pontoTuristico;
DROP TABLE IF EXISTS Transporte;
DROP TABLE IF EXISTS Cliente;
DROP TABLE IF EXISTS Guia;
DROP TABLE IF EXISTS Quarto;
DROP TABLE IF EXISTS Plano;
DROP TABLE IF EXISTS Localizacao;
DROP VIEW IF EXISTS cliente_transporte;
DROP VIEW IF EXISTS Clientes_Hoteis;
DROP VIEW IF EXISTS Planos_PontosTuristicos;
DROP TABLE IF EXISTS pontoFoto;
DROP TABLE IF EXISTS Viagens;
DROP TABLE IF EXISTS aviao;
DROP TABLE IF EXISTS localdepartida;
DROP TABLE IF EXISTS onibus;
DROP PROCEDURE IF EXISTS DeletarCliente;
DROP PROCEDURE IF EXISTS DeletarLocalizacao;
DROP PROCEDURE IF EXISTS GetImagemPonto;
DROP PROCEDURE IF EXISTS AnalisarCapacidadeTransporte;


SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE Pessoa (
    CPF varchar(11) PRIMARY KEY,
    endereco varchar(255),
    Nome varchar(100),
    dataDeNascimento DATE,
    telefone varchar(20)
);
INSERT INTO Pessoa (CPF, Nome, endereco, dataDeNascimento, telefone) VALUES
('12345678901', 'Carlos Eduardo Silva', 'Rua das Palmeiras, 123, São Paulo - SP', '1990-05-12', '(11) 98765-4321'),
('23456789012', 'Mariana Santos Oliveira', 'Avenida Brasil, 456, Rio de Janeiro - RJ', '1985-09-23', '(21) 99876-5432'),
('34567890123', 'Ricardo Pereira Costa', 'Rua XV de Novembro, 789, Curitiba - PR', '1993-02-15', '(41) 91234-5678'),
('45678901234', 'Fernanda Lima Souza', 'Alameda das Rosas, 321, Belo Horizonte - MG', '1988-07-30', '(31) 92345-6789'),
('1', '1', '1', '1988-07-30', '1'),
('56789012345', 'Thiago Mendes Rocha', 'Praça da Liberdade, 987, Porto Alegre - RS', '1995-11-05', '(51) 93456-7890');

CREATE TABLE Destino 
( 
    tipo varchar(100),  
    nome varchar(100) PRIMARY KEY
);
INSERT INTO Destino (tipo, nome) VALUES
('Praia', 'Fernando de Noronha'),
('Montanha', 'Gramado'),
('Histórico', 'Ouro Preto'),
('Urbano', 'São Paulo'),
('Ilha', 'Ilha Bela'),
('Praia', 'Florianópolis'),
('Praia','Porto Seguro'),
('Urbano','Curitiba');

CREATE TABLE Localizacao (
    endereco VARCHAR(100) PRIMARY KEY,
    nomeDestino VARCHAR(100),
    FOREIGN KEY (nomeDestino) REFERENCES Destino(nome)
);

INSERT INTO Localizacao (endereco, nomeDestino) VALUES
('Avenida Paulista 123 São Paulo - SP', 'Gramado'),
('Rodovia BR-101 Km 200 Florianópolis - SC', 'Gramado'),
('Rua das Palmeiras 456 Porto Seguro - BA', 'Gramado'),
('Rua XV de Novembro 789 Curitiba - PR', 'Curitiba'),
('Rua Augusta 321 São Paulo - SP', 'São Paulo');

CREATE TABLE Hotel (
    CNPJ VARCHAR(14) PRIMARY KEY,
    tipo VARCHAR(100),
    nome VARCHAR(100),
    endereco VARCHAR(100),
    FOREIGN KEY (endereco) REFERENCES Localizacao(endereco)
);
INSERT INTO Hotel (CNPJ, tipo, nome, endereco) VALUES
('12345678000101', 'Hotel 5 Estrelas', 'Grand Palace Hotel', 'Avenida Paulista 123 São Paulo - SP'),
('23456789000102', 'Resort', 'Paraíso das Águas Resort', 'Rodovia BR-101 Km 200 Florianópolis - SC'),
('34567890000103', 'Pousada', 'Pousada Recanto do Sol', 'Rua das Palmeiras 456 Porto Seguro - BA'),
('45678901000104', 'Hotel Executivo', 'Blue Tower Business Hotel', 'Rua XV de Novembro 789 Curitiba - PR'),
('56789012000105', 'Hostel', 'Backpackers Hostel', 'Rua Augusta 321 São Paulo - SP');

CREATE TABLE pontoTuristico 
( 
    Nome VARCHAR(100) PRIMARY KEY,  
    preço INT, 
    nomeDestino varchar(100),
    FOREIGN KEY(nomeDestino) REFERENCES Destino (nome)
);
INSERT INTO pontoTuristico (Nome, preço, nomeDestino) VALUES
('Praia do Sancho', 0, 'Fernando de Noronha'),
('Lago Negro', 10, 'Gramado'),
('Museu da Inconfidência', 20, 'Ouro Preto'),
('Avenida Paulista', 0, 'São Paulo'),
('Praia do Curral', 0, 'Ilha Bela');

create table pontoFoto
(
	Nome varchar(100) Primary key,
    foreign key (nome) references pontoTuristico (nome),
    foto LONGBLOB
);
Insert into pontoFoto (nome,foto) Values
('Praia do Sancho',NULL),
('Lago Negro',NULL),
('Museu da Inconfidência',NULL),
('Praia do Curral', NULL);

CREATE TABLE transporte 
( 
 PlacaTransporte varchar(100) primary key,
 capacidade int(10),
 tipo varchar(100)
);
INSERT INTO transporte (PlacaTransporte,capacidade,tipo) VALUES
('ABC1A23','10','onibus'),
('XYZ9B87','30','onibus'),
('LMN3C56','10','onibus'),
('QWE5D67','40','aviao'),
('RTY7E89','30','aviao');

CREATE TABLE Viagens 
( 
	ID INT AUTO_INCREMENT PRIMARY KEY,
    placa varchar(100),
    foreign key (placa) references transporte (placaTransporte),
    DataPartida varchar(100), 
    hora varchar(100),
    nomeDestino varchar(100),
    Preço INT,
    FOREIGN KEY(nomeDestino) REFERENCES Destino (nome),
    assentosOcupados int(10)
);
INSERT INTO Viagens (Preço, DataPartida, placa, hora, nomeDestino,assentosOcupados) VALUES
(150, '2024-02-10', 'ABC1A23', '08:00', 'Fernando de Noronha','3'),
(200, '2024-02-15', 'XYZ9B87', '14:30', 'Gramado','5'),
(120, '2024-02-20', 'LMN3C56', '07:45', 'Gramado','2'),
(180, '2024-02-25', 'QWE5D67', '16:00', 'Gramado','1'),
(90, '2024-03-01', 'RTY7E89', '09:15', 'Ilha Bela','5');


CREATE TABLE Cliente (
    CPF VARCHAR(11) PRIMARY KEY,
    NomeDeUsuario VARCHAR(100),
    desconto INT,
    FOREIGN KEY (CPF) REFERENCES Pessoa(CPF),
    senha varchar(100)
);

INSERT INTO Cliente (desconto, NomeDeUsuario, CPF,senha) VALUES
(10, 'joaosilva', '12345678901','12345'),
(15, 'mariasantos', '23456789012','23456'),
(5, 'pedrosouza', '34567890123','34567'),
(20, 'anacarvalho', '45678901234','45678'),
(1, '1', '1','1'),
(8, 'lucasferreira', '56789012345','56789');


CREATE TABLE Guia 
( 
    ID INT AUTO_INCREMENT PRIMARY KEY,
    CPF varchar(11),
    FOREIGN KEY(CPF) REFERENCES Pessoa (CPF),
    nomeDestino varchar(100),
    FOREIGN KEY(nomeDestino) REFERENCES Destino (nome),
    Preço INT
);
INSERT INTO Guia ( CPF, nomeDestino,Preço) VALUES
( '12345678901', 'Fernando de Noronha', 200),
('23456789012', 'Gramado',150),
('34567890123', 'Gramado',180),
('45678901234', 'Gramado',120),
('56789012345', 'Ilha Bela',170);


CREATE TABLE Quarto (
    numero INT,
    CNPJHotel varchar(14),
    PRIMARY KEY (numero, CNPJHotel),
    FOREIGN KEY (CNPJHotel) REFERENCES Hotel(CNPJ),
    preco DECIMAL(10, 2),
    capacidade INT
    
);
INSERT INTO Quarto (CNPJHotel,numero, preco, capacidade) VALUES
('12345678000101',101, 250, 2),
('12345678000101',202, 300, 4),
('12345678000101',303, 180, 3),
('45678901000104',404, 400, 2),
('56789012000105',505, 150, 1);

CREATE TABLE Plano
( 
 ID INT AUTO_INCREMENT PRIMARY KEY,  
 CPFcliente varchar(11),
 FOREIGN KEY(CPFcliente) REFERENCES Cliente (CPF),
 IDguia INT,
 FOREIGN KEY(IDguia) REFERENCES Guia (ID),
 CNPJHotel varchar(14),
 numeroQuarto int(10),
 FOREIGN KEY(numeroQuarto,CNPJHotel) REFERENCES quarto (numero, CNPJHotel),
 IDviagem int(20),
 FOREIGN KEY(IDviagem) REFERENCES viagens (ID)
);


INSERT INTO Plano (CPFcliente, IDguia, CNPJHotel, numeroQuarto, IDviagem) VALUES
('12345678901', 1,  '12345678000101', '101', '1'),
('23456789012', 2,  '23456789000102', '202', '2'),
('34567890123', 3,  '34567890000103', '303', '3'),
('45678901234', 3,  '45678901000104', '404', '4'),
('45678901234', 2,  '56789012000105', '505', '5');

-- VIEWS
CREATE VIEW cliente_transporte AS
SELECT 
    p.CPFcliente, 
    v.DataPartida, 
    v.NomeDestino, 
    v.Placa,
    v.hora
FROM Plano p
JOIN Viagens v ON p.IDviagem = v.ID;

CREATE VIEW Clientes_Hoteis AS
SELECT 
    Cliente.NomeDeUsuario,
    Cliente.CPF,
    Hotel.nome AS NomeHotel,
    Hotel.endereco AS EnderecoHotel
FROM Cliente
JOIN Plano ON Cliente.CPF = Plano.CPFcliente
JOIN Hotel ON Plano.CNPJHotel = Hotel.CNPJ;

#CREATE VIEW Planos_PontosTuristicos AS
#SELECT 
#    Plano.ID AS ID_Plano,
#    Plano.CPFcliente,
#    pontoTuristico.Nome AS NomePontoTuristico,
#    pontoTuristico.preço AS PrecoPontoTuristico
#FROM Plano
#JOIN pontoTuristico ON Plano.nomeDestino = pontoTuristico.nomeDestino;

CREATE VIEW Planos_PontosTuristicos AS
SELECT 
    p.ID AS ID_Plano,
    p.CPFcliente AS CPF_Cliente,
    pt.Nome AS Ponto_Turistico,
    pt.Preço AS Preco
FROM Plano p
JOIN Viagens v ON p.IDviagem = v.ID
JOIN Destino d ON v.NomeDestino = d.Nome
JOIN pontoTuristico pt ON d.Nome = pt.nomeDestino;

-- PROCEDURES
DELIMITER $$
CREATE PROCEDURE GetImagemPonto(IN p_nome VARCHAR(255))
BEGIN
    SELECT foto
    FROM pontoFoto
    WHERE Nome = p_nome;
END $$

DELIMITER ;


DELIMITER $$

CREATE PROCEDURE AnalisarCapacidadeTransporte(IN p_placa VARCHAR(100))
BEGIN
    DECLARE v_capacidade INT;
    DECLARE v_assentos_ocupados INT;
    DECLARE v_ocupacao DECIMAL(5,2);
    DECLARE v_desconto INT;
    DECLARE v_mensagem VARCHAR(255);
    
    SELECT t.capacidade, COALESCE(v.assentosOcupados, 0)
    INTO v_capacidade, v_assentos_ocupados
    FROM transporte t
    LEFT JOIN Viagens v ON t.PlacaTransporte = v.placa
    WHERE t.PlacaTransporte = p_placa
    LIMIT 1;

    IF v_capacidade > 0 THEN
        SET v_ocupacao = (v_assentos_ocupados / v_capacidade) * 100;
    ELSE
        SET v_ocupacao = 0;
    END IF;

    IF v_assentos_ocupados >= v_capacidade THEN
        SET v_desconto = 0;
        SET v_mensagem = 'Sem assentos disponíveis';
    ELSEIF v_ocupacao < 50 THEN
        SET v_desconto = 20;
        SET v_mensagem = 'Desconto de 20% aplicado';
    ELSEIF v_ocupacao < 75 THEN
        SET v_desconto = 10;
        SET v_mensagem = 'Desconto de 10% aplicado';
    ELSE
        SET v_desconto = 0;
        SET v_mensagem = 'Sem desconto aplicado';
    END IF;

    SELECT p_placa AS Placa, v_capacidade AS Capacidade, v_assentos_ocupados AS Passageiros,
           v_ocupacao AS `Ocupação (%)`, v_desconto AS `Desconto (%)`, v_mensagem AS Mensagem;
END $$

DELIMITER ;

DELIMITER $$
CREATE PROCEDURE DeletarCliente(IN c_cpf VARCHAR(11))
BEGIN
    DELETE FROM Pessoa WHERE CPF = c_cpf;
    DELETE FROM Cliente WHERE CPF = c_cpf;
END $$

DELIMITER ;
