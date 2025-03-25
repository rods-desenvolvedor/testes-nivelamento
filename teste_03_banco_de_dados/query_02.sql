SELECT 
  registro_ans,
  SUM(valor_saldo_final) AS total_despesa
FROM 
  tb_demonstracoes_contabeis
WHERE 
  descricao ILIKE '%ASSIST%' AND descricao ILIKE '%HOSPITAL%'
  AND EXTRACT(YEAR FROM data) = 2024
GROUP BY 
  registro_ans
ORDER BY 
  total_despesa DESC
LIMIT 10;
