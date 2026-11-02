---
tag: GJQVTDHKM2
kind: definition
name: Numerical methods for ordinary differential equations
msc: [65L05, 65L06, 65L20]
defines: 558XADG64M
uses: [0FXDW992DS, 0NT64JV96A, 0TGV80E6A4]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_methods_for_ordinary_differential_equations
---

## Definition

Let $f \colon [t_0, T] \times \R^d \to \R^d$ be continuous and Lipschitz continuous in its second argument.
Then the [[initial value problem|0FXDW992DS]] $y' = f(t, y)$, $y(t_0) = y_0$ has a unique solution $y$ on $[t_0, T]$.
For an integer $N \ge 1$ let $h = (T - t_0)/N$ and $t_n = t_0 + nh$ for $n = 0, \ldots, N$.
A *$k$-step method* is a rule that starts from given values $y_0, \ldots, y_{k-1}$.
For $0 \le n \le N - k$ it determines $y_{n+k}$ from $h$, $t_n$, the values $y_n, \ldots, y_{n+k-1}$ and finitely many evaluations of $f$.
It may do so by solving an equation that contains $y_{n+k}$.
It is *one-step* if $k = 1$, *explicit* if $y_{n+k}$ is given by a formula in the earlier values, and *implicit* otherwise.
The method is *convergent* if, for every such $f$ and starting values with $y_i \to y(t_0)$ for $i < k$ as $h \to 0$,
$$\max_{0 \le n \le N} \norm{y(t_n) - y_n} \to 0 \quad \text{as } h \to 0.$$
It is convergent *of order* $p$ if this maximum is $O(h^p)$ for every sufficiently smooth $f$ and starting values with error $O(h^p)$.

## Remarks

Example: the [[Euler method|0JARTXX4XP]] $y_{n+1} = y_n + h f(t_n, y_n)$ is an explicit one-step method, convergent of order $1$ when $f$ is Lipschitz in $y$.
Example: the two-step Adams–Bashforth method $y_{n+2} = y_{n+1} + \frac{h}{2}\big(3 f(t_{n+1}, y_{n+1}) - f(t_n, y_n)\big)$ is explicit with $k = 2$.
Non-example of convergence: the explicit two-step rule $y_{n+2} = -4 y_{n+1} + 5 y_n + h\big(4 f(t_{n+1}, y_{n+1}) + 2 f(t_n, y_n)\big)$ has local truncation error $O(h^4)$ but is not convergent, because the root $-5$ of $\zeta^2 + 4\zeta - 5$ makes perturbations grow like $5^n$.
Many methods use variable steps $h_n = t_{n+1} - t_n$; then $h$ is replaced by $\max_n h_n$.

## Explanations

### L1 human

A numerical method for an initial value problem produces a list of approximate values on a grid of times, each computed from the previous ones.
It is convergent if the approximations get uniformly close to the true solution when the steps get small.
