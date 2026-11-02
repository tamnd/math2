---
tag: XP21V9TVKK
kind: definition
name: Dehn twist
msc: [57K20, 57R50]
defines: W890NRHGS4
uses: [VGJJVBZ1MQ, 0TD904MG06, 0QT00PB5G2, JV5NYG913V]
sources:
  - url: https://en.wikipedia.org/wiki/Dehn_twist
---

## Definition

Let $A = S^1 \times [0, 1]$ be the annulus, with $S^1 = \R / 2\pi\Z$ and the orientation of the $(\theta, t)$-plane.
The *twist map* $T \colon A \to A$ is $T(\theta, t) = (\theta + 2\pi t, t)$; it is the identity on both boundary circles.

Let $S$ be an oriented [[surface|VGJJVBZ1MQ]] and let $c$ be a simple closed curve in the interior of $S$.
Choose an orientation-preserving embedding $\varphi \colon A \to S$ with $\varphi(S^1 \times \set{1/2}) = c$.
The *Dehn twist* about $c$ is the [[homeomorphism|0QT00PB5G2]] $T_c \colon S \to S$ given by
$$T_c(x) = \begin{cases} \varphi \circ T \circ \varphi^{-1}(x) & \text{if } x \in \varphi(A), \\ x & \text{otherwise.} \end{cases}$$

## Remarks

The isotopy class of $T_c$ does not depend on the choice of $\varphi$.
It depends only on the isotopy class of $c$, and it is an element of the [[mapping class group|JV5NYG913V]] of $S$.
Its definition does not depend on an orientation of $c$, but it does depend on the orientation of $S$: reversing it replaces $T_c$ by its inverse.

Example: on the torus $T^2 = \R^2 / \Z^2$, let $c$ be the image of the horizontal line.
The Dehn twist $T_c$ acts on $H_1(T^2; \Z) = \Z^2$ by the matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, up to the sign convention.
Since this matrix has infinite order, $T_c$ has infinite order in the mapping class group.

Non-example: if $c$ bounds a disc in $S$, then $T_c$ is isotopic to the identity, so it is trivial in the mapping class group.
And on a non-orientable surface, a curve whose neighbourhood is a Möbius strip has no annulus neighbourhood, so no Dehn twist about it is defined.

## Explanations

### L1 human

Cut the surface along the curve, rotate one side through a full turn, and glue it back.
To make this continuous, the rotation is spread over a thin band, from no rotation on one edge to a full turn on the other.
Every curve that crosses the band picks up one extra lap around $c$.
