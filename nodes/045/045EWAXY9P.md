---
tag: 045EWAXY9P
kind: definition
name: Disc of convergence
aliases: [disk-of-convergence, radius-of-convergence]
msc: [30B10]
defines: 0CH4VG15RE
uses: [0VARVQ9ZW1]
sources:
  - url: https://en.wikipedia.org/wiki/Radius_of_convergence
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Radius_of_convergence
    locator: Radius of convergence in complex analysis
---

## Definition

Let $\sum_{n \ge 0} a_n (z - c)^n$ be a [[power series|0VARVQ9ZW1]] with center $c \in \mathbb{C}$ and complex coefficients $a_n$.
Its radius of convergence is
$$R = \sup \{ r \ge 0 : \text{the sequence } (|a_n| r^n)_{n \ge 0} \text{ is bounded} \},$$
an element of $[0, \infty]$.
Its disc of convergence is the open disc $D = \{ z \in \mathbb{C} : |z - c| < R \}$. It is empty if $R = 0$, and it is $\mathbb{C}$ if $R = \infty$.

## Remarks

The series converges absolutely at each $z \in D$, and uniformly on each closed disc $|z - c| \le r$ with $r < R$. It diverges at each $z$ with $|z - c| > R$.
The Cauchy–Hadamard formula gives $1/R = \limsup_{n \to \infty} |a_n|^{1/n}$, with $1/0 = \infty$ and $1/\infty = 0$.
On the circle $|z - c| = R$, the series can converge at all points, at some points, or at no point.
For example, $\sum z^n$, $\sum z^n / n$ and $\sum z^n / n^2$ all have $R = 1$. On $|z| = 1$, the first converges nowhere, the second everywhere except at $z = 1$, and the third everywhere.

## Explanations

### L1 human

A power series converges inside a disc around its center and diverges outside the closed disc.
The radius of this disc is the radius of convergence. On the boundary circle, each case is possible.
