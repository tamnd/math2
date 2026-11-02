---
tag: R123NEWYZR
kind: definition
name: Smooth morphism
msc: [14A15, 14B25]
defines: EXKGG9X6J0
uses: [JXRKH6P1Z4, 5M6KS8F47R, 963QWX2E2Z, ESPG0BJERZ, 764GZHTGV8]
sources:
  - url: https://en.wikipedia.org/wiki/Smooth_morphism
---

## Definition

Let $f \colon X \to Y$ be a [[morphism of schemes|JXRKH6P1Z4]].
The morphism $f$ is *smooth* if it satisfies the following three conditions.

1. $f$ is locally of finite presentation.
This means that, for all affine opens $\operatorname{Spec} B \subseteq X$ and $\operatorname{Spec} A \subseteq Y$ with $f(\operatorname{Spec} B) \subseteq \operatorname{Spec} A$, the $A$-algebra $B$ is [[finitely presented|764GZHTGV8]].
2. $f$ is [[flat|5M6KS8F47R]].
3. For every $y \in Y$ with residue field $\kappa(y)$, the [[fiber|963QWX2E2Z]] $X_y$ is geometrically regular over $\kappa(y)$.
This means that $X_y \times_{\kappa(y)} \operatorname{Spec} \overline{\kappa(y)}$ is a [[regular scheme|ESPG0BJERZ]], where $\overline{\kappa(y)}$ is an algebraic closure of $\kappa(y)$.

## Remarks

For a ring $A$, the projection $\mathbb{A}^n_A \to \operatorname{Spec} A$ is smooth.
It is of finite presentation and flat, and each fibre is affine space over a field, which stays regular over the algebraic closure.
For a field $k$, the morphism $X = \operatorname{Spec} k[x, y]/(y^2 - x^3) \to \operatorname{Spec} k$ is not smooth.
Clause 3 fails, since the local ring at the origin has maximal ideal $(x, y)$, which needs two generators while the curve has dimension one.
Equivalently, $f$ is smooth of relative dimension $n$ if and only if three conditions hold.
It is flat and locally of finite presentation, its nonempty fibres have pure dimension $n$, and $\Omega_{X/Y}$ is locally free of rank $n$.
The ring version of this notion is a [[smooth morphism of rings|286G0P1B69]].
