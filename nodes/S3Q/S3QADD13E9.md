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

Equality by two inequalities is the method that proves $a = b$ by proving $a \le b$ and $b \le a$ separately.
It is valid whenever $\le$ is [[antisymmetric|0M0H1ZH8TT]]: $a \le b$ and $b \le a$ imply $a = b$.
This holds for the usual order of the [[real numbers|08J2M1JYAG]], for inclusion of sets, for divisibility of natural numbers, and in every [[partial order|0QV2JS9RJ3]].
In analysis the method often appears in the form "$a \le b + \varepsilon$ for every $\varepsilon > 0$, so $a \le b$", followed by the reverse inequality.
In optimization it appears as "an upper bound plus an example that attains it".
The method matters because many quantities, such as a supremum, a limit, a maximum or a cardinality, have no formula, but they can be bounded from both sides.

## Motivation

A direct computation of a number is often impossible.
The supremum of a set, the value of a limit, or the largest size of a family with some property is defined by a condition, not by a formula.
Each of the two inequalities is often easier than the equality, because it uses only one half of the information.
For a supremum $s = \sup A$ and a candidate $c$, the inequality $s \le c$ says that $c$ is an upper bound, and $s \ge c$ says that nothing smaller is an upper bound.
For a maximum $m$ and a candidate $k$, the inequality $m \le k$ is an impossibility proof, and $m \ge k$ is a construction.
So the method splits a hard equality into two proofs of different kinds, as [[double inclusion|MKHVRNW68H]] does for sets.

## Notation

1. The two halves are often marked "($\le$)" and "($\ge$)".
2. In a partial order the relation may be written $\le$, $\subseteq$, $\mid$ or $\preceq$, and the method is the same for each symbol.
3. In Mathlib the rule is `le_antisymm : a ≤ b → b ≤ a → a = b`, and `le_antisymm_iff` states $a = b \iff a \le b \wedge b \le a$. The analytic form "$a \le b + \varepsilon$ for all $\varepsilon > 0$" is `le_of_forall_pos_le_add`.

## Remarks

### Examples

1. [[The supremum of 1 - 1/n is 1|RRRZG7GDBV]]: the [[supremum|0R3H5PANRQ]] is at most $1$ because $1$ is an upper bound, and at least $1$ by the [[Archimedean property|0A74SX55QP]].
2. [[Mutual divisibility of natural numbers gives equality|P2AJBVRA3S]]: for natural numbers, $a \mid b$ and $b \mid a$ imply $a = b$, by two inequalities of size.
3. [[Set equality by double inclusion|MKHVRNW68H]] is the method for the partial order $\subseteq$ on the subsets of a set.
4. The [[uniqueness of limits|0ZXJ2455NJ]] in $\mathbb{R}$ has this form: if a sequence tends to $L$ and to $L'$, then $0 \le \lvert L - L' \rvert \le 2\varepsilon$ for every $\varepsilon > 0$, so $\lvert L - L' \rvert = 0$.
5. In a chessboard problem, "the largest number of non-attacking rooks on an $8 \times 8$ board is $8$" has two halves. Nine rooks put two rooks in one of the $8$ rows, by the [[pigeonhole principle|0HGVCWQGY3]], so at most $8$; the $8$ rooks on a diagonal do not attack each other, so at least $8$.
6. The [[Schröder-Bernstein theorem|0A9V6RKQG6]] says that injections $A \to B$ and $B \to A$ give a bijection $A \to B$. It is the antisymmetry of $\le$ for cardinalities, and it needs a real proof.

### Non-examples

1. [[Mutual divisibility of integers does not give equality|WRN90EH74V]]: on $\mathbb{Z}$ the relation $\mid$ is not antisymmetric, since $2 \mid -2$ and $-2 \mid 2$.
2. Two strict inequalities never prove an equality: $a < b$ and $b < a$ cannot both hold, so such a "proof" would start from a contradiction.
3. The bounds $a \le b + 1$ and $b \le a + 1$ give only $\lvert a - b \rvert \le 1$. The method needs the bound for every $\varepsilon > 0$, not for one fixed $\varepsilon$.

### Basic properties

