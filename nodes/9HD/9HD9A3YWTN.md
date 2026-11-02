---
tag: 9HD9A3YWTN
kind: definition
name: Dawson function
msc: ["33B20"]
defines: EQ4QB1QW60
uses: [0J0FCWV32D, 04TMP0XGMJ]
sources:
  - url: https://en.wikipedia.org/wiki/Dawson_function
---

## Definition

The *Dawson function* is the function $F \colon \R \to \R$ given by
$$F(x) = e^{-x^2} \int_0^x e^{t^2}\, dt,$$
where $e$ denotes the [[exponential function|0J0FCWV32D]] and the integral is a [[definite integral|04TMP0XGMJ]].

## Remarks

Example: $F(0) = 0$, and $F$ is odd because $e^{t^2}$ is even.
The product rule gives the differential equation $F'(x) = 1 - 2x F(x)$, with $F(0) = 0$.

Non-example: $x \mapsto e^{x^2} \int_0^x e^{-t^2}\, dt$ is not the Dawson function; the signs of the exponents are swapped, and this function grows without bound.

With the imaginary error function $\operatorname{erfi} x = \frac{2}{\sqrt{\pi}} \int_0^x e^{t^2}\, dt$ one has $F(x) = \frac{\sqrt{\pi}}{2} e^{-x^2} \operatorname{erfi} x$.
For large $x$, $F(x) \sim \frac{1}{2x}$.
Some texts call this $D_+(x)$ and also use $D_-(x) = e^{x^2} \int_0^x e^{-t^2}\, dt$, which is the non-example above.
