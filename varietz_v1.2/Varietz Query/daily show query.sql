SELECT * FROM varietz_test_v1.daily;

set sql_mode= ' ';

select rnk,style ,product,brand,price,mrp,pic_url,pic_url
from daily 
where Article_Type = 'Tops'
having rnk > 10
limit 20;

call get_bs_results('Tops');
select * from daily;
select d.Style,count(d.Style) from daily d group by d.Style;


select rnk,style ,product,brand,price,mrp,pic_url,pic_url,comp, count(comp)
from daily 
where Article_Type = 'tops'
and comp = 'LR'
having rnk < 10

union 

select rnk,style ,product,brand,price,mrp,pic_url,pic_url,comp,count(comp)
from daily 
where Article_Type = 'tops'
and comp = 'Myntra'
group by style
having rnk < 10
order by rnk
limit 40
;

select * from 
(select  distinct (style) ,rnk,product,brand,price,mrp,pic_url as aurl,pic_url as aurl2,comp
from daily 
where Article_Type = 'tops'
and comp = 'LR'
having rnk < 10
order by rnk
limit 20)
union
(select distinct (style) ,rnk ,product,brand,price,mrp,pic_url as burl,pic_url as burl2,comp
from daily 
where Article_Type = 'tops'
and comp = 'Myntra'
having rnk < 10
order by rnk
limit 20)
;
