---
tag: YHYSGRE7JV
kind: concept
name: Post's many-valued logics
aliases: [post-logic, post-many-valued-logics]
msc: ["03B50"]
topics: [WZP584JQ06]
audience: research
uses: [DWYCKAKXZD, P7E926JK13, TDZVCWYJ9F]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
    locator: Post logics Pm; Functional completeness of many-valued logics
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 3.3 The expressive power of many-valued logics
---

## Summary

Take three truth values $0, 1, 2$ and a negation that turns them in a circle: $\neg 0 = 2$, $\neg 2 = 1$ and $\neg 1 = 0$.
With "or" read as the larger value, these two connectives can express every truth table on three values, and the same holds for any number of values.
This is the idea of Post's logics.

For $m \ge 2$, *Post's logic* $\mathrm{P}_m$ has the values $0, 1, \dots, m - 1$ in their natural order, and these connectives:
$$\neg x = x - 1 \bmod m, \qquad x \lor y = \max(x, y), \qquad x \land y = \min(x, y).$$
The [[exact definition|PHGRJ2D97H]] also fixes the designated values, the $\lambda$ greatest ones for some $1 \le \lambda \le m - 1$.
The main property is [[functional completeness|8P3Y6T0RZS]]: every function on the $m$ values is a formula in $\neg$ and $\lor$.

## Motivation

In classical logic every truth function can be written with $\neg$ and $\lor$, by [[functional completeness|TDZVCWYJ9F]].
Post asked whether some $m$-valued connectives have the same property, and his cyclic negation gives a positive answer.
So the $m$-valued Post algebra plays, for $m$ values, the part that the two-element Boolean algebra plays for two.

The more familiar connectives fail this test.
Łukasiewicz's connectives send the values $0$ and $1$ to $0$ and $1$, so no formula built from them gives the constant $\tfrac12$.
Post's negation moves every value, and this breaks every such obstacle.
Post's systems, with [[Łukasiewicz's three-valued logic|1CE2TGM6MQ]], are the oldest family of [[many-valued logics|DWYCKAKXZD]], and the [[Sheffer functions|1K829SJG3K]] build on them.

## Notation

Many books write the values as $0, \tfrac{1}{m-1}, \dots, 1$, as the [[definition|PHGRJ2D97H]] does.
We relabel them as $0, 1, \dots, m - 1$, so that negation is subtraction of $1$ modulo $m$.
The *shift* $S x = x + 1 \bmod m$ is $\neg$ applied $m - 1$ times.
The Stanford Encyclopedia writes $\mathcal{P}_m^\lambda$ for the matrix with $\lambda$ designated values.
Watch out: "Post algebra" names the algebras of these logics, while "Post's lattice" is the lattice of clones on two values, a different object.

## Remarks

### A first computation

Work in $\mathrm{P}_3$ and evaluate $x \lor \neg x \lor \neg\neg x$ at $x = 1$.
First compute the negations:
$$\neg 1 = 0, \qquad \neg\neg 1 = \neg 0 = 2.$$
Then take the largest value:
$$\max(1, 0, 2) = 2.$$
The same happens at every $x$, because $x$, $\neg x$ and $\neg\neg x$ are the three different values.
So this formula is the constant $2$, the top value.
In $\mathrm{P}_m$ the formula with $m$ disjuncts $x, \neg x, \dots, \neg^{m-1} x$ is the constant $m - 1$ for the same reason.

### Building any table

The [[proof of completeness|FR9JC8MNBJ]] follows disjunctive normal form.
For each value $a$ it builds a test $J_a(x)$ that is $m - 1$ at $x = a$ and $0$ elsewhere.
In $\mathrm{P}_3$ the first test is $J_0(x) = S(\max(x, Sx))$, and its table is computed as follows:
$$J_0(0) = S(1) = 2, \qquad J_0(1) = S(2) = 0, \qquad J_0(2) = S(2) = 0.$$
The proof then lowers each test to the output it needs and joins the results with $\lor$.
[[The three-valued Post logic|FV0ZA5CEH6]] carries this out for the Łukasiewicz negation $2 - x$, and finds a formula in $\neg$ and $\lor$ for it.

