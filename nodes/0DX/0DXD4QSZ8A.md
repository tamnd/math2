---
tag: 0DXD4QSZ8A
kind: concept
name: Conjugate elements
msc: ["20E45"]
topics: [E1506A5A55]
audience: ug1
uses: [G5S1M9, 0ZNZH0EXFX, 0WE2NHZJ7B]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugacy_class
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Conjugacy_class
    locator: Properties
  - book: isbn:9780471433347
    locator: Section 4.3
---

## Summary

Let $G$ be a [[group|G5S1M9]].
Two elements $a$ and $b$ of $G$ are conjugate in $G$ when there is an element $g \in G$ with $b = gag^{-1}$.
The element $gag^{-1}$ is the conjugate of $a$ by $g$, and the map $c_g \colon G \to G$, $c_g(x) = gxg^{-1}$, is conjugation by $g$.
Conjugate elements behave in the same way inside the group, because conjugation by $g$ only changes the names of the elements.

## Motivation

In the [[symmetric group|0515A6D2Y1]] $S_3$, the transpositions $(1\,2)$ and $(2\,3)$ are different elements.
But they do the same kind of thing: each one swaps two points and fixes the third.
If we rename the points $1, 2, 3$ by a permutation $g$, then $(1\,2)$ becomes another transposition, and this new transposition is $g(1\,2)g^{-1}$.
In linear algebra, a linear map has a different matrix $A$ in each basis.
A change of basis replaces $A$ by $PAP^{-1}$ for an invertible matrix $P$.
Conjugation is the general form of these two "changes of names", and conjugate elements are the elements that differ only by such a change.

## Notation

We write $gag^{-1}$ for the conjugate of $a$ by $g$, and $a \sim b$ when $a$ and $b$ are conjugate.
Some books, for example many books on finite groups, use $a^g = g^{-1}ag$ instead.
The two conventions give the same relation, because $g^{-1}ag = hah^{-1}$ with $h = g^{-1}$.
The set of all conjugates of $a$ is the [[conjugacy class|0DEBXAJ5SA]] of $a$.

## Remarks

### Examples

- In each group, the identity $e$ is conjugate only to itself, because $geg^{-1} = gg^{-1} = e$ for each $g$.
- In an [[abelian group|082GHNPJ53]], each element is conjugate only to itself, because $gag^{-1} = agg^{-1} = a$.
- In $S_3$, the three transpositions are conjugate to each other: [[the transpositions of S3 are conjugate|~50e0bc16]].
- In the [[general linear group|0FCHE902D7]] $\mathrm{GL}_2(\mathbb{R})$, two matrices are conjugate exactly when they are similar: [[similar matrices are conjugate in GL2|~f37c5588]].
- In the [[quaternion group|0NRJGW864D]] $Q_8$, the elements $i$ and $-i$ are conjugate, because $j^{-1} = -j$ and $jij^{-1} = (ji)(-j) = (-k)(-j) = kj = -i$.

### Non-examples

- In $S_3$, the transposition $(1\,2)$ and the $3$-cycle $(1\,2\,3)$ are not conjugate, because they have different orders: [[a transposition and a 3-cycle are not conjugate|~4dee2623]].
- In $\mathbb{Z}/3\mathbb{Z}$, the elements $1$ and $2$ both have order $3$, but they are not conjugate, because the group is abelian and $1 \ne 2$.
- In the [[alternating group|0Z5905Q73D]] $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$, the two $3$-cycles are not conjugate, because $A_3$ is abelian. In the larger group $S_3$ they are conjugate.

### Basic properties

- Conjugacy is an [[equivalence relation|0G8VEZ3WTK]] on $G$. It is reflexive, because $a = eae^{-1}$. It is symmetric, because $b = gag^{-1}$ gives $a = g^{-1}b(g^{-1})^{-1}$. It is transitive, because $b = gag^{-1}$ and $c = hbh^{-1}$ give $c = (hg)a(hg)^{-1}$.
- The equivalence classes of conjugacy are the conjugacy classes, so the conjugacy classes partition $G$.
- Conjugation $c_g$ is a [[group homomorphism|0JYTG5K9Y4]], because $c_g(x)c_g(y) = gxg^{-1}gyg^{-1} = gxyg^{-1} = c_g(xy)$. It is a bijection with inverse $c_{g^{-1}}$, so it is an [[inner automorphism|0RN00NTM3S]] of $G$.
- For each integer $n$, $(gag^{-1})^n = ga^ng^{-1}$, because $c_g$ is a homomorphism and [[homomorphisms preserve powers|08FKQD7NJ3]].
- Conjugate elements have the same [[order|0WE2NHZJ7B]]. By the previous property, $(gag^{-1})^n = e$ exactly when $ga^ng^{-1} = e$, that is, when $a^n = e$.
- An element $a$ is conjugate only to itself exactly when $ga = ag$ for each $g \in G$, that is, when $a$ is in the [[centre|0DZ93493VN]] of $G$.
- Two matrices $A$ and $B$ in $\mathrm{GL}_n(F)$ are conjugate exactly when they are [[similar|0E89HQATM8]]. Then they are the matrices of one [[linear map|0NRYHJPQG2]] in two bases, and $P$ is a change of basis matrix.
- Conjugate matrices in $\mathrm{GL}_n(F)$ have the same [[determinant|00KDZRW4C0]], because $\det(PAP^{-1}) = \det(P)\det(A)\det(P)^{-1} = \det(A)$.

