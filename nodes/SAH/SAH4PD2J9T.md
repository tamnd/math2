---
tag: SAH4PD2J9T
kind: statement
role: theorem
name: Clifford theory
msc: [20C15, 20C20]
uses: [G5S1M9, 0CB0DX5BVV, WYGRXCG2RN, FX3NEFYFFN, JJP4JFH3C6, 0AYMP41THN]
about: [FX3NEFYFFN, JJP4JFH3C6]
sources:
  - url: https://en.wikipedia.org/wiki/Clifford_theory
same_as:
  wikidata: Q5133087
  wikipedia: Clifford theory
---

## Statement

Let $G$ be a finite [[group|G5S1M9]], let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$, and let $F$ be a field.
Let $V$ be an [[irreducible|FX3NEFYFFN]] [[representation|WYGRXCG2RN]] of $G$ over $F$ of finite dimension.
For a representation $W$ of $N$ and $g \in G$, the conjugate ${}^g W$ is the space $W$ with $n \in N$ acting as $g^{-1} n g$ acts on $W$.

1. The restriction $V|_N$ is a semisimple representation of $N$. There are an irreducible representation $W$ of $N$, an integer $e \ge 1$ and elements $g_1, \ldots, g_t \in G$ with $V|_N \cong e \, ({}^{g_1}W \oplus \cdots \oplus {}^{g_t}W)$. The ${}^{g_i}W$ are pairwise non-isomorphic, and every $G$-conjugate of $W$ is isomorphic to one of them.
2. Let $T = \set{g \in G : {}^g W \cong W}$, the inertia group of $W$, and let $U$ be the sum of the subrepresentations of $V|_N$ isomorphic to $W$. Then $U$ is invariant under $T$, $U$ is an irreducible representation of $T$, $t = [G : T]$, and $V \cong \operatorname{Ind}_T^G U$.

## Remarks

For the proof of part 1, take an irreducible $N$-subrepresentation $W$ of $V$.
Each $gW$ is again $N$-invariant and irreducible, and isomorphic to a conjugate of $W$.
The sum $\sum_g gW$ is a nonzero $G$-invariant subspace, so it is $V$.
The elements of $G$ permute the isotypic components of $V|_N$ transitively, and $T$ is the [[stabiliser|0AYMP41THN]] of the component $U$.
Part 2 follows, since a representation that is a direct sum of transitively permuted subspaces is [[induced|JJP4JFH3C6]] from a stabiliser.
Example: let $G = S_3$, $N = A_3 \cong \Z/3$ and let $V$ be the irreducible complex representation of degree $2$.
Then $V|_N$ is the sum of the two non-trivial characters of $A_3$, which conjugation by a transposition swaps.
Here $e = 1$, $t = 2$, $T = N$, and $V = \operatorname{Ind}_{A_3}^{S_3} \omega$ for a non-trivial character $\omega$ of $A_3$.
The theorem also holds when $G$ is any group and $N$ has finite index in $G$.

## Explanations

### L1 human

Clifford theory explains how an irreducible representation of a group looks when one only watches a normal subgroup.
It breaks into equally many copies of a few irreducible pieces, and those pieces are all twists of one another by the big group.
Moreover the whole representation can be rebuilt by induction from the subgroup that fixes one piece.

### L2 human

This is the basic tool for building representations of a group from those of a normal subgroup and of the quotient.
It applies well to solvable groups, which have chains of normal subgroups.
In character language it states that the irreducible constituents of $\chi|_N$ form one $G$-orbit and all occur with the same multiplicity $e$.
The Clifford correspondence, part 2, gives a bijection between irreducible characters of $T$ lying over $W$ and irreducible characters of $G$ lying over $W$, by induction.
It is a standard step in inductive arguments in character theory, which pass from $G$ to a normal subgroup.
