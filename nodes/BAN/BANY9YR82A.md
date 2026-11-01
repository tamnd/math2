---
tag: BANY9YR82A
kind: statement
role: theorem
name: Lagrange inversion theorem
msc: [05A15, 30B10]
uses: [033WGN00BF, 0R0D0XY4HT, 0PHAC833JF]
about: [033WGN00BF, 0PHAC833JF]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_inversion_theorem
same_as:
  wikidata: Q544292
  wikipedia: Lagrange inversion theorem
---

## Statement

Let $K$ be a field of characteristic $0$.
Let $\phi(w) \in K[\![w]\!]$ be a [[formal power series|033WGN00BF]] with $\phi(0) \ne 0$.
Then there is a unique formal power series $T(z) \in K[\![z]\!]$ with $T(0) = 0$ and $T(z) = z\, \phi(T(z))$.
For every $H(w) \in K[\![w]\!]$ and every integer $n \ge 1$,
$$[z^n]\, H(T(z)) = \frac{1}{n} [w^{n-1}]\, H'(w)\, \phi(w)^n,$$
where $[z^n] F$ is the [[coefficient|0R0D0XY4HT]] of $z^n$ in $F$.
In particular, $[z^n]\, T(z) = \frac{1}{n} [w^{n-1}]\, \phi(w)^n$.

## Remarks

Proof idea: work with formal Laurent series, where the coefficient of $w^{-1}$ in a derivative is always $0$.
Change the variable from $z$ to $w = T(z)$, so $z = w / \phi(w)$.
The coefficient of $z^{-1}$ in $z^{-n-1} H(T(z))$ becomes a coefficient of $w^{-1}$, and an integration by parts gives the formula.

Example: rooted labelled trees have the exponential [[generating function|0PHAC833JF]] $T(z) = z e^{T(z)}$.
With $\phi(w) = e^w$, the theorem gives $[z^n] T = \frac{1}{n} \cdot \frac{n^{n-1}}{(n-1)!} = \frac{n^{n-1}}{n!}$.
So there are $n^{n-1}$ [[rooted trees|0Y0JGC2K9T]] on $n$ labelled vertices.

Example: with $\phi(w) = (1 + w)^2$, the series $T$ counts binary trees by internal nodes.
The theorem gives $[z^n] T = \frac{1}{n} \binom{2n}{n-1}$, which is the [[Catalan number|0YWZJEABB2]] $C_n$.

The hypothesis $\phi(0) \ne 0$ makes the problem meaningful.
If $\phi(0) = 0$, then $T = 0$ is the only solution with $T(0) = 0$, and the equation counts nothing.
Characteristic $0$ is used to divide by $n$.
There is also an analytic version for holomorphic $\phi$ near $0$, which then gives the Taylor series of the inverse function.

## Explanations

### L1 human

Many counting problems lead to an equation of the form $T = z\, \phi(T)$ for a generating function $T$.
Such an equation is usually hard to solve for $T$ in closed form.
Lagrange inversion gives the coefficients of $T$ directly, without solving the equation.
One only has to expand the power $\phi(w)^n$ and read off one coefficient.

### L2 human

The theorem is the main tool for counting trees and tree-like structures.
A family of rooted trees defined by the allowed numbers of children has a generating function with $T = z\, \phi(T)$, where $\phi$ records the allowed numbers of children.
In the [[symbolic method|JP11D90EJC]] such equations arise at once from the recursive description of the trees.
The form with $H$ counts forests, since a sequence of $k$ trees has generating function $T^k$.
Equivalently, the theorem computes the coefficients of the compositional inverse of $z / \phi(z)$.
