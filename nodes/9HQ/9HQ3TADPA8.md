---
tag: 9HQ3TADPA8
kind: concept
name: Classification and invariants
msc: ["00A35"]
topics: [N4P3E53HM0]
audience: ug1
uses: [0G8VEZ3WTK, PZMGQMDN25, 976RZZCT1H, F3NNR77WKP]
sources:
  - url: https://en.wikipedia.org/wiki/Classification_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Invariant_(mathematics)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Complete_set_of_invariants
    locator: lead section
---

## Summary

To classify objects is to decide which of them count as the same and then to list one of each kind.
The tool is an invariant: a number or other piece of data that does not change when an object is replaced by an equivalent one, so that different values prove that two objects are different.

Let $X$ be a class of objects and let $\sim$ be an [[equivalence relation|0G8VEZ3WTK]] on $X$, such as [[isomorphism|PZMGQMDN25]], congruence or homeomorphism.
An *invariant* is a function $f$ on $X$ such that $x \sim y$ implies $f(x) = f(y)$.
The invariant is *complete* when the converse also holds, so that $f(x) = f(y)$ implies $x \sim y$.
A *classification* of $X$ up to $\sim$ is a list that contains exactly one object from each equivalence class, and it is often given by a complete invariant together with a description of all its values.
A *classification theorem* states such a list, and it is one of the most common shapes of a major result.

## Motivation

A notion such as "group" or "surface" has infinitely many instances, and many of them differ only in the names of their elements or by a harmless deformation.
So a mathematician first fixes what "the same" means, by an equivalence relation, and then looks for data that the relation does not change.
If two objects have different data, they are not equivalent, and that is often the only practical way to prove it.
If the data are rich enough that equal data force equivalence, the data classify the objects, and the study of the whole class reduces to the study of the data.

Classification is often the next step after [[abstraction|976RZZCT1H]] has produced a new notion.
It answers two questions at once: "are these two objects the same?" and "which objects exist?".

## Notation

The phrase "up to $\sim$" means "where we do not distinguish equivalent objects".
So "there are two groups of order $4$ up to isomorphism" means "the groups of order $4$ fall into two isomorphism classes".
The set of equivalence classes is written $X/{\sim}$, and a complete invariant is the same thing as an injective map from $X/{\sim}$ to a set of data.
Some authors say "complete set of invariants" for a list of invariants that together form a complete invariant.

## Remarks

### Three side lengths classify a triangle

Take the triangles in the plane up to congruence.
The multiset of the three side lengths is an invariant, because a rigid motion keeps distances.
It is complete, by side-side-side congruence.
Its values are exactly the multisets $\{a, b, c\}$ of positive numbers in which each number is less than the sum of the other two, so $\{3, 4, 5\}$ occurs and $\{1, 2, 4\}$ does not, since $4 > 1 + 2$.
[[The triangle example|EK106P37E4]] checks each step and builds the triangle with sides $3$, $4$ and $5$.

The choice of equivalence matters.
Up to similarity, the side lengths stop being an invariant, since a similarity can double them, and the multiset of the three angles takes their place.

### One number for a whole class

Fix a field $F$ and take the finite-dimensional vector spaces over $F$ up to isomorphism.
The [[dimension|03GSZ8RTZJ]] is a complete invariant, and every value $n \ge 0$ occurs, through the space $F^n$.
So the list $F^0, F^1, F^2, \dots$ is a complete classification.
The space of real polynomials of degree at most $2$ has the basis $1, x, x^2$, so it has dimension $3$ and is isomorphic to $\mathbb{R}^3$, as [[the dimension example|PRQAA1FA3Z]] shows.

### Invariants that are not complete

The order of a finite group is an invariant, since an isomorphism is a bijection.
It is not complete: $\mathbb{Z}/4\mathbb{Z}$ has an element of order $4$, the Klein four-group has none, and both have $4$ elements, as [[the order non-example|4PJETRFBEX]] proves.
The area of a triangle fails in the same way.
The right triangles with legs $1, 4$ and with legs $2, 2$ both have area $2$, but their hypotenuses are $\sqrt{17}$ and $\sqrt{8}$.

Weak invariants can combine into a complete one.
The [[Euler characteristic|RNDDWDAFJ5]] alone does not classify connected closed surfaces, because the [[torus|03NM7DZXXC]] and the [[Klein bottle|6J4C2P3ZHC]] both have Euler characteristic $0$.
The torus is orientable and the Klein bottle is not, and the pair (orientability, Euler characteristic) is complete, by the [[classification of surfaces|2SFM73YET0]].

### Classification theorems across mathematics

