CREATE TABLE Pessoa (
    CPF INT PRIMARY KEY,
    endereco varchar(255),
    Nome varchar(100),
    dataDeNascimento DATE,
    telefone varchar(20)
);

CREATE TABLE Hotel 
( 
 CNPJ INT PRIMARY KEY,  
 tipo varchar(255),  
 nome varchar(100),  
 endereço varchar(100)
); 

CREATE TABLE pontoTuristico 
( 
 Nome VARCHAR(100) PRIMARY KEY,  
 preço INT,  
 NomeDestino varchar(100)
); 

CREATE TABLE Destino 
( 
 tipo varchar(100),  
 nome varchar(100) PRIMARY KEY
); 

CREATE TABLE Transporte 
( 
 Preço INT,  
 Data INT PRIMARY KEY,  
 placa INT PRIMARY KEY,  
 hora INT,  
 NomeDestino INT,  
); 

CREATE TABLE Cliente 
( 
 desconto INT,  
 Nome de usuário INT PRIMARY KEY,  
 CPF INT,  
); 

CREATE TABLE Guia 
( 
 Preço INT,  
 CPF INT,  
 ID INT PRIMARY KEY,  
 nomeDestino INT,  
); 

CREATE TABLE quarto 
( 
 número INT PRIMARY KEY,  
 preço INT,  
 capacidade INT,  
 CNJPHotel INT,  
); 

CREATE TABLE Plano 
( 
 Data de partida INT,  
 Data de retorno INT,  
 ID INT PRIMARY KEY,  
 NomedeUsuarioCliente INT,  
 PlacaTransporte INT,  
 nomeDestino INT,  
 CNPJHotel INT,  
); 

CREATE TABLE ônibus 
( 
 PlacaTransporte INT PRIMARY KEY,  
 ID INT PRIMARY KEY,  
); 

CREATE TABLE Avião 
( 
 portão INT,  
 PlacaTransporte INT,  
 ID INT PRIMARY KEY,  
); 

CREATE TABLE local de partida 
( 
 idônibus INT,  
 Terminal INT PRIMARY KEY,  
 Plataforma INT PRIMARY KEY,  
); 

ALTER TABLE ponto turístico ADD FOREIGN KEY(NomeDestino) REFERENCES Pessoa (NomeDestino)
ALTER TABLE Transporte ADD FOREIGN KEY(NomeDestino) REFERENCES Pessoa (NomeDestino)
ALTER TABLE Cliente ADD FOREIGN KEY(CPF) REFERENCES Pessoa (CPF)
ALTER TABLE Guia ADD FOREIGN KEY(CPF) REFERENCES Pessoa (CPF)
ALTER TABLE Guia ADD FOREIGN KEY(nomeDestino) REFERENCES Pessoa (nomeDestino)
ALTER TABLE quarto ADD FOREIGN KEY(CNJPHotel) REFERENCES Pessoa (CNJPHotel)
ALTER TABLE Plano ADD FOREIGN KEY(NomedeUsuarioCliente) REFERENCES Pessoa (NomedeUsuarioCliente)
ALTER TABLE Plano ADD FOREIGN KEY(PlacaTransporte) REFERENCES Pessoa (PlacaTransporte)
ALTER TABLE Plano ADD FOREIGN KEY(nomeDestino) REFERENCES Pessoa (nomeDestino)
ALTER TABLE Plano ADD FOREIGN KEY(CNPJHotel) REFERENCES Pessoa (CNPJHotel)
ALTER TABLE ônibus ADD FOREIGN KEY(PlacaTransporte) REFERENCES Pessoa (PlacaTransporte)
ALTER TABLE Avião ADD FOREIGN KEY(PlacaTransporte) REFERENCES Pessoa (PlacaTransporte)
ALTER TABLE local de partida ADD FOREIGN KEY(idônibus) REFERENCES ônibus (idônibus)