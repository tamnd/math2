---
tag: 000AYPA9AJ
kind: concept
name: Vector space
aliases: [linear-space]
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
specializes: [0NZ8JA25WK]
uses: [04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: Definition and basic properties
  - book: isbn:9783031410253
    locator: Section 1B
  - book: isbn:9780134860244
    locator: Section 1.2
  - book: isbn:9780135367971
    locator: Section 2.1
same_as:
  wikidata: Q125977
  wikipedia: Vector space
inventory: [FS3H3KZHNY]
---

## Summary

A vector space is any collection of objects that you can add to each other and multiply by numbers, with the familiar rules of arithmetic.
Arrows, lists of numbers, matrices, polynomials and functions all qualify, so one theory of span, bases and dimension serves all of them.
Let $F$ be a [[field|04C5ZBG1WT]].
A *vector space* over $F$ is a set $V$ with an addition $V \times V \to V$ and a scalar multiplication $F \times V \to V$ such that, for all $u, v, w \in V$ and $a, b \in F$,
$$u + (v + w) = (u + v) + w, \qquad u + v = v + u, \qquad a(bv) = (ab)v, \qquad 1v = v,$$
$$a(u + v) = au + av, \qquad (a + b)v = av + bv,$$
and such that there is a zero vector $0$ with $v + 0 = v$ and each $v$ has a negative $-v$ with $v + (-v) = 0$.
The [[definition|05EGHEQZAW]] numbers these eight axioms, and the rest of the sub-area refers to them by number.

## Motivation

Arrows in the plane, columns of numbers, polynomials and continuous functions look like very different objects.
Yet in each case we add two of them, we scale one by a number, and the same rules hold: order in a sum does not matter, scaling distributes over sums, and so on.
The solutions of a [[homogeneous linear system|04KGXJG1A2]] behave the same way, and so do the solutions of a linear differential equation such as $y'' + y = 0$.

A vector space keeps only the two operations and their rules, and forgets what the objects are.
So a theorem that we prove from the axioms holds at once in every one of these settings.
For example, once the sub-area shows that every [[basis|0KCQ9Y3QKA]] of a space has the same size, we know it for $\mathbb{R}^3$, for polynomials of degree at most $5$ and for solution sets of differential equations.
The later sub-areas on [[linear maps|0NRYHJPQG2]], eigenvalues and inner products all take place inside vector spaces.

## Notation

The elements of $V$ are *vectors* and the elements of $F$ are *scalars*.
We write $0$ both for the zero vector and for the zero of $F$, and the context shows which is meant.
A *real vector space* has $F = \mathbb{R}$, and a *complex vector space* has $F = \mathbb{C}$.
Some books say *linear space*, and some list closure ($u + v \in V$ and $av \in V$) as extra axioms; here closure is part of saying that the operations are maps into $V$.
In Mathlib a vector space is a module over a field, written `[Field F] [AddCommGroup V] [Module F V]`.

## Remarks

### Familiar spaces

The first example is the [[coordinate space|713F6AM1X1]] $F^n$ of lists $(x_1, \dots, x_n)$, with entrywise operations.
In $\mathbb{R}^2$, take $u = (1, 2)$, $v = (3, -1)$ and $a = 2$.
Add and scale entry by entry, and compare the two sides of axiom 7:
$$a(u + v) = 2(4, 1) = (8, 2), \qquad au + av = (2, 4) + (6, -2) = (8, 2).$$
The two sides agree, and in general each axiom holds because it holds in each entry, where it is a rule of $F$.

The same entrywise argument works for the [[space of matrices|0RE6X3BGPN]] $M_{m \times n}(F)$, which is $F^{mn}$ written as a rectangle.
It also works for the [[space of polynomials|0JGZCDT5DN]] $F[x]$, where the entries are the coefficients: $(1 + 2x) + 3(x - x^2) = 1 + 5x - 3x^2$.
The [[spaces of functions and sequences|0GZB2SN0PH]] $F^S$ use pointwise operations, so $(f + g)(s) = f(s) + g(s)$.
Finally, a larger field is a space over a smaller one: $\mathbb{C}$ is a vector space over $\mathbb{R}$, and $\mathbb{R}$ is one over $\mathbb{Q}$.

### A space that looks strange

The operations need not be the usual ones.
On the [[positive real numbers with product as addition|DQQ6NXK1SQ]], we define $x \oplus y = xy$ and $a \odot x = x^a$.
Then the zero vector is the number $1$, since $x \oplus 1 = x$, and the negative of $x$ is $1/x$.
For example, axiom 7 with $a = 2$, $x = 3$ and $y = 5$ reads
$$2 \odot (3 \oplus 5) = 15^2 = 225, \qquad (2 \odot 3) \oplus (2 \odot 5) = 9 \cdot 25 = 225.$$
All eight axioms hold, so this is a real vector space, and the logarithm turns it into $\mathbb{R}$ with its usual operations.

### What it is not

Each axiom can fail on its own, so none of them can be left out.
On $\mathbb{R}^2$ with the usual addition, the rule $a(x, y) = (ax, 0)$ breaks only the unit law $1v = v$, since $1 \cdot (0, 1) = (0, 0)$; see [[this non-example|C4AGZJBAM6]].
The rule $a(x, y) = (a^2 x, a^2 y)$ breaks only axiom 8, since $(1 + 1) \cdot (1, 0) = (4, 0)$ while $1 \cdot (1, 0) + 1 \cdot (1, 0) = (2, 0)$; see [[the second non-example|A815XEJAF7]].

A subset of a known space can also fail closure.
The lattice $\mathbb{Z}^2$ with real scalars is not a vector space, because $\tfrac{1}{2}(1, 0) = (\tfrac{1}{2}, 0)$ is not in $\mathbb{Z}^2$.
The polynomials of degree exactly $2$ are not a vector space, because $(x^2 + x) + (-x^2) = x$ has degree $1$.

### The rules you can use

The axioms do not say that $0v = 0$, but it follows from them.
In $F$ we have $0 = 0 + 0$, so axiom 8 gives $0v = 0v + 0v$, and adding $-(0v)$ to both sides leaves $0v = 0$.
In the same way one proves $a0 = 0$, $(-1)v = -v$, and that $av = 0$ forces $a = 0$ or $v = 0$.
The [[first consequences of the axioms|5E4VBC0A4H]] collects these facts with proofs, and it also shows that the zero vector and each negative are unique.

Every [[subspace|00YC1D652K]] of a vector space is again a vector space with the same operations.
This is the usual way to find new spaces: the continuous functions on $[0, 1]$ form a subspace of all functions, so there is no need to check eight axioms again.

### Watch out

The zero vector is whatever element satisfies $v + 0 = v$, and it need not look like the number $0$.
In the positive reals above it is the number $1$, and the number $0$ is not even in the space.
A second trap is to forget the field.
The set $\mathbb{C}$ over $\mathbb{R}$ and the set $\mathbb{C}$ over $\mathbb{C}$ are different vector spaces: the first has the basis $1, i$ and dimension $2$, and the second has the basis $1$ and dimension $1$.
Finally, checking an axiom at a few sample vectors is a test, not a proof: the proof must use arbitrary vectors and scalars.

### History

Grassmann worked with sums and multiples of abstract quantities in his *Ausdehnungslehre* of 1844.
Peano gave an axiomatic definition of a real vector space in 1888.

### Try it

First, is the set of vectors $(x, y)$ in $\mathbb{R}^2$ with $x + y = 1$ a vector space with the usual operations?
No: $(1, 0)$ and $(0, 1)$ are in the set, but their sum $(1, 1)$ has $x + y = 2$, so addition leaves the set.

Second, in the positive reals with $x \oplus y = xy$ and $a \odot x = x^a$, compute $(3 \odot 2) \oplus ((-1) \odot 4)$.
This is $2^3 \cdot 4^{-1} = 8/4 = 2$.

## Explanations

### L1 human

A vector space is a collection of things that you can add together and stretch by numbers.
Arrows in the plane are the usual picture: you add two arrows by putting them head to tail, and you stretch an arrow by a number.
Lists of numbers work too, for example $(1, 2, 3) + (4, 5, 6) = (5, 7, 9)$ and $2 \cdot (1, 2, 3) = (2, 4, 6)$.
The eight axioms are the ordinary rules of arithmetic, such as "the order in a sum does not matter".
Whenever these rules hold, every fact we learn about arrows also holds for lists, polynomials and functions.

### L2 human

Here is a typical use: is the set $V$ of functions $f \colon \mathbb{R} \to \mathbb{R}$ with $f'' + f = 0$ a vector space?
We do not check eight axioms, because $V$ sits inside the space of all twice differentiable functions, which is already a vector space.
It is enough that $V$ contains $0$ and is closed under the two operations.
The zero function has $0'' + 0 = 0$, so $0 \in V$.
If $f, g \in V$ and $a \in \mathbb{R}$, then, since derivatives are linear,
$$(f + ag)'' + (f + ag) = (f'' + f) + a(g'' + g) = 0 + a \cdot 0 = 0.$$
So $V$ is a vector space, and it contains $\sin$ and $\cos$, hence also $3 \sin - 2 \cos$.
The same argument works for every homogeneous linear equation, and it is the reason that "the general solution is a combination of a few basic solutions".
Watch out: for $f'' + f = 1$ the zero function is not a solution, and the solution set is not a vector space.

### L3 human

A vector space over $F$ is a [[module|0NZ8JA25WK]] over the ring $F$, and Mathlib uses one notion for both.
The axioms say that $a \mapsto (v \mapsto av)$ is a ring homomorphism from $F$ to the endomorphism ring of the abelian group $(V, +)$.
Over a field every module is free, because [[every vector space has a basis|00MS9VMQ9Z]]; over $\mathbb{Z}$ this fails, since $\mathbb{Z}/2$ has no basis.
Vector spaces over $F$ and linear maps form a category in which each object is determined up to isomorphism by its [[dimension|03GSZ8RTZJ]].
Later sub-areas build new spaces from old ones: [[direct sums|0XYYT5KNTX]], [[quotient spaces|0BR3FY5Q8M]], [[dual spaces|07JBSZE0V4]] and [[tensor products|0BF2DE2SYK]].
