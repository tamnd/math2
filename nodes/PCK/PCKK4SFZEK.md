---
tag: PCKK4SFZEK
kind: concept
name: Skew group ring
msc: [16S35, 16W22]
specializes: [D1SA8CHJV0]
sources:
  - url: https://en.wikipedia.org/wiki/Crossed_product
---

## Summary

The skew group ring $R * G$ of a group $G$ acting on a [[ring|0B1261B5ED]] $R$ by automorphisms is like the [[group ring|4NMTSX0XDS]] $R[G]$.
The difference is that group elements and coefficients do not commute: $g r = g(r) g$.
It is the algebraic counterpart of the C*-algebra [[crossed product|8HG8TS46A6]].
It turns a [[group action|0WCY42EV9V]] on a ring into a single ring, and its modules are the $R$-modules with a compatible action of $G$.
It is used in invariant theory, Galois theory of rings and the representation theory of finite groups.

## Explanations

### L1 human

Start with a ring $R$ and a group $G$ that moves the elements of $R$ around by symmetries.
Form sums $\sum r_g g$ as in the group ring.
When a group element passes a coefficient from left to right, it acts on it: $g r = g(r) g$.
If every $g \in G$ acts as the identity map of $R$, then $g r = r g$ for all $g$ and $r$, and this is the group ring.
For the complex numbers with complex conjugation, the skew group ring is the ring of $2 \times 2$ real matrices.
