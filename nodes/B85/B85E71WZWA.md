---
tag: B85E71WZWA
kind: definition
name: Fuzzy algebraic structure
msc: [08A72, 20N25, "03E72"]
defines: FSRST924GR
uses: [QJGPT2W0FT, 0EPAT51DXQ, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Fuzzy_set
---

## Definition

Let $A$ be an [[algebra|QJGPT2W0FT]] in which every operation has arity at least $1$.
A *fuzzy subset* of $A$ is a [[function|0EPAT51DXQ]] $\mu \colon A \to [0, 1]$; the number $\mu(a)$ is the degree of membership of $a$.
A fuzzy subset $\mu$ is a *fuzzy subalgebra* of $A$ if
$$\mu(f(a_1, \dots, a_n)) \ge \min\set{\mu(a_1), \dots, \mu(a_n)}$$
for every operation $f$ of $A$ of arity $n$ and all $a_1, \dots, a_n \in A$.
For a [[group|G5S1M9]] $G$ with the operations $(x, y) \mapsto xy$ and $x \mapsto x^{-1}$, a fuzzy subalgebra is a *fuzzy subgroup*: $\mu(xy) \ge \min\set{\mu(x), \mu(y)}$ and $\mu(x^{-1}) \ge \mu(x)$ for all $x, y \in G$.

## Remarks

A fuzzy subset $\mu$ is a fuzzy subalgebra if and only if each level set $\mu_t = \set{a \in A : \mu(a) \ge t}$, for $t \in [0, 1]$, is empty or a subalgebra.
Indeed, if $a_1, \dots, a_n \in \mu_t$ then $\min_i \mu(a_i) \ge t$; conversely, apply the condition on $\mu_t$ with $t = \min_i \mu(a_i)$.
A fuzzy subset that takes only the values $0$ and $1$ is a fuzzy subalgebra exactly when $\set{a : \mu(a) = 1}$ is empty or a subalgebra.

Example: on the group $(\Z, +)$ let $\mu(n) = 1$ for even $n$ and $\mu(n) = 1/2$ for odd $n$.
If $m$ or $n$ is odd, the minimum is $1/2$ and $\mu(m + n) \ge 1/2$ holds; if both are even, $m + n$ is even and $\mu(m + n) = 1$.
Also $-n$ has the parity of $n$, so $\mu(-n) = \mu(n)$.
So $\mu$ is a fuzzy subgroup.

Non-example: on $(\Z, +)$ let $\mu(1) = 1$ and $\mu(n) = 0$ for $n \ne 1$.
Then $\mu(1 + 1) = 0 < 1 = \min\set{\mu(1), \mu(1)}$, so $\mu$ is not a fuzzy subgroup.
