---
tag: R15Z3DPF6A
kind: definition
name: Reduced scheme
msc: [14A15]
defines: ZXSN8D4MCB
uses: [5A35TYZD02, SZHY975FFX, 0ZB2JG1M9C, JTAKAPTT8H]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_algebraic_geometry
---

## Definition

A [[scheme|5A35TYZD02]] $X$ is *reduced* if for every open set $U \subseteq X$ the ring $\mathcal{O}_X(U)$ is a [[reduced ring|SZHY975FFX]].
That is, $\mathcal{O}_X(U)$ has no nonzero [[nilpotent elements|0ZB2JG1M9C]].

## Remarks

Equivalently, every [[stalk|JTAKAPTT8H]] $\mathcal{O}_{X,x}$ is a reduced ring.
An affine scheme $\operatorname{Spec} A$ is reduced if and only if $A$ is reduced.
Example: $\operatorname{Spec} k[x, y]/(xy)$ for a field $k$ is reduced, since $k[x,y]/(xy)$ has no nonzero nilpotents.
Indeed, a power of a polynomial lies in $(xy)$ only if the polynomial itself is divisible by both $x$ and $y$.
Non-example: $\operatorname{Spec} k[x]/(x^2)$ is not reduced, since the class of $x$ is nonzero but $x^2 = 0$.
Every scheme $X$ has a reduced scheme $X_{\mathrm{red}}$ with the same underlying space, obtained by dividing out the nilpotents.
