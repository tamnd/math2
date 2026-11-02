---
tag: MDPRVV9DN9
kind: definition
name: Flat morphism
msc: [14A15, 14B25, 13C11]
defines: 5M6KS8F47R
uses: [JXRKH6P1Z4, JTAKAPTT8H, 73RYYEVDKA, MZ02BKPHJA]
sources:
  - url: https://en.wikipedia.org/wiki/Flat_morphism
---

## Definition

Let $f \colon X \to Y$ be a [[morphism of schemes|JXRKH6P1Z4]].
For a point $x \in X$, let $y = f(x)$, and let $f^\# \colon \mathcal{O}_{Y,y} \to \mathcal{O}_{X,x}$ be the induced map of [[stalks|JTAKAPTT8H]].
These stalks are [[local rings|MZ02BKPHJA]], and $f^\#$ makes $\mathcal{O}_{X,x}$ a module over $\mathcal{O}_{Y,y}$.
The morphism $f$ is *flat at $x$* if $\mathcal{O}_{X,x}$ is a [[flat module|73RYYEVDKA]] over $\mathcal{O}_{Y,y}$.
The morphism $f$ is *flat* if it is flat at every point of $X$.

## Remarks

For a ring $A$, the morphism $\mathbb{A}^n_A \to \operatorname{Spec} A$ is flat.
Each local ring of $\mathbb{A}^n_A$ is a localization of $A[x_1, \dots, x_n]$, which is a free $A$-module, and localizations of flat modules are flat.
For a field $k$, the closed immersion $\operatorname{Spec} k \to \operatorname{Spec} k[t]$ given by $t \mapsto 0$ is not flat.
Its stalk map is $k[t]_{(t)} \to k$, and $k$ is not flat over $k[t]_{(t)}$, since multiplication by $t$ is injective on $k[t]_{(t)}$ but becomes zero on $k$.
For a morphism of affine schemes $\operatorname{Spec} B \to \operatorname{Spec} A$, flatness is equivalent to flatness of $B$ as an $A$-module.
