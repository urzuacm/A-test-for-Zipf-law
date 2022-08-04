# A-test-for-Zipf-law

A test statistic for Zipf's law written both in Python and R

## Author

Carlos M. Urzúa, urzuacarlosm@gmail.com

## Description

Given a vector of positive real numbers, the statistic **lmz** proposed in Urzúa (2000) can be used to test for Zipf's law. Since, under the null, **lmz** is asymptotically distributed as a chi-squared with two degrees of freedom, the p-value can be calculated accordingly. But if the number of observations is less or equal than 30, it is suggested to use instead the critical values given in Table 1 of that paper.

## Syntax

## Remarks

* It is not advisable to test for Zipf's law by means of a regression (Urzúa, 2011).

* In a diverse number of disciplines, from Linguistics to Geography, it testing for Zipf's law is a very particular case of of a power-law behavior. If the researcher A good number  The statistical test is locally optimal if the possible alternative distributions are contained in the Pareto Type (IV) family. The last output of the program provides a maximum-likelihood estimate of the shape parameter alpha. If the null hypothesis of power-law behavior cannot be rejected, this estimate may be of some interest. But if the null is rejected, then alpha is not the only parameter that determines the tail of the distribution.

* The **lmz** test is locally optimal if the alternative distributions also exhibit a power-law behavior. More generally, one could try to test first for power-law behavior by means of the **pwlaw** test (Urzúa 2020) which is 

## Bibliography

Urzúa, C. M. 2000. A simple and efficient test for Zipf´s law. *Economics Letters*, vol. 66, pp. 257-260.

Urzúa, C. M. 2011. Testing for Zipf´s law: A common pitfall. *Economics Letters*, vol. 112, pp. 254-255.

Urzúa, C. M. 2020. A simple test for power-law behavior. *Stata Journal*, vol. 20, no. 3, pp. 604-612.
