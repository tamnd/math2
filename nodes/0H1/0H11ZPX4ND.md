---
tag: 0H11ZPX4ND
kind: concept
name: Conjugate subgroup
msc: ["20E45"]
topics: [E1506A5A55]
audience: ug1
specializes: [0X1JXT47GA]
uses: [0X1JXT47GA, 0DXD4QSZ8A, 08MG7H8JW5]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugacy_class
    locator: Conjugacy of subgroups and general subsets
  - url: https://en.wikipedia.org/wiki/Centralizer_and_normalizer
    locator: Definitions
inventory: [DH5A822027]
---

## Summary

Let $G$ be a [[group|G5S1M9]], let $H$ be a [[subgroup|0X1JXT47GA]] of $G$, and let $g \in G$.
The conjugate of $H$ by $g$ is the set $gHg^{-1} = \{ghg^{-1} : h \in H\}$.
Two subgroups $H$ and $K$ of $G$ are conjugate in $G$ when $K = gHg^{-1}$ for some $g \in G$.
Each conjugate $gHg^{-1}$ is again a subgroup of $G$, and it is isomorphic to $H$.

## Motivation

[[Conjugate elements|0DXD4QSZ8A]] are elements that differ only by a renaming inside the group.
The same renaming acts on whole subgroups.
In the symmetric group $S_3$, the subgroup $\{e, (1\,2)\}$ swaps the points $1$ and $2$.
After a renaming of the points, it becomes the subgroup $\{e, (1\,3)\}$ or $\{e, (2\,3)\}$.
These three subgroups have the same structure and the same position in the group, so we want a name for this relation.
The subgroups that no renaming can move are the [[normal subgroups|0CB0DX5BVV]], and they are the subject of the rest of this topic.

## Notation

We write $gHg^{-1}$ for the conjugate of $H$ by $g$.
Some books use $H^g = g^{-1}Hg$ instead, which is the conjugate of $H$ by $g^{-1}$ in our notation.
The two conventions give the same set of conjugates.
The [[normaliser|0YGN3VAA0D]] of $H$ is $N_G(H) = \{g \in G : gHg^{-1} = H\}$.

## Remarks

### Examples

- In $S_3$, the three subgroups of order $2$ are conjugate to each other: [[the three subgroups of order two of S3 are conjugate|~fa75118f]].
- In $\mathrm{GL}_2(\mathbb{R})$, the upper triangular and the lower triangular invertible matrices form conjugate subgroups: [[conjugate triangular subgroups|~26fe0d64]].
- In each group $G$, the subgroups $\{e\}$ and $G$ are equal to all their conjugates.
- In $S_3$, the subgroup $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$ is equal to all its conjugates, because conjugation keeps the order of an element and $A_3$ holds all the elements of order $1$ and $3$.

### Non-examples

- In the Klein four-group $V_4$, two different subgroups of order $2$ are isomorphic but not conjugate: [[isomorphic but not conjugate subgroups|~462148ee]].
- In $S_3$, the subgroups $\{e, (1\,2)\}$ and $A_3$ are not conjugate, because they have different orders.

### Basic properties

- $gHg^{-1}$ is a subgroup of $G$. It contains $geg^{-1} = e$. It is closed under products, because $(gag^{-1})(gbg^{-1}) = g(ab)g^{-1}$. It is closed under inverses, because $(gag^{-1})^{-1} = ga^{-1}g^{-1}$.
- The map $c_g \colon H \to gHg^{-1}$, $c_g(h) = ghg^{-1}$, is a [[group isomorphism|08MG7H8JW5]]. It is a homomorphism by the computation above, and its inverse is $x \mapsto g^{-1}xg$. So $gHg^{-1} \cong H$.
- In particular, conjugate subgroups have the same order, and a conjugate of a [[cyclic group|0KVGH0J5B3]] is cyclic.
- Conjugacy of subgroups is an [[equivalence relation|0G8VEZ3WTK]] on the set of subgroups of $G$. The proof is the same as for [[conjugate elements|0DXD4QSZ8A]], with $c_{hg} = c_h \circ c_g$.
- The number of conjugates of $H$ is the index $[G : N_G(H)]$: [[the number of conjugates of a subgroup is the index of its normaliser|~10708e3f]].
- $H$ is equal to all its conjugates exactly when $H$ is a [[normal subgroup|0CB0DX5BVV]] of $G$.
- The intersection of all conjugates of $H$ is the [[normal core|0GETX79CJN]] of $H$, the largest normal subgroup of $G$ inside $H$.

### History

Galois worked with groups of permutations of the roots of a polynomial.
In his letter of 1832 to Auguste Chevalier, he used the subgroups that are equal to all their conjugates, which are the normal subgroups of today.

### Common errors

- Isomorphic subgroups need not be conjugate. The subgroups $\{e, a\}$ and $\{e, b\}$ of $V_4$ are an example.
- The equation $gHg^{-1} = H$ does not say that $ghg^{-1} = h$ for each $h \in H$. It says only that conjugation by $g$ sends $H$ onto $H$.
- The number of conjugates is $[G : N_G(H)]$, not $[G : H]$. For $A_3$ in $S_3$, the first number is $1$ and the second is $2$.

## Explanations

### L1 human

A subgroup is a team of elements inside a group.
Conjugation by $g$ renames all the elements of the group in a consistent way.
It sends the team to a new team with the same structure.
The new team is a conjugate subgroup.
Some teams always go to themselves, whatever the renaming is.
These teams are the normal subgroups.

### L2 human

To find all the conjugates of a subgroup $H$ of a finite group $G$, a direct method is to compute $gHg^{-1}$ for each $g$.
The work is shorter with the normaliser.
First find the elements $g$ with $gHg^{-1} = H$.
Then $H$ has $[G : N_G(H)]$ conjugates, and one $g$ from each coset of $N_G(H)$ gives each conjugate once.

For $H = \{e, (1\,2)\}$ in $S_3$, with composition from right to left, we get $N_{S_3}(H) = H$.
So $H$ has $6 / 2 = 3$ conjugates.
The cosets of $H$ are $H$, $(2\,3)H$ and $(1\,3)H$.
The elements $e$, $(2\,3)$ and $(1\,3)$ give the three conjugates $\{e, (1\,2)\}$, $\{e, (1\,3)\}$ and $\{e, (2\,3)\}$.

To show that a subgroup is not normal, it is enough to find one conjugate that is different from it.
To show that two subgroups are not conjugate, find a property that conjugation keeps, such as the order, and that one subgroup has and the other does not.

### L3 human

The group $G$ acts on the set of its subgroups by $g \cdot H = gHg^{-1}$.
The orbits of this [[group action|0WCY42EV9V]] are the conjugacy classes of subgroups, and the stabiliser of $H$ is its normaliser.
The Sylow theorems say that the Sylow $p$-subgroups of a finite group form one conjugacy class of subgroups.
In Galois theory, conjugate subgroups of the Galois group correspond to conjugate intermediate fields.
In topology, the conjugacy classes of subgroups of the fundamental group correspond to the connected covering spaces up to isomorphism, without a chosen base point.
In Lie theory, the Borel subgroups of a connected linear algebraic group over an algebraically closed field are all conjugate, and the upper triangular matrices form one of them in $\mathrm{GL}_n$.
