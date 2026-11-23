---
tag: S3QADD13E9
kind: concept
name: Equality by two inequalities
aliases: [equality-by-two-inequalities, proof-by-antisymmetry, squeeze-to-equality]
msc: ["00A35", "06A06"]
topics: [MEKKHHQTKB, G9JFJGY4TQ]
audience: ug1
specializes: [0B94TKFQJX]
uses: [0QV2JS9RJ3, 0M0H1ZH8TT, 0FRXBVVR03, 08J2M1JYAG, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Antisymmetric_relation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Partially_ordered_set
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Infimum_and_supremum
    locator: lead section
---

## Summary

When a number has no formula, you can often still pin it down from both sides.
Prove $a \le b$, prove $b \le a$, and then $a = b$.

Here is the pattern on a real goal: the [[supremum|0R3H5PANRQ]] of $A = \{1 - \tfrac1n : n \ge 1\}$ is $1$.
Every element is below $1$, so $1$ is an upper bound and $\sup A \le 1$.
For the other side, take any $c < 1$; the [[Archimedean property|0A74SX55QP]] gives an $n$ with $\tfrac1n < 1 - c$, and then
$$1 - \tfrac1n > 1 - (1 - c) = c,$$
so $c$ is not an upper bound, and $\sup A \ge 1$.
The [[full example|RRRZG7GDBV]] writes this out.

In general, the method is valid whenever the relation $\le$ is [[antisymmetric|0M0H1ZH8TT]]:
$$a \le b \ \text{ and } \ b \le a \implies a = b.$$
This holds for the usual order of the [[real numbers|08J2M1JYAG]], for inclusion of sets, for divisibility of positive integers, and in every [[partial order|0QV2JS9RJ3]].

## Motivation

A supremum, a limit, a maximum or the size of a largest family is defined by a condition, not by a formula, so you cannot compute it directly.
Each of the two inequalities uses only half of the condition, and that half is often easy.
For a supremum $s$ and a candidate $c$, the inequality $s \le c$ says that $c$ is an upper bound, and $s \ge c$ says that nothing smaller is one.
For a maximum, one half is an impossibility proof and the other is a construction.
So one hard equality becomes two proofs of different kinds.

The method for sets is [[double inclusion|MKHVRNW68H]], and the method for limits is the [[squeeze theorem|0XMF00T4XQ]].
In analysis the second inequality often comes as "$a \le b + \varepsilon$ for every $\varepsilon > 0$", which is also the shape of the [[epsilon-delta proofs|RXG5JTZ2PZ]] that come next in the list.

## Notation

The two halves are often headed "($\le$)" and "($\ge$)".
In a partial order the relation may be written $\le$, $\subseteq$, $\mid$ or $\preceq$, and the method is the same for each symbol.
In Lean's Mathlib the rule is `le_antisymm : a ≤ b → b ≤ a → a = b`, and `le_antisymm_iff` states $a = b \iff a \le b \wedge b \le a$.
The analytic form "$a \le b + \varepsilon$ for every $\varepsilon > 0$ gives $a \le b$" is `le_of_forall_pos_le_add`.

## Remarks

### The epsilon form

Analysis often gives the second inequality only with room to spare.
The lemma: if $a, b \in \mathbb{R}$ and $a \le b + \varepsilon$ for every $\varepsilon > 0$, then $a \le b$.
To prove it, suppose $a > b$ and take $\varepsilon = (a - b)/2 > 0$; then
$$a \le b + \frac{a - b}{2} \quad \text{gives} \quad \frac{a - b}{2} \le 0,$$
which contradicts $a > b$.
A special case: if $0 \le x \le \varepsilon$ for every $\varepsilon > 0$, then $x = 0$.
The [[uniqueness of limits|0ZXJ2455NJ]] uses exactly this, since two limits $L$ and $L'$ of one sequence satisfy $0 \le \lvert L - L' \rvert \le 2\varepsilon$ for every $\varepsilon > 0$.

### An upper bound and a construction

How many rooks can stand on an $8 \times 8$ board with no two attacking each other?
At most $8$: nine rooks would put two in one of the $8$ rows, by the [[pigeonhole principle|0HGVCWQGY3]].
At least $8$: eight rooks on a diagonal share no row and no column.
So the answer is $8$, and neither half alone would do.

The same shape proves that [[mutual divisibility of positive integers gives equality|P2AJBVRA3S]]: $a \mid b$ forces $a \le b$, and $b \mid a$ forces $b \le a$.
For infinite sets, injections $A \to B$ and $B \to A$ give a bijection by the [[Schröder-Bernstein theorem|0A9V6RKQG6]]; that is antisymmetry for cardinalities, and it needs a real proof.

### When antisymmetry fails

The method is only as good as the antisymmetry behind it.
On all of $\mathbb{Z}$, [[divisibility is not antisymmetric|WRN90EH74V]], since $2 \mid -2$ and $-2 \mid 2$.
A relation that is reflexive and transitive but not antisymmetric is a preorder, and there the two inequalities give only "$a$ and $b$ are equivalent", here $b = \pm a$.

Bounds with a fixed gap do not help either.
From $a \le b + 1$ and $b \le a + 1$ you get only $\lvert a - b \rvert \le 1$; the epsilon form needs every $\varepsilon > 0$.

### Watch out

A common slip is to prove $a \le b$ twice, with the letters renamed, and claim $a = b$.
Another is to prove the second half for one $\varepsilon$, such as $\varepsilon = 0.01$, which gives only $a < b + 0.01$.
In optimization, the slip is to show one example with value $k$ and announce that the maximum is $k$, with no proof that nothing does better.

### History

The pattern goes back to the method of exhaustion of Greek geometry.
Archimedes found the area of a segment of a parabola by showing that the area can be neither larger nor smaller than his value, each by a proof by contradiction.
Modern $\varepsilon$ proofs keep the same two-sided structure.

### Try it

Show that if $a \le b \le c \le a$ in a partial order, then $a = b = c$.
Transitivity gives $b \le a$ from $b \le c \le a$, and with $a \le b$ antisymmetry gives $a = b$; in the same way $c = a$.

Show that $\inf \{ 1/n : n \ge 1 \} = 0$.
Zero is a lower bound, so the infimum is at least $0$, and for each $\varepsilon > 0$ some $1/n < \varepsilon$, so the infimum is at most $\varepsilon$ for every $\varepsilon$, hence at most $0$.

## Explanations

### L1 human

Suppose you want to show that two numbers are equal, but you cannot compute either of them.
First show that the first number is not bigger than the second.
Then show that the second is not bigger than the first.
Neither can be bigger, so they are equal.
For example, at most $8$ rooks fit on a chessboard without attacking each other, because there are only $8$ rows, and $8$ fit on a diagonal, so the answer is exactly $8$.

### L2 human

We prove that the [[infimum|0QF1MZ9FRG]] of $A = \{ 1/n : n \ge 1 \text{ an integer} \}$ is $0$.

1. ($\inf A \ge 0$) Each $1/n$ is positive, so $0$ is a lower bound, and the infimum is the greatest lower bound, so $\inf A \ge 0$.
2. ($\inf A \le 0$) Let $\varepsilon > 0$.
   The Archimedean property gives an integer $n > 1/\varepsilon$, so $\inf A \le 1/n < \varepsilon$.
3. Step 2 holds for every $\varepsilon > 0$, so $\inf A \le 0$ by the epsilon lemma with $b = 0$.
4. Steps 1 and 3 give $\inf A = 0$.

This is the usual shape for a value defined by a bound: one inequality is a general fact, and the other needs an $\varepsilon$.
Watch out: step 2 must hold for every $\varepsilon$, and one value such as $0.01$ proves only $\inf A < 0.01$.

### L3 human

The method is the antisymmetry axiom of a partial order, used as a rule of proof.
In a lattice the inequality $x \wedge (y \vee z) \ge (x \wedge y) \vee (x \wedge z)$ always holds, and the lattice is distributive exactly when the reverse also holds.
A preorder is a category with at most one arrow between two objects, and antisymmetry says that isomorphic objects are equal.
In a general category, arrows $A \to B$ and $B \to A$ do not give an isomorphism, which is why Schröder-Bernstein needs a proof and fails for many structures.
In extremal combinatorics the two halves have different characters, a counting bound and a construction, as in the [[counting, invariant and extremal arguments|GB14W4SYPK]]; when they do not meet, as for many Ramsey numbers, the gap measures what is unknown.
