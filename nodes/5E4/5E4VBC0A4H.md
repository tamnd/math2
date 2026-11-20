---
tag: 5E4VBC0A4H
kind: statement
role: proposition
name: First consequences of the vector space axioms
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [000AYPA9AJ]
uses: [05EGHEQZAW]
proofs: [SQS8CTP3EX]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: Definition and basic properties
  - book: isbn:9783031410253
    locator: Section 1B
---

## Statement

Let $F$ be a field and let $V$ be a [[vector space|000AYPA9AJ]] over $F$, with the axioms numbered as in the [[definition|05EGHEQZAW]].
Then for all $u, v, w \in V$ and $a \in F$:

1. (Cancellation) If $u + w = v + w$, then $u = v$.
2. (Unique zero) If $z \in V$ satisfies $v + z = v$ for one vector $v$, then $z = 0$.
3. (Unique negative) If $v + w = 0$, then $w = -v$.
4. $0v = 0$, where the first $0$ is the zero of $F$ and the second is the zero vector.
5. $a0 = 0$.
6. $(-1)v = -v$.
7. If $av = 0$, then $a = 0$ or $v = 0$.

## Remarks

### Why each hypothesis is needed

1. Part 7 needs inverses of nonzero scalars, so it needs $F$ to be a field. Over the ring $\Z$, the module $\Z/2$ has $2 \cdot \bar 1 = \bar 0$ with $2 \ne 0$ and $\bar 1 \ne \bar 0$.
2. Part 4 needs axiom 8. On $\R^2$ with the rule $a(x, y) = (x, y)$ for every $a$, all axioms except axiom 8 hold, and $0 \cdot (1, 0) = (1, 0) \ne 0$.
3. Part 6 uses axiom 6. With $a(x, y) = (0, 0)$ for every $a$, all axioms except axiom 6 hold, and $(-1)(1, 0) = (0, 0) \ne -(1, 0)$.

### Consequences

1. The zero vector and the negative of a vector are determined by the operations, so the notation $0$ and $-v$ is well defined.
2. $(-a)v = -(av) = a(-v)$, by part 6 and axiom 5: $(-a)v = ((-1)a)v = (-1)(av)$.
3. A nonzero vector space over an infinite field is infinite: by part 7, the multiples $av$ of a vector $v \ne 0$ are pairwise different.

### Converse

The converse of part 7 holds: if $a = 0$ or $v = 0$, then $av = 0$, by parts 4 and 5.

### Generalizations

Parts 1 to 6 hold in every module over a ring, with the same proofs.
Part 7 holds for modules over a division ring, and it fails over rings with zero divisors or with torsion modules.

## Explanations

### L1 human

The axioms do not say that "zero times a vector is the zero vector".
We still expect it, and it follows from the axioms in a few lines.
For example, $0 \cdot (3, 4) = (0, 0)$ in the plane.
In the same way, $(-1)$ times a vector is the vector that points the other way.

### L2 human

We see each part at work in $\R^2$ with $v = (3, 4)$.

1. Part 4: $0 \cdot (3, 4) = (0 \cdot 3, 0 \cdot 4) = (0, 0)$.
2. Part 6: $(-1)(3, 4) = (-3, -4)$, and $(3, 4) + (-3, -4) = (0, 0)$, so this is $-v$.
3. Part 7: if $a(3, 4) = (0, 0)$, then $3a = 0$, so $a = 0$.

The typical use is in computations with abstract vectors, where we may only use the axioms.
A trap: in an unusual vector space these facts still hold, but the zero vector may look different; in the [[positive reals|DQQ6NXK1SQ]] the zero vector is the number $1$.

### L3 human

Parts 1 to 3 are facts about groups: they use only axioms 1 to 4.
Parts 4 to 6 say that $a \mapsto (v \mapsto av)$ is a ring homomorphism from $F$ to the endomorphism ring of $(V, +)$, so it sends $0$ to $0$ and $-1$ to $-1$.
Part 7 says that $V$ is torsion-free, which is automatic over a field and is the first difference between vector spaces and general modules.
