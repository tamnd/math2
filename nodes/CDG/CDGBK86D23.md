---
tag: CDGBK86D23
kind: definition
name: De Morgan algebra
msc: ["06D30"]
defines: 5Q53XWV0QN
uses: [72V1Z82M5F, 0HM0HQCK6N]
sources:
  - url: https://en.wikipedia.org/wiki/De_Morgan_algebra
---

## Definition

A *De Morgan algebra* is a structure $(A, \vee, \wedge, 0, 1, \sim)$ such that:

1. $(A, \vee, \wedge, 0, 1)$ is a [[bounded lattice|72V1Z82M5F]] that is a [[distributive lattice|0HM0HQCK6N]].
2. ${\sim} \colon A \to A$ satisfies ${\sim}{\sim} a = a$ for every $a \in A$.
3. ${\sim}(a \vee b) = {\sim} a \wedge {\sim} b$ for all $a, b \in A$.

## Remarks

From clauses 2 and 3 one gets ${\sim}(a \wedge b) = {\sim} a \vee {\sim} b$, ${\sim} 0 = 1$ and ${\sim} 1 = 0$.
So ${\sim}$ is an order-reversing bijection of $A$ onto itself.

Example: the interval $[0, 1]$ with $a \vee b = \max(a, b)$, $a \wedge b = \min(a, b)$ and ${\sim} a = 1 - a$.
A chain is a distributive lattice, $1 - (1 - a) = a$, and $1 - \max(a, b) = \min(1 - a, 1 - b)$.
It is not a Boolean algebra, since $\tfrac12 \wedge {\sim} \tfrac12 = \tfrac12 \ne 0$.

Non-example: the chain $0 < m < 1$ with ${\sim}$ the [[pseudocomplement|WMR73J0S26]], so ${\sim} 0 = 1$, ${\sim} m = 0$, ${\sim} 1 = 0$.
Clause 2 fails, since ${\sim}{\sim} m = 1 \ne m$.
