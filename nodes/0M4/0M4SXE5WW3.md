---
tag: 0M4SXE5WW3
kind: statement
role: theorem
name: Extension of an independent set to a basis
aliases: [basis-extension-theorem]
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [0KCQ9Y3QKA]
uses: [0VTQTPQGAV, 0EVHJFTG9Z, 0BJKVF90Z6]
proofs: [SS0XKV9TAN, MEFZB7GHA9]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Properties
  - book: isbn:9783031410253
    locator: Section 2B
  - book: isbn:9780134860244
    locator: Section 1.6
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$, and let $L \subseteq V$ be a [[linearly independent|0EVHJFTG9Z]] set.

1. There is a [[basis|0VTQTPQGAV]] $B$ of $V$ with $L \subseteq B$.
2. More precisely, if $S \subseteq V$ is a [[spanning set|0BJKVF90Z6]] with $L \subseteq S$, then there is a basis $B$ with $L \subseteq B \subseteq S$.

## Remarks

### Why each hypothesis is needed

If $L$ is dependent, then no basis contains $L$, because each subset of an independent set is independent.
Example: $L = \set{(1, 0), (2, 0)}$ in $\R^2$ fails independence, so it lies in no basis.
In part 2, the condition $L \subseteq S$ is needed: $L = \set{(1, 1)}$ and $S = \set{(1, 0), (0, 1)}$ give no basis $B$ with $L \subseteq B \subseteq S$.
Over a ring, the statement fails: $\set{2}$ is independent in $\Z$, but no basis of $\Z$ contains $2$.
The only bases of $\Z$ are $\set{1}$ and $\set{-1}$.
For infinite-dimensional $V$, the proof uses [[Zorn's lemma|04RXTQA5ZA]].

### Consequences

1. In a space of dimension $n$, each independent set has at most $n$ vectors.
2. Each subspace $U \subseteq V$ has a complement: extend a basis $B_U$ of $U$ to a basis $B$ of $V$, and let $W = \operatorname{span}(B \setminus B_U)$; then $V = U \oplus W$.
3. An independent set of exactly $\dim V$ vectors is a basis; see [[the right-size criterion|096V7H13H9]].
4. Taking $L = \emptyset$ in part 1 gives the [[existence of a basis|00MS9VMQ9Z]].

### Converse

Each subset of a basis is independent.
So a subset $L \subseteq V$ is independent if and only if it lies in some basis.

### Generalizations

Part 2 with $L = \emptyset$ gives [[every spanning set contains a basis|06MRNP4BNT]].
In a matroid, each independent set extends to a basis.
For modules, the statement holds for vector spaces over division rings, but fails for free modules over $\Z$.

## Explanations

### L1 human

We can always complete an independent set of vectors to a basis.
We keep adding vectors that point in new directions until the set reaches the whole space.
This shows that an independent set can never be larger than a basis.

### L2 human

Example: extend $L = \set{(1, 1, 0)}$ to a basis of $\R^3$, with vectors from the standard basis.
The vector $e_1 = (1, 0, 0)$ is not a multiple of $(1, 1, 0)$, so add it.
Then $e_2 = (0, 1, 0) = (1, 1, 0) - e_1$ is in the span, so skip it.
The vector $e_3 = (0, 0, 1)$ has third entry $1$, and the span has third entry $0$, so add it.
The result $\set{(1, 1, 0), (1, 0, 0), (0, 0, 1)}$ has $3 = \dim \R^3$ independent vectors, so it is a basis.
