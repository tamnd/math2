---
tag: AFQ3HQYEPS
kind: definition
name: Branched covering
msc: [57M12, 30F10]
defines: YARENZRXTD
uses: [5K0N8QMV6Q, T19P7J53A1, 00R0X1WGPX, XP5JC1VXKZ]
sources:
  - url: https://en.wikipedia.org/wiki/Branched_covering
---

## Definition

Let $X$ and $Y$ be [[Riemann surfaces|5K0N8QMV6Q]].
A map $f \colon X \to Y$ is a *(holomorphic) branched covering* if:

1. $f$ is a [[holomorphic map|T19P7J53A1]] that is not constant, and
2. $f$ is proper, that is, $f^{-1}(K)$ is [[compact|00R0X1WGPX]] for every compact $K \subseteq Y$.

A point $x \in X$ is a *ramification point* of $f$ if $f$ is not injective on any neighbourhood of $x$; its image is a *branch point*.

## Remarks

Every branched covering $f$ is surjective, and its ramification points form a closed discrete set $R \subseteq X$.
There is an integer $d \ge 1$, the degree, such that $f$ restricts to a $d$-sheeted covering map from $X \setminus f^{-1}(f(R))$ onto $Y \setminus f(R)$.
Every fibre has exactly $d$ points when counted with multiplicity, where the multiplicity at $x$ is the $k$ such that $f$ looks like $z \mapsto z^k$ near $x$ in suitable charts.
If $X$ is compact, every non-constant holomorphic map $X \to Y$ is a branched covering.
In topology, a branched covering of surfaces is defined in the same way with continuous maps that look locally like $z \mapsto z^k$.

Example: $f \colon \C \to \C$, $f(z) = z^2$.
It is holomorphic and non-constant, and $f^{-1}(K)$ is closed and bounded for compact $K$, since $\abs{z}^2 = \abs{f(z)}$.
Its degree is $2$, its only ramification point is $0$, and the only [[branch point|XP5JC1VXKZ]] is $0$.

Non-example: $\exp \colon \C \to \C$ is holomorphic and non-constant but not proper.
The preimage of the compact set $\set{1}$ is $2\pi i \Z$, which is not compact; clause 2 fails.
