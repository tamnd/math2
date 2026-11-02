---
tag: 4HH0RPA7E6
kind: definition
name: Linear recurrence with polynomial coefficients
msc: [39A06, 33F10]
defines: K6QV4WSTXX
uses: [07TZV87Y0T, 0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Holonomic_function
---

## Definition

Let $K$ be a field and let $r \ge 0$ be an integer.
Let $p_0, \dots, p_r \in K[n]$ be polynomials in the [[polynomial ring|0SDC934R52]] over $K$, with $p_r \ne 0$.
The *linear recurrence with polynomial coefficients* $p_0, \dots, p_r$ is the [[recurrence relation|07TZV87Y0T]]
$$p_r(n)\, u_{n+r} + p_{r-1}(n)\, u_{n+r-1} + \cdots + p_0(n)\, u_n = 0 \qquad (n \in \N)$$
for a sequence $u \colon \N \to K$.
Its order is $r$, when $p_0 \ne 0$.

## Remarks

Example: the [[Catalan numbers|0YWZJEABB2]] $C_n$ satisfy $(n + 2)\, C_{n+1} - (4n + 2)\, C_n = 0$.
Check for $n = 0, 1$: $2 C_1 = 2 = 2 C_0$ and $3 C_2 = 6 = 6 C_1$, with $C_0 = C_1 = 1$ and $C_2 = 2$.
Non-example: $u_{n+1} - 2^n u_n = 0$ fails the definition, since the coefficient $2^n$ is not a polynomial in $n$.
When all $p_i$ are constant, the recurrence has constant coefficients.
If $p_r$ has a root $n_0 \in \N$, the equation for $n = n_0$ does not determine $u_{n_0 + r}$, so the initial values may not fix the solution.
Other names are P-recursive or holonomic recurrence; an inhomogeneous version allows a polynomial right side.
