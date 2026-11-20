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

A *t-norm* is a function $* \colon [0, 1] \times [0, 1] \to [0, 1]$ such that for all $a, b, c, d \in [0, 1]$:

1. commutativity: $a * b = b * a$;
2. associativity: $a * (b * c) = (a * b) * c$;
3. monotonicity: $a * b \le c * d$ if $a \le c$ and $b \le d$;
4. unit: $a * 1 = a$.

The t-norm is *continuous* if it is continuous on $[0, 1]^2$.
It is *left-continuous* if for each $b$ the map $a \mapsto a * b$ is left-continuous: $a_n \uparrow a$ implies $a_n * b \to a * b$.

A *residuum* of $*$ is a function $\Rightarrow_* \colon [0, 1]^2 \to [0, 1]$ such that for all $x, y, z$:
$$z * x \le y \iff z \le (x \Rightarrow_* y).$$
The *residual negation* is $\neg_* x = x \Rightarrow_* 0$.
The *t-conorm* of $*$ is $a \oplus_* b = 1 - (1 - a) * (1 - b)$.

The three basic t-norms are:

1. Łukasiewicz: $a *_{Ł} b = \max(0, a + b - 1)$;
2. Gödel: $a *_{G} b = \min(a, b)$;
3. product: $a *_{\Pi} b = a \cdot b$.

## Notation

In this sub-area the Łukasiewicz t-norm is written $\odot$, and its t-conorm $\min(1, a + b)$ is written $\oplus$.
Other sources write the strong conjunction as $\otimes$ or $\&$; Wikipedia also writes $\top$ for a t-norm and $\bot$ for a t-conorm.

## Remarks

1. The axioms say that $\langle [0, 1], *, 1, \le \rangle$ is a commutative ordered [[monoid|0N6R902FG1]] with the top element as unit, as Wikipedia notes.
2. Wikipedia states that a t-norm is continuous iff it is continuous in one variable; the same holds for left-continuity.
3. A residuum, if it exists, is unique: $z \le x \Rightarrow y$ and $z \le x \Rightarrow' y$ hold for the same $z$.
4. A t-norm has a residuum iff it is left-continuous; see [[the left-continuity statement|D1R4D2HEPP]].
5. A t-conorm is commutative, associative, monotone, and has $0$ as unit.

## Explanations

### L1 human

A t-norm is a way to combine two degrees of truth into a degree for "and".
It must not care about order, it must not get smaller when an input gets larger, and "and fully true" must change nothing.

### L2 human

1. Check the four axioms for a candidate operation.
2. The unit axiom with commutativity gives $1 * a = a$, and monotonicity then gives $a * b \le \min(a, b)$.
3. So $a * 0 = 0$, and every t-norm is below the minimum.

A trap: the residuum is defined by an inequality for all $z$, not by a formula.
Its formula depends on the t-norm.
