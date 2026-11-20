---
tag: ~aa47af8f
kind: definition
name: BL-algebra
msc: ["03G25", "06D35", "03B52"]
topics: [QYA4H5Y7VR]
audience: research
defines: ~d07e9350
uses: [S9Z6PKTXAS, 0N6R902FG1, TGQ8T276MG]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: "5. Other notable fuzzy logics; 7. Algebraic semantics"
  - url: https://en.wikipedia.org/wiki/BL_(logic)
    locator: Semantics
  - book: isbn:9780792352389
---

## Definition

A *BL-algebra* is a structure $(A, \land, \lor, \otimes, \to, 0, 1)$ such that, for all $x, y, z \in A$:

1. $(A, \land, \lor, 0, 1)$ is a bounded lattice.
2. $(A, \otimes, 1)$ is a commutative [[monoid|0N6R902FG1]].
3. Residuation: $x \otimes y \le z$ iff $x \le y \to z$.
4. Prelinearity: $(x \to y) \lor (y \to x) = 1$.
5. Divisibility: $x \land y = x \otimes (x \to y)$.

Clauses 1 to 4 define an MTL-algebra; clauses 1 to 3 define a bounded commutative integral [[residuated lattice|S9Z6PKTXAS]].
A *BL-chain* is a BL-algebra whose order is linear.

## Notation

We write $\neg x := x \to 0$.
The standard BL-algebra of a continuous t-norm $\ast$ is $[0, 1]$ with $\otimes = \ast$ and $\to$ its residuum.

## Remarks

1. Example: [[the Gödel three-element chain|~6b09f453]], with $\otimes = \min$.
2. Non-example: [[a five-element Heyting algebra|~32d5d900]] satisfies clauses 1 to 3 and 5, but fails clause 4.
3. Divisibility says that the meet is definable from $\otimes$ and $\to$.
4. An identity version of residuation exists, so BL-algebras form a variety.

## Explanations

### L1 human

A BL-algebra has truth values with an order, an "and" and an "if then".
"If $x$ then $z$" is the weakest value that, combined with $x$, stays below $z$.
Of any two values, one implies the other fully: this is prelinearity.

### L2 human

1. In $[0, 1]$ with $\otimes = \min$, the residuum is $x \to y = 1$ if $x \le y$, and $y$ otherwise.
2. Check divisibility at $x = 0.7$, $y = 0.3$: $0.7 \otimes (0.7 \to 0.3) = \min(0.7, 0.3) = 0.3 = x \land y$.
3. Check prelinearity: $0.3 \to 0.7 = 1$, so the join is $1$.

The typical use: BL-algebras give the algebraic semantics of [[Hájek's basic logic|3AQ5GHTXA4]].
The trap: the lattice order is part of the structure, but divisibility makes $\land$ definable.
