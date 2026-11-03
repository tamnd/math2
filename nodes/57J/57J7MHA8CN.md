---
tag: 57J7MHA8CN
kind: concept
name: Derivation of a Lie algebra
msc: [17B40]
specializes: [3J89REV9WQ]
sources:
  - url: https://en.wikipedia.org/wiki/Derivation_(differential_algebra)
---

## Summary

A derivation of a [[Lie algebra|5JJYBJ6A8K]] $\mathfrak g$ is a linear map $D$ on $\mathfrak g$ that obeys the product rule $D[x, y] = [Dx, y] + [x, Dy]$.
It is the special case of a [[derivation|3J89REV9WQ]] of an algebra when the product is the Lie bracket.
The derivations of $\mathfrak g$ form a Lie algebra $\operatorname{Der}(\mathfrak g)$ under the commutator.
The maps $\operatorname{ad}_x = [x, \cdot]$ are derivations, called inner derivations.
For a finite-dimensional semisimple Lie algebra over a field of characteristic $0$, every derivation is inner.

## Explanations

### L1 human

A derivation behaves like differentiation, with the bracket in place of the product.
The rule is the product rule: the derivative of $[x, y]$ is $[Dx, y] + [x, Dy]$.
For any fixed $a$, the map $y \mapsto [a, y]$ satisfies this rule, by the Jacobi identity.
Derivations are the infinitesimal symmetries of the Lie algebra: for a real Lie algebra they are the derivatives at $t = 0$ of smooth families of automorphisms starting at the identity.
