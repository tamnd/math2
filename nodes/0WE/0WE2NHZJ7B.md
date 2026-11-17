---
tag: 0WE2NHZJ7B
kind: concept
name: Order of an element
aliases: [period-of-an-element]
msc: [20A05]
topics: [BAZT8JJ70S]
audience: ug1
uses: [G5S1M9, 00DRK90Z6K]
sources:
  - url: https://en.wikipedia.org/wiki/Order_(group_theory)
    locator: lead section
  - book: isbn:9781305657960
    locator: Chapter 3
inventory: [2WR87G5VKX]
---

## Summary

Let $G$ be a [[group|G5S1M9]] with identity element $e$, and let $g \in G$.
The order of $g$ is the smallest positive integer $n$ with $g^n = e$, where $g^n$ is the $n$th power of $g$ by the [[laws of exponents|00DRK90Z6K]].
When no positive integer $n$ has $g^n = e$, the element $g$ has infinite order.
The order of $g$ equals the [[order|0B85S2V2DR]] of the [[cyclic subgroup|031M8HX7DA]] $\langle g \rangle$ that $g$ generates.
So the order tells how many different powers $g$ has before they repeat.

## Motivation

When we take the powers $g, g^2, g^3, \ldots$ of an element of a finite group, they must repeat, because the group has only finitely many elements.
In a group, a repeat $g^a = g^b$ with $a < b$ gives $g^{b - a} = e$ by cancellation.
So some positive power of $g$ is $e$, and the powers of $g$ run around a cycle.
The order is the length of this cycle.
It answers the question: after how many steps does $g$ come back to the start?
Rotations give the simplest picture: a rotation of the plane by $360/n$ degrees comes back to the identity after $n$ steps, and not before.
The orders of the elements are the first tool to tell two groups of the same order apart.

## Notation

The order of $g$ is written $\ord(g)$, $|g|$ or $o(g)$.
The notation $|g|$ matches the notation $|G|$ for the order of a group, because $|g| = |\langle g \rangle|$.
In math2 the word "order" also means the order $|G|$ of a group, and the object (a group or an element) shows which meaning is used.
In an abelian group written additively, the order of $g$ is the smallest positive integer $n$ with $n g = 0$.
In Mathlib the order of $g$ is `orderOf g`, and it is a natural number.
Mathlib uses the value $0$ for an element of infinite order, so `orderOf g = 0` means that $g$ has infinite order.

## Remarks

### Examples

1. The identity element $e$ of each group has order $1$, because $e^1 = e$.
2. [[The orders of the elements of the integers modulo 6|77N4TVRM15]] are $1, 6, 3, 2, 3, 6$ for the elements $0, 1, 2, 3, 4, 5$.
3. [[The orders of the elements of the symmetric group S3|Y20PEX049W]] are $1$ for the identity, $2$ for the three transpositions and $3$ for the two $3$-cycles.
4. In the multiplicative group of nonzero [[complex numbers|09FTAET5Z4]], the number $i$ has order $4$, because $i^1 = i$, $i^2 = -1$ and $i^3 = -i$ are not $1$, and $i^4 = 1$.
5. In the group $(\mathbb{Z}, +)$ of [[integers|0C4JS9RF5M]], each nonzero integer $m$ has infinite order, because $n m \neq 0$ for each positive integer $n$.
6. In the [[general linear group|0FCHE902D7]] $\mathrm{GL}_2(\mathbb{R})$, the [[rotation|0HFREYRSZP]] matrix $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has order $4$, because $R^2 = -I$, $R^3 = -R$ and $R^4 = I$, and none of $R$, $-I$ and $-R$ is $I$.
7. In the same group, the matrix $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has infinite order, because $A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$ by induction, and this is not $I$ for $n \geq 1$.

### Non-examples

1. [[An idempotent matrix whose powers never reach the identity|5VEW97EQR6]]: the matrix $E$ with $E^2 = E \neq I$ is not invertible, so it is not an element of a group with identity $I$, and it has no order.
2. In $\mathbb{Z}/6\mathbb{Z}$ with multiplication, the powers of $2$ are $2, 4, 2, 4, \ldots$ and never $1$. This does not give an element of infinite order: $2$ has no multiplicative inverse modulo $6$, so it is not an element of a group under multiplication.

### Basic properties

