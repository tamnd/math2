---
tag: EV6ZDQ0NDY
kind: concept
name: Exponential integral
msc: ["33B20", "33E20"]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_integral
same_as:
  wikidata: Q1419948
  wikipedia: Exponential integral
---

## Summary

The exponential integrals are the functions $E_1(x) = \int_x^\infty \frac{e^{-t}}{t}\, dt$ for $x > 0$ and $\operatorname{Ei}(x)$, the principal value of $\int_{-\infty}^x \frac{e^t}{t}\, dt$ for $x \ne 0$.
They are related by $E_1(x) = -\operatorname{Ei}(-x)$ for $x > 0$, and $E_1(x)$ is the [[upper incomplete gamma function|YB7ZV0HG7K]] $\Gamma(0, x)$.
The [[logarithmic integral|VP98WSTZWT]] is $\operatorname{li}(x) = \operatorname{Ei}(\ln x)$.
They occur in heat transfer, in groundwater flow and in radiative transfer.

## Explanations

### L1 human

The function $e^t / t$ has no antiderivative made from elementary functions.
The exponential integral gives a name to its antiderivative, fixed by a choice of starting point.
The function $E_1(x)$ is the area under $e^{-t}/t$ to the right of $x$; it is large near $0$ and very small for large $x$.
Near $0$ it behaves like $-\ln x$, because $e^{-t}/t$ is close to $1/t$ there.
