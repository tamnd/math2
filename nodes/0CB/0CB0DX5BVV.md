---
tag: 0CB0DX5BVV
kind: concept
name: Normal subgroup
aliases: [invariant-subgroup]
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
specializes: [0X1JXT47GA]
uses: [0X1JXT47GA, 0DXD4QSZ8A, 0H11ZPX4ND]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Equivalent conditions
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Properties
  - book: isbn:9780471433347
    locator: Section 3.1
same_as:
  wikidata: Q743179
  wikipedia: Normal subgroup
inventory: [F3D99PH13A]
---

## Summary

Let $G$ be a [[group|G5S1M9]].
A [[subgroup|0X1JXT47GA]] $N$ of $G$ is normal in $G$ when $gng^{-1} \in N$ for each $g \in G$ and each $n \in N$.
In other words, $N$ is closed under [[conjugation|0DXD4QSZ8A]] by all the elements of $G$.
The normal subgroups are exactly the subgroups that give a quotient group, and exactly the kernels of the homomorphisms from $G$.

## Motivation

For a subgroup $H$ of $G$, we want to make the set of cosets of $H$ into a group, with the product $(aH)(bH) = abH$.
For the integers and the subgroup $3\mathbb{Z}$, this works, and it gives the integers modulo $3$.
But for $H = \{e, (1\,2)\}$ in $S_3$ it fails: the product depends on the choice of $a$ and $b$ in their cosets.
The condition that makes the product well defined is that $H$ is closed under conjugation.
The same condition appears when we ask which subgroups are kernels of homomorphisms.
So normal subgroups are the subgroups that we can "divide by", in the same way that we divide the integers by $n$.

## Notation

We write $N \trianglelefteq G$ when $N$ is a normal subgroup of $G$.
We write $N \triangleleft G$ when $N$ is normal in $G$ and $N \ne G$, that is, when $N$ is a proper normal subgroup.
Some books use $N \triangleleft G$ for all normal subgroups, so check the convention of each book.
We write $gNg^{-1} = \{gng^{-1} : n \in N\}$.
Some books write conjugation as $g^{-1}ng$; this gives the same definition, because $g$ runs over all of $G$.
Older books use the names invariant subgroup and self-conjugate subgroup.

## Remarks

### Examples

- In each group $G$, the subgroups $\{e\}$ and $G$ are normal.
- Each subgroup of an [[abelian group|082GHNPJ53]] is normal ([[subgroups of abelian groups are normal|0JPDTEDCFD]]). For example, the [[even integers|8WJPSS7TE9]] form a normal subgroup of $\mathbb{Z}$.
- The [[alternating group|0Z5905Q73D]] $A_3$ is normal in $S_3$ ([[A3 is normal in S3|T4PCQ68C5K]]). More generally, $A_n \trianglelefteq S_n$, because $A_n$ has index $2$.
- The special linear group $\mathrm{SL}_n(F)$ is normal in $\mathrm{GL}_n(F)$, because it is a kernel ([[the special linear group is the kernel of the determinant|556HZEYCQF]]).
- The [[centre|0DZ93493VN]] $Z(G)$ is normal in $G$, because $gzg^{-1} = zgg^{-1} = z$ for $z \in Z(G)$.
- In the [[dihedral group|0JZ27DMJ5D]] $D_n$ of order $2n$, the subgroup of rotations has index $2$, so it is normal.
- Each subgroup of the [[quaternion group|0NRJGW864D]] $Q_8$ is normal, although $Q_8$ is not abelian ([[every subgroup of Q8 is normal|R58NSPHAYJ]]).

### Non-examples

- The subgroup $\{e, (1\,2)\}$ of $S_3$ is not normal ([[a subgroup of order two in S3 is not normal|XD0WBC1MWB]]).
- The upper triangular matrices form a subgroup of $\mathrm{GL}_2(\mathbb{R})$ that is not normal ([[conjugate triangular subgroups|MXTMGWMERC]]).
- The subgroup $\{e, (1\,2)(3\,4)\}$ of $A_4$ is not normal, although it is normal in a normal subgroup of $A_4$ ([[normality is not transitive|PVB7ZSPZR6]]).

