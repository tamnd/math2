---
tag: VT9QWDTKA4
kind: definition
name: Normalization
msc: [14A15, 13B22, 14B05]
defines: M2FAMD9HZN
uses: [17NVR4XBHK, EK261G1XP9, JXRKH6P1Z4, G0V86SJBQW, 0F2PTGX1A2, ABVBHCA9VW]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_scheme
---

## Definition

Let $X$ be an [[integral scheme|17NVR4XBHK]] with function field $K$.
For each open affine subscheme $U = \operatorname{Spec} A$ of $X$, let $\tilde{A}$ be the [[integral closure|G0V86SJBQW]] of $A$ in its [[field of fractions|0F2PTGX1A2]] $K$.
The *normalization* of $X$ is the integral scheme $\tilde{X}$ with a [[morphism|JXRKH6P1Z4]] $\nu \colon \tilde{X} \to X$ such that, for every such $U$:

1. $\nu^{-1}(U)$ is isomorphic to $\operatorname{Spec} \tilde{A}$;
2. under this isomorphism, $\nu$ restricted to $\nu^{-1}(U)$ is the morphism $\operatorname{Spec} \tilde{A} \to \operatorname{Spec} A$ induced by the inclusion $A \subseteq \tilde{A}$.

It is obtained by [[gluing|ABVBHCA9VW]] the schemes $\operatorname{Spec} \tilde{A}$, and it is unique up to unique isomorphism over $X$.

## Remarks

The scheme $\tilde{X}$ is [[normal|EK261G1XP9]].
For every normal integral scheme $Z$ and every dominant morphism $f \colon Z \to X$, there is a unique morphism $g \colon Z \to \tilde{X}$ with $f = \nu \circ g$.
Example: let $A = k[x, y]/(y^2 - x^3) \cong k[t^2, t^3]$ over a field $k$, with $x = t^2$ and $y = t^3$.
Its fraction field is $k(t)$, and $t$ is integral over $A$ since $t^2 = x$; also $k[t]$ is integrally closed, so $\tilde{A} = k[t]$.
The normalization of the cusp is $\mathbb{A}^1_k \to \operatorname{Spec} A$, $t \mapsto (t^2, t^3)$.
Non-example: the identity morphism of the cusp is not its normalization, since the cusp is not normal and $A \ne \tilde{A}$.
If $X$ is normal, then $\nu$ is an isomorphism.
