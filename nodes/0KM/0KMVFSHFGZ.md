---
tag: 0KMVFSHFGZ
kind: statement
role: theorem
name: Strong induction
aliases: [complete-induction, course-of-values-induction]
msc: ["03F30", "00A35"]
topics: [EEH2F76CYQ]
audience: school
about: [0ASJVEFA9J, 0MWKJ44V5A]
uses: [0ASJVEFA9J, 0Y9H52BT03]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Complete (strong) induction
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Equivalence with ordinary induction
  - book: isbn:9781108439534
    locator: Chapter 6
---

## Statement

Let $P(n)$ be a property of [[natural numbers|0MWKJ44V5A]] $n$, and let $<$ be the [[order on the natural numbers|0Y9H52BT03]].
Suppose that the following holds for each natural number $n$: if $P(k)$ holds for every natural number $k < n$, then $P(n)$ holds.
Then $P(n)$ holds for every natural number $n$.

The hypothesis is the strong induction step, and the assumption "$P(k)$ for every $k < n$" is the strong induction hypothesis.

## Remarks

### How the statement is used

A proof by strong induction has the following form.

1. Let $n$ be an arbitrary natural number.
2. Assume that $P(k)$ holds for every $k < n$.
3. Prove $P(n)$. The proof may use $P(k)$ for any $k < n$, and not only for $k = n - 1$.

For $n = 0$ there is no $k < 0$, so step 2 assumes nothing and step 3 must prove $P(0)$ directly.
In practice the small values of $n$ for which the general argument does not work are proved separately, as base cases.

### Other forms

1. Base $n_0$: if, for each $n \ge n_0$, the truth of $P(k)$ for all $k$ with $n_0 \le k < n$ implies $P(n)$, then $P(n)$ holds for all $n \ge n_0$. Apply the statement to $Q(m) = P(n_0 + m)$.
2. Several base cases: suppose $P(n_0), P(n_0 + 1), \ldots, P(n_0 + j - 1)$ hold, and for each $n \ge n_0 + j$ the cases $P(n - j), \ldots, P(n - 1)$ imply $P(n)$. Then $P(n)$ holds for all $n \ge n_0$. This follows from form 1, because each $n$ is either one of the $j$ base cases or at least $n_0 + j$.
3. Set form: if $A \subseteq \mathbb{N}$ and, for each $n$, $\{k : k < n\} \subseteq A$ implies $n \in A$, then $A = \mathbb{N}$.

### Examples

1. [[Postage with stamps of $4$ and $5$ cents|~aac374d2]]: every amount $n \ge 12$ is $4a + 5b$, with four base cases $12, 13, 14, 15$ and a step from $n - 4$ to $n$.
2. [[Each integer $n \ge 2$ is a product of primes|~5e97f240]]: a composite $n = ab$ uses the cases $a$ and $b$, which are not $n - 1$.
3. The bound $F_n < 2^n$ for the Fibonacci numbers uses the two cases $n - 1$ and $n - 2$, so it needs the [[two base cases $F_0$ and $F_1$|~e88f896d]].
4. The uniqueness part of the [[fundamental theorem of arithmetic|CTSV0ZESYF]] is proved by strong induction on $n$.

### Why each hypothesis is needed

1. The step must hold for every $n$, including $n = 0$. The property "$n \ge 1$" satisfies the step for every $n \ge 1$, because it is true there, but it fails at $n = 0$.
2. The step must hold for every $n$, and not only from some point on. The property "$n \ne 5$" satisfies the step for all $n \ne 5$, and it fails at $n = 5$.
3. The induction hypothesis may use only $k < n$. A "step" that uses $P(n + 1)$ to prove $P(n)$ proves nothing: the [[upward recursion|CCNEXYJDC0]] shows the same failure for definitions.

### Consequences

1. Ordinary [[mathematical induction|0ASJVEFA9J]] is a special case: its step uses only $P(n - 1)$, which is one of the cases $k < n$.
2. The [[well-ordering principle|01BX15HSRR]] follows from strong induction, by the [[proof with the property $n \notin A$|QPX5Z5YFH8]].
3. The [[minimal counterexample|~f8c099da]] method and [[infinite descent|0EFYCFHYFG]] are strong induction in contrapositive form.

### Converse

The converse direction also holds: strong induction implies ordinary induction, and the [[proof from ordinary induction|C54QYDXFP3]] shows that ordinary induction implies strong induction.
So the two principles are equivalent, together with the well-ordering principle; the [[equivalence of induction and well-ordering|~00389da2]] states the base theory.
Strong induction is "strong" in what a proof may assume, not in what it can prove.

### Names

The names "strong induction", "complete induction", "course-of-values induction" and "the second principle of induction" all name this statement.
Ordinary induction is then called "weak" or "the first principle".

### In Lean

Mathlib states strong induction on $\mathbb{N}$ as `Nat.strong_induction_on`.
In Lean 4 the tactic `induction n using Nat.strong_induction_on` starts a proof of this form.

## History

Strong induction grew out of ordinary [[induction|0ASJVEFA9J]], and its history is a part of the history of that method.

## Explanations

### L1 human

In ordinary induction, the proof for a number may use only the case just before it.
In strong induction, it may use all the cases before it.
This helps when a number breaks into smaller pieces that are not just "one less".
For example, $12 = 3 \times 4$, and a fact about $3$ and a fact about $4$ can give the fact about $12$.
The cases below $12$ are all known when we reach $12$, so we may use any of them.

### L2 human

We prove that every natural number $n \ge 1$ is a sum of distinct powers of $2$.

1. Let $P(n)$ be the statement "$n$ is a sum of distinct powers of $2$". Let $n \ge 1$, and assume $P(k)$ for every $k$ with $1 \le k < n$.
2. Let $2^m$ be the largest power of $2$ with $2^m \le n$. Then $n < 2^{m+1}$.
3. If $n = 2^m$, then $n$ is a sum of one power of $2$, and $P(n)$ holds.
4. Otherwise $k = n - 2^m$ satisfies $1 \le k < n$, so $P(k)$ holds by the hypothesis of step 1.
5. Also $k < 2^{m+1} - 2^m = 2^m$, so every power of $2$ in the sum for $k$ is less than $2^m$.
6. So $n = 2^m + k$ is a sum of distinct powers of $2$, and $P(n)$ holds.
7. By strong induction (form 1 with $n_0 = 1$), $P(n)$ holds for all $n \ge 1$.

The typical use is a statement about $n$ that reduces to a smaller case of unknown size, such as $n - 2^m$ or a factor of $n$.
A trap: a proof that uses $P(n - 1)$ and $P(n - 2)$ must check two base cases.
One base case leaves $P(1)$ unproved when the step starts at $n = 2$.

### L3 human

Strong induction on $\mathbb{N}$ is the special case of well-founded induction for the relation $<$.
For any well-founded relation $R$ on a set $X$, if each $x$ has property $P$ whenever all its $R$-predecessors have it, then every element of $X$ has $P$.
This includes induction over $\mathbb{N} \times \mathbb{N}$ in [[lexicographic order|0B68KNPGCG]], [[structural induction|~f9cfa40d]] over trees, and transfinite induction over the ordinals.
In computability theory, the same pattern defines functions by course-of-values recursion.
In type theory, strong induction is derived from the recursor of the natural numbers, as in the [[proof from ordinary induction|C54QYDXFP3]].
