---
tag: PCEVB6XV6J
kind: definition
name: Derived category
msc: [18G80, 14F08, 13D09]
defines: 5ST7NVJFSM
uses: [Y9CZ3MTNF1, WQ82C0M3QB, HTK9WQZJ1G, C9JEC2WQKV, DNFR3YP0XF, 9Y5Y92R4D5]
sources:
  - url: https://en.wikipedia.org/wiki/Derived_category
---

## Definition

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]] and let $\operatorname{Ch}(\mathcal{A})$ be the category of [[chain complexes|WQ82C0M3QB]] in $\mathcal{A}$ and [[chain maps|HTK9WQZJ1G]].
The *derived category* of $\mathcal{A}$ is the [[localization|DNFR3YP0XF]] of $\operatorname{Ch}(\mathcal{A})$ at the class of [[quasi-isomorphisms|C9JEC2WQKV]].
That is, it is a category $D(\mathcal{A})$ with a functor $Q \colon \operatorname{Ch}(\mathcal{A}) \to D(\mathcal{A})$ such that:

1. $Q(f)$ is an isomorphism for every quasi-isomorphism $f$;
2. every functor $F \colon \operatorname{Ch}(\mathcal{A}) \to \mathcal{C}$ that sends quasi-isomorphisms to isomorphisms factors as $F = G \circ Q$ for a unique functor $G \colon D(\mathcal{A}) \to \mathcal{C}$.

## Remarks

The localization can be computed in two steps: first pass to the [[homotopy category|9Y5Y92R4D5]] $K(\mathcal{A})$, then invert quasi-isomorphisms there by a calculus of fractions.
A morphism $X \to Y$ in $D(\mathcal{A})$ is then represented by a roof $X \xleftarrow{s} X' \to Y$ with $s$ a quasi-isomorphism.
For general $\mathcal{A}$ the morphisms between two objects might not form a set.
They do form a set for module categories, and for bounded below complexes when $\mathcal{A}$ has enough injectives.
Example: over $\Z$, let $C$ be $\Z \xrightarrow{\cdot 2} \Z$ in degrees $1$ and $0$, and let $\Z/2\Z$ sit in degree $0$.
The quotient map $C_0 = \Z \to \Z/2\Z$ is a chain map, and it is a quasi-isomorphism since $H_0(C) \cong \Z/2\Z$ and $H_1(C) = 0$; so $C \cong \Z/2\Z$ in $D(\mathcal{A})$.
Non-example: $C$ and $\Z/2\Z$ are not isomorphic in $K(\mathcal{A})$, since every chain map $\Z/2\Z \to C$ is zero, because $\Hom(\Z/2\Z, \Z) = 0$; so $K(\mathcal{A})$ is not the derived category.
The bounded variants $D^b$, $D^+$ and $D^-$ are defined in the same way from bounded complexes.
