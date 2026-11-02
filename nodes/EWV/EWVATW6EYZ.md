---
tag: EWVATW6EYZ
kind: definition
name: Transversality
msc: [57R35, 57N75]
defines: A2PDZ8GA9C
uses: [F45VQ47GPV, VKFW27WXEZ, 6P9PXQDSEN]
sources:
  - url: https://en.wikipedia.org/wiki/Transversality
---

## Definition

Let $X$ and $Y$ be [[smooth manifolds|F45VQ47GPV]], let $Z \subseteq Y$ be an [[embedded submanifold|VKFW27WXEZ]], and let $f \colon X \to Y$ be a smooth map.
The map $f$ is *transverse* to $Z$, written $f \pitchfork Z$, if for every $x \in X$ with $f(x) \in Z$,
$$df_x(T_xX) + T_{f(x)}Z = T_{f(x)}Y,$$
where $df_x$ is the [[differential|6P9PXQDSEN]] of $f$ at $x$.
Two embedded submanifolds $A, B \subseteq Y$ are *transverse*, written $A \pitchfork B$, if $T_pA + T_pB = T_pY$ for every $p \in A \cap B$; this is transversality of the inclusion $A \to Y$ to $B$.

## Remarks

The condition is empty where $f(X)$ misses $Z$, so a map whose image avoids $Z$ is transverse to $Z$.
If $Z$ is a point $y$, then $f \pitchfork \set{y}$ means that $y$ is a regular value of $f$.
If $f \pitchfork Z$, then $f^{-1}(Z)$ is an embedded submanifold of $X$ with $\dim X - \dim f^{-1}(Z) = \dim Y - \dim Z$.
Example: in $\R^2$ the $x$-axis and the line $y = x$ are transverse at the origin, since their directions $(1, 0)$ and $(1, 1)$ span $\R^2$.
Non-example: the $x$-axis and the parabola $y = x^2$ meet at the origin, where both tangent lines equal the $x$-axis, which does not span $\R^2$; so they are not transverse.
