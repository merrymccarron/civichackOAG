select year, count(*) FROM ( 
    SELECT  extract(year from Date1_10) as year
    FROM Sun_Boe_Efsrecbs       
    WHERE  Transaction_Code IN ('A','B','C','D','G','P') 
    AND Date1_10 BETWEEN TO_DATE ('1999/01/01', 'yyyy/mm/dd') AND TO_DATE ('2014/12/31', 'yyyy/mm/dd')
) y
GROUP by year
ORDER BY year;