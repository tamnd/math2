---
tag: 01BX15HSRR
kind: statement
role: theorem
name: Well-ordering principle
aliases: [least-number-principle]
msc: ["03F30", "00A35"]
topics: [EEH2F76CYQ]
audience: school
about: [0MWKJ44V5A, 0Y9H52BT03]
uses: [0Y9H52BT03, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Well-ordering_principle
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Relationship to the well-ordering principle
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_induction_posintsord.ptx#L9
    locator: source/s_induction_posintsord.ptx:9
  - book: isbn:9781108439534
    locator: Chapter 6
same_as:
  wikidata: Q2488476
  wikipedia: Well-ordering principle
---

## Statement

Let $\mathbb{N} = \{0, 1, 2, \ldots\}$ be the set of [[natural numbers|0MWKJ44V5A]] with its usual [[order|0Y9H52BT03]] $\le$.
Every nonempty subset of $\mathbb{N}$ has a least element.
That is, if $A \subseteq \mathbb{N}$ and $A \neq \emptyset$, then there is an element $a \in A$ with $a \le x$ for every $x \in A$.

## Remarks

### Proof and equivalence

The [[proof from strong induction|QPX5Z5YFH8]] assumes that $A$ has no least element and shows, by [[strong induction|0KMVFSHFGZ]], that no number lies in $A$.
Conversely, the principle implies ordinary [[induction|0ASJVEFA9J]] when each nonzero natural number is a successor.
The [[equivalence of induction and well-ordering|~00389da2]] states the three principles and the base theory in which they are equivalent.

### Basic facts

1. The least element is unique. If $a$ and $a'$ are both least, then $a \le a'$ and $a' \le a$, so $a = a'$ by antisymmetry.
2. The principle holds for each set $\{n \in \mathbb{Z} : n \ge m\}$, for a fixed integer $m$, because $n \mapsto n - m$ maps it onto $\mathbb{N}$ and keeps the order.
3. A nonempty set of natural numbers need not have a largest element: $\mathbb{N}$ itself has none. A nonempty set of natural numbers with an upper bound has a largest element.

### Why each hypothesis is needed

1. The set must be nonempty: the empty set has no least element.
2. The set must consist of natural numbers. The [[failure for the integers and the positive rationals|~063fd5b5]] shows two sets with no least element: the negative integers, and the positive rational numbers.
3. The order must be the usual order of $\mathbb{N}$. For the reversed order $\ge$ on $\mathbb{N}$, the set $\mathbb{N}$ has no least element, because each $n$ has $n + 1 \ge n$.

### Consequences

1. The [[minimal counterexample|~f8c099da]] method: if a property fails for some natural number, it fails for a least one.
2. [[Infinite descent|0EFYCFHYFG]]: there is no infinite strictly decreasing sequence of natural numbers, because the set of its terms would have no least element.
3. Division with remainder: for integers $a \ge 0$ and $b \ge 1$, the least element of $\{a - qb : q \in \mathbb{N}, \ a - qb \ge 0\}$ is the remainder $r$, with $0 \le r < b$.
4. The [[Euclidean algorithm|0TRNT4X7J0]] stops, because the remainders form a strictly decreasing sequence of natural numbers.

### Converse

The converse question asks which ordered sets have the property.
A [[well-order|01CGSJ0GNQ]] is a linear order in which every nonempty subset has a least element.
So the statement says that $(\mathbb{N}, \le)$ is a well-order, and well-orders in general belong to set theory.
The well-ordering principle must not be confused with the [[well-ordering theorem|0N109NG5ZX]] of Zermelo, which says that every set has some well-order and which is equivalent to the axiom of choice.

### In Lean

Mathlib gives the least element of a nonempty decidable set of natural numbers as `Nat.find`.
The fact that $<$ on $\mathbb{N}$ is well-founded is the instance `WellFoundedLT ℕ`.

## History

The principle was used in the form of [[infinite descent|0EFYCFHYFG]] by Fermat in the 17th century, long before it had a name.

## Explanations

### L1 human

If some whole numbers have a property, then one of them is the smallest.
For example, among the whole numbers larger than $10$ that are even, the smallest is $12$.
This is true because we can count up from $0$: the first number we meet with the property is the smallest one.
For fractions it fails: among the positive fractions there is no smallest, because half of any positive fraction is smaller.

### L2 human

We use the principle to prove that each integer $n \ge 2$ has a prime divisor.

1. Let $n \ge 2$, and let $D$ be the set of divisors $d$ of $n$ with $d \ge 2$.
2. The set $D$ is nonempty, because $n \in D$.
3. By the well-ordering principle, $D$ has a least element $p$.
4. Suppose that $p$ is not prime. Then $p = ab$ with $2 \le a < p$.
5. Then $a$ divides $p$, and $p$ divides $n$, so $a$ divides $n$. So $a \in D$ and $a < p$.
6. This contradicts the choice of $p$ as least element. So $p$ is a prime divisor of $n$.

The typical use is to pick the least element of a set defined by the problem, and to show that it has the wanted property.
A trap: the set must be shown to be nonempty before its least element is used.
A second trap: the principle needs a set of natural numbers. "The least positive real number with a property" may not exist.

### L3 human

The well-ordering principle says that $(\mathbb{N}, <)$ is a well-founded linear order, and every well-founded relation supports a form of induction.
In set theory, the ordinals are exactly the order types of well-orders, and transfinite induction extends this page beyond $\mathbb{N}$.
In first-order arithmetic, the least number principle for a class of formulas is compared with the induction schema for related classes, and these comparisons belong to mathematical logic.
In constructive mathematics, the principle in its full form implies instances of the law of excluded middle, so constructive texts replace it by induction.
