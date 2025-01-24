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
 FOREIGN KEY(NomeDestino) REFERENCES Destino (nome)
); 

CREATE TABLE Destino 
( 
 tipo varchar(100),  
 nome varchar(100) PRIMARY KEY
); 

CREATE TABLE Transporte 
( 
 Preço INT,  
 DataPartida varchar(100) PRIMARY KEY,  
 placa varchar(100) PRIMARY KEY,  
 hora varchar(100),  
 FOREIGN KEY(NomeDestino) REFERENCES Destino (nome)
); 

CREATE TABLE Cliente 
( 
 desconto INT,
 NomeDeUsuario INT PRIMARY KEY,  
 FOREIGN KEY (CPF) REFERENCES Pessoa (CPF)
); 

CREATE TABLE Guia 
( 
 Preço INT,  
 ID INT PRIMARY KEY,  
 FOREIGN KEY(CPF) REFERENCES Pessoa (CPF),
 FOREIGN KEY(nomeDestino) REFERENCES Destino (nome)
); 

CREATE TABLE quarto 
( 
 número INT PRIMARY KEY,  
 preço INT,  
 capacidade INT,  
 FOREIGN KEY(CNJPHotel) REFERENCES Hotel (CNPJ)
); 

CREATE TABLE Plano
( 
 DataDePartida varchar(100),  
 DataDeRetorno varchar(100),  
 ID INT PRIMARY KEY,  
 FOREIGN KEY(NomedeUsuario) REFERENCES Cliente (NomeDeUsuario),
 FOREIGN KEY(PlacaTransporte) REFERENCES Transporte (Placa),
 FOREIGN KEY(nomeDestino) REFERENCES Destino (nome),
 FOREIGN KEY(CNPJHotel) REFERENCES Hotel (CNPJ)
); 

CREATE TABLE onibus 
( 
 ID INT PRIMARY KEY,
 FOREIGN KEY(PlacaTransporte) REFERENCES Transporte (placa)
); 

CREATE TABLE Aviao 
( 
 portao INT,  
 ID INT PRIMARY KEY,
 FOREIGN KEY(PlacaTransporte) REFERENCES Transporte (placa)
); 

CREATE TABLE localDePartida 
( 
 idonibus INT,  
 Terminal INT PRIMARY KEY,  
 Plataforma INT PRIMARY KEY,
 FOREIGN KEY(idonibus) REFERENCES onibus (ID)
); 