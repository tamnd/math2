---
tag: BHGCVPAJW0
kind: definition
name: Triangular norm
msc: ["03B52", "26B99"]
topics: [WZP584JQ06]
audience: grad
defines: VR6D8JXX1W
uses: [0N6R902FG1]
sources:
  - url: https://en.wikipedia.org/wiki/T-norm
    locator: Definition; Classification of t-norms; Residuum; T-conorms
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms
---

## Definition

A t-norm is an operation on $[0, 1]$ that can serve as the conjunction of degrees of truth.

A *t-norm* is a function $* \colon [0, 1] \times [0, 1] \to [0, 1]$ such that for all $a, b, c, d \in [0, 1]$ the following hold.

1. Commutativity: $a * b = b * a$.
2. Associativity: $a * (b * c) = (a * b) * c$.
3. Monotonicity: if $a \le c$ and $b \le d$, then $a * b \le c * d$.
4. Unit: $a * 1 = a$.

The t-norm is *continuous* if it is continuous as a map on $[0, 1]^2$.
It is *left-continuous* if for each $b$ the map $a \mapsto a * b$ is left-continuous, that is, $a_n \uparrow a$ implies $a_n * b \to a * b$.

A *residuum* of $*$ is a function $\Rightarrow_* \colon [0, 1]^2 \to [0, 1]$ such that the following holds for all $x, y, z \in [0, 1]$.

$$z * x \le y \iff z \le (x \Rightarrow_* y).$$

The *residual negation* is $\neg_* x = x \Rightarrow_* 0$.
The *t-conorm* of $*$ is $a \oplus_* b = 1 - (1 - a) * (1 - b)$.

The three basic t-norms are the Łukasiewicz t-norm $a \odot b = \max(0, a + b - 1)$, the Gödel t-norm $\min(a, b)$, and the product t-norm $a \cdot b$.

## Notation

We write $\odot$ for the Łukasiewicz t-norm and $\oplus$ for its t-conorm $\min(1, a + b)$.
Other books write a strong conjunction as $\otimes$ or $\&$, and a t-norm as $\top$ or $T$ with the t-conorm as $\bot$ or $S$.
Watch out that $\bot$ also names the constant "false" in fuzzy logics.

## Remarks

Each axiom has a reason.
Commutativity and associativity say that a conjunction of several statements does not depend on their order or grouping.
Monotonicity says that a more true conjunct never makes the conjunction less true.
The unit law says that "and fully true" changes nothing, so on $\{0, 1\}$ every t-norm is classical conjunction.
Together the axioms make $\langle [0, 1], *, 1, \le \rangle$ a commutative ordered [[monoid|0N6R902FG1]] whose unit is the top element.

The axioms have a first consequence.
Monotonicity and the unit law give $a * b \le a * 1 = a$, and by commutativity also $a * b \le b$, so $a * b \le \min(a, b)$.
For the product at $(0.5, 0.8)$ this reads $0.4 \le 0.5$.

A case that fails is the arithmetic mean $(a + b)/2$, which breaks the unit law, since $(0.4 + 1)/2 = 0.7 \ne 0.4$; see [[the mean non-example|NP9MTQ5QPZ]].
The residuum is defined by an inequality for all $z$, not by a formula, and so it is unique when it exists.
It exists exactly when the t-norm is left-continuous, by [[the left-continuity statement|D1R4D2HEPP]].
For the left-continuity condition, one variable is enough: by commutativity, left-continuity in $a$ for each $b$ gives it in $b$ for each $a$.
The examples, the ordinal sums and the Mostert-Shields theorem are treated under [[triangular norms|VR6D8JXX1W]].

## Explanations

### L1 human

A t-norm is a way to combine two degrees of truth into a degree for "and".
It must not care about the order of its inputs.
It must not get smaller when an input gets larger.
And "and fully true" must change nothing.

### L2 human

We check that the Łukasiewicz operation $a \odot b = \max(0, a + b - 1)$ is a t-norm.
Commutativity holds because $a + b = b + a$.
The unit law holds because $\max(0, a + 1 - 1) = a$.
Monotonicity holds because $a + b - 1$ grows with $a$ and with $b$, and $\max(0, \cdot)$ keeps the order.
For associativity, both groupings equal the expression below.

$$\max(0, a + b + c - 2).$$

Check at $(0.9, 0.8, 0.7)$: $0.9 \odot 0.8 = 0.7$ and $0.7 \odot 0.7 = 0.4$, while $0.8 \odot 0.7 = 0.5$ and $0.9 \odot 0.5 = 0.4$.
Watch out: the residuum is defined by an inequality, and its formula has to be computed for each t-norm.
