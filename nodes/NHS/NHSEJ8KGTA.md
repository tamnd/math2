---
tag: NHSEJ8KGTA
kind: proof
name: Proof of the third isomorphism theorem for rings
msc: [16D25]
proves: 073C80EC63
uses: [0894J980RK, 0DDA6CY7GJ, 0VFW4Y69BT, 0GGE0Z0JQ1, 0AAHE7GEW6, 0R74MZYNRB, 0ZMYX7GMH0, 0B6QC0C0G1]
sources:
  - url: https://proofwiki.org/wiki/Third_Isomorphism_Theorem_for_Rings
---

## Proof

1. Let $R$ be a [[ring|0894J980RK]] and let $I \subseteq J$ be [[two-sided ideals|0DDA6CY7GJ]] of $R$. Put $J/I = \set{a + I : a \in J}$, a subset of the [[quotient ring|0VFW4Y69BT]] $R/I$.
2. For an ideal $L$ and $a, b \in R$, $a + L = b + L$ if and only if $a - b \in L$. Indeed, if the cosets are equal, then $a \in b + L$. Conversely, if $a - b = x \in L$, then $a + y = b + (x + y)$ and $b + y = a + (y - x)$ for each $y \in L$.
3. The set $J/I$ contains $0 + I$, since $0 \in J$. For $a, b \in J$, $(a + I) - (b + I) = (a - b) + I$ lies in $J/I$, since $a - b \in J$. So $J/I$ is an additive subgroup of $R/I$.
4. For $r \in R$ and $a \in J$, $(r + I)(a + I) = r a + I$ and $(a + I)(r + I) = a r + I$. Both lie in $J/I$, since $r a, a r \in J$. So $J/I$ is a two-sided ideal of $R/I$.
5. Let $\rho \colon R \to R/J$, $\rho(a) = a + J$. By the definition of the operations of $R/J$, $\rho$ is a [[ring homomorphism|0GGE0Z0JQ1]]. By step 2, its [[kernel|0AAHE7GEW6]] is $J$.
6. Since $I \subseteq J = \ker \rho$, the [[universal property of the quotient ring|0R74MZYNRB]] gives a ring homomorphism $\psi \colon R/I \to R/J$ with $\psi(a + I) = a + J$.
7. The map $\psi$ is surjective, because each $a + J$ equals $\psi(a + I)$.
8. The kernel of $\psi$ is $J/I$. First, if $a \in J$, then $\psi(a + I) = a + J = 0 + J$ by step 2.
9. Conversely, let $\psi(a + I) = 0 + J$. Then $a \in J$ by step 2, so $a + I \in J/I$.
10. By the [[first isomorphism theorem|0ZMYX7GMH0]] applied to $\psi$, with steps 7 to 9, the map $(R/I)/(J/I) \to R/J$, $(a + I) + J/I \mapsto \psi(a + I) = a + J$, is a [[ring isomorphism|0B6QC0C0G1]].

## Idea

Reducing modulo $J$ kills everything in $I$, so it factors through $R/I$. The resulting map $R/I \to R/J$ is onto, and it kills exactly the cosets of elements of $J$. The first isomorphism theorem turns this into the isomorphism.
