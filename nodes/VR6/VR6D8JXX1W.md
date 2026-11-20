---
tag: VR6D8JXX1W
kind: concept
name: Triangular norm
aliases: [t-norm, triangular-norm]
msc: ["03B52", "26B99"]
topics: [WZP584JQ06]
audience: grad
uses: [0N6R902FG1]
sources:
  - url: https://en.wikipedia.org/wiki/T-norm
    locator: Definition; Prominent examples; Properties of continuous t-norms; Residuum
  - url: https://en.wikipedia.org/wiki/Construction_of_t-norms
    locator: Ordinal sums
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms
  - book: isbn:9780792352389
---

## Summary

A *triangular norm*, or *t-norm*, is a binary operation on $[0, 1]$ that is commutative, associative, monotone and has $1$ as neutral element; see [[the definition|BHGCVPAJW0]].
In [[fuzzy logic|8DH4QM6AX8]] a t-norm interprets strong conjunction.
When the t-norm is left-continuous, it has a residuum, which interprets implication.
The three basic continuous t-norms are the Łukasiewicz, Gödel (minimum) and product t-norms.
By the Mostert-Shields theorem, every continuous t-norm is built from these three by ordinal sums.

## Motivation

A conjunction of degrees of truth should agree with classical conjunction on $0$ and $1$, and it should not depend on the order or grouping of the conjuncts.
It should also not decrease when a conjunct becomes more true.
These requirements are the t-norm axioms.
SEP adds the reason for a second, non-idempotent conjunction: using a partially true hypothesis twice may give a lower degree than using it once.

## Notation

> **Notation warning.**
> This sub-area writes the strong conjunction as $\odot$ and the strong disjunction as $\oplus$, as in the MV-algebra literature.
> Other sources use $\otimes$ or $\&$ for the strong conjunction: Wikipedia writes $\otimes$ in Łukasiewicz logic and $*$ or $\top$ for t-norms, and SEP writes $\&$ in formulas.
> A generic t-norm is written $*$ here, and its residuum $\Rightarrow_*$.

The t-conorm of $*$ is $x \oplus_* y = 1 - (1 - x) * (1 - y)$.

## Remarks

### Examples

1. Łukasiewicz t-norm: $x * y = \max(0, x + y - 1)$, with residuum $\min(1, 1 - x + y)$.
2. Minimum (Gödel) t-norm: $x * y = \min(x, y)$, the pointwise largest t-norm.
3. Product t-norm: $x * y = x y$, a strict t-norm.
4. Nilpotent minimum: $\min(x, y)$ if $x + y > 1$, else $0$; it is left-continuous but not continuous.
5. Ordinal sums, such as the Łukasiewicz t-norm on $[0, \tfrac12]$ and the product t-norm on $[\tfrac12, 1]$; see [[the ordinal sum example|Z6H5WJYJ4H]].
6. Explicit values at $(0.7, 0.4)$ are in [[the values example|TGD3MEZCNH]].

### Non-examples

1. The arithmetic mean $(x + y)/2$: $1$ is not neutral, and it is not associative; see [[the mean non-example|NP9MTQ5QPZ]].
2. The drastic t-norm is a t-norm, but it is not left-continuous and has no residuum; see [[the drastic non-example|VK2A62AQ0F]].
3. $\max(x, y)$ is a t-conorm, not a t-norm: $\max(x, 1) = 1 \neq x$ for $x < 1$.

### Basic properties

1. $x * 0 = 0$ for every t-norm.
2. Drastic $\le$ Łukasiewicz $\le$ product $\le$ minimum, pointwise; every t-norm lies between the drastic t-norm and the minimum.
3. A t-norm is left-continuous iff it has a residuum, and then $x \Rightarrow_* y = \max \set{z : z * x \le y}$; see [[the residuum statement|D1R4D2HEPP]].
4. For a residuum, $x \Rightarrow_* y = 1$ iff $x \le y$, and $1 \Rightarrow_* y = y$.
5. The residua of the three basic t-norms are computed in [[the residua statement|7R2JBNNMT5]].
6. Mostert-Shields: a t-norm is continuous iff it is isomorphic to an ordinal sum of Łukasiewicz and product t-norms, with the minimum outside the summands. This is cited from Wikipedia and SEP, and it is not proved here.

### History

Wikipedia explains the name: t-norms first generalized the triangle inequality in probabilistic metric spaces.
SEP cites Mostert and Shields (1957) and Ling (1965) for the representation of continuous t-norms as ordinal sums.
SEP cites Klement, Mesiar and Pap (2000) for the theory of t-norms.

### Common errors

1. Reading "stronger t-norm" in two opposite ways.
   As functions, larger t-norms are called stronger; in logic, a larger t-norm gives a weaker conjunction, as Wikipedia notes.
2. Taking $1 - x$ as the negation of every t-norm logic.
   The residual negation $x \Rightarrow_* 0$ of the minimum and product t-norms is the Gödel negation, which takes only the values $0$ and $1$.
3. Assuming every t-norm has a residuum.
   Only left-continuous t-norms do.
4. Mixing up the notations: $\odot$, $\otimes$, $\&$ and $*$ can all mean the same strong conjunction.

## Explanations

### L1 human

A t-norm is a rule for "and" when statements can be partly true.
If one statement is true to degree $0.7$ and another to degree $0.4$, a t-norm says how true "both" is.
The minimum gives $0.4$, the product gives $0.28$, and the Łukasiewicz rule gives $0.1$.

### L2 human

To check that an operation is a t-norm, check four things: commutativity, associativity, monotonicity, and $x * 1 = x$.
To find its residuum, solve $z * x \le y$ for the largest $z$.

Example: for the product, $z x \le y$ with $x > y$ gives $z \le y / x$, so $x \Rightarrow y = y / x$.
A trap: the residuum is $1$ whenever $x \le y$, for every left-continuous t-norm, so the interesting case is $x > y$.

### L3 human

A t-norm makes $[0, 1]$ an ordered commutative [[monoid|0N6R902FG1]] with top element as unit.
With a residuum, $[0, 1]$ becomes a residuated lattice, the standard algebra of MTL.
Continuous t-norms give BL-algebras; their structure is fixed by the set of idempotents, which is closed, and by Łukasiewicz or product copies on the open intervals between them.
