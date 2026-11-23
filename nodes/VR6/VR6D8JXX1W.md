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

Take two statements that are each half true, with degree $0.5$.
The minimum says "both" is half true, the product says it is true to degree $0.25$, and the Łukasiewicz rule $\max(0, x + y - 1)$ says it is false.
These are the three basic *triangular norms*, or *t-norms*: the candidate meanings of "and" in [[fuzzy logic|8DH4QM6AX8]].

A t-norm is a binary operation $*$ on $[0, 1]$ that is commutative, associative and monotone in each argument, and that has $1$ as neutral element; see [[the definition|BHGCVPAJW0]].
When a t-norm is left-continuous, it has a residuum $\Rightarrow_*$, defined by the law below, and the residuum interprets implication.

$$z * x \le y \iff z \le (x \Rightarrow_* y).$$

## Motivation

A conjunction of degrees of truth should agree with classical conjunction on $0$ and $1$.
It should not depend on the order or the grouping of the conjuncts, and it should not decrease when a conjunct becomes more true.
These four requirements are exactly the t-norm axioms.

Why allow anything other than the minimum?
Using a partly true premise twice can be weaker than using it once.
A t-norm below the minimum, such as the Łukasiewicz t-norm, records this loss, and that is what resolves the [[sorites paradox|EP8J937EQC]].
Each left-continuous t-norm then gives a logic, and the pages on [[BL|3AQ5GHTXA4]], [[MTL|PT5PHKJDYM]] and [[product logic|YTHRDT9PDR]] study these logics.

## Notation

We write a generic t-norm as $*$ and its residuum as $\Rightarrow_*$.
For the Łukasiewicz t-norm we write $\odot$, and for its t-conorm $\min(1, x + y)$ we write $\oplus$, as in the literature on MV-algebras.
Other books write $\otimes$, $\&$, $\top$ or $T$ for a t-norm, and $\bot$ or $S$ for a t-conorm.
The *t-conorm* of $*$ is its dual, $x \oplus_* y = 1 - (1 - x) * (1 - y)$.

## Remarks

### Three t-norms at one point

Evaluate the three basic t-norms at $(0.5, 0.5)$.

$$\min(0.5, 0.5) = 0.5, \qquad 0.5 \cdot 0.5 = 0.25, \qquad \max(0, 0.5 + 0.5 - 1) = 0.$$

The order $0 \le 0.25 \le 0.5$ is no accident.
Pointwise, Łukasiewicz $\le$ product $\le$ minimum, and the first inequality holds because $xy - (x + y - 1) = (1 - x)(1 - y) \ge 0$.
At $(0.7, 0.4)$ the three values are $0.1$, $0.28$ and $0.4$, and [[the values example|TGD3MEZCNH]] computes their residua there.

### What the axioms force

The axioms already fix a lot.
Monotonicity and the unit law give $x * y \le x * 1 = x$, and commutativity gives $x * y \le y$, so every t-norm lies below the minimum.
In particular $x * 0 = 0$.
At the other end lies the *drastic t-norm*, which is $\min(x, y)$ when one argument is $1$ and $0$ otherwise.
Every t-norm $T$ satisfies $T(x, y) = \min(x, y)$ when one argument is $1$, and $T(x, y) \ge 0$ always, so every t-norm lies above the drastic one.

### Where implication comes from

The residuum answers the question "how large can $z$ be so that $z$ and $x$ together give at most $y$?"
It exists exactly for the left-continuous t-norms, by [[the left-continuity statement|D1R4D2HEPP]], and then it is the maximum below.

$$x \Rightarrow_* y = \max \{ z \in [0, 1] : z * x \le y \}.$$

For every residuum, $x \Rightarrow_* y = 1$ exactly when $x \le y$, and $1 \Rightarrow_* y = y$.
The residua of the three basic t-norms are $\min(1, 1 - x + y)$ for Łukasiewicz, and for Gödel and product they are $1$ when $x \le y$ and $y$ or $y / x$ otherwise; [[the residua statement|7R2JBNNMT5]] proves this.
The *nilpotent minimum*, which is $\min(x, y)$ when $x + y > 1$ and $0$ otherwise, is left-continuous but not continuous, and it still has a residuum.

### Building t-norms by ordinal sums

