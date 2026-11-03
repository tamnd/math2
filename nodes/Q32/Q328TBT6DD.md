---
tag: Q328TBT6DD
kind: definition
name: Cayley–Dickson construction
msc: [17A75, 17A45]
defines: T9XW7RBEHY
uses: [1SENAHZW5A, GP56NBN9RY]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Dickson_construction
---

## Definition

Let $K$ be a field and let $B$ be a unital [[algebra|1SENAHZW5A]] over $K$.
Let $x \mapsto \bar{x}$ be a $K$-linear [[involution|GP56NBN9RY]] of $B$ with $\overline{xy} = \bar{y}\bar{x}$ and $\bar{1} = 1$.
Let $\mu \in K$ with $\mu \neq 0$.
The *Cayley–Dickson double* $\mathrm{CD}(B, \mu)$ is the vector space $B \oplus B$ with the product
$$(a, b)(c, d) = (ac + \mu \bar{d} b,\; da + b\bar{c})$$
and the involution $\overline{(a, b)} = (\bar{a}, -b)$.

## Remarks

The element $(1, 0)$ is a unit, and $B$ embeds as the pairs $(a, 0)$.
The element $\ell = (0, 1)$ satisfies $\ell^2 = (\mu, 0)$.
If $B$ has a norm with $x\bar{x} = N(x)1$, then $\mathrm{CD}(B, \mu)$ has the norm $N(a, b) = N(a) - \mu N(b)$.
Example: $B = \R$ with the identity involution and $\mu = -1$ gives $(a, b)(c, d) = (ac - bd, da + bc)$, the product of $a + bi$ and $c + di$ in $\C$.
Repeating with $\mu = -1$ gives the quaternions, the octonions and the sedenions; taking $\mu = 1$ at some step gives split forms.
Non-example: the identity map of the quaternions is not an allowed involution, since $\overline{ij} = k$ while $\bar{j}\bar{i} = ji = -k$.
Sign and order conventions for the product vary between authors.
