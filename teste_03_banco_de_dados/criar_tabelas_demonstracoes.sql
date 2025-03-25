DROP TABLE IF EXISTS tb_demonstracoes_contabeis;

CREATE TABLE tb_demonstracoes_contabeis (
    data DATE,
    registro_ans VARCHAR(10),
    codigo_conta_contabil VARCHAR(20),
    descricao TEXT,
    valor_saldo_inicial NUMERIC,
    valor_saldo_final NUMERIC
);
