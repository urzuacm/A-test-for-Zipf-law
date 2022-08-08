# A-test-for-Zipf-law

A test statistic for Zipf's law written both in Python and R

## Author

Carlos M. Urzúa, urzuacarlosm@gmail.com

## Description

Given a vector *x* of positive real numbers, the statistic **lmz** proposed in Urzúa (2000) can be used to test for Zipf's law. Since, under the null, **lmz** is asymptotically distributed as a chi-squared distribution with two degrees of freedom, the p-value is calculated accordingly. But if the number of observations is less or equal than 30, it is suggested to use instead the critical values given in Table 1 of that paper.

The statistic will be computed 

## Syntax

* In the case of both the Python script **lmz.py** and R program , included in this repository, the   in this repository 

## 

* It is not advisable to test for Zipf's law by means of a regression (Urzúa, 2011).

* In a diverse number of disciplines, from Linguistics to Geography, it is not uncommon to test for Zipf's law. It is worth noticing, however, that such a law is a limit case among the distributions that exhibit a power-law behavior. If the reader wants to check first if the data  A good number. The **lmz** test is locally optimal if the alternative distributions also exhibit a power-law behavior. More generally, one could try to test first for power-law behavior by means of the **pwlaw** test (Urzúa 2020), which can be found in the repository https://github.com/urzuacarlosm/A-test-for-power-law

## Examples



## Bibliography

Urzúa, C. M. 2000. A simple and efficient test for Zipf´s law. *Economics Letters*, vol. 66, pp. 257-260.

Urzúa, C. M. 2011. Testing for Zipf´s law: A common pitfall. *Economics Letters*, vol. 112, pp. 254-255.

Urzúa, C. M. 2020. A simple test for power-law behavior. *Stata Journal*, vol. 20, no. 3, pp. 604-612.
