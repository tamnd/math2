---
tag: 4EJED0YZBB
kind: concept
name: C-infinity ring
msc: [58A03, 18F40, 51K10]
sources:
  - url: https://en.wikipedia.org/wiki/Synthetic_differential_geometry
---

## Summary

A $C^\infty$-ring is a set on which every [[smooth function|0V33BNKZ9S]] $f \colon \R^n \to \R$ acts as an $n$-ary operation, compatibly with composition.
The basic example is the ring $C^\infty(M)$ of smooth functions on a [[smooth manifold|F45VQ47GPV]], where the operations are composition with $f$.
Every $C^\infty$-ring is in particular a commutative $\R$-algebra, but it also knows how to apply $\exp$, $\sin$ and all other smooth functions.
$C^\infty$-rings play for smooth manifolds the role that commutative rings play in algebraic geometry, and they give models of synthetic differential geometry.

## Explanations

### L1 human

In a ring one can add and multiply, so one can plug elements into polynomials.
In a $C^\infty$-ring one can plug elements into any smooth function, such as $e^x$ or $\sin(x + y)$.
For functions on a manifold this is natural: if $a$ and $b$ are smooth functions, so is $\sin(a + b)$.
Rings of germs and rings such as $\R[\varepsilon]/(\varepsilon^2)$, with $\varepsilon^2 = 0$, are also $C^\infty$-rings, and they let one treat infinitesimal points algebraically.
