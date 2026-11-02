---
tag: EAX2SYK8C5
kind: definition
name: Homotopy category
msc: [18N40, 55U35, 55P10]
defines: 48QQ7T98Z9
uses: [SDTZVZ6B4Q, E2870TEDG7, DNFR3YP0XF, HSV1J7BJXX, 9YA6S6HD9V, 4Q3WY1RX91, 5W95QFHXPR]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_category
---

## Definition

Let $\mathcal{M}$ be a [[model category|SDTZVZ6B4Q]] with class of [[weak equivalences|E2870TEDG7]] $W$.
The *homotopy category* of $\mathcal{M}$ is the [[localization|DNFR3YP0XF]]
$$\gamma \colon \mathcal{M} \to \mathrm{Ho}(\mathcal{M}) = \mathcal{M}[W^{-1}].$$

## Remarks

Quillen's fundamental theorem says that this localization exists with small hom-sets.
If $X$ is cofibrant and $Y$ is fibrant (see [[fibration and cofibration|HSV1J7BJXX]]), then $\mathrm{Ho}(\mathcal{M})(\gamma X, \gamma Y)$ is the set of homotopy classes of morphisms $X \to Y$.
Every object is isomorphic in $\mathrm{Ho}(\mathcal{M})$ to one that is both fibrant and cofibrant, by the factorization axiom.

Example: for topological spaces with the Quillen model structure, $W$ consists of the [[weak homotopy equivalences|4Q3WY1RX91]].
Every space is fibrant, and the [[CW complexes|5W95QFHXPR]] are cofibrant.
So $\mathrm{Ho}(\mathrm{Top})$ is equivalent to the category of CW complexes with [[homotopy|9YA6S6HD9V]] classes of continuous maps as morphisms.
Non-example: the naive homotopy category, with all spaces as objects and homotopy classes of maps as morphisms, is a different category.
In it, the map from the Warsaw circle to a point is not invertible, although it is a weak homotopy equivalence.

The name is also used for the homotopy category of chain complexes, whose morphisms are chain homotopy classes of chain maps.
That category is related to, but different from, the derived category.
