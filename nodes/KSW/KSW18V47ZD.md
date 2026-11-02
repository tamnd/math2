---
tag: KSW18V47ZD
kind: statement
role: theorem
name: Kakeya problem over finite fields
msc: ["51E20", 05B25, 11T06]
uses: [0ZXZ82FTX2, 07GNX8GCYP, 6PEN7AKC7M]
about: [6PEN7AKC7M]
sources:
  - url: https://en.wikipedia.org/wiki/Kakeya_set
---

## Statement

Let $\F_q$ be a [[finite field|0ZXZ82FTX2]] with $q$ elements and let $n \ge 1$.
A *Kakeya set* in $\F_q^n$ is a set $K \subseteq \F_q^n$ such that for every $x \in \F_q^n \setminus \set{0}$ there is $y \in \F_q^n$ with $\set{y + t x : t \in \F_q} \subseteq K$.
Then every Kakeya set $K$ in $\F_q^n$ satisfies
$$\abs{K} \ge \binom{q + n - 1}{n} \ge \frac{q^n}{n!}.$$

## Remarks

This is Dvir's theorem, which answered the finite field analogue of the [[Kakeya problem|6PEN7AKC7M]] asked by Thomas Wolff.
The proof uses the polynomial method.
If $\abs{K} < \binom{q + n - 1}{n}$, the number of monomials of degree at most $q - 1$ in $n$ variables, then some nonzero [[polynomial|07GNX8GCYP]] $P$ of degree $d \le q - 1$ vanishes on $K$.
Let $P_d$ be the top-degree homogeneous part of $P$.
Restricting $P$ to a line $y + t x$ inside $K$ gives a polynomial in $t$ of degree at most $d < q$ with $q$ roots, so it is zero.
Its coefficient of $t^d$ is $P_d(x)$, so $P_d(x) = 0$.
So $P_d$ vanishes on all of $\F_q^n$, which is impossible for a nonzero polynomial of degree less than $q$ in each variable.

For $n = 1$ the bound gives $\abs{K} \ge q$, and indeed $K$ must be the whole line $\F_q$.
For $n = 2$ it gives $\abs{K} \ge q(q + 1)/2$.

## Explanations

### L1 human

A Kakeya set is a set that contains a full line pointing in every direction.
Over the real numbers such sets can have measure zero, which is surprising.
Over a finite field the theorem says the opposite: such a set must contain a fixed positive fraction, about $1/n!$, of all the points of the space.

### L2 human

Dvir's proof is a few lines long and made the polynomial method a standard tool in combinatorics.
The idea is that a set too small cannot avoid being the zero set of a low-degree polynomial, while lines in all directions force the polynomial to vanish identically.
The constant $1/n!$ has since been improved, but the order $q^n$ is optimal.
The finite field result does not solve the Euclidean Kakeya conjecture, whose difficulty comes from the multiscale structure of $\R^n$.
