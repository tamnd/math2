---
tag: F9FTASTFSX
kind: definition
name: Homotopy continuation for polynomial systems
msc: [65H14, 65H20, 14Q65]
defines: 5VR7XNNXN0
uses: [5V3GJ84CPQ, 07GNX8GCYP, 09FTAET5Z4, KWNVF194D8, 9YA6S6HD9V]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_algebraic_geometry
---

## Definition

Let $f = (f_1, \dots, f_n)$ be a system of [[polynomials|07GNX8GCYP]] in $n$ variables with [[complex|09FTAET5Z4]] coefficients, and let $d_i \ge 1$ be the degree of $f_i$.
Let $g = (g_1, \dots, g_n)$ be a *start system* with known solutions.
An example is the total-degree start system $g_i(x) = x_i^{d_i} - 1$, whose $d_1 d_2 \cdots d_n$ solutions are the tuples of roots of unity.
Fix a complex number $\gamma$ and define the [[homotopy|9YA6S6HD9V]]
$$H(x, t) = (1 - t) \, \gamma \, g(x) + t \, f(x), \qquad x \in \C^n, \ t \in [0, 1].$$
*Homotopy continuation* for $f$ is the following procedure.
For each solution $x_0$ of $g$, it follows the path $x(t)$ with $H(x(t), t) = 0$ and $x(0) = x_0$ by [[numerical continuation|5V3GJ84CPQ]], for $t$ from $0$ towards $1$.
It returns the limits of $x(t)$ as $t \to 1$.

## Remarks

With the total-degree start system and a generic choice of $\gamma$, the paths are smooth and do not meet for $t \in [0, 1)$.
Every isolated solution of $f$ is then the limit of at least one path, and the number of paths is the Bézout number $d_1 \cdots d_n$, the bound of [[Bézout's theorem|KWNVF194D8]].
Choosing $\gamma$ at random is called the gamma trick; with probability one it avoids the values of $\gamma$ for which paths collide or blow up before $t = 1$.
Example: for $f(x) = x^2 - 4$ in one variable, $g(x) = x^2 - 1$ and $\gamma = 1$, one gets $H(x, t) = x^2 - 1 - 3t$, and the two paths $x(t) = \pm\sqrt{1 + 3t}$ start at $\pm 1$ and end at $\pm 2$.
Non-example: with $\gamma = -1$ and the same $f$ and $g$, one gets $H(x, t) = (2t - 1) x^2 + 1 - 5t$, whose leading coefficient vanishes at $t = 1/2$, so both paths go to infinity there and the procedure fails.
Some paths may diverge or end at singular or non-isolated solutions; practical codes detect and handle these endgames.

## Explanations

### L1 human

Start with equations whose solutions you know, and blend them gradually into the equations you want to solve.
Each known solution moves continuously during the blend, and you track it with small steps.
Where the tracks end, you read off the solutions you were looking for.
