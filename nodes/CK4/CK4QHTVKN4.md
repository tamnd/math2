---
tag: CK4QHTVKN4
kind: definition
name: Space of functions of bounded variation
msc: [26A45, "46E99"]
defines: 9YQ999QHHT
uses: [A8251BHCMP, 8QA5DEWNYD, 03J5RAKB30]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_variation
---

## Definition

Let $a < b$ be real numbers.
The *space of functions of bounded variation* $BV([a, b])$ is the set of functions $f \colon [a, b] \to \R$ of [[bounded variation|A8251BHCMP]], with pointwise operations.
Its norm is
$$\norm{f}_{BV} = \abs{f(a)} + V_a^b(f),$$
where $V_a^b(f)$ is the [[total variation|8QA5DEWNYD]] of $f$ on $[a, b]$.

## Remarks

This is a [[normed space|03J5RAKB30]].
The variation is subadditive and $V_a^b(t f) = \abs{t} V_a^b(f)$, which gives the triangle inequality and homogeneity.
If $\norm{f}_{BV} = 0$, then $V_a^b(f) = 0$, so $f$ is constant, and $f(a) = 0$ gives $f = 0$.
The space is complete, so it is a Banach space.

Example: $f(x) = x$ on $[0, 1]$.
It is increasing, so $V_0^1(f) = f(1) - f(0) = 1$ and $\norm{f}_{BV} = 0 + 1 = 1$.

Non-example: $f(x) = x \sin(1/x)$ for $0 < x \le 1$, with $f(0) = 0$.
It is continuous on $[0, 1]$, but its total variation is infinite, so it is not in $BV([0, 1])$.

An equivalent norm is $\sup_{x} \abs{f(x)} + V_a^b(f)$.
