---
tag: W44XETYC4Q
kind: proof
name: Proof of Lagrange's theorem
msc: ["20D60"]
topics: [1VHQWXC64D]
audience: ug1
proves: 3C53TD
uses: [G5S1M9, 0X1JXT47GA, 0G8VEZ3WTK, 01HT2CH8BH, 03DEH43F4H, 0DKMBWTD7P]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)
    locator: Proof
  - book: isbn:9780471433347
    locator: Section 3.2, Theorem 8
---

## Proof

Let $G$ be a finite [[group|G5S1M9]] with identity $e$, and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
We show that $|G| = k \cdot |H|$, where $k$ is the number of left cosets of $H$.

1. For $a, b \in G$, write $a \sim b$ if $a^{-1}b \in H$.
2. The relation $\sim$ is reflexive: $a^{-1}a = e$, and $e \in H$ because $H$ is a subgroup.
3. The relation $\sim$ is symmetric: if $a^{-1}b \in H$, then its inverse $b^{-1}a$ is in $H$, because $H$ contains inverses.
4. The relation $\sim$ is transitive: if $a^{-1}b \in H$ and $b^{-1}c \in H$, then their product $a^{-1}c$ is in $H$, because $H$ is closed under products.
5. By steps 2 to 4, $\sim$ is an [[equivalence relation|0G8VEZ3WTK]] on $G$.
6. The class of $a$ is the [[left coset|03DEH43F4H]] $aH$. Indeed, $a^{-1}b = h$ with $h \in H$ holds exactly when $b = ah$ with $h \in H$.
7. The [[equivalence classes form a partition|01HT2CH8BH]] of $G$. Thus $G$ is the disjoint union of its distinct left cosets.
8. The set $G$ is finite, so there are finitely many distinct left cosets. Call them $C_1, \ldots, C_k$.
9. Each left coset has exactly $|H|$ elements, by the [[lemma on the size of cosets|0DKMBWTD7P]].
10. By steps 7 and 9, $|G| = |C_1| + \cdots + |C_k| = k \cdot |H|$.
11. Thus $|H|$ divides $|G|$, with quotient $k = [G : H]$.

This proves Lagrange's theorem.

## Idea

The left cosets of $H$ are the classes of an equivalence relation, so they cut $G$ into disjoint pieces.
Each piece is a copy of $H$ moved by one element, so each piece has $|H|$ elements.
Counting the elements of $G$ piece by piece gives $|G| = k \cdot |H|$.

## Variants

The same proof works with right cosets and the relation $a b^{-1} \in H$.
A second proof uses the [[orbit-stabiliser theorem|0E2HSCKZ6C]] for the action of $G$ on $G/H$ by left multiplication: the orbit of $H$ is $G/H$, and the stabiliser of $H$ is $H$.
A third proof lets $H$ act on $G$ by right multiplication.
Each orbit is a left coset, and the action is free, so each orbit has $|H|$ elements.
