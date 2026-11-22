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

The well-ordering principle says that among natural numbers you can always pick a smallest one.

Let $\mathbb{N} = \{0, 1, 2, \ldots\}$ be the set of [[natural numbers|0MWKJ44V5A]] with its usual [[order|0Y9H52BT03]] $\le$.
Every nonempty subset of $\mathbb{N}$ has a least element.
That is, if $A \subseteq \mathbb{N}$ and $A \ne \emptyset$, then there is an element $a \in A$ with $a \le x$ for every $x \in A$.

## Remarks

### A first proof with the least element

Here is a theorem that the principle proves in a few lines: every integer $n \ge 2$ has a prime divisor.
Let $D$ be the set of divisors $d$ of $n$ with $d \ge 2$.
The set $D$ is nonempty, because $n \in D$, so the principle gives a least element $p$ of $D$.
Suppose $p$ is not prime.
Then $p = ab$ with $2 \le a < p$, and $a$ divides $p$, which divides $n$, so $a \in D$.
But $a < p$, and $p$ was the least element of $D$, so this is impossible, and $p$ is a prime divisor of $n$.
For $n = 91$ the set is $D = \{7, 13, 91\}$, and its least element $7$ is prime.

The pattern is typical: define a set from the problem, check that it is nonempty, take its least element, and show that anything else would give a smaller element.

### Why the principle is true

If $A$ had no least element, then $0 \notin A$, since $0$ would be least.
Then $1 \notin A$, since $1$ would be least, and so on: no number could be the first to enter $A$.
[[Strong induction|0KMVFSHFGZ]] makes "and so on" exact, and the [[proof from strong induction|QPX5Z5YFH8]] shows that $A$ is empty.
In the other direction the principle implies [[ordinary induction|0ASJVEFA9J]], provided each nonzero natural number is a successor.
The [[equivalence of induction and well-ordering|J2P9FWBP3Q]] states the three principles together with the base theory in which they are equivalent.

### Why each hypothesis is needed

The set must be nonempty, because the empty set has no least element.
This is why every use of the principle starts by naming an element of the set, as $n \in D$ above.

The set must consist of natural numbers.
The negative integers have no least element, and neither do the positive rational numbers, as [[the failure for the integers and the positive rationals|CY6WC4F1RP]] shows.

The order must be the usual order.
For the reversed order $\ge$ on $\mathbb{N}$, the set $\mathbb{N}$ has no least element, because each $n$ has $n + 1 \ge n$.

### The rules you can use

The least element is unique: if $a$ and $a'$ are both least, then $a \le a'$ and $a' \le a$, so $a = a'$.
The principle also holds for each set $\{n \in \mathbb{Z} : n \ge m\}$ with a fixed integer $m$, because $n \mapsto n - m$ maps it onto $\mathbb{N}$ and keeps the order.
It does not give a largest element: $\mathbb{N}$ itself has none.
A nonempty set of natural numbers with an upper bound does have a largest element, because the set of its upper bounds in $\mathbb{N}$ is nonempty, and the least of these upper bounds lies in the set.

### What it gives you

The [[minimal counterexample|JGRCNPKNGG]] method is the principle applied to the set of counterexamples.
[[Infinite descent|0EFYCFHYFG]] uses it in the form "there is no infinite strictly decreasing sequence of natural numbers", since the set of terms of such a sequence would have no least element.
Division with remainder follows too: for $a \ge 0$ and $b \ge 1$, the least element of $\{a - qb : q \in \mathbb{N}, \ a - qb \ge 0\}$ is the remainder $r$, and $0 \le r < b$.
The [[Euclidean algorithm|0TRNT4X7J0]] stops for the same reason, because its remainders form a strictly decreasing sequence of natural numbers.

### Well-orders in general

Which other ordered sets have the property?
A [[well-order|01CGSJ0GNQ]] is a linear order in which every nonempty subset has a least element.
So the principle says that $(\mathbb{N}, \le)$ is a well-order, and the study of well-orders in general belongs to set theory.
Do not confuse the principle with the [[well-ordering theorem|0N109NG5ZX]] of Zermelo, which says that every set has some well-order and which is equivalent to the axiom of choice.

### Watch out

The principle fails outside the natural numbers, and arguments that forget this go wrong.
"Take the least positive rational $q$ with property $X$" is not a valid step, since the positive rationals with $X$ may have no least element: for "$q > 0$" itself, every $q$ has the smaller $q / 2$.
The correct move is to replace the rational by a natural number attached to it, such as its denominator in lowest terms, and to take the least of those.
The [[false minimal counterexample over the positive rationals|7YZWT2AA6R]] shows the error in a full argument.

### In Lean

Mathlib gives the least natural number with a decidable property, once one is known to exist, as `Nat.find`.
The fact that $<$ on $\mathbb{N}$ is well-founded is the instance `WellFoundedLT ℕ`.

### Try it

First, let $A = \{n \in \mathbb{N} : n^2 > 50\}$, and find its least element.
Since $7^2 = 49 \le 50$ and $8^2 = 64 > 50$, and squares grow with $n$, the least element is $8$.

Second, does the set of even integers have a least element?
No: for each even integer $m$, the number $m - 2$ is even and smaller, and the set is not a set of natural numbers.

## History

Fermat used the principle in the 17th century in the form of [[infinite descent|0EFYCFHYFG]], long before it had a name.

## Explanations

### L1 human

If some whole numbers have a property, then one of them is the smallest.
Among the even whole numbers larger than $10$, for example, the smallest is $12$.
You can see why by counting up from $0$: the first number you meet with the property is the smallest one.
For fractions this fails, because half of a positive fraction is a smaller positive fraction, so there is no smallest one.

### L2 human

We use the principle to divide $47$ by $6$ with remainder.
Look at the numbers $47 - 6q$ for $q = 0, 1, 2, \ldots$ that are not negative:
$$47, \; 41, \; 35, \; 29, \; 23, \; 17, \; 11, \; 5.$$
The set is nonempty, because it contains $47$, so it has a least element, which is $5$ at $q = 7$.
That least element is less than $6$, for otherwise subtracting $6$ once more would give a smaller element of the set.
So $47 = 6 \cdot 7 + 5$ with $0 \le 5 < 6$.
Check: $42 + 5 = 47$.

The same argument works for every $a \ge 0$ and $b \ge 1$, and it is the standard proof of division with remainder.
Watch out: the set must be shown to be nonempty before its least element is used, and here $a$ itself, at $q = 0$, does that job.

### L3 human

The principle says that $(\mathbb{N}, <)$ is a well-founded linear order, and every well-founded relation supports a form of induction, stated in Mathlib as `WellFounded.induction`.
In set theory the ordinals are the order types of well-orders, and transfinite induction extends the principle beyond $\mathbb{N}$.
In first-order arithmetic the least number principle for a class of formulas is compared with the induction schema for related classes, which is a topic of mathematical logic.
In constructive mathematics the principle for arbitrary subsets implies the law of excluded middle, so constructive texts use induction instead.