New t-norms come from old ones by placing rescaled copies on disjoint intervals of the diagonal and using the minimum elsewhere.
This is an *ordinal sum*, and [[the ordinal sum example|Z6H5WJYJ4H]] puts the Łukasiewicz t-norm on $[0, \tfrac12]$ and the product on $[\tfrac12, 1]$.
The Mostert-Shields theorem of 1957 says that this is the whole story for continuous t-norms.
A t-norm is continuous exactly when it is an ordinal sum of copies of the Łukasiewicz and product t-norms, with the minimum outside the copies.
We cite the theorem and do not prove it.

### What it is not

The arithmetic mean $(x + y)/2$ is not a t-norm.
It is commutative and monotone, but $1$ is not neutral and it is not associative, as [[the mean non-example|NP9MTQ5QPZ]] checks.
The maximum is not a t-norm either, since $\max(x, 1) = 1 \ne x$ for $x < 1$; it is a t-conorm.
The drastic t-norm is a t-norm, but it is not left-continuous, and [[the drastic non-example|VK2A62AQ0F]] shows that it has no residuum.

### Watch out

Two traps are common.
First, $1 - x$ is not the negation of every t-norm logic.
The residual negation $x \Rightarrow_* 0$ of the minimum and of the product is $1$ at $x = 0$ and $0$ everywhere else.
For example, $0.3 \Rightarrow_{\Pi} 0 = 0 / 0.3 = 0$, not $0.7$.
Second, a continuous t-norm can have a residuum that is not continuous.
The Gödel residuum at $y = 0.4$ is $1$ for $x = 0.4$ and $0.4$ for every $x > 0.4$, so it jumps on the diagonal.
Of the three basic residua, only the Łukasiewicz one is continuous.

### History

Menger introduced triangular norms in 1942, in his work on statistical metric spaces, where they replace the triangle inequality; this is the origin of the name.
Mostert and Shields proved the representation of continuous t-norms by ordinal sums in 1957, in their work on topological semigroups.
Ling gave the representation of continuous Archimedean t-norms in 1965.
The monograph *Triangular Norms* by Klement, Mesiar and Pap appeared in 2000.

### Try it

First, compute the product residuum $0.5 \Rightarrow_\Pi 0.2$.
Since $0.5 > 0.2$, it is $0.2 / 0.5 = 0.4$, and indeed $0.4 \cdot 0.5 = 0.2$.

Second, show that $x * x \le x$ for every t-norm.
This is the bound $x * y \le \min(x, y)$ with $y = x$.

## Explanations

### L1 human

A t-norm is a rule for "and" when statements can be partly true.
If one statement is true to degree $0.7$ and another to degree $0.4$, a t-norm says how true "both" is.
The minimum gives $0.4$, the product gives $0.28$, and the Łukasiewicz rule gives $0.1$.
Every rule must give "fully true and $x$" the value $x$, and none may give more than the smaller degree.

### L2 human

We check that the product is a t-norm and find its residuum.
Commutativity and associativity of $xy$ are the laws of real multiplication, and $x \cdot 1 = x$.
If $x \le x'$ and $y \le y'$, then $xy \le x'y'$, because all the numbers are nonnegative.
For the residuum at $x > y$, solve $z x \le y$ for the largest $z$.

$$z x \le y \iff z \le \frac{y}{x}, \qquad \text{so} \qquad x \Rightarrow_\Pi y = \frac{y}{x}.$$

Check at $x = 0.8$, $y = 0.2$: the residuum is $0.25$, and $0.25 \cdot 0.8 = 0.2$.
This is the typical use: for a residuum, solve the inequality $z * x \le y$ for $z$, and the case $x \le y$ always gives $1$.

### L3 human

A t-norm makes $[0, 1]$ a commutative ordered [[monoid|0N6R902FG1]] in which the top element is the unit.
With a residuum, $[0, 1]$ becomes a linearly ordered [[residuated lattice|E337A6WVH3]], the standard algebra of MTL.
Continuous t-norms give the standard [[BL-algebras|ERNYMVEGKC]].
Their structure is fixed by the closed set of idempotents and by a Łukasiewicz or product copy on each open interval between idempotents, which is the content of the Mostert-Shields theorem.
