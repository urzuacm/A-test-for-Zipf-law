# A-test-for-Zipf-law

A test statistic for Zipf's law written both in Python and R

A test for Zipf's law written both in Pyhton and R.

lmztest [varname] {in} [, option]

mu Only the observations greater than mu are used. 

Description

    Given the column vector varname, lmztest calculates the statistic
    proposed in Urzúa (2000) to test for Zipf's law. Since under the null
    hypothesis LMZ is asymptotically distributed as a chi-squared with two
    degrees of freedom, the p-value is calculated accordingly. But if the
    number of observations is less or equal than 30, it is better to use the
    critical values given in Table 1 of that paper.

Remarks

    It is not advisable to test for Zipf's law by means of a regression
    (Urzúa, 2011). The LMZ test is locally optimal if the alternative
    distributions also exhibit a power-law behavior. More generally, one
    could try to test first for power-law behavior by means of the PWL test
    (Urzúa 2020), which can be calculated using the software program pwlaw
    in the SSC Archive.

Example

    . lmztest uscities, mu(100000)

## Author

Carlos M. Urzúa, urzuacarlosm@gmail.com

## Description

Given a vector of positive real numbers, the statistic **lmztest** proposed in Urzúa (2000) can be used to test for Zipf's law. Since, under the null, **pwlaw** is asymptotically distributed as a chi-squared with two degrees of freedom, the p-value is calculated accordingly. But if the number of observations is less or equal than 100, it is suggested to use instead the critical values given in Table 1 of that paper.

## Notes

* The statistical test is locally optimal if the possible alternative distributions are contained in the Pareto Type (IV) family. The last output of the program provides a maximum-likelihood estimate of the shape parameter alpha. If the null hypothesis of power-law behavior cannot be rejected, this estimate may be of some interest. But if the null is rejected, then alpha is not the only parameter that determines the tail of the distribution.

* If the researcher is interested on testing in particular for Zipf's law, the LMZ test proposed in Urzúa (2000) can be used for that end. It can be calculated using the Pyhton script or the R program in the companion repository A-test-for-zipf's-law.



## Bibliography

Urzúa, C. M. 2000. A simple and efficient test for Zipf´s law. *Economics Letters*, vol. 66, pp. 257-260.

Urzúa, C. M. 2011. Testing for Zipf´s law: A common pitfall. *Economics Letters*, vol. 112, pp. 254-255.

Urzúa, C. M. 2020. A simple test for power-law behavior. *Stata Journal*, vol. 20, no. 3, pp. 604-612.
