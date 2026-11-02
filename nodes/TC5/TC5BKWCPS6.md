---
tag: TC5BKWCPS6
kind: definition
name: Cauchy's logarithmic equation
msc: [39B22]
defines: 9HTRR4P4M1
uses: [SRAN4EKWS0, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_functional_equation
---

## Definition

*Cauchy's logarithmic equation* is the [[functional equation|SRAN4EKWS0]]
$$f(xy) = f(x) + f(y) \quad \text{for all } x, y > 0,$$
for an unknown [[function|0EPAT51DXQ]] $f \colon (0, \infty) \to \R$.
A solution is a function $f$ that satisfies this identity for all positive $x$ and $y$.

## Remarks

Example: $f(x) = \log_2 x$ is a solution, since $\log_2(xy) = \log_2 x + \log_2 y$.
Non-example: $f(x) = x - 1$ is not a solution, since $f(2 \cdot 2) = 3$ while $f(2) + f(2) = 2$.
The substitution $x = e^s$, $y = e^t$ turns the equation into additivity of $A(s) = f(e^s)$.
So the solutions are $f(x) = A(\ln x)$ with $A$ an [[additive function|KF719SZD5T]], and the continuous ones are $f(x) = c \ln x$.
On the domain $\R \setminus \set{0}$ the solutions are $f(x) = A(\ln \abs{x})$; on all of $\R$ only $f = 0$ is a solution, since $f(0) = f(0) + f(x)$.
