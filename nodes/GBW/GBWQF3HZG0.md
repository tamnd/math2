---
tag: GBWQF3HZG0
kind: concept
name: Ring of differential operators
msc: [16S32, 13N10]
specializes: [D1SA8CHJV0]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_operator
---

## Summary

The ring of differential operators $D(A)$ of a commutative algebra $A$ over a field $k$ is a ring of $k$-linear maps $A \to A$.
Its elements behave like linear differential operators of finite order.
Grothendieck's definition uses only commutators with multiplication maps, so it makes sense for any commutative algebra, without coordinates.
For the polynomial ring $k[x_1, \dots, x_n]$ in characteristic $0$ it is the [[Weyl algebra|98QE7KY55W]] $A_n(k)$.
Its modules, called $D$-modules, are a tool for studying linear partial differential equations by algebra.

## Explanations

### L1 human

A differential operator such as $f \mapsto x^2 f'' + 3 f'$ combines multiplications by functions with derivatives.
Commuting such an operator with a multiplication by a function lowers its order by one, by the product rule.
An operator of order $0$ is just a multiplication, and the definition builds the higher orders from there.
For polynomials in one variable over the rationals, every such operator is a finite sum $\sum_{j} a_j(x) \, d^j/dx^j$ with polynomial coefficients $a_j$.
