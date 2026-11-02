---
tag: 2KVA0Q66RE
kind: definition
name: Morse–Bott function
msc: [57R70, "58E05"]
defines: 47096P24SB
uses: [F45VQ47GPV, 0V33BNKZ9S, 0YTCMFB4HC, MGPPCDFQDG]
sources:
  - url: https://en.wikipedia.org/wiki/Morse_theory
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] and let $f \colon M \to \R$ be a [[smooth function|0V33BNKZ9S]] with set of [[critical points|0YTCMFB4HC]] $\operatorname{Crit}(f) = \set{p \in M : df_p = 0}$.
The function $f$ is a *Morse–Bott function* if:

1. each connected component of $\operatorname{Crit}(f)$ is a closed submanifold of $M$; and
2. for each $p \in \operatorname{Crit}(f)$, the kernel of the Hessian $\operatorname{Hess}_p f$ on $T_p M$ equals $T_p C$, where $C$ is the component of $\operatorname{Crit}(f)$ through $p$.

## Remarks

The Hessian is defined at critical points as in the definition of a [[nondegenerate critical point|MGPPCDFQDG]].
Since $f$ is constant on each component $C$, the Hessian always vanishes on $T_p C$; the second condition says it is nondegenerate on the normal space $T_p M / T_p C$.
The *index* of a critical component is the number of negative directions of the Hessian on this normal space.
A [[Morse function|KPQ96640ZJ]] is a Morse–Bott function whose critical components are points.

Example: $f(x, y) = x^2$ on $\R^2$ has $\operatorname{Crit}(f) = \set{x = 0}$, a line.
At $(0, y)$ the Hessian matrix is $\operatorname{diag}(2, 0)$, whose kernel is spanned by $\partial_y$, the tangent direction of the line; so $f$ is Morse–Bott, with critical line of index $0$.

Non-example: $g(x, y) = x^4$ also has $\operatorname{Crit}(g) = \set{x = 0}$, a submanifold, but its Hessian at $(0, y)$ is $0$.
Its kernel is all of $\R^2$, not the tangent line, so the second condition fails.
Another non-example is $h(x, y) = x^2 y^2$, whose critical set is the union of the two axes, which is not a submanifold near the origin.
