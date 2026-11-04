---
tag: A5B8MTG5X5
kind: proof
name: Proof of the first isomorphism theorem for rings
msc: [16D25]
proves: 0ZMYX7GMH0
uses: [0GGE0Z0JQ1, 0AAHE7GEW6, 0DDA6CY7GJ, 0859D58WPD, 0VFW4Y69BT, 0R74MZYNRB, 0MMCB8RXGA, 0B6QC0C0G1]
sources:
  - url: https://proofwiki.org/wiki/First_Isomorphism_Theorem_for_Rings
---

## Proof

1. Let $f \colon R \to S$ be a [[ring homomorphism|0GGE0Z0JQ1]], and write $K = \ker f$ for its [[kernel|0AAHE7GEW6]].
2. As for any additive map, $f(0) = 0$ and $f(a - b) = f(a) - f(b)$ for $a, b \in R$. Indeed, $f(0) = f(0) + f(0)$ gives $f(0) = 0$, and then $f(a - b) + f(b) = f(a)$.
3. The set $K$ is an additive subgroup of $R$. Indeed, $0 \in K$, and if $a, b \in K$, then $f(a - b) = 0 - 0 = 0$.
4. For $r \in R$ and $a \in K$, $f(r a) = f(r) \cdot 0 = 0$ and $f(a r) = 0 \cdot f(r) = 0$. So $r a, a r \in K$, and $K$ is a [[two-sided ideal|0DDA6CY7GJ]] of $R$.
5. The image $f(R)$ is a [[subring|0859D58WPD]] of $S$. Indeed, $1 = f(1) \in f(R)$, $f(a) - f(b) = f(a - b)$ and $f(a) f(b) = f(a b)$.
6. Since $K \subseteq \ker f$, the [[universal property of the quotient ring|0R74MZYNRB]] gives a ring homomorphism $\bar{f} \colon R/K \to S$ with $\bar{f}(a + K) = f(a)$. Here $R/K$ is the [[quotient ring|0VFW4Y69BT]].
7. The values of $\bar{f}$ are the values $f(a)$, so $\bar{f}$ takes values in $f(R)$. As a map $R/K \to f(R)$, it is still a ring homomorphism, because $f(R)$ is a subring with the operations of $S$.
8. This map is surjective onto $f(R)$, because each $f(a)$ equals $\bar{f}(a + K)$.
9. Its kernel is $\set{0 + K}$. Indeed, $\bar{f}(a + K) = 0$ means $f(a) = 0$, that is, $a \in K$. Then $a - 0 \in K$, so $a + K = 0 + K$.
10. A ring homomorphism with zero kernel [[is injective|0MMCB8RXGA]]. So $\bar{f} \colon R/K \to f(R)$ is bijective, and it is a [[ring isomorphism|0B6QC0C0G1]].
11. If $f$ is surjective, then $f(R) = S$. So $\bar{f}$ is an isomorphism from $R/\ker f$ to $S$, and $R/\ker f \cong S$.

## Idea

The kernel is an ideal, so one can form $R/\ker f$, and $f$ passes to a map on cosets. This map hits the whole image. Its kernel is only the zero coset, because dividing by $\ker f$ removed exactly what $f$ sends to zero.
