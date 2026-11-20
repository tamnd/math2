---
tag: 05EGHEQZAW
kind: definition
name: Vector space
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
defines: 000AYPA9AJ
uses: [04C5ZBG1WT]
formal:
  - system: lean4
    library: mathlib
    decl: Module
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: Definition and basic properties
  - book: isbn:9783031410253
    locator: Section 1B
inventory: [FS3H3KZHNY]
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]].
A *vector space* over $F$ is a set $V$ with two maps: an addition $V \times V \to V$, $(u, v) \mapsto u + v$, and a scalar multiplication $F \times V \to V$, $(a, v) \mapsto av$.
These axioms must hold for all $u, v, w \in V$ and $a, b \in F$:

1. $u + (v + w) = (u + v) + w$ (associativity of addition).
2. $u + v = v + u$ (commutativity of addition).
3. There is an element $0 \in V$ with $v + 0 = v$ for all $v \in V$ (zero vector).
4. For each $v \in V$ there is an element $-v \in V$ with $v + (-v) = 0$ (negatives).
5. $a(bv) = (ab)v$ (compatibility of the two multiplications).
6. $1v = v$, where $1$ is the unit of $F$ (unit law).
7. $a(u + v) = au + av$ (distributivity over vectors).
8. $(a + b)v = av + bv$ (distributivity over scalars).

The elements of $V$ are *vectors*, and the elements of $F$ are *scalars*.

## Notation

We write $u - v$ for $u + (-v)$.
Some books list closure ("$u + v \in V$ and $av \in V$") as two more axioms; here closure is part of the statement that the operations are maps into $V$.

## Remarks

Axioms 1 to 4 say that $(V, +)$ is an [[abelian group|082GHNPJ53]].
The axioms give $0v = 0$ and $(-1)v = -v$ for all $v \in V$, see [[first consequences of the axioms|5E4VBC0A4H]].
A vector space is a [[module|0NZ8JA25WK]] over a field; Mathlib uses `Module F V` for both, with `[Field F]` for the vector space case.
Examples are the [[coordinate space|713F6AM1X1]] $F^n$, [[spaces of matrices|0RE6X3BGPN]] and [[function spaces|0GZB2SN0PH]].
The axioms are not independent: commutativity of addition follows from the others, by expanding $(1 + 1)(u + v)$ in two ways with axioms 7 and 8.
Axiom 6 does not follow from the others, as [[this non-example|C4AGZJBAM6]] shows.

## Explanations

### L1 human

A vector space is a collection of objects that we can add together and stretch by numbers.
Arrows in the plane are the standard picture, but polynomials and functions also form vector spaces.
The eight axioms list the rules that make the usual algebra work.

### L2 human

To show that a set with two operations is a vector space, we check each axiom with arbitrary vectors and scalars.

1. Check that the sum and the scalar multiple of elements of the set are again in the set.
2. Find the zero vector and the negative of each vector; they need not look like the number $0$ or a minus sign.
3. Check the four rules that mix scalars and vectors: axioms 5 to 8.

A trap: axiom 6 does not follow from the others, so it must be checked.
The rule $a(x, y) = (ax, 0)$ on $\R^2$ satisfies all axioms except axiom 6.
