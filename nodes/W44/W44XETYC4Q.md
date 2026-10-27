---
tag: W44XETYC4Q
kind: proof
name: Proof of Lagrange's theorem
msc: [20D60]
proves: 3C53TD
uses: [G5S1M9, 03DEH43F4H, 01HT2CH8BH, 0DKMBWTD7P]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)
    locator: Proof
---

## Proof

1. Let $G$ be a finite [[group|G5S1M9]] and let $H$ be a subgroup of $G$.
2. For $a, b \in G$, let $a \sim b$ when $a^{-1}b \in H$. Since $H$ contains the identity, inverses and products, this relation is reflexive, symmetric and transitive.
3. The class of $a$ under $\sim$ is the [[left coset|03DEH43F4H]] $aH$, because $a^{-1}b \in H$ exactly when $b \in aH$.
4. The [[equivalence classes form a partition|01HT2CH8BH]] of $G$. Thus $G$ is the disjoint union of $k$ distinct left cosets for some integer $k \ge 1$.
5. [[Each left coset has $|H|$ elements|0DKMBWTD7P]].
6. Thus $|G| = k\,|H|$, and $|H|$ divides $|G|$.

## Idea

The left cosets of the subgroup cut the group into blocks of equal size. The order of the group is the number of blocks times the size of one block.
