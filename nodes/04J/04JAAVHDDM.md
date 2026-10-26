---
tag: 04JAAVHDDM
kind: definition
name: Consistent and inconsistent systems
msc: [15A06]
defines: 0X6V9B1V10
uses: [0JTRMBQ1SA]
sources:
  - url: https://en.wikipedia.org/wiki/Consistent_and_inconsistent_equations
    locator: lead section
---

## Definition

Let $F$ be a field.
A [[system of linear equations|0GT4WWGWH2]] over $F$ is *consistent* when it has at least one solution in $F^n$.
It is *inconsistent* when it has no solution.

## Remarks

The system $x + y = 1$, $x + y = 2$ over $\R$ is inconsistent.
Every homogeneous system is consistent, because the zero tuple is a solution.
The [[Rouché–Capelli theorem|0HV1SKWPMS]] gives a test with ranks: $Ax = b$ is consistent if and only if $\rank A = \rank [A \mid b]$.

## Explanations

### L1 human

"Consistent" means that the equations can all be true at the same time.
Two parallel lines in the plane, like $x + y = 1$ and $x + y = 2$, have no common point, so their system is inconsistent.
Elimination shows inconsistency when it produces an equation $0 = c$ with $c \ne 0$.
