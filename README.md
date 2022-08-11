# A-test-for-Zipf-law

A test statistic for Zipf's law written both in Python and R

## Author

Carlos M. Urzúa, urzuacarlosm@gmail.com

## Description

Given a vector *x* of positive real numbers, the statistic **lmz** proposed in Urzúa (2000) can be used to test for Zipf's law. Under the null, **lmz** is asymptotically distributed as a chi-squared distribution with two degrees of freedom, and so the p-value can be estimated accordingly. But if the number of observations is less or equal than 30, it is suggested to use instead the critical values given in Table 1 of that paper.

The vector *x* does not need to be ordered, and only the observations greater or equal than a given value of *mu* are used to compute the statistic. This is handy because Zipf's law is typically rejected when *mu* (>= minimum element of *x*) is not close to the right-hand side tail of the distribution. Contrast the two examples given in the last section of Urzúa (2000).  

## Syntax

* In the case of both the Python script *lmz.py* and the R program *lmz.R* included in this repository the call 

## Notes

* It is not advisable to test for Zipf's law by means of a regression (Urzúa, 2011).

* In a diverse number of disciplines, from Linguistics to Geography, it is not uncommon to test for Zipf's law. It is worth noticing, however, that such a law is a limit case among the distributions that exhibit a power-law behavior. To test for that behavior the **pwlaw** statistic proposed in Urzúa (2020) can be used. The repository https://github.com/urzuacarlosm/A-test-for-power-law 

## Bibliography

Urzúa, C. M. 2000. A simple and efficient test for Zipf´s law. *Economics Letters*, vol. 66, pp. 257-260.

Urzúa, C. M. 2011. Testing for Zipf´s law: A common pitfall. *Economics Letters*, vol. 112, pp. 254-255.

Urzúa, C. M. 2020. A simple test for power-law behavior. *Stata Journal*, vol. 20, no. 3, pp. 604-612.