### Basic properties

Let $N$ be a subgroup of $G$.
The following conditions are equivalent, and each one can serve as the definition.

1. $gNg^{-1} \subseteq N$ for each $g \in G$. This is the definition above.
2. $gNg^{-1} = N$ for each $g \in G$. So $N$ is equal to each of its [[conjugate subgroups|0H11ZPX4ND]].
3. $gN = Ng$ for each $g \in G$. So each left coset is a right coset ([[normality via cosets|01E7SWYJX3]]).
4. The product $(aN)(bN) = abN$ of left cosets is well defined ([[normality via cosets|01E7SWYJX3]]).
5. $N$ is a union of [[conjugacy classes|0DEBXAJ5SA]] of $G$.
6. $N$ is the kernel of a homomorphism from $G$ to some group ([[kernels are normal|0C9ZKYSPYR]] and its converse).

Here is the proof that conditions 1, 2 and 5 are equivalent.
Condition 2 gives condition 1 at once.
If condition 1 holds, apply it to $g^{-1}$: then $g^{-1}Ng \subseteq N$, so $N = g(g^{-1}Ng)g^{-1} \subseteq gNg^{-1}$, and condition 2 holds.
Condition 1 says that each conjugate of each element of $N$ is in $N$, and this is condition 5.

Other properties:

- A subgroup of [[index|0DTXBQPA2S]] $2$ is normal ([[subgroups of index two are normal|0V547YQRMV]]).
- In a finite group, a subgroup whose index is the smallest prime divisor of $|G|$ is normal ([[smallest prime index|0FEBE9NC0E]]).
- The intersection of a family of normal subgroups is normal. If $x$ is in each of them, then so is $gxg^{-1}$.
- If $N \trianglelefteq G$ and $H \le G$, then $HN$ is a subgroup of $G$ ([[HN is a subgroup when N is normal|0TXWV1JGG1]]).
- If $N \trianglelefteq G$ and $N \le H \le G$, then $N \trianglelefteq H$, because the condition for $H$ uses fewer elements $g$.
- Let $\varphi \colon G \to K$ be a [[group homomorphism|0JYTG5K9Y4]] and let $M \trianglelefteq K$. Then the preimage $\varphi^{-1}(M)$ is normal in $G$, because $\varphi(gxg^{-1}) = \varphi(g)\varphi(x)\varphi(g)^{-1} \in M$ for $x \in \varphi^{-1}(M)$.
- If $N \trianglelefteq G$ and $\varphi \colon G \to K$ is a homomorphism, then $\varphi(N)$ is normal in the [[image|0S21GNW9ZB]] $\varphi(G)$. It need not be normal in $K$; see the common errors.

### History

Galois used normal subgroups in his letter of 1832 to Auguste Chevalier.
He needed them to decide when a polynomial equation can be solved by radicals.
Hölder defined quotient groups in 1889, and the quotient by a normal subgroup became a standard construction.

### Common errors

