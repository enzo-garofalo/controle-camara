-- Tabela para tipos de produto
CREATE TABLE TIPO
(
  ID_TIPO NUMBER(10) PRIMARY KEY,
  DESCRICAO VARCHAR2(50) NOT NULL
);

-- Tabela para produtos
CREATE TABLE SORVETES
(
  ID_PRODUTO NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) PRIMARY KEY,
  TIPO NUMBER(10) NOT NULL,
  NOME VARCHAR2(50) NOT NULL,
  QUANTIDADE NUMBER(10),
  FOREIGN KEY (TIPO) REFERENCES TIPO(ID_TIPO)
);

DROP TABLE SORVETES;
DELETE FROM TIPO;

-- Inserir tipos de produto
INSERT INTO tipo(ID_TIPO, DESCRICAO) VALUES (1, 'Pote 1 litro');
INSERT INTO tipo(ID_TIPO, DESCRICAO) VALUES (2, 'Pote 2 litros');
INSERT INTO tipo(ID_TIPO, DESCRICAO) VALUES (3, 'Picolé');
INSERT INTO tipo(ID_TIPO, DESCRICAO) VALUES (4, 'Bombom');

INSERT INTO SORVETES (TIPO_ID, NOME, QUANTIDADE) VALUES(2, 'leite', 0);
COMMIT;

SELECT s.NOME, t.DESCRICAO 
FROM SORVETES s
JOIN TIPO t ON s.TIPO = t.ID_TIPO
WHERE s.TIPO = 2;

SELECT * FROM SORVETES;

UPDATE TIPO 
SET descricao = '2 Litros' 
WHERE id_tipo = 2;