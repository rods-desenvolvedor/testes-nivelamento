SELECT 
  registro_ans,
  SUM(valor_saldo_final) AS total_despesa
FROM 
  tb_demonstracoes_contabeis
WHERE 
  descricao ILIKE '%ASSIST%' AND descricao ILIKE '%HOSPITAL%'
  AND data >= '2024-07-01' AND data <= '2024-09-30'
GROUP BY 
  registro_ans
ORDER BY 
  total_despesa DESC
LIMIT 10;
