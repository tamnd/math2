---
tag: ~fbfe9e5e
kind: definition
name: Residuated Boolean algebra
msc: ["03G15", "06E25", "06F05"]
topics: [QYA4H5Y7VR]
audience: research
defines: KCG48CWY69
uses: [S9Z6PKTXAS, 0XADJKM699, 0N6R902FG1]
sources:
  - url: https://en.wikipedia.org/wiki/Residuated_Boolean_algebra
    locator: Definition; Conjugation
  - book: isbn:9780444521415
---

## Definition

A *residuated Boolean algebra* is a structure $(A, \land, \lor, \neg, 0, 1, \cdot, e, \backslash, /)$ such that:

1. $(A, \land, \lor, \neg, 0, 1)$ is a [[Boolean algebra|0XADJKM699]].
2. $(A, \cdot, e)$ is a [[monoid|0N6R902FG1]].
3. Residuation: for all $x, y, z \in A$, we have $x \cdot y \le z$ iff $y \le x \backslash z$ iff $x \le z / y$.

So it is a [[residuated lattice|S9Z6PKTXAS]] whose lattice reduct is Boolean.

## Notation

The conjugates are $x \rhd z := \neg(x \backslash \neg z)$ and $z \lhd y := \neg(\neg z / y)$.
Clause 3 is equivalent to the conjugation law: $(x \cdot y) \land z = 0$ iff $y \land (x \rhd z) = 0$ iff $x \land (z \lhd y) = 0$.
To see one half, note that $y \le x \backslash \neg z$ iff $y \land \neg(x \backslash \neg z) = 0$, and that $x \cdot y \le \neg z$ iff $(x \cdot y) \land z = 0$.

## Remarks

1. Example: [[the formal languages over an alphabet|~92bb6b9d]], with concatenation.
2. Example: [[a Boolean algebra with multiplication $\land$|~0eedd6e6]].
3. Non-example: [[a Boolean algebra with multiplication $\lor$|~9f52e2ba]] satisfies clauses 1 and 2, but fails clause 3.
4. Clause 3 holds iff two identities and the monotonicity of the operations hold, as for every residuated lattice. So the class is a variety.
5. Relation algebras are the residuated Boolean algebras with an operation $x^{\smile}$ such that $x^{\smile} \rhd e = x = e \lhd x^{\smile}$, by a result of Jónsson and Tsinakis.

## Explanations

### L1 human

Start with the algebra of sets.
Add a way to put two elements in sequence, with a neutral element.
Ask that each sequence can be undone in the best way on the left and on the right.

### L2 human

1. Take $A = \set{0, 1}$, with $x \cdot y = x \land y$ and $e = 1$.
2. Put $x \backslash z = z / x = \neg x \lor z$.
3. Check one case: $1 \cdot y \le 0$ iff $y = 0$ iff $y \le \neg 1 \lor 0 = 0$.
4. The other cases are similar, so this is a residuated Boolean algebra.

The typical use: conjugation lets one work with $\land$ and $0$ instead of with the order.
The trap: clause 2 asks for a unit $e$, and $e$ need not be the top $1$.
