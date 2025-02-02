show databases;
CREATE DATABASE turismo;
use turismo;

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
 tipo varchar(100),
 nome varchar(100),  
 endereço varchar(100)
); 

CREATE TABLE Destino 
( 
 tipo varchar(100),  
 nome varchar(100) PRIMARY KEY
); 

CREATE TABLE pontoTuristico 
( 
 Nome VARCHAR(100) PRIMARY KEY,  
 preço INT, 
 nomeDestino varchar(100),
 FOREIGN KEY(nomeDestino) REFERENCES Destino (nome)
); 

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

CREATE TABLE Cliente 
( 
 desconto INT,
 NomeDeUsuario varchar(100) PRIMARY KEY,
 CPF INT,
 FOREIGN KEY (CPF) REFERENCES Pessoa (CPF)
); 

CREATE TABLE Guia 
( 
 Preço INT,  
 ID INT AUTO_INCREMENT PRIMARY KEY,
 CPF INT,
 FOREIGN KEY(CPF) REFERENCES Pessoa (CPF),
 nomeDestino varchar(100),
 FOREIGN KEY(nomeDestino) REFERENCES Destino (nome)
); 

CREATE TABLE Quarto (
    numero INT,
    preco DECIMAL(10, 2),
    capacidade INT,
    PRIMARY KEY (numero, CNPJHotel),
    CNPJHotel INT,
    FOREIGN KEY (CNPJHotel) REFERENCES Hotel(CNPJ)
);

CREATE TABLE onibus 
( 
 ID INT AUTO_INCREMENT PRIMARY KEY,
 PlacaTransporte varchar(100),
 FOREIGN KEY(PlacaTransporte) REFERENCES Transporte (placa)
); 

CREATE TABLE Aviao 
( 
 portao INT,  
 ID INT AUTO_INCREMENT PRIMARY KEY,
  PlacaTransporte varchar(100),
 FOREIGN KEY(PlacaTransporte) REFERENCES Transporte (placa)
); 

CREATE TABLE localDePartida 
( 
 Terminal INT,  
 Plataforma INT,
 Primary KEY(Terminal,Plataforma),
 idonibus INT AUTO_INCREMENT,
 FOREIGN KEY(idonibus) REFERENCES onibus (ID)
); 

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
 CNPJHotel INT,
 FOREIGN KEY(CNPJHotel) REFERENCES Hotel (CNPJ)
); 