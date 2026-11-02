---
tag: ZD73KPKPJ4
kind: definition
name: Birational map
msc: ["14E05"]
defines: KA5890R9YM
uses: [HV6YBS0YDH, 4D073CCYGV, CDS1VWB7A3, 2D5SS6WM14, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Birational_geometry
---

## Definition

Let $X$ and $Y$ be [[algebraic varieties|HV6YBS0YDH]] over an algebraically closed field $k$.
A *birational map* $\varphi \colon X \dashrightarrow Y$ is a [[rational map|4D073CCYGV]] that has an inverse: a rational map $\psi \colon Y \dashrightarrow X$ such that $\psi \circ \varphi = \id_X$ and $\varphi \circ \psi = \id_Y$ as rational maps.
Here $\varphi$ and $\psi$ are required to be dominant, so that the compositions are defined.
$X$ and $Y$ are *birational*, or birationally equivalent, if there is a birational map $X \dashrightarrow Y$.

## Remarks

Equivalently, there are nonempty [[open subsets|02BH3MCBQB]] $U \subseteq X$ and $V \subseteq Y$ and an isomorphism of varieties $U \to V$ (a [[morphism|CDS1VWB7A3]] with inverse morphism).
Also equivalently, there is an isomorphism of $k$-algebras between the [[function fields|2D5SS6WM14]] $k(Y)$ and $k(X)$.

Example: $\mathbb{A}^2$ and $\mathbb{P}^2$ are birational, since $\mathbb{A}^2$ is isomorphic to the open subset $\set{z \ne 0}$ of $\mathbb{P}^2$.
They are not isomorphic, since every regular function on $\mathbb{P}^2$ is constant and $\mathbb{A}^2$ has the nonconstant regular function $x$.

Example: the conic $C = V(x^2 + y^2 - 1) \subseteq k^2$, with $\operatorname{char} k \ne 2$, is birational to $\mathbb{A}^1$ through $t \mapsto \left(\frac{1 - t^2}{1 + t^2}, \frac{2t}{1 + t^2}\right)$, whose inverse is $(x, y) \mapsto y/(1 + x)$.

Non-example: the rational map $\mathbb{P}^2 \dashrightarrow \mathbb{P}^1$, $[x : y : z] \mapsto [x : y]$, is dominant but not birational, since $\dim \mathbb{P}^2 = 2 \ne 1 = \dim \mathbb{P}^1$ and birational varieties have the same dimension.
