---
tag: 0V547YQRMV
kind: statement
role: theorem
name: Subgroups of index two are normal
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
about: [0CB0DX5BVV, 0DTXBQPA2S]
uses: [0X1JXT47GA, 0DTXBQPA2S, 03DEH43F4H, 01E7SWYJX3]
formal:
  - system: lean4
    library: mathlib
    decl: Subgroup.normal_of_index_eq_two
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Examples
---

## Statement

Let $G$ be a [[group|G5S1M9]] and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$ of [[index|0DTXBQPA2S]] $2$.
Then $H$ is [[normal|0CB0DX5BVV]] in $G$.

## Remarks

The group $G$ can be finite or infinite.
The proof shows that the two [[left cosets|03DEH43F4H]] of $H$ are $H$ and $G \setminus H$, and that the two right cosets are the same two sets.
So $gH = Hg$ for each $g \in G$, and $H$ is normal by [[normality via cosets|01E7SWYJX3]].

### Why each hypothesis is needed

The index must be $2$; index $3$ is not enough.
In $S_3$, with composition from right to left, the subgroup $H = \{e, (1\,2)\}$ has index $3$.
It is not normal, because $(1\,2\,3)H = \{(1\,2\,3), (1\,3)\}$ and $H(1\,2\,3) = \{(1\,2\,3), (2\,3)\}$ ([[a subgroup of order two in S3 is not normal|XD0WBC1MWB]]).
With three cosets, the complement $G \setminus H$ is the union of two left cosets, and these need not be right cosets.

### Consequences

- The [[alternating group|0Z5905Q73D]] $A_n$ is normal in the [[symmetric group|0515A6D2Y1]] $S_n$ for $n \ge 2$, because $|S_n| = n!$ and $|A_n| = n!/2$.
- In the [[dihedral group|0JZ27DMJ5D]] $D_n$ of order $2n$, the subgroup of the $n$ rotations has index $2$, so it is normal.
- In the [[quaternion group|0NRJGW864D]] $Q_8$, the subgroups $\langle i \rangle$, $\langle j \rangle$ and $\langle k \rangle$ have index $2$, so they are normal.
- If $[G : H] = 2$, then $g^2 \in H$ for each $g \in G$. If $g \notin H$ and $g^2 \notin H$, then $g^2H = G \setminus H = gH$. Then $g = g^{-1}g^2 \in H$, which is false.
- If $[G : H] = 2$, then $H$ contains each element $g$ of odd order $2m + 1$, because $g = g^{2m+2} = (g^2)^{m+1}$.
- A group of order more than $2$ with a subgroup of index $2$ is not [[simple|0YMYMNQ0QZ]], because that subgroup is a normal subgroup different from $\{e\}$ and $G$.

### Converse

The converse is false.
A normal subgroup can have any index: $\{e\}$ is normal in $S_3$ and has index $6$.

### Generalizations

In a finite group, a subgroup whose index is the smallest prime divisor of $|G|$ is normal ([[smallest prime index|0FEBE9NC0E]]).
For $|G|$ even, the smallest prime divisor is $2$, and this gives the present theorem for finite groups.

## History

Galois used normal subgroups in his letter of 1832 to Auguste Chevalier, in his study of polynomial equations.
In Galois theory, a subgroup of index $2$ of the Galois group corresponds to an extension of degree $2$, and such an extension is always normal.

## Explanations

### L1 human

When a subgroup has only two cosets, one coset is the subgroup and the other coset is everything else.
This is true for the left cosets and for the right cosets.
So the left cosets and the right cosets are the same, and the subgroup is normal.
For example, the even permutations form half of all permutations, and the odd permutations form the other half.

### L2 human

We check the theorem for $G = S_3$ and $H = A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$, with composition from right to left.

1. $|S_3| = 6$ and $|A_3| = 3$, so the index is $2$.
2. For $g = (1\,2)$, the left coset $gA_3$ is $\{(1\,2), (1\,2)(1\,2\,3), (1\,2)(1\,3\,2)\} = \{(1\,2), (2\,3), (1\,3)\}$.
3. The right coset $A_3g$ is $\{(1\,2), (1\,2\,3)(1\,2), (1\,3\,2)(1\,2)\} = \{(1\,2), (1\,3), (2\,3)\}$.
4. So $gA_3 = A_3g$, although $g(1\,2\,3) \ne (1\,2\,3)g$.

The theorem saves the work of checking each conjugate.
A common error is to think that it also holds for index $3$; the example above with $\{e, (1\,2)\}$ shows that it does not.
Another common error is to apply the theorem to a subset that is not a subgroup.
The three odd permutations form half of $S_3$, but they do not form a subgroup, so the theorem says nothing about them.

### L3 human

A subgroup $H$ of index $2$ is the kernel of the homomorphism $G \to \{1, -1\}$ that sends $H$ to $1$ and $G \setminus H$ to $-1$.
So the subgroups of index $2$ correspond to the surjective homomorphisms from $G$ onto a group of order $2$.
For $S_n$ with $n \ge 2$, the sign is the only such homomorphism, and $A_n$ is the only subgroup of index $2$.
The reason is that each subgroup of index $2$ contains all elements of odd order, so it contains all $3$-cycles, and for $n \ge 3$ the $3$-cycles generate $A_n$.
In topology, a subgroup of index $2$ of the fundamental group gives a double cover, such as the orientation double cover.
