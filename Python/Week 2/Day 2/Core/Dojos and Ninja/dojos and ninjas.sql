select * from dojos ;
insert into dojos (name)
values  ("benmoussa") ,("ouslati "), ("mraad");
DELETE from dojos 
WHERE id=1 or id=2  or id =3 ; 
insert into ninjas (first_name,last_name,age,dojo_id)
value ("walid","benmoussa",24,5),("ouslati","amine",23,6),("irad","mraad",27,7);
SELECT *
FROM ninjas
WHERE dojo_id = 5;
SELECT *
FROM ninjas
WHERE dojo_id = 7;
SELECT  * 
FROM ninjas
 LIMIT  1 ;
 SELECT  * 
FROM ninjas
 LIMIT  3 ;
 SELECT  * 
FROM ninjas
 LIMIT  3 ;
 SELECT  * 
FROM ninjas
 where dojo_id = 7 ;
 SELECT * FROM ninjas
JOIN dojos ON dojo_id = ninjas.dojo_id

