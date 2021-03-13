select * from sentencedb;
select * from exercisedetails;
select * from score_details;
select * from accounts;
SET SQL_SAFE_UPDATES=0;
delete from sentencedb where exerciseid>=134;
delete from exercisedetails where exerciseid=67;
insert into sentencedb values(0," "," "," "," ","0 "," ");
update sentencedb set displayorder=0 where exerciseid>=119;
select max(rid) from exercisedetails where nattempts=2
create table score_details(userid INT,username VARCHAR (20),exerciseid INT,score INT,category VARCHAR(20),duration time,maxattempts INT);      
select max(nattempts) from exercisedetails where exerciseid=1 and userid=8;
ALTER TABLE exercisedetails MODIFY response1 VARCHAR(500);
SELECT * FROM sentencedb ORDER BY exerciseid DESC LIMIT 1;