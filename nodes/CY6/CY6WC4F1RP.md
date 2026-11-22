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

1. Let $A = \{-1, -2, -3, \ldots\}$ be the set of negative integers.
   It is nonempty, because $-1 \in A$.
2. Let $a \in A$.
   Then $a - 1$ is a negative integer, so $a - 1 \in A$, and $a - 1 < a$.
3. So no element of $A$ is less than or equal to every element of $A$, and $A$ has no least element.
4. Let $B = \{q \in \mathbb{Q} : q > 0\}$.
   It is nonempty, because $1 \in B$.
5. Let $q \in B$.
   Then $q / 2$ is rational and positive, so $q / 2 \in B$, and $q / 2 < q$ because $q > 0$.
6. So $B$ has no least element either.

Each set also contains an infinite strictly decreasing sequence:
$$-1 > -2 > -3 > \cdots \text{ in } A, \qquad 1 > \tfrac{1}{2} > \tfrac{1}{4} > \cdots \text{ in } B.$$

## Remarks

The two sets fail for different reasons.
The integers fail because they have no lower bound.
A nonempty set $E$ of integers with a lower bound $m$ does have a least element, by the principle applied to the shifted set $\{e - m : e \in E\} \subseteq \mathbb{N}$.
The positive rationals have the lower bound $0$, but their order is dense, so no element is next above $0$.
The infimum of $B$ is $0$, and $0 \notin B$, while a least element must belong to the set.
The positive real numbers fail in the same way as $B$, by the same halving.

So every argument that takes "the smallest counterexample" or uses [[infinite descent|0EFYCFHYFG]] must work inside $\mathbb{N}$, or inside a set of integers with a lower bound.

The rationals can be well-ordered by some other order, because they are countable.
List them as $q_0, q_1, q_2, \ldots$ and order them by their index; that order is not the usual one.

## Explanations

### L1 human

Among the whole numbers $0, 1, 2, \ldots$, every collection has a smallest member.
Among the negative whole numbers there is no smallest one, because you can always go one further down.
Among the positive fractions there is no smallest one either, because half of a positive fraction is smaller and still positive.
So "take the smallest one" is safe for counting numbers and unsafe for other kinds of numbers.

### L2 human

Compare a set of integers with no lower bound and the same set cut off at a lower bound.
Let $C = \{n \in \mathbb{Z} : n^2 \ge 10\}$.
Since $3^2 = 9 < 10 \le 16 = 4^2$, the set is
$$C = \{\ldots, -6, -5, -4\} \cup \{4, 5, 6, \ldots\}.$$
It has no least element: each negative element $n$ has the smaller element $n - 1$, and each positive element is larger than $-4$.
Now let $C' = \{n \in C : n \ge -10\}$, which has the lower bound $-10$.
Shift by $10$: the set $\{n + 10 : n \in C'\}$ is a nonempty set of natural numbers with least element $0$, so $C'$ has the least element $-10$.
Check: $(-10)^2 = 100 \ge 10$, so $-10 \in C'$.

Use the counterexample as a test for every proof that picks a smallest element: name the set, and show that it lies in $\mathbb{N}$ or has a lower bound in $\mathbb{Z}$.
Watch out for integers that can be negative, such as the exponent of a prime in a rational number; "the least exponent" needs a lower bound.
The [[false minimal counterexample over the positive rationals|7YZWT2AA6R]] shows an argument that breaks in exactly this way.
