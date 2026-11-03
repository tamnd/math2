---
tag: QE20P81GXX
kind: concept
name: Karoubi–Villamayor K-theory
msc: [19D25]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Summary

Karoubi–Villamayor K-theory assigns to a ring $R$ groups $KV_n(R)$, $n \ge 1$, built from invertible matrices over the rings of polynomial functions on algebraic simplices.
By construction it is homotopy invariant: $KV_n(R[t]) \cong KV_n(R)$.
It agrees with Quillen's [[algebraic K-theory|5GVFZWMWC8]] on regular Noetherian rings, but differs in general.
It was one of the first definitions of higher K-groups, and it shows what part of K-theory survives when polynomial deformations are made trivial.

## Explanations

### L1 human

Two invertible matrices $g_0$ and $g_1$ are joined by a polynomial path if there is an invertible matrix $g(t)$ with polynomial entries in $t$, with $g(0) = g_0$ and $g(1) = g_1$.
In $KV_1$, matrices joined by such a path are identified.
Elementary matrices are joined to the identity by $t \mapsto e_{ij}(ta)$, so $KV_1(R)$ is a quotient of $K_1(R)$.
The higher groups $KV_n$ come from polynomial families of such paths over higher-dimensional simplices, just as higher homotopy groups of a space come from maps of spheres.
