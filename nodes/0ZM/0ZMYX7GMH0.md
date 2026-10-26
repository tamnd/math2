---
tag: 0ZMYX7GMH0
kind: statement
role: theorem
name: First isomorphism theorem for rings
msc: [16D25]
uses: [0VFW4Y69BT, 0AAHE7GEW6, 0B6QC0C0G1, 0R74MZYNRB]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem A (rings)
---

## Statement

Let $f \colon R \to S$ be a [[ring homomorphism|0GGE0Z0JQ1]].
Then the [[kernel|0AAHE7GEW6]] $\ker f$ is a two-sided ideal of $R$, and the image $f(R)$ is a subring of $S$.
The map $R/\ker f \to f(R)$, $a + \ker f \mapsto f(a)$, is a [[ring isomorphism|0B6QC0C0G1]].
In particular, if $f$ is surjective, then $R/\ker f \cong S$.

## Remarks

The reduction map $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ has kernel $n\mathbb{Z}$.
The evaluation map $\mathbb{R}[x] \to \mathbb{C}$, $p \mapsto p(i)$, is surjective with kernel $(x^2 + 1)$. So $\mathbb{R}[x]/(x^2 + 1) \cong \mathbb{C}$.
The theorem has the same form for groups and for modules.

## Explanations

### L1 human

A homomorphism forgets exactly the information in its kernel.
If you divide out the kernel, the homomorphism becomes a bijection onto its image.
So every image of a ring is a quotient of that ring.
