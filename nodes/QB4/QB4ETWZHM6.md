---
tag: QB4ETWZHM6
kind: example
name: The diagonal of a list of finitely supported binary sequences
msc: ["03E10", "00A35"]
topics: [GB14W4SYPK]
audience: ug1
not_instance_of:
  - target: V2H30SA654
    note: the diagonal sequence is not finitely supported, so it is not in the class under study, and the argument proves nothing about the class
uses: [V2H30SA654, 0G9EKM0E15, 01TQB88H4C, 0XCH8QVDCQ]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument
    locator: lead section
---

## Example

A binary [[sequence|0G9EKM0E15]] $s = (s(0), s(1), s(2), \ldots)$ is finitely supported if only finitely many terms $s(k)$ are $1$.
Let $E$ be the set of finitely supported binary sequences.
We list $E$, apply a [[diagonal|V2H30SA654]] flip, and see that the flip gives no contradiction.

1. For $n \in \mathbb{N}$, let $e_n(k)$ be bit $k$ of the binary expansion of $n$, so that $n = \sum_k e_n(k) 2^k$.
   Each $e_n$ has only finitely many $1$s, so $e_n \in E$.
2. Each $s \in E$ equals $e_n$ for exactly one $n$, namely $n = \sum_k s(k) 2^k$, a finite sum.
   So $e_0, e_1, e_2, \ldots$ lists $E$, and $E$ is [[countable|01TQB88H4C]].
3. Define the diagonal sequence by $t(n) = 1 - e_n(n)$.
4. For $n \ge 1$ we have $n < 2^n$, so bit $n$ of $n$ is $0$.
   Also $e_0$ is the zero sequence, so $e_0(0) = 0$.
5. So $e_n(n) = 0$ for every $n$, and $t = (1, 1, 1, \ldots)$.
6. The sequence $t$ differs from each $e_n$ at the place $n$, so $t$ is not in the list.
7. But $t$ has infinitely many terms equal to $1$, so $t \notin E$.
   The step of the method that checks that the diagonal object lies in the class fails.

## Remarks

The check that the diagonal object lies in the class is part of the method, and this example shows why.
Without the check, the same argument would "prove" that the countable set $E$ is uncountable.
In [[Cantor's diagonal argument|0XCH8QVDCQ]] the class is the set of all binary sequences, so the diagonal is always in the class.

The result changes with the class.
For the eventually periodic binary sequences, another countable set, the diagonal of any list of all of them again lies outside the set; it must, since it differs from every member.
For the set of all binary sequences, the diagonal lies inside, and the set is uncountable.
So for a countable class, the diagonal of a complete list always escapes the class, and that escape is a sign of countability, not a contradiction.

## Explanations

### L1 human

Take all strings of $0$s and $1$s that have only a few $1$s and then $0$s forever.
You can put them in one list, using the binary form of the numbers $0, 1, 2, \ldots$.
Now flip the diagonal: the new string is all $1$s.
It is not in the list, but it is also not a string with only a few $1$s.
So the diagonal trick does not show that the list misses one of our strings.

### L2 human

We compute the first diagonal entries of the list.
The zero sequence $e_0 = (0, 0, 0, \ldots)$ gives $e_0(0) = 0$.
Since $1 = 2^0$, the sequence $e_1 = (1, 0, 0, \ldots)$ gives $e_1(1) = 0$.
Since $2 = 2^1$, the sequence $e_2 = (0, 1, 0, \ldots)$ gives $e_2(2) = 0$.
Since $3 = 2^0 + 2^1$, the sequence $e_3 = (1, 1, 0, \ldots)$ gives $e_3(3) = 0$.
So the flipped diagonal starts $1, 1, 1, 1$, and by step 4 it continues with $1$ forever.

Use the example as a test of any diagonal proof: check the class of the diagonal object.
Watch out: a diagonal object outside the list need not be a new member of the class.
