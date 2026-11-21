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

Counting equations against unknowns predicts what a system usually does: too many conditions clash, and too few leave freedom.
An overdetermined system is a [[system of linear equations|0GT4WWGWH2]] with more equations than unknowns, $m > n$.
An underdetermined system has fewer equations than unknowns, $m < n$.
An overdetermined system usually has no solution, that is, it is usually [[inconsistent|0X6V9B1V10]].
An underdetermined system never has exactly one solution: it has none, or more than one.
Overdetermined systems arise when many measurements are fitted with a model that has few parameters, and [[least squares|0BYTQ4X1HC]] then finds the vector that comes closest to solving all equations.
Underdetermined systems arise when a model has more parameters than the data can fix, and one then asks for the solution of smallest length.

## Motivation

Picture three lines in the plane.
Two of them usually meet in one point, and the third line usually misses that point, so three equations in two unknowns usually have no common solution.
Two planes in space usually meet in a line, so two equations in three unknowns leave one unknown free.
The prediction fails when some equations depend on others, so the exact answer needs the [[rank|0EWQEYRVA8]].

## Notation

A square system has $m = n$, and it is neither overdetermined nor underdetermined.
Write $r = \rank A$; then $r \le \min(m, n)$, and a matrix with $r = \min(m, n)$ has full rank.

## Remarks

### An overdetermined system that is consistent

Take $x + y = 2$, $x - y = 0$, $2x + y = 3$ over $\mathbb{R}$.
The first two equations give $x = y = 1$, and the third then reads $2 + 1 = 3$, which is true.
So the system is consistent, with the unique solution $(1, 1)$.
If the third right side were $4$, the third equation would read $3 = 4$, and there would be no solution.

### More examples

[[Three lines without a common point|XJX2NN45ED]] is an overdetermined system that is inconsistent.
[[A consistent overdetermined system and a least squares fit|XYTJ19AEKC]] has $3$ equations, $2$ unknowns and a solution, until one right side changes.
[[Two planes meeting in a line|PRB44DTZ1P]] is an underdetermined system with a line of solutions.
The system $x + y + z = 1$, $x + y + z = 2$ is underdetermined and inconsistent.
The system $x + y = 1$, $2x + 2y = 2$, $3x + 3y = 3$ is overdetermined by count, but it has infinitely many solutions, because its rank is $1$.
[[A square system|SZZX4B3JMY]] is neither, and so is a single equation $ax = b$ in one unknown.

### What the counts force

If $m > n$, the column space of $A$ has dimension at most $n < m$, so some right sides $b \in F^m$ give an inconsistent system.
If $m < n$, then $A$ has at most $m < n$ pivots, so a consistent system has a free variable and more than one solution.
If $m < n$ and $\rank A = m$, the system is consistent for every $b$, by the [[Rouché-Capelli theorem|0HV1SKWPMS]], and the solutions form a flat of dimension $n - m$.
If $m > n$ and $\rank A = n$, a consistent system has a unique solution.
A real matrix whose entries are drawn from a continuous distribution has full rank with probability $1$, which is the precise sense of "usually" above.

### History

Fitting an overdetermined system of observations was the origin of least squares, in the work of Legendre in 1805 and of Gauss.

### Watch out

An overdetermined system is not always inconsistent, since dependent equations can make it consistent.
An underdetermined system does not always have a solution, since two parallel planes in $\mathbb{R}^3$ give none.
Uniqueness is decided by the rank, not by the number of equations.

### Try it

Is $x + y + z = 1$, $x - y = 0$ underdetermined, and what are its solutions?
It has $2$ equations in $3$ unknowns, so yes, and with $z = t$ we get $x = y = \tfrac{1 - t}{2}$, a line.

## Explanations

### L1 human

With more conditions than freedoms, the conditions usually contradict each other.
Picture three lines in the plane: two lines usually meet in a point, but a third line usually misses that point.
With fewer conditions than freedoms, some unknowns stay free.
Two planes in space usually meet in a line, not in a point.

### L2 human

The typical use is to predict, from the shape of $A$, whether to expect no solution, one solution, or many.
Watch out: the counts $m$ and $n$ give only the usual case, and the ranks of $A$ and of $[A \mid b]$ decide the actual case.

### L3 human

For an inconsistent overdetermined system over $\mathbb{R}$, the least squares solutions solve the normal equations $A^{\mathsf{T}} A x = A^{\mathsf{T}} b$, which are always consistent.
For a consistent underdetermined system of full row rank, the solution of smallest length is $x = A^{\mathsf{T}} (A A^{\mathsf{T}})^{-1} b$, the [[Moore-Penrose inverse|0YY8VX28JR]] applied to $b$.
Both are orthogonal projections: of $b$ onto the column space, and of any solution onto the row space.