1. $\ord(g) = 1$ if and only if $g = e$, because $g^1 = g$.
2. [[An element and its inverse have the same order|0PMT9YJZVW]]. Reason: for each positive integer $n$, $(g^{-1})^n = (g^n)^{-1}$, and an element is $e$ if and only if its inverse is $e$. So $g^n = e$ and $(g^{-1})^n = e$ hold for the same $n$.
3. When $g$ has finite order $n$, [[$g^m = e$ if and only if $n$ divides $m$|0F5QC101Q7]].
4. When $g$ has finite order $n$, [[the order of $g^k$ is $n / \gcd(n, k)$|0VVPQNVM8S]].
5. In a finite group each element has finite order, by the argument in Motivation. The order of $g$ is $|\langle g \rangle|$, so [[it divides the order of the group|08V7JHS3QZ]].
6. An [[isomorphism|08MG7H8JW5]] $\varphi$ keeps orders: $\varphi(g)^n = \varphi(g^n)$, and $\varphi(g^n) = e$ if and only if $g^n = e$, because $\varphi$ is injective and maps $e$ to $e$.

### History

In his Disquisitiones Arithmeticae of 1801, Carl Friedrich Gauss studied, for a prime $p$ and an integer $a$ not divisible by $p$, the least positive exponent $t$ with $a^t \equiv 1 \pmod p$.
This number is the order of $a$ in the multiplicative group of the nonzero residues modulo $p$.
The abstract notion for an element of any group came later, with the abstract definition of a group.

### Common errors

1. The order of a product is taken to be the product of the orders. In $S_3$, the elements $(1\,2)$ and $(1\,2\,3)$ have orders $2$ and $3$, but their product $(1\,2)(1\,2\,3) = (2\,3)$ has order $2$.
2. From $g^n = e$ the conclusion $\ord(g) = n$ is drawn. The correct conclusion is only that $\ord(g)$ divides $n$. In $\mathbb{Z}/6\mathbb{Z}$, $6 \cdot 2 = 0$, but the order of $2$ is $3$.
3. In additive notation the power $g^n$ is written as $g^n$ instead of $n g$. In $\mathbb{Z}/6\mathbb{Z}$ the order of $2$ asks for $n \cdot 2 = 0$, not for a product $2 \cdot 2 \cdots 2$.

## Explanations

### L1 human

Think of the hand of a clock with $12$ hours.
A move of $3$ hours, done again and again, brings the hand back to the start after $4$ moves, because $4 \cdot 3 = 12$.
So the move of $3$ hours has order $4$.
A move of $5$ hours needs $12$ moves to come back, so it has order $12$.
The order of an element is this number of moves.
When the element never comes back, as a step of $1$ on an endless number line, its order is infinite.

### L2 human

We compute the order of $3$ in the group of nonzero residues modulo $7$ under multiplication.

1. $3^1 = 3$.
2. $3^2 = 9 \equiv 2 \pmod 7$.
3. $3^3 \equiv 2 \cdot 3 = 6 \pmod 7$.
4. $3^4 \equiv 6 \cdot 3 = 18 \equiv 4 \pmod 7$.
5. $3^5 \equiv 4 \cdot 3 = 12 \equiv 5 \pmod 7$.
6. $3^6 \equiv 5 \cdot 3 = 15 \equiv 1 \pmod 7$.

The first power equal to $1$ is the sixth power, so $\ord(3) = 6$.
The group has order $6$, so $3$ generates the whole group, and $3$ is a [[primitive root modulo|0F33KX9Q6F]] $7$.
The typical use of the order is this kind of test: an element whose order equals $|G|$ generates $G$, and then $G$ is [[cyclic|0KVGH0J5B3]].
A trap is to stop at the first power that looks small; each power up to the first $1$ must be checked, and only the first $1$ gives the order.

### L3 human

The map $\mathbb{Z} \to G$, $n \mapsto g^n$, is a [[group homomorphism|0JYTG5K9Y4]] from $(\mathbb{Z}, +)$.
Its kernel is a subgroup of $\mathbb{Z}$, so it is $m \mathbb{Z}$ for a unique $m \geq 0$.
When $m > 0$, the element $g$ has order $m$; when $m = 0$, the element $g$ has infinite order.
This is the reason for the Mathlib convention that `orderOf g = 0` for an element of infinite order.
The elements of finite order are the torsion elements, and a group in which each element has finite order is a [[torsion group|JZNQTTMG58]].
In an abelian group the torsion elements form the [[torsion subgroup|0DBWXQRXQJ]].
The least common multiple of all element orders, when it is finite, is the [[exponent|0ZDW0H0VX4]] of the group.
In a monoid that is not a group, the powers of an element can enter a cycle that does not contain the identity, and then one speaks of the index and the period of the element instead.
