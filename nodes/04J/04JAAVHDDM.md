---
tag: 04JAAVHDDM
kind: definition
name: Consistent and inconsistent systems
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
defines: 0X6V9B1V10
uses: [0JTRMBQ1SA]
sources:
  - url: https://en.wikipedia.org/wiki/Consistent_and_inconsistent_equations
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 1.1
---

## Definition

A system is consistent when it has a solution, and inconsistent when it has none.
Let $F$ be a [[field|04C5ZBG1WT]].
A [[system of linear equations|0GT4WWGWH2]] over $F$ in $n$ unknowns is *consistent* when it has at least one solution in $F^n$.
It is *inconsistent* when it has no solution in $F^n$.

## Remarks

The definition asks only for existence.
A consistent system may have one solution or many, and the question of how many is separate, answered by the theorem on [[existence and uniqueness of solutions|BKA191KD1S]].

The solutions must lie in $F^n$, so the field is part of the question.
The equation $2x = 1$ is consistent over $\mathbb{Q}$, but over $\mathbb{F}_2$ the coefficient $2$ is $0$ and the equation reads $0 = 1$.

Every homogeneous system is consistent, because the zero tuple is a solution.
In contrast, the system $x + y = 1$, $x + y = 2$ over $\mathbb{R}$ is inconsistent, since one sum cannot equal two different numbers.
The [[Rouché-Capelli theorem|0HV1SKWPMS]] gives a test with ranks: $Ax = b$ is consistent if and only if $\rank A = \rank\, [A \mid b]$.
The concept page on [[consistent and inconsistent systems|0X6V9B1V10]] shows how elimination decides the question.

## Explanations

### L1 human

"Consistent" means that the equations can all be true at the same time.
Two parallel lines in the plane, like $x + y = 1$ and $x + y = 2$, have no common point, so their system is inconsistent.
Elimination shows inconsistency when it produces an equation $0 = c$ with $c \ne 0$.

### L2 human

To show that $x - y = 1$, $2x - 2y = 3$ is inconsistent, apply $R_2 - 2R_1$:
$$(2x - 2y) - 2(x - y) = 3 - 2 \cdot 1, \qquad \text{that is,} \qquad 0 = 1.$$
No pair $(x, y)$ satisfies $0 = 1$, and row operations keep the solution set, so the original system has no solution either.
Watch out: a row $0 = 0$ does not show inconsistency, because it only says that one equation was redundant.
