---
tag: 5ENHTF01Z8
kind: concept
name: Saddle point of a Lagrangian
msc: [90C46, 49J35, 49K99]
sources:
  - url: https://en.wikipedia.org/wiki/Saddle_point
---

## Summary

A saddle point of a Lagrangian is a pair made of a point and a vector of multipliers.
At this pair the Lagrangian of a constrained optimization problem is minimal in the point and maximal in the multipliers.
Whenever such a pair exists, the point solves the constrained problem and the multipliers satisfy complementary slackness.
For convex problems that satisfy a constraint qualification, saddle points exist and they are the basis of Lagrangian duality.
The [[definition|QQMQGXS0XE]] gives the precise conditions.

## Explanations

### L1 human

A constrained problem asks for the smallest value of $f$ among points that obey some constraints.
The Lagrangian adds to $f$ a penalty for each constraint, with a price $\lambda_i \ge 0$ per unit of violation.
At a saddle point, the chooser of the point cannot gain by moving and the chooser of the prices cannot gain by changing them.
For example, to minimize $x^2$ subject to $x \ge 1$, the point $x = 1$ with price $\lambda = 2$ is a saddle point.
Unlike the [[saddle point|0JW6MDHAZD]] of a surface in calculus, it is defined by inequalities, not by derivatives.
