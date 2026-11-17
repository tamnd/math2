---
tag: 04DC0SRN2K
kind: statement
role: theorem
name: Order of G equals index times order of H
aliases: [order-of-a-group-is-the-index-times-the-order-of-the-subgroup]
msc: ["20D60"]
topics: [1VHQWXC64D]
audience: ug1
about: [0B85S2V2DR, 0DTXBQPA2S]
uses: [G5S1M9, 0X1JXT47GA, 0DTXBQPA2S, 0B85S2V2DR, 0DKMBWTD7P, 0EBACQFAZW]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)
    locator: Proof
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: lead section
  - book: isbn:9780471433347
    locator: Section 3.2
---

## Statement

Let $G$ be a [[group|G5S1M9]] and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
Let $[G : H]$ be the [[index|0DTXBQPA2S]] of $H$ in $G$, and let $|G|$ and $|H|$ be the [[orders|0B85S2V2DR]] of $G$ and $H$.

1. If $G$ is finite, then $|G| = [G : H] \cdot |H|$, as an equation of natural numbers. Thus $[G : H] = |G| / |H|$.
2. For each group $G$, finite or infinite, $|G| = [G : H] \cdot |H|$ as an equation of [[cardinal numbers|0EBACQFAZW]].

## Remarks

### Why each hypothesis is needed

- Part 1 needs $G$ to be finite, so that the three numbers are natural numbers and the division makes sense.
- Part 2 has no finiteness hypothesis, but its proof uses the axiom of choice to pick one element from each coset.
- The set $H$ must be a subgroup. In $\mathbb{Z}/4\mathbb{Z}$, the subset $S = \{0, 1\}$ has $4$ different translates $g + S$, and $4 \cdot 2 \neq 4$.

### Consequences

- [[Lagrange's theorem|3C53TD]]: for finite $G$, the order $|H|$ divides $|G|$.
- For finite $G$, the index $[G : H]$ also divides $|G|$.
- If $G$ is finite and $|H| = |G|$, then $H = G$, because the index is $1$.
- If $G$ is infinite and $H$ is finite, then $[G : H]$ is infinite, because a finite product of finite cardinals is finite.
- If $G$ is infinite, then $|G| = \max([G : H], |H|)$, by the rule $\kappa \cdot \lambda = \max(\kappa, \lambda)$ for nonzero cardinals with one of them infinite. The proof of this rule uses the axiom of choice.

### Converse

The converse question is whether each factorization $|G| = m \cdot d$ comes from a subgroup of order $d$ and index $m$.
This is false.
The [[alternating group $A_4$|0PDBVPP233]] has order $12 = 2 \cdot 6$, but no subgroup of order $6$.

### Generalizations

- The [[tower law|0ZQJ7KEFQ5]] $[G : K] = [G : H] \cdot [H : K]$ for $K \le H \le G$. The statement here is the case $K = \{e\}$, because $[G : \{e\}] = |G|$.
- The [[orbit-stabiliser theorem|0E2HSCKZ6C]]: for a finite group acting on a set, the size of the orbit of $x$ times the order of the stabiliser of $x$ is $|G|$.

## Explanations

### L1 human

Cut a finite group into the cosets of a subgroup.
Each piece has the same size as the subgroup, and the number of pieces is the index.
So the size of the group is the number of pieces times the size of one piece.
For example, $12$ objects in $4$ boxes of $3$ objects each give $12 = 4 \cdot 3$.

### L2 human

We use the formula to find an index in the [[dihedral group|0JZ27DMJ5D]] $D_4$ of the $8$ symmetries of a square.
Some books write $D_8$ for this group.

1. The rotations by $0$, $90$, $180$ and $270$ degrees form a subgroup $R$ of order $4$.
2. The group $D_4$ has order $8$.
3. By the formula, $[D_4 : R] = 8 / 4 = 2$.
4. The two cosets are $R$ and the set of the $4$ reflections.

The typical use is to compute an index from two orders, or an order from an index and an order.
For example, a subgroup of index $3$ in a group of order $18$ has order $6$.

A trap is to use part 1 for infinite groups.
For $G = \mathbb{Z}$ and $H = 2\mathbb{Z}$, the index is $2$, but $|G| / |H|$ is not defined.
Part 2 gives $\aleph_0 = 2 \cdot \aleph_0$, which is true but does not determine the index.

### L3 human

Part 2 says that $G$ is in bijection with $G/H \times H$, by the map $(C, h) \mapsto t(C)h$ for a choice $t(C)$ of a representative of each coset.
In topology, the analogous statement is that a principal $H$-bundle $G \to G/H$ is a product locally, but not always globally.
For groups the bijection exists as sets, but it is in general not a group isomorphism, and $G$ need not be a product of $H$ and a complement.