### History

Conjugation of matrices is the change of basis of linear algebra, and the classification of square matrices up to conjugation is a classical problem.
Camille Jordan published the [[Jordan normal form|085HQ5G5TE]] in 1870, and this normal form describes the conjugacy classes of $\mathrm{GL}_n(\mathbb{C})$.

### Common errors

- Conjugacy depends on the group. The $3$-cycles $(1\,2\,3)$ and $(1\,3\,2)$ are conjugate in $S_3$, but not in its subgroup $A_3$.
- Elements with the same order need not be conjugate. The elements $1$ and $2$ of $\mathbb{Z}/3\mathbb{Z}$ have the same order and are not conjugate.
- A conjugate $gag^{-1}$ is not in general equal to $a$. The equation $gag^{-1} = a$ holds only when $g$ and $a$ commute.

## Explanations

### L1 human

Two elements of a group are conjugate when one becomes the other after a renaming.
Think of three cups in a row, numbered $1$, $2$ and $3$.
The move "swap cups $1$ and $2$" and the move "swap cups $2$ and $3$" are different moves.
But if a friend first renames the cups, the first move can turn into the second move.
So the two moves are of the same type, and group theory calls them conjugate.
A swap of two cups and a turn of all three cups are not of the same type, so they are not conjugate.

### L2 human

We find the conjugacy class of $a = (1\,2\,3)$ in $S_3$.
We compose permutations from right to left, so $\sigma\tau$ means first $\tau$, then $\sigma$.

1. For $g$ in the subgroup $\{e, (1\,2\,3), (1\,3\,2)\}$, $g$ commutes with $a$, because all three elements are powers of $a$. So $gag^{-1} = a$.
2. Let $g = (1\,2)$, so $g^{-1} = (1\,2)$. We follow each point through $(1\,2)$, then $(1\,2\,3)$, then $(1\,2)$.
3. The point $1$ goes to $2$, then to $3$, then stays at $3$. The point $3$ stays at $3$, then goes to $1$, then to $2$. The point $2$ goes to $1$, then to $2$, then to $1$.
4. So $(1\,2)(1\,2\,3)(1\,2)^{-1} = (1\,3\,2)$.
5. Each of the other two transpositions is $(1\,2)$ times an element of step 1. Thus they also send $a$ to $(1\,3\,2)$.
6. The conjugacy class of $(1\,2\,3)$ is $\{(1\,2\,3), (1\,3\,2)\}$.

A typical use of conjugacy is a proof that two elements are not conjugate: compute an invariant, such as the order or the determinant, and show that it differs.
In $\mathrm{GL}_2(\mathbb{R})$ the matrices $\operatorname{diag}(1, 2)$ and $\operatorname{diag}(1, 3)$ are not conjugate, because their determinants are $2$ and $3$.

A trap is the converse of this test.
Equal invariants do not prove that two elements are conjugate.
The matrices $I$ and $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ have the same determinant, the same trace and the same eigenvalues, but they are not conjugate, because $PIP^{-1} = I$ for each $P$.

### L3 human

Conjugation is the action of $G$ on itself by $g \cdot x = gxg^{-1}$, and the conjugacy classes are the orbits of this [[group action|0WCY42EV9V]].
The [[orbit-stabiliser theorem|0E2HSCKZ6C]] gives that the size of the class of $a$ is the index of its [[centraliser|02YYV36BFM]], and summing over the classes gives the [[class equation|08BPSC6YTE]].
The map $g \mapsto c_g$ is a homomorphism from $G$ to its [[automorphism group|0K1SCPBNKJ]], with kernel the centre and image the group of inner automorphisms.

In concrete groups, the classification of conjugacy classes is often a central result.
In $S_n$, two permutations are conjugate exactly when they have the same cycle type ([[conjugacy classes of symmetric groups|0J438GAC8K]]).
In $\mathrm{GL}_n(\mathbb{C})$, two matrices are conjugate exactly when they have the same Jordan normal form.
In topology, conjugacy classes of the fundamental group correspond to free homotopy classes of loops.
The same idea applies to subgroups, which gives [[conjugate subgroups|0H11ZPX4ND]], and the subgroups that are equal to all their conjugates are the [[normal subgroups|0CB0DX5BVV]].
