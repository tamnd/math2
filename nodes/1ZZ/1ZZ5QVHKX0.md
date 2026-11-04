---
tag: 1ZZ5QVHKX0
kind: proof
name: Proof that the complex exponential is its own derivative
msc: [33B10]
proves: 019H1Z6419
uses: [054VXHMCA3, 045EWAXY9P, 0PVJRACB9H, 0YMP521ZR5, 0D1C9Y1EXA]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_function
    locator: Complex exponential
---

## Proof

We differentiate the exponential series term by term.

1. By definition, $\exp z = \sum_{n \ge 0} a_n z^n$ with $a_n = 1/n!$, for each $z \in \C$.
2. The [[radius of convergence|045EWAXY9P]] of this series is $\sup \set{r \ge 0 : (r^n/n!)_{n \ge 0} \text{ is bounded}}$. This is the formula for the real series $\sum x^n/n!$, whose radius is $\infty$ by [[the exponential series has infinite radius of convergence|0PVJRACB9H]]. So the disc of convergence is $\C$.
3. By [[power series are holomorphic in the disc of convergence|0YMP521ZR5]], $\exp$ is [[complex differentiable|0D1C9Y1EXA]] at each $z \in \C$, and
$$\exp'(z) = \sum_{n=1}^{\infty} n a_n z^{n-1} = \sum_{n=1}^{\infty} \frac{n}{n!} z^{n-1}.$$
4. For $n \ge 1$ we have $n / n! = 1/(n-1)!$.
5. Put $m = n - 1$. The series becomes $\sum_{m=0}^{\infty} z^m / m!$, which is $\exp z$.
6. So $\exp'(z) = \exp z$ for each $z \in \C$.

## Idea

Differentiating $z^n/n!$ gives $z^{n-1}/(n-1)!$, the previous term of the same series. So term-by-term differentiation only shifts the index. The theorem on power series makes term-by-term differentiation legal.
