---
tag: 00EHX6FWC0
kind: definition
name: Root of a polynomial
msc: [13F20]
defines: 019MA1VTR2
uses: [0GJ7T0NK49]
sources:
  - url: https://en.wikipedia.org/wiki/Zero_of_a_function
    locator: Polynomial roots
---

## Definition

Let $R$ be a [[ring|0894J980RK]] and let $f \in R[x]$.
An element $c \in R$ is a root of $f$ if $f(c) = 0$, where $f(c)$ is the [[value of $f$ at $c$|0GJ7T0NK49]].

## Remarks

The roots of $x^2 - 1$ in $\mathbb{Z}$ are $1$ and $-1$.
The polynomial $x^2 + 1$ has no root in $\mathbb{R}$. It has the roots $i$ and $-i$ in $\mathbb{C}$.
By the [[factor theorem|0K3MWA7DMC]], over a commutative ring, $c$ is a root of $f$ if and only if $x - c$ divides $f$.

## Explanations

### L1 human

A root is a solution of the equation $f(x) = 0$.
Whether a polynomial has a root depends on the ring: $x^2 - 2$ has no root in $\mathbb{Q}$, but it has the root $\sqrt{2}$ in $\mathbb{R}$.
