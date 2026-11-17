---
tag: BMD35Z5SGC
kind: proof
name: Proof that the order of an element divides the order of the group
msc: ["20D60"]
topics: [1VHQWXC64D]
audience: ug1
proves: 08V7JHS3QZ
uses: [G5S1M9, 0WE2NHZJ7B, 08ABT85339, 031M8HX7DA, 3C53TD]
methods: [0NTF6DMVAP, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)
    locator: Applications
  - book: isbn:9780471433347
    locator: Section 3.2
---

## Proof

Let $G$ be a finite [[group|G5S1M9]] and let $g \in G$.

1. The [[cyclic subgroup|08ABT85339]] $\langle g \rangle = \{g^k : k \in \mathbb{Z}\}$ is a subgroup of $G$, by its definition.
2. The element $g$ has finite [[order|0WE2NHZJ7B]]. Suppose not. Then the powers $g^k$, $k \in \mathbb{Z}$, are pairwise distinct, by [[the theorem on the order of a cyclic subgroup|031M8HX7DA]]. So $\langle g \rangle$ is infinite. But $\langle g \rangle \subseteq G$ and $G$ is finite. This is a contradiction.
3. Let $n$ be the order of $g$. By [[the same theorem|031M8HX7DA]], $|\langle g \rangle| = n$.
4. By [[Lagrange's theorem|3C53TD]], applied to the subgroup $\langle g \rangle$ of the finite group $G$, the number $|\langle g \rangle|$ divides $|G|$.
5. By steps 3 and 4, $n$ divides $|G|$.

Thus the order of $g$ divides the order of $G$.

## Idea

The element $g$ generates a subgroup with exactly as many elements as the order of $g$.
Lagrange's theorem says that the order of this subgroup divides $|G|$.

## Variants

A proof without the name of Lagrange's theorem uses the same idea directly.
The subgroup $\langle g \rangle$ acts on $G$ by left multiplication.
Each orbit $\langle g \rangle x$ has exactly $n$ elements, because $g^i x = g^j x$ implies $g^i = g^j$.
The orbits partition $G$, so $|G|$ is a multiple of $n$.
