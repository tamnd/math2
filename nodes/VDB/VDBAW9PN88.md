---
tag: VDBAW9PN88
kind: concept
name: Generalized hypergeometric function
msc: ["33C20"]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_hypergeometric_function
same_as:
  wikidata: Q109744257
  wikipedia: Generalized hypergeometric function
---

## Summary

The generalized hypergeometric function ${}_pF_q$ is a power series whose coefficient ratio is a rational function of $n$.
That rational function has $p$ numerator parameters and $q$ denominator parameters.
The [[hypergeometric function|463X5V31D9]] ${}_2F_1$ is the case $p = 2$, $q = 1$, and the exponential, the binomial series and the Bessel functions come from smaller $p$ and $q$.
Many classical summation formulas, such as those of Pfaff–Saalschütz, Dixon and Dougall, are evaluations of ${}_3F_2$ and higher series at $z = 1$.

## Explanations

### L1 human

A series $\sum t_n$ is called hypergeometric when the ratio $t_{n+1}/t_n$ of consecutive terms is a rational function of $n$.
After factoring numerator and denominator into linear factors, such a series can be written in a standard form ${}_pF_q$ with $p$ upper and $q$ lower parameters.
For example, $e^z = \sum z^n / n!$ has ratio $\frac{z}{n+1}$, so it is ${}_0F_0(;;z)$.
The numbers $p$ and $q$ control growth: the series is entire when $p \le q$, converges in the unit disc when $p = q + 1$, and diverges when $p > q + 1$, except when it is a polynomial.
