---
tag: X6ZQPAQF76
kind: statement
role: theorem
name: Inner-outer factorization
msc: [30H10, 30J05]
uses: [PNNNFJVF6W, NN8XH5RJYB, KGJD4A4ATY, 9N6R5ADJXT, 8G5ABXRK85]
about: [PNNNFJVF6W, NN8XH5RJYB, KGJD4A4ATY]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy_space
---

## Statement

Let $0 < p \le \infty$, and let $f$ be a function in the [[Hardy space|PNNNFJVF6W]] $H^p$ of the [[unit disc|8G5ABXRK85]] $\mathbb{D}$, with $f$ not identically $0$.
Then $f = I F$, where $I$ is an [[inner function|NN8XH5RJYB]] and $F$ is an [[outer function|KGJD4A4ATY]] that lies in $H^p$.
The factors are unique up to constants of modulus $1$, and $\abs{F^*} = \abs{f^*}$ almost everywhere on the circle.
Moreover $I = c B S_\mu$, where $\abs{c} = 1$ and $B$ is the [[Blaschke product|9N6R5ADJXT]] of the zeros of $f$, with multiplicity.
The last factor is
$$S_\mu(z) = \exp\left(-\int_0^{2\pi} \frac{e^{it} + z}{e^{it} - z} \, d\mu(t)\right)$$
for a finite positive Borel measure $\mu$ on the circle that is singular with respect to Lebesgue measure.

## Remarks

Proof idea: the zeros of $f$ satisfy the Blaschke condition, by Jensen's formula.
Dividing by their Blaschke product $B$ gives a function $g = f/B$ in $H^p$ with no zeros and the same norm.
The outer function $F$ with modulus $\abs{g^*}$ dominates $g$ in the sense that $\abs{g} \le \abs{F}$, because $\log \abs{g(z)}$ is at most the Poisson integral of $\log \abs{g^*}$ for $g \in H^p$.
Then $g/F$ is bounded, has no zeros and has boundary modulus $1$, and such a function is a singular inner function $c S_\mu$.

Example: $f(z) = z (2 + z)$ is bounded, its inner factor is $z$ and its outer factor is $2 + z$.

The hypothesis $f \not\equiv 0$ is needed, since the zero function has no inner factor.

## Explanations

### L1 human

Every function in a Hardy space splits into two parts.
The outer part is fixed by the size of the function on the boundary circle.
The inner part has size $1$ on the circle and holds the zeros of the function and a hidden "singular" part.
This is the disc analogue of writing a number as a sign times a size.

### L2 human

The factorization is the main structural tool for Hardy spaces.
It reduces many questions to zero-free functions, for which one can take logarithms and roots: for example $f = B g$ with $g$ zero-free gives $g^{p/2} \in H^2$, which transfers results from $H^2$ to $H^p$.
It underlies [[Beurling's theorem|2V1DXXM9FA]] on shift-invariant subspaces, where outer functions are exactly the cyclic vectors of the shift on $H^2$.
The same factorization holds in the [[Nevanlinna class|M3WQTN3FH2]] if one allows quotients of singular inner functions.
