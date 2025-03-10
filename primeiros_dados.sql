-- Active: 1731016514374@@127.0.0.1@3306

INSERT INTO cliente (id_cliente, nome_completo, email, num_telefone, senha)  -- senha = password
VALUES (0001, 'Ana Soares', 'soares.ana@hotmail.com', '921459270', 'ana_soares123'),
(0002, 'João Almeida', 'joao.almeida@gmail.com', 921234567, 'joao1234!'),
(0003, 'Maria Santos', 'maria.santos@outlook.com', 926543210, 'maria@2023'),
(0004, 'António Costa', 'antonio.costa@hotmail.com', 923456789, 'costa#987'),
(0005, 'Catarina Silva', 'catarina.silva@live.com', 924567890, 'silvaCat@22'),
(0006, 'Pedro Oliveira', 'pedro.oliveira@yahoo.com', 927654321, 'oliveiraP456'),
(0007, 'Ana Pereira', 'ana.pereira@icloud.com', 922345678, 'anaPereira@99'),
(0008, 'José Rodrigues', 'jose.rodrigues@gmail.com', 925678910, 'rodrigues*321'),
(0009, 'Rita Fernandes', 'rita.fernandes@outlook.com', 929876543, 'fernandes@12'),
(0010, 'Tiago Monteiro', 'tiago.monteiro@gmail.com', 928765432, 'monteiro#789'),
(0011, 'Inês Sousa', 'ines.sousa@hotmail.com', 923123456, 'sousa!in34');

INSERT INTO imoveis (id_imovel, tipo_imovel, num_quartos, endereco, area_metragem, num_banheiros, cidade, valor_mensalidade)
VALUES (5501, 'Apartamento', 2, 'Rua das Flores 123', '80m²', 1, 'Lisboa', 850.00),
(5502, 'Casa', 4, 'Avenida da Liberdade 45', '200m²', 3, 'Porto', 1500.00),
(5503, 'Estúdio', 1, 'Rua da Saudade 10', '35m²', 1, 'Coimbra', 500.00),
(5504, 'Moradia', 3, 'Estrada de Sintra 98', '150m²', 2, 'Sintra', 1200.00),
(5505, 'Apartamento', 3, 'Rua do Comércio 65', '100m²', 2, 'Braga', 900.00),
(5506, 'Casa', 5, 'Rua do Sol 25', '250m²', 3, 'Faro', 1800.00),
(5507, 'Estúdio', 1, 'Avenida do Mar 77', '40m²', 1, 'Cascais', 600.00),
(5508, 'Apartamento', 2, 'Rua do Jardim 12', '75m²', 1, 'Leiria', 700.00),
(5509, 'Moradia', 4, 'Rua da Serra 30', '180m²', 3, 'Évora', 1400.00),
(5510, 'Apartamento', 1, 'Rua das Oliveiras 56', '50m²', 1, 'Setúbal', 600.00),
(5511, 'Apartamento', 2, 'Avenida da República 101', '90m²', 2, 'Lisboa', 950.00),
(5512, 'Casa', 3, 'Rua das Laranjeiras 25', '160m²', 2, 'Albufeira', 1300.00),
(5513, 'Estúdio', 1, 'Rua Nova 14', '30m²', 1, 'Aveiro', 450.00),
(5514, 'Moradia', 5, 'Largo do Palácio 8', '300m²', 4, 'Sintra', 2200.00),
(5515, 'Apartamento', 1, 'Rua dos Anjos 78', '55m²', 1, 'Porto', 650.00),
(5516, 'Casa', 4, 'Rua da Praia 32', '210m²', 3, 'Cascais', 1700.00),
(5517, 'Estúdio', 1, 'Rua do Campo 47', '35m²', 1, 'Funchal', 550.00),
(5518, 'Moradia', 3, 'Rua da Vitória 29', '170m²', 2, 'Viseu', 1100.00),
(5519, 'Apartamento', 3, 'Avenida Central 99', '120m²', 2, 'Braga', 950.00),
(5520, 'Casa', 6, 'Rua da Montanha 14', '400m²', 5, 'Guimarães', 2500.00),
(5521, 'Estúdio', 1, 'Rua das Oliveiras 76', '40m²', 1, 'Coimbra', 480.00),
(5522, 'Apartamento', 2, 'Rua do Mercado 34', '85m²', 1, 'Faro', 800.00),
(5523, 'Moradia', 4, 'Rua dos Ciprestes 52', '250m²', 3, 'Évora', 1450.00),
(5524, 'Apartamento', 2, 'Rua do Porto 15', '95m²', 2, 'Leiria', 720.00),
(5525, 'Casa', 3, 'Largo das Rosas 44', '180m²', 2, 'Tomar', 1100.00);

SELECT * FROM imoveis;