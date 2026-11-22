---
tag: 0XCH8QVDCQ
kind: concept
name: Cantor's diagonal argument
aliases: [diagonal-argument, diagonalization]
msc: ["03E10"]
topics: [G9JFJGY4TQ, GB14W4SYPK]
audience: ug1
uses: [0X55M9XET4, 0ZG61TFBES]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor's_diagonal_argument
    locator: lead section
same_as:
  wikidata: Q729471
  wikipedia: Cantor's diagonal argument
---

## Summary

Cantor's diagonal argument shows that some infinite sets are too large to be listed: every list of infinite binary sequences misses some binary sequence.
It is the first proof that there are different sizes of infinity, and its idea, [[diagonalization|V2H30SA654]], returns in logic and computer science.

Given any list $s_0, s_1, s_2, \ldots$ of infinite sequences of $0$s and $1$s, define a new sequence $t$ by flipping the diagonal entries:
$$t(n) = 1 - s_n(n) \quad \text{for every } n \ge 0.$$
Then $t(n) \ne s_n(n)$, so $t$ differs from each $s_n$ at the position $n$, and $t$ is not in the list.
So the set $\{0, 1\}^{\mathbb{N}}$ of all binary sequences is not [[countable|0ZG61TFBES]]; it is [[uncountable|0X55M9XET4]].

## Motivation

The natural numbers, the integers and the rationals can all be listed, so it is tempting to think that every infinite set can be.
To refute this, one must show that every list misses something, not only that some list does.
The diagonal argument does exactly that: from any list it builds, by one explicit rule, a sequence that the list does not contain.