Many central results have this shape.
By the [[classification of finite abelian groups|07CQR9BW3R]], every finite abelian group is a product of cyclic groups of prime power order, and the list of these prime powers is a complete invariant.
For order $8 = 2^3$ the lists come from the ways to write $3$ as a sum of positive integers, $3$, $2 + 1$ and $1 + 1 + 1$, so there are exactly three abelian groups of order $8$:
$$\mathbb{Z}/8\mathbb{Z}, \qquad \mathbb{Z}/4\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}, \qquad \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}.$$
There are exactly five convex regular polyhedra up to similarity, by the [[classification of the Platonic solids|0M4TCS0RRG]].
The [[classification of finite simple groups|06J6P03MG7]] lists the cyclic groups of prime order, the alternating groups, the groups of Lie type and $26$ sporadic groups.

### The rules you can use

An invariant proves non-equivalence: if $f(x) \ne f(y)$, then $x \not\sim y$, which is the contrapositive of the definition.
Equal values of an incomplete invariant prove nothing, since they only show that this invariant cannot tell the objects apart.
If $f$ and $g$ are invariants, the pair $(f, g)$ is an invariant that separates at least as many objects as each of them.
A complete invariant gives a bijection between $X/{\sim}$ and its set of values, and a classification theorem usually describes that set.

### Watch out

The most common error is to conclude that two objects are equivalent because they agree in one invariant.
The groups $\mathbb{Z}/4\mathbb{Z}$ and $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ are both abelian and both have order $4$, but they are not isomorphic, because only the first has an element of order $4$.
A second error is to use a quantity that is not an invariant at all.
The number of edges in a drawing of a surface changes when the drawing changes, so it cannot classify surfaces, while the Euler characteristic, vertices minus edges plus faces, does not change.
A third error is to forget to fix the equivalence relation, since "are these two triangles the same?" has different answers for congruence and for similarity.

### History

Euclid's Elements ends, in Book XIII, with the construction of the five regular solids and an argument that no other regular solid exists.
Felix Klein proposed in his [[Erlangen program|9QW65PGEPW]] of 1872 to view each geometry as the study of the invariants of a group of transformations.
Arthur Cayley, James Joseph Sylvester and others developed the theory of algebraic invariants of polynomials in the nineteenth century.
The classification of finite simple groups, one of the largest classification theorems, was completed in 2004.

### Try it

First, are the triangles with sides $3, 4, 5$ and $6, 8, 10$ congruent, and are they similar?
They are not congruent, because the multisets of side lengths differ, but they are similar, because the second triangle is the first scaled by $2$.

Second, show that $\mathbb{Z}/8\mathbb{Z}$ and $\mathbb{Z}/4\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ are not isomorphic.
The element $1$ of $\mathbb{Z}/8\mathbb{Z}$ has order $8$, while every element $(x, y)$ of the second group satisfies $4 \cdot (x, y) = (0, 0)$, so no element there has order $8$.

## Explanations

### L1 human

To classify things is to sort them into piles of things that count as "the same".
For triangles, "the same" can mean "the same shape and size".
A measurement that never changes when we move a triangle around is an invariant, for example the length of its longest side.
One measurement is usually not enough to tell all triangles apart.
But the three side lengths together are enough, because two triangles with the same three side lengths have the same shape and size.

### L2 human

Here is a typical use: the groups $\mathbb{Z}/6\mathbb{Z}$ and $S_3$ both have $6$ elements, and we show that they are not isomorphic.
The property "abelian" is an invariant.
If $\varphi \colon G \to H$ is an isomorphism and $G$ is abelian, then every element of $H$ is some $\varphi(a)$, and
$$\varphi(a)\varphi(b) = \varphi(ab) = \varphi(ba) = \varphi(b)\varphi(a).$$
The group $\mathbb{Z}/6\mathbb{Z}$ is abelian, because addition of integers is commutative.
In $S_3$, with products computed from right to left, $(1\,2)(1\,3) = (1\,3\,2)$ and $(1\,3)(1\,2) = (1\,2\,3)$.
These differ, so $S_3$ is not abelian, and the two groups are not isomorphic.
Invariants are the standard way to prove that two objects differ.
Watch out for the reverse use: two abelian groups of the same order still need not be isomorphic, as $\mathbb{Z}/4\mathbb{Z}$ and $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ show.

### L3 human

A classification problem has three parts: the class of objects, the equivalence relation and the target of the invariant, and changing any part changes the problem.
Connected closed surfaces up to homeomorphism have a short list.
For closed $4$-manifolds, Andrey Markov Jr. proved that no algorithm decides homeomorphism, using the fact that every finitely presented group is the fundamental group of a closed $4$-manifold.
In other cases the classification is complete but the list is long and hard, as for finite simple groups.

Many invariants are functors.
Homology, the fundamental group and the Euler characteristic send spaces to algebraic data, and homeomorphic spaces go to isomorphic data.
Such a functor is rarely a complete invariant, so much of algebraic topology and representation theory searches for finer invariants, such as the [[knot invariants|GZQ5ZE3X6G]] that separate more and more knots.
In logic, classification theory in the sense of Shelah asks which first-order theories have models that can be classified by invariants at all.
