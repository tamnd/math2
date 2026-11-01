---
tag: SHFJH5JZ5P
kind: definition
name: Siegel zero
msc: [11M20, 11M26]
defines: 5VBZBXSFDQ
uses: [7XB5VJKDPG, 9D2Z543EJQ, DNKA4WBKDS]
sources:
  - url: https://en.wikipedia.org/wiki/Siegel_zero
---

## Definition

There is an absolute constant $c > 0$ with the following property.
Let $q \ge 3$ be an integer and $\chi$ a [[Dirichlet character|7XB5VJKDPG]] modulo $q$.
Then the [[Dirichlet L-function|9D2Z543EJQ]] $L(s, \chi)$ has no zero $s = \sigma + it$ in the region
$$\sigma \ge 1 - \frac{c}{\log\big(q(\abs{t} + 2)\big)}.$$
The one possible exception is a single zero when $\chi$ is a real nonprincipal character; such a zero is real and simple.
Fix such a constant $c$.
A *Siegel zero* (or *exceptional zero*) for the modulus $q$ is a real number $\beta$ with
$$1 - \frac{c}{\log q} < \beta < 1 \quad\text{and}\quad L(\beta, \chi) = 0$$
for some real nonprincipal character $\chi$ modulo $q$.

## Remarks

No Siegel zero is known, so there is no example to check.
If the [[generalized Riemann hypothesis|DNKA4WBKDS]] holds, every zero of $L(s, \chi)$ in the strip $0 < \operatorname{Re} s < 1$ has real part $1/2$, so for large $q$ no Siegel zero exists.
A non-example: a zero of $L(s, \chi)$ for a character $\chi$ that is not real is never a Siegel zero, because the zero-free region has no exception for such $\chi$.
Siegel's theorem bounds a possible exceptional zero: for every $\varepsilon > 0$ there is $c(\varepsilon) > 0$ with $\beta < 1 - c(\varepsilon) q^{-\varepsilon}$, but $c(\varepsilon)$ is not effectively computable.
The notion depends on the choice of $c$; statements about Siegel zeros are usually about a sequence of moduli $q$ with $(1 - \beta)\log q \to 0$.
