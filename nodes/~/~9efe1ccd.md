---
tag: ~9efe1ccd
kind: definition
name: Characteristic polynomial of a linear recurrence
msc: [39A06]
defines: ~aebf75d9
uses: [~d312aec3]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_recurrence_with_constant_coefficients
    locator: Characteristic polynomial and roots
---

## Definition

Let $R$ be a commutative ring, and let $E$ be a [[linear recurrence with constant coefficients|~d312aec3]] over $R$, of order $d$ with coefficients $c_0, \dots, c_{d-1}$.
The characteristic polynomial of $E$ is the polynomial
$$\chi_E(X) = X^d - \sum_{i=0}^{d-1} c_i X^i \in R[X].$$

## Remarks

For the Fibonacci recurrence $u_{n+2} = u_{n+1} + u_n$, the characteristic polynomial is $X^2 - X - 1$. Its roots are the [[golden ratio|~2297c8d3]] $\varphi$ and $1 - \varphi$.
A geometric sequence $q^n$ is a solution if and only if $q$ is a root of $\chi_E$. The node [[geometric solutions|~4eb1a320]] states this.

## Explanations

### L1 human

Replace $u_{n+i}$ by $X^i$ in the recurrence and move everything to one side.
This gives the characteristic polynomial, and its roots tell you the geometric sequences that solve the recurrence.
