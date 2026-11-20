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

Let $F$ be a [[field|04C5ZBG1WT]].
A [[system of linear equations|0GT4WWGWH2]] over $F$ in $n$ unknowns is *consistent* when it has at least one solution in $F^n$.
It is *inconsistent* when it has no solution.

## Remarks

The system $x + y = 1$, $x + y = 2$ over $\R$ is inconsistent.
Every homogeneous system is consistent, because the zero tuple is a solution.
The [[Rouché-Capelli theorem|0HV1SKWPMS]] gives a test with ranks: $Ax = b$ is consistent if and only if $\rank A = \rank [A \mid b]$.
Consistency depends on the field: $2x = 1$ is consistent over $\mathbb{Q}$ and inconsistent over $\mathbb{F}_2$.

## Explanations

### L1 human

"Consistent" means that the equations can all be true at the same time.
Two parallel lines in the plane, like $x + y = 1$ and $x + y = 2$, have no common point, so their system is inconsistent.
Elimination shows inconsistency when it produces an equation $0 = c$ with $c \ne 0$.

### L2 human

We show that $x - y = 1$, $2x - 2y = 3$ is inconsistent.

1. $R_2 \leftarrow R_2 - 2R_1$ gives $0x + 0y = 1$.
2. No pair $(x, y)$ satisfies $0 = 1$.
3. Row operations keep the solution set, so the original system has no solution either.

A trap: a row $0 = 0$ does not show inconsistency; it only shows that one equation was redundant.
