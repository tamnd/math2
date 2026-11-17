---
tag: CY6WC4F1RP
kind: counterexample
name: The well-ordering principle fails for the integers and the positive rationals
msc: ["00A35", "06A05"]
topics: [EEH2F76CYQ]
audience: school
uses: [01BX15HSRR, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/Well-ordering_principle
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Well-order
    locator: Examples and counterexamples
---

## Counterexample

The [[well-ordering principle|01BX15HSRR]] says that every nonempty set of natural numbers has a least element.
We show that the same claim is false for the [[integers|0C4JS9RF5M]] and for the positive rational numbers, each with its usual order.

1. Let $A = \{-1, -2, -3, \ldots\}$ be the set of negative integers. It is nonempty, because $-1 \in A$.
2. Let $a \in A$. Then $a - 1$ is a negative integer, so $a - 1 \in A$, and $a - 1 < a$.
3. So no element of $A$ is less than or equal to every element of $A$, and $A$ has no least element.
4. Let $B = \{q \in \mathbb{Q} : q > 0\}$. It is nonempty, because $1 \in B$.
5. Let $q \in B$. Then $q / 2$ is rational and $q / 2 > 0$, so $q / 2 \in B$, and $q / 2 < q$ because $q > 0$.
6. So $B$ has no least element.

Both sets also give infinite strictly decreasing sequences: $-1 > -2 > -3 > \cdots$ in $A$, and $1 > \tfrac12 > \tfrac14 > \cdots$ in $B$.

## Remarks

1. The integers fail because they are not bounded below. Each nonempty set of integers that is bounded below has a least element, by the well-ordering principle applied to the shifted set $\{a - m : a \in A\}$, where $m$ is a lower bound.
2. The positive rationals fail for a different reason: they are bounded below by $0$, but the order is dense, so no element is next above $0$.
3. The set $B$ has an infimum, $0$, but $0 \notin B$. A least element must belong to the set.
4. The positive real numbers fail in the same way as $B$, by the same halving argument.
5. So arguments that take "the smallest counterexample" or that use [[infinite descent|0EFYCFHYFG]] must work inside $\mathbb{N}$, or inside a set that is bounded below in $\mathbb{Z}$.
6. The rationals can be well-ordered by a different order, because they are countable: list them as $q_0, q_1, q_2, \ldots$ and order them by their index. That order is not the usual order.

## Explanations

### L1 human

Among the whole numbers $0, 1, 2, \ldots$, any collection has a smallest member.
Among the negative whole numbers there is no smallest one, because we can always go one further down.
Among the positive fractions there is no smallest one either, because half of a positive fraction is smaller and still positive.
So "take the smallest one" is safe for counting numbers and unsafe for other kinds of numbers.

### L2 human

We compare a set of integers with no lower bound and the same set cut at a lower bound.

1. Let $C = \{n \in \mathbb{Z} : n^2 \ge 10\}$. Then $C$ contains $4, 5, 6, \ldots$ and $-4, -5, -6, \ldots$, because $3^2 = 9 < 10 \le 16 = 4^2$.
2. The set $C$ has no least element: for each $n \in C$ with $n < 0$, the number $n - 1$ is in $C$ and smaller, and each positive element is larger than $-4 \in C$.
3. Let $C' = \{n \in C : n \ge -10\}$. It is bounded below by $-10$.
4. Shift by $10$: the set $\{n + 10 : n \in C'\}$ is a nonempty set of natural numbers, with least element $0$.
5. So $C'$ has the least element $0 - 10 = -10$.

The typical use of this counterexample is as a check on any proof that picks a smallest element: name the set, and show that it lies in $\mathbb{N}$ or is bounded below in $\mathbb{Z}$.
A trap is to work with integers that can be negative, such as the exponent of a prime in a rational number, and to take "the least exponent" without a lower bound.
The [[minimal counterexample|JGRCNPKNGG]] page shows a false argument of this kind on the positive rationals.
