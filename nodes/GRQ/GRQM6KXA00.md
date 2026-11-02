---
tag: GRQM6KXA00
kind: definition
name: (∞,1)-category
msc: [18N60]
defines: YFY1FWA1MY
uses: [9328WEVJEK, BPH9SJ30Y0, FDFYCM3YYC, WW81ARB8K9, SDTZVZ6B4Q]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-category
---

## Definition

An *$(\infty,1)$-category* is a higher category with $k$-morphisms for every $k \ge 1$, in which every $k$-morphism with $k \ge 2$ is invertible.
This informal notion is made precise by a choice of model; the most used one is the following.
In the quasi-categorical model, an $(\infty,1)$-category is a [[quasi-category|9328WEVJEK]]: a [[simplicial set|WW81ARB8K9]] in which every inner horn $\Lambda^n_k \to X$, $0 < k < n$, extends to the $n$-simplex $\Delta^n$.

## Remarks

Other standard models are:

1. simplicial categories, that is, categories [[enriched|BPH9SJ30Y0]] over simplicial sets, whose hom-objects are all [[Kan complexes|FDFYCM3YYC]];
2. complete Segal spaces, which are certain simplicial objects in simplicial sets;
3. Segal categories.

Each model carries a [[model category|SDTZVZ6B4Q]] structure, and these model categories are connected by Quillen equivalences, so the models give the same homotopy theory of $(\infty,1)$-categories.
Example: the nerve of an ordinary category is a quasi-category, so every category is an $(\infty,1)$-category with only identity higher morphisms.
Example: Kan complexes are the $(\infty,1)$-categories in which every morphism is invertible, the $\infty$-groupoids.
Non-example: $\mathbf{Cat}$, viewed as a strict $2$-category, is not an $(\infty,1)$-category in its own right.
It has non-invertible natural transformations as $2$-morphisms, while the $2$-morphisms of an $(\infty,1)$-category must be invertible.
