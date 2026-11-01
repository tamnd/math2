---
tag: 8DJPSYSHGJ
kind: concept
name: Borel summation
msc: ["40G10", "30E15"]
sources:
  - url: https://en.wikipedia.org/wiki/Borel_summation
same_as:
  wikidata: Q2329388
  wikipedia: Borel summation
---

## Summary

Borel summation is a method that assigns a value to many [[divergent series|0NBRP6093V]], in particular to series whose coefficients grow like factorials.
It divides the $k$-th coefficient by $k!$, sums the resulting convergent series, and recovers the lost factorials with a [[Laplace transform|05XT5AVJBK]].
The method gives the usual sum for every convergent series.
It is a basic tool for the asymptotic series of perturbation theory and of differential equations.

## Explanations

### L1 human

Some series, such as $1 - 1! + 2! - 3! + \cdots$, grow too fast to have a sum in the usual sense.
The identity $k! = \int_0^\infty t^k e^{-t} \, dt$ suggests a trick: replace $k!$ by this integral and exchange sum and integral.
After dividing by $k!$, the series becomes a convergent one, and the integral then gives a finite number.
For this example the Borel sum is $\int_0^\infty e^{-t}/(1+t) \, dt$, about $0.596$.
