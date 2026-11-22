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

The rules of school algebra for zero and for minus signs hold in every vector space, even though the axioms do not list them.
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

### A check in the plane

In $\mathbb{R}^2$ with $v = (3, 4)$, part 4 reads $0 \cdot (3, 4) = (0, 0)$, and part 6 reads $(-1)(3, 4) = (-3, -4)$.
Both are obvious from the entries here, so the point of the statement is that they also hold in spaces where we cannot compute entry by entry.
In the [[positive reals with product as addition|DQQ6NXK1SQ]], the zero vector is the number $1$ and scaling is a power.
There part 4 says $x^0 = 1$, and part 6 says $x^{-1} = 1/x$ is the negative of $x$.

### Why each hypothesis is needed

Part 7 divides by the scalar $a$, so it needs $F$ to be a field.
Over the ring $\mathbb{Z}$, the module $\mathbb{Z}/2$ has $2 \cdot \bar{1} = \bar{0}$, although $2 \ne 0$ and $\bar{1} \ne \bar{0}$.

Part 4 rests on axiom 8.
On $\mathbb{R}^2$ with the usual addition and the rule $a(x, y) = (x, y)$ for every $a$, axioms 5, 6 and 7 hold, since every product is the vector itself.
Axiom 8 fails, because $(a + b)v = v$ while $av + bv = 2v$, and part 4 fails with it: $0 \cdot (1, 0) = (1, 0)$.

Part 6 rests on axiom 6.
With the rule $a(x, y) = (0, 0)$ for every $a$, axioms 5, 7 and 8 hold, since both sides are always $(0, 0)$, but $1v = 0 \ne v$.
Then $(-1)(1, 0) = (0, 0)$, which is not $-(1, 0) = (-1, 0)$.

### What it gives you

Parts 2 and 3 say that the zero vector and the negative of a vector are determined by the addition, so the symbols $0$ and $-v$ have one meaning.
Combining part 6 with axiom 5 gives the sign rules
$$(-a)v = ((-1)a)v = (-1)(av) = -(av), \qquad a(-v) = a((-1)v) = (a(-1))v = (-a)v.$$
Part 7 shows that a nonzero space over an infinite field is infinite.
If $v \ne 0$ and $av = bv$, then $(a - b)v = 0$, so $a = b$, and the multiples of $v$ are pairwise different.

### The converse

The converse of part 7 is true: if $a = 0$ or $v = 0$, then $av = 0$, by parts 4 and 5.

### Generalizations

Parts 1 to 3 use only axioms 1 to 4, so they hold in every abelian group, and in fact in every group.
Parts 1 to 6 hold in every module over a ring, with the same proofs.
Part 7 holds for modules over a division ring, and it fails for modules with torsion, such as $\mathbb{Z}/2$ over $\mathbb{Z}$.

## Explanations

### L1 human

The rules of a vector space do not say that zero times a vector is the zero vector.
We still expect it, and it follows from the rules in a few lines.
For example, $0 \cdot (3, 4) = (0, 0)$ in the plane.
In the same way, $-1$ times a vector is the arrow of the same length that points the other way.

### L2 human

Here is a typical use: solve $3v + w = 5v$ for $v$ in an abstract vector space.
Add $-(3v)$ to both sides and use part 1, then collect the multiples of $v$ with axiom 8 and the sign rules:
$$w = 5v + (-(3v)) = 5v + (-3)v = (5 - 3)v = 2v.$$
Now multiply both sides by $\tfrac{1}{2}$ and use axioms 5 and 6, so $v = \tfrac{1}{2} w$.
Every step was a rule of the statement or an axiom, and this is how all algebra with abstract vectors runs.
Watch out: the step from $2v = w$ to $v = \tfrac{1}{2} w$ needs $2 \ne 0$ in $F$, which fails over the field $\mathbb{F}_2$.

### L3 human

Parts 4 to 6 say that the map $a \mapsto (v \mapsto av)$ from $F$ to the endomorphism ring of $(V, +)$ is a ring homomorphism, so it sends $0$ to $0$ and $-1$ to $-1$.
Part 7 says that $V$ has no torsion, which is automatic over a field and is the first difference between vector spaces and general [[modules|0NZ8JA25WK]].
The same arguments reappear for rings, where $0 \cdot r = 0$ is proved by the same trick $0 = 0 + 0$.
