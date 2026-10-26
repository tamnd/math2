---
tag: 0Z3FEWZ8HA
kind: statement
role: theorem
name: Diagonalisation of a quadratic form
msc: ["11E04", 15A63]
uses: [0HZNE5QZDJ, 05Q4JD6XEH]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Equivalence of forms
---

## Statement

Let $F$ be a field of characteristic not $2$, and let $V$ be a vector space over $F$ of finite dimension $n$.
Let $Q$ be a [[quadratic form|0RBQS1JJCR]] on $V$.
Then $V$ has a basis $(e_1, \dots, e_n)$ and there are $a_1, \dots, a_n \in F$ such that, for all $x_1, \dots, x_n \in F$,
$$Q(x_1 e_1 + \cdots + x_n e_n) = a_1 x_1^2 + a_2 x_2^2 + \cdots + a_n x_n^2.$$

## Remarks

The basis is [[orthogonal|01TXN7ETH2]] for the associated symmetric bilinear form, and $a_i = Q(e_i)$.
In matrix terms, each symmetric matrix $A$ over $F$ has an invertible $P$ such that $P^T A P$ is diagonal.
The numbers $a_i$ are not unique; for example, each $a_i$ can be multiplied by a nonzero square.
Over $\R$, the orthogonal diagonalisation of the [[principal axis theorem|0PR5P9Z4KM]] is a special case.

## Explanations

### L1 human

Every quadratic form becomes a sum of squares with coefficients after a good change of variables.
For example, $x^2 + 2xy = (x + y)^2 - y^2$.
With $u = x + y$ and $v = y$, the form becomes $u^2 - v^2$.
