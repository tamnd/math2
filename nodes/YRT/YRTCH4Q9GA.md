---
tag: YRTCH4Q9GA
kind: definition
name: Order of an entire function
msc: ["30D15", "30D20"]
defines: SHF8Z7GMFX
uses: [0419794R0T, 0P8BA7T7S5, 0VP56B4EMX]
sources:
  - url: https://en.wikipedia.org/wiki/Entire_function
    locator: Order and type
---

## Definition

Let $f$ be an [[entire function|0419794R0T]] that is not constant.
For $r > 0$, let $M(r) = \max_{\abs{z} = r} \abs{f(z)}$.
The *order* of $f$ is
$$\rho = \limsup_{r \to \infty} \frac{\log \log M(r)}{\log r} \in [0, \infty],$$
where $\limsup$ is the [[limit superior|0P8BA7T7S5]].
By convention, constant functions have order $0$.

## Remarks

Equivalently, $\rho$ is the infimum of the numbers $\lambda \ge 0$ such that $M(r) < \exp(r^\lambda)$ for all sufficiently large $r$.
Example: for $f(z) = e^{z^2}$, $M(r) = e^{r^2}$, so $\log \log M(r)/\log r = 2$ and the order is $2$.
Non-example for a bound: $e^{z^2}$ does not satisfy $M(r) < \exp(r^{\lambda})$ for large $r$ when $\lambda < 2$, so its order is not at most $1$.
For a nonconstant polynomial, $\log M(r) \sim d \log r$ with $d$ the degree, so the order is $0$.
In terms of the Taylor coefficients of $f(z) = \sum_n a_n z^n$, the order is $\limsup_{n \to \infty} \dfrac{n \log n}{\log(1/\abs{a_n})}$, where terms with $a_n = 0$ are omitted.
If $0 < \rho < \infty$, the *type* of $f$ is $\sigma = \limsup_{r \to \infty} r^{-\rho} \log M(r)$; functions of order $1$ and finite type, or of order less than $1$, are those of [[exponential type|9P8D8YAHQS]].
