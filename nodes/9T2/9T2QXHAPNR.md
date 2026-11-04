---
tag: 9T2QXHAPNR
kind: proof
name: Proof of the order of the alternating group
msc: [20B30]
proves: 0SZ1KMNWVE
uses: [0T13HM377F, 0771AJP4BX, 0JEJJCB0EX, 0C9ZKYSPYR, 0PCKBBMEXC, 04DC0SRN2K, 02DTRYKGE8, 0SK90238BH]
sources:
  - url: https://en.wikipedia.org/wiki/Parity_of_a_permutation
    locator: Properties
---

## Proof

We pair the even and the odd permutations by a bijection. Let $n \geq 2$.

1. By the [[definition of the alternating group|0T13HM377F]], $A_n$ is the set of [[even permutations|0771AJP4BX]], that is, of $\sigma \in S_n$ with $\operatorname{sgn}(\sigma) = 1$. Let $O$ be the set of odd permutations, with sign $-1$.
2. Each permutation has sign $1$ or $-1$, so $S_n$ is the disjoint union of $A_n$ and $O$. Hence $|S_n| = |A_n| + |O|$.
3. The [[sign is a homomorphism|0JEJJCB0EX]], and $A_n$ is its kernel. So $A_n$ is a [[subgroup|0C9ZKYSPYR]] of $S_n$.
4. Let $t = (1\ 2)$. It is a [[transposition|02DTRYKGE8]], so $\operatorname{sgn}(t) = -1$ by the [[definition of the sign|0SK90238BH]].
5. Define $L \colon S_n \to S_n$ by $L(\sigma) = t\sigma$. Since the sign is a homomorphism, $\operatorname{sgn}(L(\sigma)) = -\operatorname{sgn}(\sigma)$.
6. By step 5, $L$ maps $A_n$ into $O$ and maps $O$ into $A_n$.
7. Since $t t = e$, we get $L(L(\sigma)) = \sigma$ for all $\sigma$. So the restriction $A_n \to O$ of $L$ has the inverse $O \to A_n$, also given by $L$.
8. Thus $L$ gives a bijection from $A_n$ to $O$, and $|A_n| = |O|$.
9. By the [[order of the symmetric group|0PCKBBMEXC]], $|S_n| = n!$. With steps 2 and 8, $n! = 2|A_n|$, so $|A_n| = n!/2$.
10. Since $A_n$ is a subgroup of the finite group $S_n$, we have [[$|S_n| = [S_n : A_n] \cdot |A_n|$|04DC0SRN2K]]. So $[S_n : A_n] = n! / (n!/2) = 2$.

## Idea

Multiplying by one fixed transposition flips the sign of every permutation. It is its own inverse, so it matches the even permutations one to one with the odd ones. Hence exactly half of the $n!$ permutations are even.
