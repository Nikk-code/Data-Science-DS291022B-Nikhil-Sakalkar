-- create
CREATE TABLE SalesPeople (
Snum INT,
Sname VARCHAR(255) UNIQUE,
City VARCHAR(255),
Comm DECIMAL(5,2),
PRIMARY KEY(Snum)
);

CREATE TABLE Customers (
Cnum INT,
Cname VARCHAR(255),
City VARCHAR(255) NOT NULL,
Snum INT,
PRIMARY KEY(Cnum),
FOREIGN KEY (Snum) REFERENCES SalesPeople(Snum)
);

CREATE TABLE Orders (
Onum INT,
Amt DECIMAL(10,2),
Odate DATE,
Cnum INT,
Snum INT,
PRIMARY KEY(Onum),
FOREIGN KEY (Cnum) REFERENCES Customers(Cnum),
FOREIGN KEY (Snum) REFERENCES SalesPeople(Snum)
);



-- insert

INSERT INTO SalesPeople VALUES 
       (1001, 'Peel', 'London', 0.12),
       (1002, 'Serres', 'Sanjose', 0.13),
       (1004, 'Motika', 'London', 0.11),
       (1007, 'Rifkin', 'Barcelona', 0.15),
       (1003, 'Axelrod', 'Newyork', 0.10);


INSERT INTO Customers VALUES 
       (2001, 'Hoffman', 'London', 1001),
       (2002, 'Giovanni', 'Rome', 1003),
       (2003, 'Liu', 'Sanjose', 1002),
       (2004, 'Grass', 'Berlin', 1002),
       (2006, 'Clemens', 'London', 1001),
       (2008, 'Cisneros', 'Sanjose', 1007),
       (2007, 'Pereira', 'Rome', 1004);
          
          
INSERT INTO Orders VALUES 
       (3001, 18.69, '1990-10-03', 2008, 1007),
       (3003, 767.19, '1990-10-03', 2001, 1001),
       (3002, 1900.10, '1990-10-03', 2007, 1004),
       (3005, 5160.45, '1990-10-03', 2003, 1002),
       (3006, 1098.16, '1990-10-03', 2008, 1007),
       (3009, 1713.23, '1990-10-04', 2002, 1003),
       (3007, 75.75, '1990-10-04', 2004, 1002),
       (3008, 4273.00, '1990-10-05', 2006, 1001),
       (3010, 1309.95, '1990-10-06', 2004, 1002),
       (3011, 9891.88, '1990-10-06', 2006, 1001);
       
-- fetch 
SELECT COUNT(*) FROM SalesPeople WHERE Sname LIKE 'A%' OR Sname LIKE 'a%';
SELECT Sname FROM SalesPeople WHERE Snum IN (SELECT Snum FROM Orders GROUP BY Snum HAVING SUM(Amt) > 2000);
SELECT COUNT(*) FROM SalesPeople WHERE City = 'Newyork';
SELECT COUNT(*) FROM SalesPeople WHERE City IN ('London', 'Paris');
SELECT Sname, COUNT(Onum), GROUP_CONCAT(DATE(Odate)) FROM SalesPeople
JOIN Orders ON SalesPeople.Snum = Orders.Snum
GROUP BY Sname;