The argument turns uncountability into a construction.
From it come the uncountability of the real numbers, [[Cantor's theorem|0WTEMGYV2C]] that no set maps onto its power set, and the proof patterns of the halting problem and of Gödel's incompleteness theorems.

## Notation

A binary sequence is a function $s \colon \mathbb{N} \to \{0, 1\}$, and $s(n)$ is its entry at position $n$.
The set of all of them is written $\{0, 1\}^{\mathbb{N}}$ or $2^{\mathbb{N}}$.
Some books start the positions at $1$, which changes nothing.
Picture the list as a table whose row $n$ is $s_n$: the entries $s_n(n)$ lie on the diagonal, and $t$ is the diagonal with every entry flipped.

## Remarks

### A first computation

Take a list that starts with
$$s_0 = 0\,1\,1\,0 \ldots, \quad s_1 = 1\,1\,0\,0 \ldots, \quad s_2 = 0\,0\,0\,1 \ldots, \quad s_3 = 1\,0\,1\,0 \ldots.$$
The diagonal entries are $s_0(0) = 0$, $s_1(1) = 1$, $s_2(2) = 0$ and $s_3(3) = 0$.
Flip each of them, and the new sequence starts $t = 1\,0\,1\,1 \ldots$.
Check: $t$ differs from $s_0$ at position $0$, from $s_1$ at position $1$, from $s_2$ at position $2$ and from $s_3$ at position $3$.
The same rule continues down the whole list, so $t$ differs from every row.

### From sequences to real numbers

To show that the [[real numbers are uncountable|0518MM6BE1]], send each binary sequence $s$ to the decimal number
$$\phi(s) = 0.s(0)\,s(1)\,s(2)\ldots = \sum_{n \ge 0} s(n)\, 10^{-n-1}.$$
Two different sequences give two different numbers, because a number has two decimal expansions only when one of them ends in repeated $9$s, and these expansions use only the digits $0$ and $1$.
So $\phi$ is injective, and a list of all real numbers in $[0, 1)$ would give a list of all binary sequences, which is impossible.
Cantor's first proof of 1874 used nested intervals instead.

### The same idea for every set

For any set $X$ and any map $f \colon X \to \mathcal{P}(X)$, the set $D = \{x \in X : x \notin f(x)\}$ differs from each $f(x)$ at the element $x$.
This is Cantor's theorem, and [[the three-element example|Z9Q8PGPQ1Y]] computes $D$ for one map.
For $X = \mathbb{N}$, a subset is a binary sequence, its indicator, and the set $D$ is exactly the flipped diagonal $t$.

### When the diagonal proves nothing

The finitely supported binary sequences, those with only finitely many $1$s, can be listed, for example by the binary digits of $0, 1, 2, \ldots$.
The flipped diagonal of that list is $1, 1, 1, \ldots$, which is not in the list but also not finitely supported, as [[the finitely supported example|QB4ETWZHM6]] shows.
So the argument proves uncountability only when the diagonal object lies in the set under study.

A finite list behaves differently too.
For the $8$ binary strings of length $3$, the diagonal has only $3$ positions, so it can only avoid the first $3$ strings, and the list of all $8$ is complete.

### Watch out

With decimal digits, a flip such as "$9$ becomes $0$" can produce a second name of a listed number, because $0.0999\ldots = 0.1000\ldots$.
The safe rule changes each digit to $5$, and a $5$ to $6$, so the new number has no $0$ or $9$ in its expansion and only one name.
A second slip is to think that the argument shows only one missing sequence: if a list missed only countably many sequences, adding them would give a list of all, so every list misses uncountably many.

### History

Georg Cantor published the diagonal argument in 1891.
His first proof that $\mathbb{R}$ is uncountable, from 1874, used another method.

### Try it

First, a list starts with $s_0 = 1111\ldots$, $s_1 = 0000\ldots$, $s_2 = 1010\ldots$.
Give the first three entries of $t$.
They are $1 - 1 = 0$, $1 - 0 = 1$ and $1 - 1 = 0$, so $t$ starts $0\,1\,0$.

Second, does the argument work with the change $t(n) = s_n(n)$, without the flip?
No, because then $t$ agrees with $s_n$ at position $n$, and $t$ may equal a row: if every row of the list is $0\,0\,0 \ldots$, then $t = s_0$.

## Explanations

### L1 human

Write the list of sequences as the rows of a table, one row per sequence.
Go down the diagonal, from the top left corner, and change each entry: $0$ to $1$ and $1$ to $0$.
Read the changed diagonal as a new row.
It differs from row $0$ in column $0$, from row $1$ in column $1$, and so on, so it cannot be any row of the table.
No matter how cleverly the list is made, it always misses a row.

### L2 human

Here is a typical problem: show that the set of infinite sequences of digits from $\{1, 2, 3\}$ is uncountable.
Suppose $s_0, s_1, s_2, \ldots$ lists them all.
Choose a change with no fixed value, for example $\sigma(1) = 2$, $\sigma(2) = 3$ and $\sigma(3) = 1$, and define
$$t(n) = \sigma(s_n(n)).$$
Each $t(n)$ is one of $1, 2, 3$, so $t$ is a sequence of the kind under study.
Since $\sigma$ moves every value, $t(n) \ne s_n(n)$, and $t$ differs from each $s_n$.
So the list misses $t$, and the set is uncountable.
The problem shows that the flip $1 - y$ is just one choice: any change of values with no fixed point works, and that is the general form of [[diagonalization|V2H30SA654]].

### L3 human

In the language of functions, the argument shows that no map $\mathbb{N} \to \{0, 1\}^{\mathbb{N}}$ is onto, and with $X$ in place of $\mathbb{N}$ it proves $|X| < |\mathcal{P}(X)|$ for every set.
So there is no largest cardinal, and the power set gives an endless chain of larger and larger infinities.
Lawvere's fixed-point theorem gives the abstract form, in which Russell's paradox, the [[undecidability of the halting problem|Z7TN2B35B0]] and [[Gödel's incompleteness theorems|X9WYNYE29C]] are instances of the same diagonal step.
The [[counting arguments for existence|1KVSS0KRZA]] use the result to show that transcendental numbers exist and that most real numbers are not computable.
