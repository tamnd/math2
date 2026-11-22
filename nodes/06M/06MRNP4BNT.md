---
tag: 06MRNP4BNT
kind: statement
role: theorem
name: Every spanning set contains a basis
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [0KCQ9Y3QKA]
uses: [0VTQTPQGAV, 0BJKVF90Z6]
proofs: [GJKC4QQWAW, KS6PP0BVSD]
formal:
  - system: lean4
    library: mathlib
    decl: exists_linearIndependent
    match: stronger
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Properties
  - book: isbn:9783031410253
    locator: Section 2B
  - book: isbn:9780134860244
    locator: Section 1.6
---

## Statement

A set of vectors that reaches the whole space can be thinned out to a basis, without adding anything new.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $S \subseteq V$ be a [[spanning set|0BJKVF90Z6]] of $V$.
Then there is a subset $B \subseteq S$ that is a [[basis|0VTQTPQGAV]] of $V$.

## Remarks

### Thinning out a set by hand

Take the four vectors of $\mathbb{R}^3$
$$v_1 = (1, 2, 1), \quad v_2 = (2, 4, 2), \quad v_3 = (0, 1, 1), \quad v_4 = (1, 3, 2),$$
and let $V = \operatorname{span}(v_1, v_2, v_3, v_4)$, so that $S = \{v_1, v_2, v_3, v_4\}$ spans $V$ by definition.
The vector $v_2 = 2 v_1$ adds nothing, so we drop it, and the span stays the same.
Next, $v_4 = v_1 + v_3$, so we drop $v_4$ as well.
The two vectors left are independent, because $v_1 \ne 0$ and $v_3$ is not a multiple of $v_1$.
Indeed, a multiple $c v_1$ with first entry $0$ has $c = 0$, and $v_3 \ne 0$.
So $\{v_1, v_3\}$ is a basis of $V$ inside $S$, and $\dim V = 2$.

Row reduction does the same work in one pass.
Put the vectors as the columns of a matrix and reduce:
$$\begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 3 \\ 1 & 2 & 1 & 2 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
The pivots sit in columns $1$ and $3$, so the original columns $v_1$ and $v_3$ form a basis of the column space.
This is the algorithmic form of the theorem, and the [[pivot basis of the column space|11CSKXQNG3]] proves it in general.

### Why each hypothesis is needed

The set must span.
In $\mathbb{R}^2$ the set $S = \{(1, 0)\}$ has only the subsets $\emptyset$ and $S$, and neither spans $\mathbb{R}^2$, so no subset is a basis.

The scalars must form a field.
Over the integers, the set $\{2, 3\}$ spans $\mathbb{Z}$, since $1 = 3 - 2$.
But $\{2\}$ and $\{3\}$ do not span, and $\{2, 3\}$ is dependent, because $3 \cdot 2 - 2 \cdot 3 = 0$.
So no subset of $\{2, 3\}$ is a basis of $\mathbb{Z}$.
The proofs fail at the step where we divide by a nonzero coefficient.

For a finite set $S$, the [[proof by removal|GJKC4QQWAW]] needs no form of the axiom of choice.
For an infinite set, the [[proof by Zorn's lemma|KS6PP0BVSD]] uses the axiom of choice.

### What it gives you

A finite-dimensional space has a finite basis, and $\dim V \le \abs{S}$ for every finite spanning set $S$.
A spanning set of exactly $\dim V$ vectors has no room to lose a vector, so it is already a basis; this is half of the [[right-size criterion|096V7H13H9]].
Taking $S = V$ gives a basis of every vector space, which is the theorem that [[every vector space has a basis|00MS9VMQ9Z]].

The converse holds too.
A basis spans $V$, so every set that contains a basis spans $V$.
So a subset of $V$ spans $V$ exactly when it contains a basis.

### Watch out

Remove redundant vectors one at a time, and recheck after each removal.
In $S = \{(1, 0), (2, 0), (0, 1)\}$ both $(1, 0)$ and $(2, 0)$ are combinations of the other vectors.
If you drop both at once, only $(0, 1)$ is left, and it does not span $\mathbb{R}^2$.
Dropping one of them leaves a basis.

The basis inside $S$ is not unique either.
In the example above, $\{v_2, v_3\}$ and $\{v_1, v_4\}$ are also bases of $V$.
Finally, the zero space is spanned by $S = \{0\}$, and the basis inside it is the empty set.

### Generalizations

The [[extension theorem|0M4SXE5WW3]] combines this theorem with its mirror image: if $L \subseteq S$ with $L$ independent and $S$ spanning, there is a basis $B$ with $L \subseteq B \subseteq S$.
The same argument works in every matroid, where a spanning set always contains a basis.
In Mathlib, `exists_linearIndependent` says that every set $t$ contains an independent set $b$ with the same span as $t$, which is the theorem applied to $V = \operatorname{span}(t)$.

## Explanations

### L1 human

Suppose a set of arrows can build every vector of the space.
Some arrows may be spare, because the others can already build them.
Throw the spare arrows away, one at a time.
When no spare arrow is left, the arrows that remain form a basis.
For example, $(1, 0)$, $(0, 1)$ and $(1, 1)$ build the whole plane, and $(1, 1) = (1, 0) + (0, 1)$ is spare.

### L2 human

Here is a typical use: find a basis of the plane $V$ in $\mathbb{R}^3$ spanned by $(1, 1, 0)$, $(0, 1, 1)$ and $(1, 2, 1)$.
Put the vectors as columns and reduce:
$$\begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 0 & 1 & 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}.$$
The pivots are in columns $1$ and $2$, so $(1, 1, 0)$ and $(0, 1, 1)$ form a basis of $V$.
Check: the third column of the reduced matrix says that the third vector is $1$ times the first plus $1$ times the second, and indeed $(1, 1, 0) + (0, 1, 1) = (1, 2, 1)$.
Watch out: take the pivot columns of the original matrix, not of the reduced one, because row operations change the column space.

### L3 human

The theorem says that the spanning sets and the independent sets of a vector space meet in the bases, and that every spanning set sits above one of them.
This is the defining property of a matroid, and linear algebra is the source of the axioms of matroid theory.
Over a ring that is not a field the statement fails, as $\{2, 3\}$ in $\mathbb{Z}$ shows, and modules may have no basis at all.
In infinite dimension the theorem is a form of the axiom of choice, and the page on [[every vector space has a basis|00MS9VMQ9Z]] discusses that link.
