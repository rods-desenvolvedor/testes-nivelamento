-- Importar dados das demonstrações contábeis
COPY tb_demonstracoes_contabeis
FROM '/dados/1T2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'LATIN1';

COPY tb_demonstracoes_contabeis
FROM '/dados/2T2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'LATIN1';

COPY tb_demonstracoes_contabeis
FROM '/dados/3T2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'LATIN1';

COPY tb_demonstracoes_contabeis
FROM '/dados/4T2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'LATIN1';

COPY tb_demonstracoes_contabeis
FROM '/dados/1T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'LATIN1';

COPY tb_demonstracoes_contabeis
FROM '/dados/2T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'LATIN1';

COPY tb_demonstracoes_contabeis
FROM '/dados/3T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'LATIN1';

COPY tb_demonstracoes_contabeis
FROM '/dados/4T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'LATIN1';


COPY operadoras_ativas
FROM '/dados/Relatorio_cadop.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'LATIN1';
