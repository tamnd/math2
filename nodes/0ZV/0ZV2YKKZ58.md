---
tag: 0ZV2YKKZ58
kind: definition
name: Solution of a linear recurrence
msc: [39A06]
defines: 06MJC8YDYR
uses: [081THG13JZ]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_recurrence_with_constant_coefficients
    locator: General solution
---

## Definition

Let $R$ be a commutative ring, and let $E$ be a [[linear recurrence with constant coefficients|081THG13JZ]] over $R$, of order $d$ with coefficients $c_0, \dots, c_{d-1}$.
A solution of $E$ is a sequence $u : \mathbb{N} \to R$ such that
$$u_{n+d} = \sum_{i=0}^{d-1} c_i\, u_{n+i} \quad \text{for all } n \in \mathbb{N}.$$

## Remarks

Each choice of the initial values $u_0, \dots, u_{d-1}$ gives exactly one solution.
The sum of two solutions is a solution, and a multiple of a solution is a solution. So the solutions form the [[space of solutions|05BDYVQQ0T]].
For $u_{n+2} = u_{n+1} + u_n$, the Lucas numbers $2, 1, 3, 4, 7, 11, \dots$ form a solution.

## Explanations

### L1 human

A solution is a sequence that obeys the rule of the recurrence at every step.
The rule alone does not fix the sequence: you also choose the first $d$ terms.
