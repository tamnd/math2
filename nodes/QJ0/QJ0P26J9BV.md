---
tag: QJ0P26J9BV
kind: concept
name: Overdetermined and underdetermined systems
aliases: [overdetermined-system, underdetermined-system]
msc: [15A06, 65F20]
topics: [DXSXFVDMXQ]
audience: ug1
specializes: [0GT4WWGWH2]
uses: [0GT4WWGWH2, 0X6V9B1V10, 0EWQEYRVA8, 0HV1SKWPMS]
sources:
  - url: https://en.wikipedia.org/wiki/Overdetermined_system
  - url: https://en.wikipedia.org/wiki/Underdetermined_system
    locator: lead section
  - book: isbn:9781733146678
    locator: Chapter 4
same_as:
  wikidata: Q331348
  wikipedia: Overdetermined system
---

## Summary

An overdetermined system is a [[system of linear equations|0GT4WWGWH2]] with more equations than unknowns, $m > n$.
An underdetermined system has fewer equations than unknowns, $m < n$.
An overdetermined system usually has no solution; a system with no solution is called [[inconsistent|0X6V9B1V10]].
An underdetermined system never has exactly one solution: it has none, or more than one.
Overdetermined systems arise whenever many measurements are fitted with a model that has few parameters, and the method of [[least squares|0BYTQ4X1HC]] then finds the vector that comes closest to solving all equations.
Underdetermined systems arise when a model has more parameters than the data can fix, and one then asks for the solution of smallest length.

## Motivation

Each equation is a condition, and each unknown is a freedom.
Counting conditions against freedoms predicts the usual behaviour of a system before we solve it.
The prediction can fail when some equations depend on others, so the exact answer needs the [[rank|0EWQEYRVA8]].

## Notation

1. A square system has $m = n$; it is neither overdetermined nor underdetermined.
2. Write $r = \rank A$; then $r \le \min(m, n)$, and a matrix with $r = \min(m, n)$ has full rank.

## Remarks

### Examples

1. [[Three lines without a common point|XJX2NN45ED]] is an overdetermined system that is inconsistent.
2. [[A consistent overdetermined system and a least squares fit|XYTJ19AEKC]] has $3$ equations, $2$ unknowns and a solution, until one right side changes.
3. [[Two planes meeting in a line|PRB44DTZ1P]] is an underdetermined system with a line of solutions.
4. The system $x + y + z = 1$, $x + y + z = 2$ is underdetermined and inconsistent.
5. The system $x + y = 1$, $2x + 2y = 2$, $3x + 3y = 3$ is overdetermined by count, but it has infinitely many solutions, because its rank is $1$.

### Non-examples

1. [[A square system|SZZX4B3JMY]] has as many equations as unknowns.
2. A single equation $ax = b$ in one unknown is square, not underdetermined.

### Basic properties

1. If $m > n$, the column space of $A$ has dimension at most $n < m$, so some right-hand sides $b \in F^m$ give an inconsistent system.
2. If $m < n$, then $A$ has at most $m < n$ pivots, so a consistent system has a free variable and more than one solution.
3. If $m < n$ and $\rank A = m$, the system is consistent for every $b$, by the [[Rouché-Capelli theorem|0HV1SKWPMS]], and the solutions form a flat of dimension $n - m$.
4. If $m > n$ and $\rank A = n$, a consistent system has a unique solution.
5. Over $\R$, a matrix with random real entries has full rank with probability $1$; this is the precise sense of "usually" above.

### History

Fitting an overdetermined system of observations was the origin of least squares, in the work of Legendre in 1805 and of Gauss.
The terms "overdetermined" and "underdetermined" are standard in numerical linear algebra and in statistics.

### Common errors

1. Thinking that an overdetermined system is always inconsistent; dependent equations can make it consistent.
2. Thinking that an underdetermined system always has a solution; two parallel planes in $\R^3$ give none.
3. Counting the equations instead of the rank to decide uniqueness.

## Explanations

### L1 human

With more conditions than freedoms, the conditions usually contradict each other.
Picture three lines in the plane: two lines usually meet in a point, but a third line usually misses that point.
With fewer conditions than freedoms, some unknowns stay free.
Two planes in space usually meet in a line, not in a point.

### L2 human

We look at the overdetermined system $x + y = 2$, $x - y = 0$, $2x + y = 3$ over $\R$.

1. The first two equations give $x = y = 1$.
2. The third equation then reads $2 + 1 = 3$, which is true.
3. So the system is consistent, with the unique solution $(1, 1)$.
4. If the third right side were $4$, the third equation would read $3 = 4$, and there would be no solution.
5. Check: $1 + 1 = 2$, $1 - 1 = 0$ and $2 + 1 = 3$.

The typical use is to predict, from the shape of $A$, whether to expect no solution, one solution, or many.
A trap: the counts $m$ and $n$ give only the usual case; the rank of $A$ and of $[A \mid b]$ decides the actual case.

### L3 human

For an inconsistent overdetermined system over $\R$, the least squares solutions solve the normal equations $A^T A x = A^T b$, which are always consistent.
For a consistent underdetermined system of full row rank, the solution of smallest length is $x = A^T (A A^T)^{-1} b$, the [[Moore-Penrose inverse|0YY8VX28JR]] applied to $b$.
Both are orthogonal projections: of $b$ onto the column space, and of any solution onto the row space.
