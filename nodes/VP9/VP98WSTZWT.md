---
tag: VP98WSTZWT
kind: concept
name: Logarithmic integral
msc: ["33E20", "11N05"]
sources:
  - url: https://en.wikipedia.org/wiki/Logarithmic_integral_function
same_as:
  wikidata: Q1350206
  wikipedia: Logarithmic integral function
---

## Summary

The logarithmic integral is $\operatorname{li}(x) = \int_0^x \frac{dt}{\ln t}$, taken as a principal value at $t = 1$.
By the [[prime number theorem|0EHBY5Y84N]], it is asymptotic to, and an excellent approximation of, the [[prime-counting function|0RQSNVTFVZ]] $\pi(x)$.
The offset version $\operatorname{Li}(x) = \int_2^x \frac{dt}{\ln t}$ avoids the singularity at $1$.
It is the [[exponential integral|EV6ZDQ0NDY]] composed with the logarithm: $\operatorname{li}(x) = \operatorname{Ei}(\ln x)$.

## Explanations

### L1 human

Near a large number $t$, about one number in $\ln t$ is prime.
Adding up these densities from $2$ to $x$ gives the integral $\int_2^x \frac{dt}{\ln t}$.
So the logarithmic integral predicts how many primes there are up to $x$.
For $x = 10^6$ the prediction is about $78\,627$, while the true count is $78\,498$.
