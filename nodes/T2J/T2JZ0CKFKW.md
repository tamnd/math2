---
tag: T2JZ0CKFKW
kind: example
name: Fatou–Bieberbach domain
msc: [32H02, 32M17, 32H50]
illustrates: [FX92PP3HZR, 2J7JB3H3FD]
sources:
  - url: https://en.wikipedia.org/wiki/Fatou%E2%80%93Bieberbach_domain
same_as:
  wikidata: Q1398230
  wikipedia: Fatou–Bieberbach domain
---

## Example

Let $n \ge 2$.
A *Fatou–Bieberbach domain* is an open set $\Omega \subseteq \C^n$ with $\Omega \ne \C^n$ that is [[biholomorphic|FX92PP3HZR]] to $\C^n$.

A concrete one comes from an [[automorphism of $\C^2$|2J7JB3H3FD]].
Let $F(z, w) = (w/2, \, z/2 + w^2)$.
It is a polynomial map with polynomial inverse $(u, v) \mapsto (2v - 8u^2, \, 2u)$, so it is a holomorphic automorphism of $\C^2$.
The origin is a fixed point, and the Jacobian matrix of $F$ there has eigenvalues $1/2$ and $-1/2$.
So the origin is an attracting fixed point.
Let $\Omega$ be its basin of attraction, the set of points $q$ with $F^m(q) \to 0$ as $m \to \infty$.
It is a known theorem that the basin of attraction of an attracting fixed point of a holomorphic automorphism of $\C^n$ is biholomorphic to $\C^n$.
The point $(3/8, 3/4)$ is a second fixed point of $F$, so it is not in $\Omega$.
Hence $\Omega$ is a proper open subset of $\C^2$ biholomorphic to $\C^2$.

## Remarks

No such domain exists in dimension one.
If $\Omega \subsetneq \C$ were biholomorphic to $\C$, then $\Omega$ would be simply connected, so its complement has at least two points.
A biholomorphism $\C \to \Omega$ would then be an entire function omitting two values, hence constant by Picard's little theorem, which is absurd.

## Explanations

### L1 human

In the plane, the whole complex line cannot be squeezed holomorphically and bijectively onto a smaller region.
In two or more complex dimensions this can happen: all of $\C^n$ fits, holomorphically and without distortion of its complex structure, inside a proper part of itself.
The pieces left out can even contain open sets.
This shows how much more flexible holomorphic maps become in several variables.
