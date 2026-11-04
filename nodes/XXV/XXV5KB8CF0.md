---
tag: XXV5KB8CF0
kind: proof
name: Proof that the multiplicative group of a finite field is cyclic
msc: ["12E20"]
proves: 0EBZ3G455G
uses: [08RTDHX1SK, 05THZKR9AN, 0CKGBEJX6B]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Multiplicative structure
---

## Proof

1. Let $F$ be a [[finite field|08RTDHX1SK]] of order $q$, and let $F^\times$ be its [[group of units|05THZKR9AN]].
2. In a field, every nonzero element is a unit. So $F^\times = F \setminus \set{0}$ has $q - 1$ elements.
3. So $F^\times$ is a finite subgroup of the multiplicative group of the field $F$.
4. By the [[theorem on finite subgroups of $K^\times$|0CKGBEJX6B]], with $K = F$ and $G = F^\times$, the group $F^\times$ is cyclic.
5. By step 2, it is cyclic of order $q - 1$.

## Idea

The whole group $F^\times$ is itself a finite subgroup of the multiplicative group of $F$. So the general theorem applies to it directly.
