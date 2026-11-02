---
tag: EJJYCPWHPA
kind: statement
role: lemma
name: Eckmann–Hilton argument
msc: [55Q05, 20M14]
uses: [0M418FE7BB, 07WYQPB8E3]
about: [0M418FE7BB]
sources:
  - url: https://en.wikipedia.org/wiki/Eckmann–Hilton_argument
same_as:
  wikidata: Q5332932
  wikipedia: Eckmann–Hilton argument
---

## Statement

Let $X$ be a set with two [[binary operations|0M418FE7BB]] $\circ$ and $\otimes$.
Assume that $\circ$ has an [[identity element|07WYQPB8E3]] $1_\circ$, that $\otimes$ has an identity element $1_\otimes$, and that the interchange law
$$(a \otimes b) \circ (c \otimes d) = (a \circ c) \otimes (b \circ d)$$
holds for all $a, b, c, d \in X$.
Then $1_\circ = 1_\otimes$, the two operations are equal, and this common operation is commutative and associative.

## Remarks

Put $a = d = 1_\circ$ and $b = c = 1_\otimes$ in the interchange law: the left side is $1_\circ \circ 1_\circ = 1_\circ$ and the right side is $1_\otimes \otimes 1_\otimes = 1_\otimes$, so the units agree; write $1$ for both.
Then $a \circ d = (a \otimes 1) \circ (1 \otimes d) = (a \circ 1) \otimes (1 \circ d) = a \otimes d$, so the operations agree.
Also $b \circ c = (1 \otimes b) \circ (c \otimes 1) = (1 \circ c) \otimes (b \circ 1) = c \otimes b = c \circ b$, which is commutativity.
Associativity follows in the same way from $(a \otimes b) \circ (1 \otimes c) = (a \circ 1) \otimes (b \circ c)$.
The units are needed: on a set with at least two elements, the operations $a \circ b = a$ and $a \otimes b = b$ satisfy the interchange law, but they differ.
The main application: for $n \ge 2$, the homotopy group $\pi_n(X, x_0)$ carries two compatible products, concatenation in two different coordinates, so it is abelian.

## Explanations

### L1 human

Suppose a set has two ways of combining elements, each with a neutral element, and the two ways commute with each other in the sense of the interchange law.
Then they are secretly one and the same operation, and this operation is commutative.
A picture: arrange four elements in a square grid.
Combine them first by rows and then by columns, or first by columns and then by rows; the interchange law says the results agree.

### L2 human

The argument explains why the higher homotopy groups $\pi_n$ for $n \ge 2$ are abelian, while $\pi_1$ need not be.
In dimension $n \ge 2$ there are two independent directions in which to concatenate maps of cubes.
For the same reason, the fundamental group of an H-space, such as a topological group, is abelian.
There, pointwise multiplication of loops satisfies the interchange law with concatenation.
In category theory it shows that a monoid object in the category of monoids is a commutative monoid.
It also shows that the endomorphisms of the unit object in a monoidal category form a commutative monoid.