- The equation $gN = Ng$ is an equation of sets. It does not say that $gn = ng$ for each $n \in N$. In $S_3$, $(1\,2)A_3 = A_3(1\,2)$, but $(1\,2)$ does not commute with $(1\,2\,3)$.
- Normality is not transitive. From $K \trianglelefteq N$ and $N \trianglelefteq G$ we cannot conclude $K \trianglelefteq G$ ([[normality is not transitive|PVB7ZSPZR6]]).
- The image of a normal subgroup is normal only in the image of the homomorphism. The inclusion $\iota \colon H \to S_3$ of $H = \{e, (1\,2)\}$ is a homomorphism, and $H \trianglelefteq H$, but $\iota(H) = H$ is not normal in $S_3$. If $\varphi$ is surjective, then $\varphi(N)$ is normal in the target.
- Normality depends on the large group. Each subgroup is normal in itself, so the phrase "$N$ is normal" must name the large group.
- For one fixed $g$, the inclusion $gNg^{-1} \subseteq N$ can be strict. Let $G$ be the group of matrices $\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}$ with $a \in \mathbb{Q}$, $a \ne 0$ and $b \in \mathbb{Q}$. Let $N$ be the subgroup with $a = 1$ and $b \in \mathbb{Z}$, and $g = \operatorname{diag}(2, 1)$. Then $gNg^{-1}$ is the subgroup with $a = 1$ and $b \in 2\mathbb{Z}$, which is smaller than $N$. Equality in condition 2 comes from the use of both $g$ and $g^{-1}$.

## Explanations

### L1 human

A subgroup is a smaller group inside a group.
The elements of the large group can "rename" the elements of the subgroup by conjugation.
For most subgroups, a renaming moves some elements out of the subgroup.
A normal subgroup is a subgroup that no renaming can break: each renamed element is still inside.
For example, think of the moves of three cups.
The two turns of all three cups, together with "do nothing", form a normal subgroup.
If we rename the cups, a turn is still a turn.
But the moves "do nothing" and "swap cups $1$ and $2$" do not form a normal subgroup.
After a renaming, the swap of cups $1$ and $2$ can become the swap of cups $2$ and $3$.

### L2 human

To prove that $N$ is normal, take any $g \in G$ and any $n \in N$, and show that $gng^{-1} \in N$.
We do this for $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$ in $S_3$, with composition from right to left.

1. Conjugation keeps the order of an element, by the properties of [[conjugate elements|0DXD4QSZ8A]].
2. The elements of $S_3$ of order $1$ or $3$ are $e$, $(1\,2\,3)$ and $(1\,3\,2)$, so they are exactly the elements of $A_3$.
3. So for $n \in A_3$ and $g \in S_3$, the order of $gng^{-1}$ is $1$ or $3$, and $gng^{-1} \in A_3$.

To prove that $N$ is not normal, it is enough to find one $g \in G$ and one $n \in N$ with $gng^{-1} \notin N$.
For $H = \{e, (1\,2)\}$ in $S_3$, take $g = (1\,3)$ and $n = (1\,2)$.
Then $gng^{-1} = (2\,3)$, which is not in $H$.

There are three useful shortcuts.
A subgroup of index $2$ is normal.
A kernel of a homomorphism is normal.
A subgroup that is a union of conjugacy classes is normal; in $S_n$ the conjugacy classes are the cycle types.
For example, $V = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$ is the union of $\{e\}$ and one cycle type of $S_4$, so $V \trianglelefteq S_4$.

### L3 human

A subgroup $N$ is normal exactly when the product of cosets makes the set $G/N$ of cosets into a group, the [[quotient group|0KYX2N69J0]].
Then $N$ is the kernel of the projection $G \to G/N$, and the [[first isomorphism theorem|0CXXJNG5B6]] says that every homomorphic image of $G$ has this form.
The ideals of a ring play the same role for rings, and the congruences of an algebraic structure play this role in universal algebra.
In the category of groups, the normal subgroups are exactly the kernels.

A group with no normal subgroups other than $\{e\}$ and itself is a [[simple group|0YMYMNQ0QZ]].
The finite simple groups are the building blocks of all finite groups, through chains of normal subgroups.
A subgroup that is reached by a chain of normal subgroups is a [[subnormal subgroup|FKTQ1WBMKM]].
A [[characteristic subgroup|0KABPMRHM2]] is a subgroup fixed by all automorphisms, and it is normal, because conjugation is an automorphism.
In Galois theory, the normal subgroups of the Galois group correspond to the intermediate fields that are normal extensions of the base field.
