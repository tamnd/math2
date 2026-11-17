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

Let $X$ be a class of mathematical objects and let $\sim$ be an [[equivalence relation|0G8VEZ3WTK]] on $X$, such as [[isomorphism|PZMGQMDN25]], congruence or homeomorphism.
An invariant is a function $f$ on $X$ such that $x \sim y$ implies $f(x) = f(y)$.
The invariant is complete when the converse also holds: $f(x) = f(y)$ implies $x \sim y$.
A classification of $X$ up to $\sim$ is a list that contains exactly one object from each equivalence class, often given by a complete invariant together with a description of all its values.
A classification theorem states such a list, and it is one of the most common shapes of a major result, because it answers at once each question of the form "are these two objects the same?" and "which objects exist?".

## Motivation

A notion such as "group" or "surface" has infinitely many instances, and many of them differ only in the names of their elements or in an inessential deformation.
A mathematician wants to know which instances are really different.
For this we first fix what "the same" means, by an equivalence relation.
Then we look for numbers or other data that do not change under the equivalence.
If two objects have different data, they are not equivalent.
If the data are rich enough that equal data force equivalence, the data classify the objects, and the study of the class reduces to the study of the data.

## Notation

The phrase "up to $\sim$" means "where we do not distinguish equivalent objects".
So "there are two groups of order $4$ up to isomorphism" means "there are two equivalence classes of groups of order $4$".
The set of equivalence classes is written $X/{\sim}$.
A complete invariant is the same thing as an injective map from $X/{\sim}$ to a set of data.
Some authors use "complete set of invariants" for a list of invariants that together form a complete invariant.

## Remarks

### Examples

- Triangles up to congruence. The multiset of the three side lengths is a complete invariant, and the triangle inequality describes the values that occur, as [[this example|EK106P37E4]] shows.
- Finite-dimensional vector spaces over a field $F$ up to isomorphism. The [[dimension|03GSZ8RTZJ]] is a complete invariant, and each value $n \geq 0$ occurs, by the space $F^n$, as [[this example|PRQAA1FA3Z]] shows.
- Finite abelian groups up to isomorphism. The list of prime powers in the [[classification of finite abelian groups|07CQR9BW3R]] is a complete invariant.
- Closed surfaces up to homeomorphism. Orientability and the [[Euler characteristic|RNDDWDAFJ5]] together form a complete invariant, by the [[classification of surfaces|2SFM73YET0]].
- Convex regular polyhedra up to similarity. There are exactly five, by the [[classification of the Platonic solids|0M4TCS0RRG]].
- Finite simple groups up to isomorphism. The [[classification of finite simple groups|06J6P03MG7]] gives four families: cyclic groups of prime order, alternating groups, groups of Lie type and $26$ sporadic groups.

### Non-examples

- The order of a finite group is an invariant under isomorphism, but it is not complete. [[This non-example|4PJETRFBEX]] shows that $\mathbb{Z}/4\mathbb{Z}$ and the Klein four-group have the same order but are not isomorphic.
- The Euler characteristic alone does not classify closed surfaces. The torus and the Klein bottle both have Euler characteristic $0$, but the torus is orientable and the Klein bottle is not.
- The area of a triangle is not a complete invariant for congruence. The right triangle with legs $1$ and $4$ and the right triangle with legs $2$ and $2$ both have area $2$, but their hypotenuses are $\sqrt{17}$ and $\sqrt{8}$.
- The number of sides is an invariant of polygons under congruence, but it is far from complete. A square of side $1$ and a rectangle with sides $1$ and $2$ both have four sides, and they are not congruent.

### Basic properties

- An invariant shows non-equivalence: if $f(x) \neq f(y)$, then $x \not\sim y$. This is the contrapositive of the definition.
- Equal values of an invariant that is not complete prove nothing. They only show that the invariant cannot tell the objects apart.
- If $f$ and $g$ are invariants, then the pair $(f, g)$ is an invariant, and it is at least as fine as each of them. Several weak invariants can combine to a complete one, as orientability and Euler characteristic do for surfaces.
- A complete invariant $f$ gives a bijection between $X/{\sim}$ and the set of values of $f$. A classification theorem usually describes this set of values.

### History

Euclid's Elements ends, in Book XIII, with the construction of the five regular solids and an argument that no other regular solid exists.
Felix Klein proposed in his Erlangen program of 1872 to view each geometry as the study of the invariants of a group of transformations.
The theory of algebraic invariants of polynomials was developed in the nineteenth century by Arthur Cayley, James Joseph Sylvester and others.
The classification of finite simple groups, one of the largest classification theorems, was completed in 2004.

### Common errors

- Students conclude that two objects are equivalent because they agree in one invariant. This needs a complete invariant.
- Students use a quantity that is not an invariant. The number of edges of a drawing of a surface changes when the drawing changes, so it does not classify surfaces.
- Students forget to fix the equivalence relation. "Are these two triangles the same?" has different answers for congruence and for similarity.

## Explanations

### L1 human

To classify things is to sort them into piles of things that count as "the same".
For triangles, "the same" can mean "the same shape and size".
A measurement that never changes when we move a triangle around is an invariant, for example the length of its longest side.
One measurement is usually not enough to tell all triangles apart.
But the three side lengths together are enough: two triangles with the same three side lengths have the same shape and size.
So the three side lengths classify triangles.

### L2 human

We show that the groups $\mathbb{Z}/6\mathbb{Z}$ and the symmetric group $S_3$ are not isomorphic, although both have $6$ elements.

1. The property "the group is abelian" is an invariant under isomorphism. If $\varphi \colon G \to H$ is an isomorphism and $G$ is abelian, then $\varphi(a)\varphi(b) = \varphi(ab) = \varphi(ba) = \varphi(b)\varphi(a)$, and each element of $H$ is some $\varphi(a)$.
2. The group $\mathbb{Z}/6\mathbb{Z}$ is abelian, because $a + b = b + a$ for integers.
3. In $S_3$, $(1\,2)(1\,3) = (1\,3\,2)$ and $(1\,3)(1\,2) = (1\,2\,3)$, with products computed from right to left. These differ, so $S_3$ is not abelian.
4. The invariant takes different values, so the groups are not isomorphic.

The typical use of an invariant is exactly this: to prove that two objects are different.
A trap is the reverse use.
Two groups that are both abelian and have the same order need not be isomorphic: $\mathbb{Z}/4\mathbb{Z}$ and $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ are an example.

### L3 human

A classification problem has three parts: the class of objects, the equivalence relation, and the target of the invariant.
Changing any part changes the problem.
Closed surfaces up to homeomorphism have a simple classification.
For closed $4$-manifolds, Andrey Markov Jr. proved that no algorithm decides homeomorphism.
His proof uses the fact that each finitely presented group is the fundamental group of a closed $4$-manifold.
In other cases the classification is complete but the list is hard, as for finite simple groups.

Many invariants are functors.
Homology, the fundamental group and the Euler characteristic send spaces to algebraic data, and homeomorphic spaces go to isomorphic data.
A functor is a complete invariant only in rare cases, so much of algebraic topology and of representation theory searches for finer invariants, such as [[knot invariants|GZQ5ZE3X6G]] that separate more and more knots.
In logic, classification theory in the sense of Shelah asks which first-order theories have models that can be classified by invariants at all.
The [[abstraction of a notion|976RZZCT1H]] creates a class of objects, and classification is often the next step in its study.