1. In any partial order, the method is valid by antisymmetry. In a preorder, which is reflexive and transitive but not antisymmetric, the two inequalities give only $a \sim b$ for the equivalence relation "$a \le b$ and $b \le a$".
2. Lemma for the analytic form: if $a, b \in \mathbb{R}$ and $a \le b + \varepsilon$ for every $\varepsilon > 0$, then $a \le b$. Proof: if $a > b$, take $\varepsilon = (a - b)/2 > 0$; then $a \le b + (a - b)/2$ gives $a \le b$, a contradiction.
3. A special case: if $0 \le x \le \varepsilon$ for every $\varepsilon > 0$, then $x = 0$. The two inequalities are $x \ge 0$ and $x \le 0$, and the second follows from property 2 with $b = 0$.
4. The [[squeeze theorem|0XMF00T4XQ]] is the same idea for limits: a sequence between two sequences with the same limit $L$ has limit at least $L$ and at most $L$.
5. The method can give equality in a chain: if $a \le b \le c \le a$, then $a = b = c$. This is the standard way to prove that a list of conditions are equivalent, with implications in place of inequalities.

### History

The method is as old as the method of exhaustion of Greek geometry.
Archimedes proved the area of a parabolic segment by showing that the area can be neither larger nor smaller than his value.
Each of these two arguments was a proof by contradiction, and together they give the equality.
Modern analysis keeps the same structure in the proofs with $\varepsilon$.

### Common errors

1. A student proves $a \le b$ twice, once directly and once with other letters, and claims $a = b$.
2. A student uses the method on a relation that is not antisymmetric, such as divisibility on $\mathbb{Z}$ or "$f$ grows at most as fast as $g$".
3. In an optimization problem a student gives an example with value $k$ and claims that the maximum is $k$, without the proof that no example has a larger value.

## Explanations

### L1 human

Suppose we want to show that two numbers are equal, but we cannot compute them.
We show first that the first number is not bigger than the second.
Then we show that the second number is not bigger than the first.
Then neither can be bigger, so they must be equal.
For example, the largest number of rooks that fit on a chessboard without attacking each other is $8$: there are only $8$ rows, so $9$ rooks would put two in one row, and $8$ rooks fit on a diagonal.

### L2 human

We prove that the [[infimum|0QF1MZ9FRG]] of $A = \{ 1/n : n \ge 1 \text{ an integer} \}$ is $0$.

1. ($\inf A \ge 0$) Each element $1/n$ is positive, so $0$ is a lower bound of $A$. The infimum is the greatest lower bound, so $\inf A \ge 0$.
2. ($\inf A \le 0$) Let $\varepsilon > 0$. By the Archimedean property there is an integer $n$ with $n > 1/\varepsilon$, so $1/n < \varepsilon$.
3. So $\inf A \le 1/n < \varepsilon$, since the infimum is at most each element of $A$.
4. This holds for every $\varepsilon > 0$, so $\inf A \le 0$ by Basic property 2 with $a = \inf A$ and $b = 0$.
5. Steps 1 and 4 give $\inf A = 0$.

The typical use is a value defined by a bound, such as an infimum, a supremum or a limit, where one inequality is a general fact and the other needs an $\varepsilon$.
A trap is to prove step 3 for one $\varepsilon$, such as $\varepsilon = 0.01$.
This gives only $\inf A < 0.01$, not $\inf A \le 0$.

### L3 human

The method is the antisymmetry axiom of a partial order, used as a proof rule.
In a lattice, the inequality $x \wedge (y \vee z) \ge (x \wedge y) \vee (x \wedge z)$ always holds, and a lattice is distributive exactly when the reverse inequality also holds.
In a category, the analogue of a partial order is a preorder seen as a category with at most one morphism between two objects.
In such a category, antisymmetry says that isomorphic objects are equal.
In a general category, two maps $A \to B$ and $B \to A$ do not give an isomorphism.
This is why the Schröder-Bernstein theorem needs a proof, and why it fails for many kinds of structure.
In analysis and in combinatorics the two halves often have different characters: an upper bound by an inequality chain and a lower bound by a construction, as in extremal problems and in the [[counting, invariant and extremal arguments|GB14W4SYPK]].
When the two bounds do not meet, the gap measures what is unknown, as in the bounds for Ramsey numbers.
