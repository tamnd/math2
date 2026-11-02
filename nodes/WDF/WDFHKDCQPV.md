---
tag: WDFHKDCQPV
kind: definition
name: Complex measure
msc: [28A10]
defines: NY6TYHRGMS
uses: [N4KDT83V3S, D7KB9HFCGZ, 09FTAET5Z4, VG2P7R91Z7]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_measure
---

## Definition

Let $(X, \Sigma)$ be a [[measurable space|N4KDT83V3S]].
A *complex measure* on $(X, \Sigma)$ is a map $\nu \colon \Sigma \to \C$ with the following property.
For every sequence $(E_n)$ of pairwise disjoint sets in $\Sigma$,
$$\nu\Big( \bigcup_{n} E_n \Big) = \sum_{n} \nu(E_n),$$
where the series of [[complex numbers|09FTAET5Z4]] converges.

## Remarks

Taking all $E_n = \emptyset$ gives $\nu(\emptyset) = 0$.
The left side does not depend on the order of the $E_n$, so every rearrangement of the series converges to the same value, and the series converges absolutely.

Example: let $\mu$ be a measure and $f \in L^1(\mu)$ complex-valued.
Then $\nu(E) = \int_E f \, d\mu$ is a complex measure; countable additivity follows from the dominated convergence theorem with dominating function $\abs{f}$.

Non-example: Lebesgue measure on $\R$ is not a complex measure, because $\lambda(\R) = \infty$ is not a complex number.

Writing $\nu = \nu_r + i \nu_i$, the real and imaginary parts $\nu_r$ and $\nu_i$ are finite [[signed measures|VG2P7R91Z7]].
Integration against $\nu$ is defined by $\int f \, d\nu = \int f \, d\nu_r + i \int f \, d\nu_i$.
