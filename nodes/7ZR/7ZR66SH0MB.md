---
tag: 7ZR66SH0MB
kind: definition
name: Flat module
msc: [13C11, 16D40]
defines: 73RYYEVDKA
uses: [0310REJJY8, 0NZ8JA25WK, 0NRYHJPQG2, F0HQXQ0HCD, JB7ZBFBA9C, 096Z9MP2ME, 0CMD0BCH8T]
sources:
  - url: https://en.wikipedia.org/wiki/Flat_module
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $M$ be an [[$R$-module|0NZ8JA25WK]].
The module $M$ is *flat* if the following holds for every injective $R$-[[linear map|0NRYHJPQG2]] $f \colon N' \to N$ of $R$-modules.
The map
$$f \otimes \id_M \colon N' \otimes_R M \to N \otimes_R M$$
is injective, where $\otimes_R$ is the [[tensor product|F0HQXQ0HCD]].

## Remarks

Since $- \otimes_R M$ is always right exact, $M$ is flat exactly when $- \otimes_R M$ takes [[exact sequences|JB7ZBFBA9C]] to exact sequences.
It is enough to check the condition for the inclusions $I \to R$ of finitely generated [[ideals|096Z9MP2ME]]: $M$ is flat if and only if $I \otimes_R M \to M$ is injective for each such $I$.
Over a [[principal ideal domain|0CMD0BCH8T]], a module is flat exactly when it is torsion-free.
Projective modules are flat, and a finitely presented flat module is projective.

Example: $\Q$ is a flat $\Z$-module.
For any $\Z$-module $N$, the module $N \otimes_\Z \Q$ is the localization $S^{-1}N$ with $S = \Z \setminus \set{0}$, and localization preserves injective maps.

Non-example: $\Z/2\Z$ is not a flat $\Z$-module.
The map $f \colon \Z \to \Z$, $x \mapsto 2x$, is injective, but $f \otimes \id$ is multiplication by $2$ on $\Z \otimes_\Z \Z/2\Z \cong \Z/2\Z$, which is the zero map on a nonzero module.
