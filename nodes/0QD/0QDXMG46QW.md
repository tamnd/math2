---
tag: 0QDXMG46QW
kind: definition
name: Characteristic equation
aliases: [auxiliary-equation]
msc: [34A30]
defines: 0GZWXM2DKE
uses: [0A6PGTTP2A]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_equation_(calculus)
    locator: Derivation
---

## Definition

Let $a_0, \dots, a_{n-1}$ be real numbers, and consider the homogeneous [[linear equation with constant coefficients|0A6PGTTP2A]]
$$y^{(n)} + a_{n-1}\, y^{(n-1)} + \dots + a_1\, y' + a_0\, y = 0.$$
Its characteristic polynomial is $p(r) = r^n + a_{n-1} r^{n-1} + \dots + a_1 r + a_0$.
Its characteristic equation is the polynomial equation $p(r) = 0$ for an unknown complex number $r$.

## Remarks

For each complex $r$, the function $y = e^{r x}$ satisfies $y^{(n)} + \dots + a_0 y = p(r)\, e^{r x}$. So $e^{rx}$ is a solution if and only if $p(r) = 0$.
Example: the equation $y'' - 3 y' + 2 y = 0$ has the characteristic equation $r^2 - 3 r + 2 = 0$, with roots $1$ and $2$.
The [[characteristic polynomial of a linear recurrence|0BWDJGQYST]] plays the same role for recurrences, with $r^k$ in place of $e^{r x}$.

## Explanations

### L1 human

Try a solution of the form $e^{r x}$.
Each derivative multiplies it by $r$, so the equation becomes $p(r) e^{rx} = 0$.
Since $e^{rx}$ is never zero, $r$ must be a root of $p$.
