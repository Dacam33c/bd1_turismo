show databases;
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
DROP TABLE IF EXISTS onibus;
DROP TABLE IF EXISTS Aviao;
DROP TABLE IF EXISTS localDePartida;
DROP TABLE IF EXISTS Plano;
DROP VIEW IF EXISTS Clientes_Transporte;
DROP VIEW IF EXISTS Clientes_Hoteis;
DROP VIEW IF EXISTS Planos_PontosTuristicos;


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
('56789012345', 'Thiago Mendes Rocha', 'Praça da Liberdade, 987, Porto Alegre - RS', '1995-11-05', '(51) 93456-7890');

CREATE TABLE Hotel 
( 
 CNPJ varchar(14) PRIMARY KEY,  
 tipo varchar(100),
 nome varchar(100),  
 endereço varchar(100)
); 
INSERT INTO Hotel (CNPJ, tipo, nome, endereço) VALUES
('12345678000101', 'Hotel 5 Estrelas', 'Grand Palace Hotel', 'Avenida Paulista, 123, São Paulo - SP'),
('23456789000102', 'Resort', 'Paraíso das Águas Resort', 'Rodovia BR-101, Km 200, Florianópolis - SC'),
('34567890000103', 'Pousada', 'Pousada Recanto do Sol', 'Rua das Palmeiras, 456, Porto Seguro - BA'),
('45678901000104', 'Hotel Executivo', 'Blue Tower Business Hotel', 'Rua XV de Novembro, 789, Curitiba - PR'),
('56789012000105', 'Hostel', 'Backpackers Hostel', 'Rua Augusta, 321, São Paulo - SP');


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
('Ilha', 'Ilha Bela');


CREATE TABLE pontoTuristico 
( 
 Nome VARCHAR(100) PRIMARY KEY,  
 preço INT, 
 nomeDestino varchar(100),
 foto LONGBLOB,
 FOREIGN KEY(nomeDestino) REFERENCES Destino (nome)
);
INSERT INTO pontoTuristico (Nome, preço, nomeDestino, foto) VALUES
('Praia do Sancho', 0, 'Fernando de Noronha', NULL),
('Lago Negro', 10, 'Gramado', NULL),
('Museu da Inconfidência', 20, 'Ouro Preto', NULL),
('Avenida Paulista', 0, 'São Paulo', NULL),
('Praia do Curral', 0, 'Ilha Bela', NULL);

CREATE TABLE Transporte 
( 
 Preço INT,  
 DataPartida varchar(100),  
 placa varchar(100),
 Primary key (placa,DataPartida),
 hora varchar(100),
 nomeDestino varchar(100),
 FOREIGN KEY(nomeDestino) REFERENCES Destino (nome)
); 
INSERT INTO Transporte (Preço, DataPartida, placa, hora, nomeDestino) VALUES
(150, '2024-02-10', 'ABC1A23', '08:00', 'Fernando de Noronha'),
(200, '2024-02-15', 'XYZ9B87', '14:30', 'Gramado'),
(120, '2024-02-20', 'LMN3C56', '07:45', 'Ouro Preto'),
(180, '2024-02-25', 'QWE5D67', '16:00', 'São Paulo'),
(90, '2024-03-01', 'RTY7E89', '09:15', 'Ilha Bela');


CREATE TABLE Cliente 
( 
 desconto INT,
 NomeDeUsuario varchar(100) PRIMARY KEY,
 CPF varchar(11),
 FOREIGN KEY (CPF) REFERENCES Pessoa (CPF)
);
INSERT INTO Cliente (desconto, NomeDeUsuario, CPF) VALUES
(10, 'joaosilva', '12345678901'),
(15, 'mariasantos', '23456789012'),
(5, 'pedrosouza', '34567890123'),
(20, 'anacarvalho', '45678901234'),
(8, 'lucasferreira', '56789012345');


CREATE TABLE Guia 
( 
 Preço INT,  
 ID INT AUTO_INCREMENT PRIMARY KEY,
 CPF varchar(11),
 FOREIGN KEY(CPF) REFERENCES Pessoa (CPF),
 nomeDestino varchar(100),
 FOREIGN KEY(nomeDestino) REFERENCES Destino (nome)
);
INSERT INTO Guia (Preço, CPF, nomeDestino) VALUES
(200, '12345678901', 'Fernando de Noronha'),
(150, '23456789012', 'Gramado'),
(180, '34567890123', 'Ouro Preto'),
(120, '45678901234', 'São Paulo'),
(170, '56789012345', 'Ilha Bela');


