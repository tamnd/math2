---
tag: 0JPDTEDCFD
kind: statement
role: theorem
name: Subgroups of abelian groups are normal
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
about: [0CB0DX5BVV, 082GHNPJ53]
uses: [082GHNPJ53, 0X1JXT47GA, 0CB0DX5BVV]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Quaternion_group
    locator: Properties
---

## Statement

Let $G$ be an [[abelian group|082GHNPJ53]] and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
Then $H$ is [[normal|0CB0DX5BVV]] in $G$.

## Remarks

For $g \in G$ and $h \in H$, commutativity gives $ghg^{-1} = hgg^{-1} = h$, and $h \in H$.
So conjugation by $g$ fixes each element of $H$, and in particular $gHg^{-1} = H$.

### Why each hypothesis is needed

The group must be abelian.
In the non-abelian group $S_3$, with composition from right to left, the subgroup $H = \{e, (1\,2)\}$ is not normal ([[a subgroup of order two in S3 is not normal|XD0WBC1MWB]]).
For example, $(1\,3)(1\,2)(1\,3)^{-1} = (2\,3)$, and $(2\,3) \notin H$.

### Consequences

- Each subgroup of the integers is normal, so each $n\mathbb{Z}$ gives a quotient group $\mathbb{Z}/n\mathbb{Z}$ ([[Z/nZ as a quotient|0YJ3WRR9RY]]).
- Each subgroup of a [[cyclic group|0KVGH0J5B3]] is normal, because cyclic groups are abelian.
- Each subgroup of $(\mathbb{R}, +)$, of $\mathbb{R}^\times$ and of the [[circle group|04EAFVFTF7]] is normal.
- Each quotient of an abelian group by a subgroup exists, and it is again abelian.

### Converse

The converse is false.
In the [[quaternion group|0NRJGW864D]] $Q_8$, each subgroup is normal, but $Q_8$ is not abelian ([[every subgroup of Q8 is normal|~eb292eed]]).
A group in which each subgroup is normal is a Dedekind group, and a non-abelian Dedekind group is a Hamiltonian group.
$Q_8$ is the smallest Hamiltonian group.

### Generalizations

- Each subgroup of the [[centre|0DZ93493VN]] $Z(G)$ of any group $G$ is normal in $G$. The proof needs only that each $h \in H$ commutes with each $g \in G$, and this holds for $H \le Z(G)$.

## History

The commutative groups are named abelian groups after Niels Henrik Abel.
For these groups, the condition of normality is empty, so the theory of quotients of abelian groups is simpler than the general theory.

## Explanations

### L1 human

In an abelian group, the order of multiplication does not matter.
So conjugation does nothing: $ghg^{-1}$ is just $h$ again.
A normal subgroup is a subgroup that conjugation cannot move out of its place.
In an abelian group conjugation moves nothing, so each subgroup is normal.

### L2 human

The theorem is often used without comment.
For example, the subgroup $3\mathbb{Z}$ of $\mathbb{Z}$ is normal, so the cosets $3\mathbb{Z}$, $1 + 3\mathbb{Z}$ and $2 + 3\mathbb{Z}$ form a group.
In additive notation the conjugate of $h$ by $g$ is $g + h - g = h$.

A common error is to use the converse.
If each subgroup of a group is normal, the group need not be abelian.
In $Q_8$, the element $j$ does not commute with $i$, because $jij^{-1} = -i$.
But $-i$ is in $\langle i \rangle$, so $\langle i \rangle$ is still normal.
Normality asks only that $gHg^{-1} = H$ as a set, not that $ghg^{-1} = h$ for each $h$.

### L3 human

In the category of abelian groups, each subgroup is a kernel, and each quotient is again abelian.
This is one reason why the category of abelian groups is an [[abelian category|Y9CZ3MTNF1]], while the [[category of groups|2CX7RPPXA9]] is not.
The same is true for modules over a ring: each submodule is the kernel of the projection to the quotient module.
The Dedekind groups are classified: a non-abelian Dedekind group is the direct product of $Q_8$, an elementary abelian $2$-group and an abelian group of odd order whose elements all have finite order.
