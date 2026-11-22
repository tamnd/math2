---
tag: E2ZRZGXSNX
kind: statement
role: proposition
name: A basis gives unique coordinates
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [0KCQ9Y3QKA]
uses: [0VTQTPQGAV, 0EVHJFTG9Z, 0BJKVF90Z6]
proofs: [2X763GJP3M]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 2B
  - book: isbn:9780134860244
    locator: Section 1.6
---

## Statement

A family is a basis exactly when every vector can be built from it in one and only one way.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $(b_i)_{i \in I}$ be a family of vectors of $V$.
Then $(b_i)_{i \in I}$ is a [[basis|0VTQTPQGAV]] of $V$ if and only if, for each $v \in V$, there is exactly one family of scalars $(a_i)_{i \in I}$, with $a_i \ne 0$ for only finitely many $i$, such that
$$v = \sum_{i \in I} a_i b_i.$$

## Remarks

### A first computation

Take the basis $(1, 1), (1, -1)$ of $\mathbb{R}^2$ and the vector $(3, 1)$.
We look for $c$ and $d$ with $c(1, 1) + d(1, -1) = (3, 1)$, that is,
$$c + d = 3, \qquad c - d = 1.$$
Adding the equations gives $2c = 4$, so $c = 2$, and then $d = 1$.
The steps leave no choice, so this is the only solution.
Check: $2(1, 1) + 1(1, -1) = (3, 1)$.

### Why each condition is needed

The two halves of "exactly one" come from the two conditions of a basis.
Spanning gives at least one expression.
Without it, some vectors have no expression at all: $(0, 0, 1)$ is not a combination of $(1, 0, 0)$ and $(0, 1, 0)$.

Independence gives at most one expression.
Without it, coordinates are ambiguous: in the spanning family $(1, 0), (0, 1), (1, 1)$ of $\mathbb{R}^2$, the vector $(1, 1)$ is both $1 (1, 0) + 1 (0, 1) + 0 (1, 1)$ and $0 (1, 0) + 0 (0, 1) + 1 (1, 1)$.
In fact any two expressions differ by a relation among the vectors, and independence says that the only relation is the trivial one.

### What it gives you

For an ordered basis $B = (b_1, \dots, b_n)$, the map that sends $v$ to its list of coefficients is well defined.
This list is the [[coordinate vector|04CYQHN6MC]] $[v]_B$, and the map $v \mapsto [v]_B$ is a [[linear isomorphism onto F^n|059THXBRBB]].
The same uniqueness is the reason that a linear map is [[fixed by its values on a basis|0R8X9XA83A]], and that any choice of those values gives exactly one linear map.

### The converse

The statement is already an equivalence.
In the backward direction we use less than the full hypothesis.
Existence of an expression for every $v$ gives spanning, and uniqueness for the single vector $v = 0$ gives independence.

### Generalizations

Over a ring $R$ in place of $F$, the same equivalence holds with the same proof, and the modules that have such a family are the [[free modules|0DZ9DKAKZR]].
For a [[Schauder basis|528G11SDWR]] of a Banach space, the expression $v = \sum_i a_i b_i$ is a convergent series, and uniqueness becomes part of the definition rather than a consequence of independence.

## Explanations

### L1 human

With a basis, every vector has one and only one recipe made from the basis vectors.
Spanning means that a recipe always exists.
Independence means that two different recipes never give the same vector.
For example, with the steps $(1, 1)$ and $(1, -1)$, the point $(3, 1)$ is two of the first step and one of the second, and nothing else works.

### L2 human

Here is a typical use in the [[space of polynomials|0JGZCDT5DN]] $P_2(\mathbb{R})$, with the basis $1, x - 1, (x - 1)^2$.
Write $p(x) = x^2 + 3x$ in this basis.
Put $t = x - 1$, so $x = t + 1$ and
$$p = (t + 1)^2 + 3(t + 1) = t^2 + 5t + 4.$$
So $p = 4 \cdot 1 + 5 (x - 1) + 1 (x - 1)^2$.
Uniqueness tells us that any other method, such as comparing coefficients, must give the same three numbers $4, 5, 1$.
Watch out: the coefficients of $p$ in the monomial basis are $0, 3, 1$, so the coordinates depend on the basis.

### L3 human

The statement says that the linear map $F^{(I)} \to V$, $(a_i) \mapsto \sum_i a_i b_i$, is a bijection exactly when $(b_i)$ is a basis.
Spanning is surjectivity of this map, and independence is injectivity, since the kernel consists of the relations among the $b_i$.
In this form the result is a special case of the fact that a linear map is [[injective exactly when its kernel is zero|0BJBYCGMWE]], which the sub-area on linear maps proves.