### The rules you can use

The order of $\neg$ is $m$: applying it $m$ times returns every value to its start.
Every function $V^n \to V$ with $n \ge 1$ is a term in $\neg$ and $\lor$, so $\land$ is redundant.
This makes $\langle V, \neg, \lor \rangle$ a [[primal algebra|XD01Y7B6XW]].
The only sets of values closed under $\neg$ are the empty set and the whole set, since a closed set that contains $a$ contains $a - 1, a - 2$, and so on.
For $m = 2$, negation swaps $0$ and $1$, and $\mathrm{P}_2$ is classical logic.

### What it is not

[[Łukasiewicz's three-valued connectives are not functionally complete|TCVVFJ46VR]], because they keep the set $\{0, 1\}$ closed.
Kleene's connectives on three values keep the set $\{\tfrac12\}$ closed, so no formula in them gives the constant $0$ or $1$.
The negation $u \mapsto 1 - u$ is not Post's negation for $m \ge 3$: it reverses the order, while Post's negation turns the values in a circle.

### Watch out

Post's negation is not an involution.
In $\mathrm{P}_3$ we get $\neg\neg 1 = 2$, not $1$.
It does not reverse the order either, so De Morgan's laws fail.
At $x = 1$ and $y = 2$ in $\mathrm{P}_3$, the left side is $\neg \max(1, 2) = \neg 2 = 1$.
The right side is $\min(\neg 1, \neg 2) = \min(0, 1) = 0$.
So do not read the values of $\mathrm{P}_m$ as degrees of truth; the order serves $\lor$, and negation ignores it.

### History

Post introduced the systems $\mathrm{P}_m$ in his 1921 paper "Introduction to a general theory of elementary propositions", and proved there that they are functionally complete.
Łukasiewicz had introduced his three-valued logic one year earlier, in 1920.
Słupecki gave a general criterion for the completeness of sets of $m$-valued functions in 1939.
Rosenbloom introduced Post algebras in 1942 as the algebras of these logics.

### Try it

First, in $\mathrm{P}_4$ with values $0, 1, 2, 3$, compute $\neg\neg\neg 1$.
We get $\neg 1 = 0$, then $\neg 0 = 3$, then $\neg 3 = 2$, so the answer is $2 = S(1)$.

Second, is $x \lor \neg x$ a constant in $\mathrm{P}_3$?
No: it is $\max(0, 2) = 2$ at $x = 0$ and $\max(1, 0) = 1$ at $x = 1$.

## Explanations

### L1 human

Put the values $0, 1, 2$ around a clock face.
"Or" picks the larger of two values.
"Not" moves one step back, and from $0$ it jumps to the top value $2$.
These two operations are enough to build every possible table on the three values, and the same holds with $4$, $5$ or any number of values.

### L2 human

We build the test $J_0$ for $m = 4$, the formula that is $3$ at $x = 0$ and $0$ elsewhere.
Put $J_0(x) = S(\max(x, Sx, S^2 x))$ with $S x = x + 1 \bmod 4$.
At $x = 0$ the maximum is $\max(0, 1, 2) = 2$, and $S(2) = 3$.
At $x = 1$ the maximum is $\max(1, 2, 3) = 3$, and $S(3) = 0$.
At $x = 2$ and $x = 3$ the maximum is again $3$, so $J_0$ is $0$ there.
Check: the maximum misses $3$ only when $x - 1 \equiv 3$, that is at $x = 0$.
The tests for other values come from shifting the input, and they are the literals of a many-valued normal form.
This is the typical use: to show a set of connectives complete, define $\neg$ and $\lor$ of $\mathrm{P}_m$ from it.

### L3 human

In the language of clones, the clone generated by $\neg$ and $\max$ on $m$ elements is the clone of all operations.
The variety generated by a primal algebra is categorically equivalent to the variety of Boolean algebras, so [[Post algebras|RD2A5Z7E2B]] behave much like Boolean algebras.
For $m \ge 3$ the lattice of clones on $m$ elements is uncountable, and completeness is decided by the finitely many maximal clones of [[Rosenberg's classification|GF1RK91VED]].
