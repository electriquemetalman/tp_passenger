/*question 1*/

SELECT city,state,country
FROM offices
WHERE officeCode=(
	SELECT officeCode
	FROM employees
	GROUP BY officeCode
	ORDER BY COUNT(*) DESC
	LIMIT 0,1);
	
/*question 2*/
	
SELECT YEAR(shippedDate) AS annee, MONTH(shippedDate) AS shippedDate, COUNT(quantityOrdered)
FROM orders
INNER JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
WHERE (STATUS = 'Shipped') AND (shippedDate IS NOT NULL) AND (shippedDate LIKE "2004-%")
GROUP BY shippedDate
ORDER BY shippedDate;
/*ou*/
select Month(orderDate) as mois ,  YEAR(orderDate) as annee,COUNT(orderDate) as nombre
from orders 
GROUP BY Month(orderDate),YEAR(orderDate)

/*question 3*/

SELECT firstName, lastName, COUNT(salesRepEmployeeNumber) AS salesRepEmployeeNumber
FROM employees
INNER JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber
WHERE salesRepEmployeeNumber IS NOT NULL
GROUP BY salesRepEmployeeNumber
ORDER BY COUNT(*) DESC
LIMIT 0,3;

/*determiner le stock total par categorie de produit: qui pourais aider a la decision sur l'aprovisionement*/

SELECT productLine, SUM(quantityInStock)
FROM products
GROUP BY productLine
ORDER BY COUNT(*) DESC

/*determiner les categories de produit les plus consomer*/

SELECT productLine, SUM(quantityOrdered)
FROM products
INNER JOIN orderdetails ON products.productCode = orderdetails.productCode
GROUP BY productLine
ORDER BY COUNT(*) DESC

/*determiner le pays dans le quel on a plus de client*/
SELECT country, COUNT(country)
FROM customers
WHERE country IS NOT NULL 
GROUP BY country
ORDER BY COUNT(*) DESC