CREATE TABLE Quarto (
    numero INT,
    preco DECIMAL(10, 2),
    capacidade INT,
    PRIMARY KEY (numero, CNPJHotel),
    CNPJHotel varchar(14),
    FOREIGN KEY (CNPJHotel) REFERENCES Hotel(CNPJ)
);
INSERT INTO Quarto (numero, preco, capacidade, CNPJHotel) VALUES
(101, 250.00, 2, '12345678000101'),
(202, 300.50, 4, '23456789000102'),
(303, 180.75, 3, '34567890000103'),
(404, 400.00, 2, '45678901000104'),
(505, 150.25, 1, '56789012000105');


CREATE TABLE onibus 
( 
 ID INT AUTO_INCREMENT PRIMARY KEY,
 PlacaTransporte varchar(100),
 FOREIGN KEY(PlacaTransporte) REFERENCES Transporte (placa)
);
INSERT INTO onibus (PlacaTransporte) VALUES
('ABC1A23'),
('XYZ9B87'),
('LMN3C56'),
('QWE5D67'),
('RTY7E89');


CREATE TABLE Aviao 
( 
 portao INT,  
 ID INT AUTO_INCREMENT PRIMARY KEY,
  PlacaTransporte varchar(100),
 FOREIGN KEY(PlacaTransporte) REFERENCES Transporte (placa)
);
INSERT INTO Aviao (portao, PlacaTransporte) VALUES
(1, 'ABC1A23'),
(2, 'XYZ9B87'),
(3, 'LMN3C56'),
(4, 'QWE5D67'),
(5, 'RTY7E89');


CREATE TABLE localDePartida 
( 
 Terminal INT,  
 Plataforma INT,
 Primary KEY(Terminal,Plataforma),
 idonibus INT AUTO_INCREMENT,
 FOREIGN KEY(idonibus) REFERENCES onibus (ID)
);
INSERT INTO localDePartida (Terminal, Plataforma, idonibus) VALUES
(1, 5, 1),
(2, 3, 2),
(3, 7, 3),
(4, 1, 4),
(5, 9, 5);


CREATE TABLE Plano
( 
 DataDePartida varchar(100),  
 DataDeRetorno varchar(100),  
 ID INT AUTO_INCREMENT PRIMARY KEY,  
 NomeDeUsuario varchar(100),
 FOREIGN KEY(NomedeUsuario) REFERENCES Cliente (NomeDeUsuario),
 PlacaTransporte varchar(100),
 FOREIGN KEY(PlacaTransporte) REFERENCES Transporte (Placa),
 nomeDestino varchar(100),
 FOREIGN KEY(nomeDestino) REFERENCES Destino (nome),
 CNPJHotel varchar(14),
 FOREIGN KEY(CNPJHotel) REFERENCES Hotel (CNPJ)
);

INSERT INTO Plano (DataDePartida, DataDeRetorno, NomeDeUsuario, PlacaTransporte, nomeDestino, CNPJHotel) VALUES
('2024-03-10', '2024-03-15', 'joaosilva', 'ABC1A23', 'Fernando de Noronha', '12345678000101'),
('2024-02-18', '2024-02-23', 'mariasantos', 'XYZ9B87', 'Gramado', '23456789000102'),
('2024-05-01', '2024-05-07', 'pedrosouza', 'LMN3C56', 'Ouro Preto', '34567890000103'),
('2024-04-05', '2024-04-12', 'anacarvalho', 'QWE5D67', 'São Paulo', '45678901000104'),
('2024-06-10', '2024-06-14', 'lucasferreira', 'RTY7E89', 'Ilha Bela', '56789012000105');

-- VIEWS
CREATE VIEW Clientes_Transporte AS
SELECT 
    Cliente.NomeDeUsuario,
    Cliente.CPF,
    Transporte.Placa AS PlacaTransporte,
    Transporte.DataPartida,
    Transporte.NomeDestino
FROM Cliente
JOIN Plano ON Cliente.NomeDeUsuario = Plano.NomeDeUsuario
JOIN Transporte ON Plano.PlacaTransporte = Transporte.Placa;

CREATE VIEW Clientes_Hoteis AS
SELECT 
    Cliente.NomeDeUsuario,
    Cliente.CPF,
    Hotel.nome AS NomeHotel,
    Hotel.endereço AS EnderecoHotel
FROM Cliente
JOIN Plano ON Cliente.NomeDeUsuario = Plano.NomeDeUsuario
JOIN Hotel ON Plano.CNPJHotel = Hotel.CNPJ;

CREATE VIEW Planos_PontosTuristicos AS
SELECT 
    Plano.ID AS ID_Plano,
    Plano.NomeDeUsuario,
    Plano.DataDePartida,
    Plano.DataDeRetorno,
    Plano.nomeDestino AS Destino,
    pontoTuristico.Nome AS NomePontoTuristico,
    pontoTuristico.preço AS PrecoPontoTuristico
FROM Plano
JOIN pontoTuristico ON Plano.nomeDestino = pontoTuristico.nomeDestino;
