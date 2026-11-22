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

A vector space is a set with an addition and a scaling by elements of a field that obey eight rules of arithmetic.
Let $F$ be a [[field|04C5ZBG1WT]].
A *vector space* over $F$ is a set $V$ with two maps, an addition $V \times V \to V$, $(u, v) \mapsto u + v$, and a scalar multiplication $F \times V \to V$, $(a, v) \mapsto av$, such that the following axioms hold for all $u, v, w \in V$ and $a, b \in F$.

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
Some books add closure ($u + v \in V$ and $av \in V$) as two more axioms.
Here closure is part of the statement that the two operations are maps into $V$, so it must still be checked when a new set is proposed.

## Remarks

The axioms fall into two groups.
Axioms 1 to 4 concern only the addition, and they say that $(V, +)$ is an [[abelian group|082GHNPJ53]].
Axioms 5 to 8 tie the scalars to the vectors: axiom 5 makes repeated scaling agree with multiplication in $F$, and axioms 7 and 8 are the two distributive laws.

Axiom 6 looks too obvious to state, but it cannot be dropped.
The rule $a(x, y) = (ax, 0)$ on $\mathbb{R}^2$ satisfies every other axiom, yet $1 \cdot (0, 1) = (0, 0)$; [[this non-example|C4AGZJBAM6]] checks all eight.
Without axiom 6 the rule $av = 0$ for all $a$ and $v$ would also be allowed, and scalars would carry no information.

Axiom 2, in contrast, follows from the others.
Expand $(1 + 1)(u + v)$ in two ways.
Axiom 8 gives the first form below, and axiom 7 followed by axiom 8 gives the second, where axiom 6 turns each $1u$ into $u$:
$$(1 + 1)(u + v) = (u + v) + (u + v), \qquad (1 + 1)(u + v) = (u + u) + (v + v).$$
Cancel $u$ on the left and $v$ on the right, which uses only axioms 1, 3 and 4, and $v + u = u + v$ remains.
Books keep axiom 2 in the list anyway, because it makes the group structure visible at once.

For a small example, $\mathbb{R}^2$ with entrywise operations satisfies all eight axioms, since each one is a rule of $\mathbb{R}$ in each entry.
The concept page on [[vector spaces|000AYPA9AJ]] gives more examples, and the [[first consequences of the axioms|5E4VBC0A4H]] derives $0v = 0$ and $(-1)v = -v$.
In Mathlib, `Module F V` with `[Field F]` is exactly this definition.

## Explanations

### L1 human

A vector space is a collection of objects that you can add together and stretch by numbers.
Arrows in the plane are the standard picture, but polynomials and functions also form vector spaces.
The eight axioms list the rules that make the usual algebra work, for example $2(u + v) = 2u + 2v$.

### L2 human

To show that a set with two operations is a vector space, check the operations first and the axioms second.
First make sure that the sum and the scalar multiple of elements of the set land in the set.
Then find the zero vector and the negative of each vector, which need not look like the number $0$ or a minus sign.
Last, check axioms 5 to 8 with arbitrary vectors and scalars.
For example, on the positive reals with $x \oplus y = xy$ and $a \odot x = x^a$, the zero vector is $1$ and the negative of $x$ is $1/x$, and axiom 8 reads $x^{a + b} = x^a x^b$.
