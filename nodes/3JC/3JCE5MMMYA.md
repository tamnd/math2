---
tag: 3JCE5MMMYA
kind: proof
name: Proof that the complex exponential is entire
msc: [33B10]
proves: 0G2YJN0H5S
uses: [054VXHMCA3, 0VARVQ9ZW1, 045EWAXY9P, 0660QX1VPR, 0PVJRACB9H, 0YMP521ZR5, 0419794R0T]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_function
    locator: Complex exponential
---

## Proof

We show that the exponential series is a power series with infinite radius of convergence.

1. By definition, $\exp z = \sum_{n \ge 0} a_n z^n$ with $a_n = 1/n!$. This is a [[power series|0VARVQ9ZW1]] with center $0$.
2. Its [[radius of convergence|045EWAXY9P]] is $R = \sup \set{r \ge 0 : (r^n / n!)_{n \ge 0} \text{ is bounded}}$.
3. The real series $\sum x^n / n!$ has the same coefficients, and its [[radius of convergence|0660QX1VPR]] is given by the same formula. It is $\infty$, by [[the exponential series has infinite radius of convergence|0PVJRACB9H]].
4. So $R = \infty$, and the disc of convergence is all of $\C$.
5. The sum of the series on this disc is $\exp$, by step 1. By [[power series are holomorphic in the disc of convergence|0YMP521ZR5]], $\exp$ is holomorphic on $\C$.
6. So $\exp$ is complex differentiable at each $z \in \C$. That is, $\exp$ is an [[entire function|0419794R0T]].

## Idea

An entire function is one with a complex derivative everywhere. The exponential is a power series that converges on the whole plane, and power series can be differentiated inside their disc of convergence. So all the work is in the general theorem on power series.
