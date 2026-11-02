---
tag: 1S9JGHT5HJ
kind: definition
name: t-structure
msc: [18G80, 14F08]
defines: 2GD9V7SA0E
uses: [T2V7GJJ2EN, ADKK56VZHW, V3BFGKBJF7]
sources:
  - url: https://en.wikipedia.org/wiki/T-structure
---

## Definition

Let $\mathcal{D}$ be a [[triangulated category|T2V7GJJ2EN]] with shift $X \mapsto X[1]$.
A *t-structure* on $\mathcal{D}$ is a pair $(\mathcal{D}^{\le 0}, \mathcal{D}^{\ge 0})$ of [[full subcategories|V3BFGKBJF7]], each closed under isomorphisms.
Write $\mathcal{D}^{\le n} = \mathcal{D}^{\le 0}[-n]$ and $\mathcal{D}^{\ge n} = \mathcal{D}^{\ge 0}[-n]$.
The pair must satisfy:

1. $\mathcal{D}^{\le -1} \subseteq \mathcal{D}^{\le 0}$ and $\mathcal{D}^{\ge 1} \subseteq \mathcal{D}^{\ge 0}$;
2. $\Hom(X, Y) = 0$ for every $X$ in $\mathcal{D}^{\le 0}$ and every $Y$ in $\mathcal{D}^{\ge 1}$;
3. every object $X$ fits into a [[distinguished triangle|ADKK56VZHW]] $A \to X \to B \to A[1]$ with $A$ in $\mathcal{D}^{\le 0}$ and $B$ in $\mathcal{D}^{\ge 1}$.

The *heart* of the t-structure is the full subcategory $\mathcal{D}^{\le 0} \cap \mathcal{D}^{\ge 0}$.

## Remarks

The heart is always an abelian category, and the triangle in clause 3 is unique up to a unique isomorphism; this gives truncation functors $\tau_{\le 0}$ and $\tau_{\ge 1}$.
Example: let $D(\mathcal{A})$ be the derived category of an abelian category, written with cochain complexes.
Its *standard* t-structure has $\mathcal{D}^{\le 0}$ the complexes with $H^i = 0$ for $i > 0$ and $\mathcal{D}^{\ge 0}$ those with $H^i = 0$ for $i < 0$.
The triangle of clause 3 is $\tau_{\le 0} X \to X \to \tau_{\ge 1} X \to$, built from the truncated complexes, and the heart is equivalent to $\mathcal{A}$.
Non-example: if $\mathcal{D} \ne 0$, taking $\mathcal{D}^{\le 0} = \mathcal{D}^{\ge 0} = \mathcal{D}$ fails clause 2, because for $X \ne 0$ the identity of $X$ is a nonzero element of $\Hom(X, X)$, while $X$ lies in both $\mathcal{D}^{\le 0}$ and $\mathcal{D}^{\ge 1} = \mathcal{D}$.
