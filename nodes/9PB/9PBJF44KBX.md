---
tag: 9PBJF44KBX
kind: statement
role: theorem
name: Quadratic convergence of Newton's method
msc: [65H05]
uses: [07EXVNF9VP, YWZQC5E54B, 0VW90BBSJ4, 0Q4QJWEHW3, 0H5ZAZCX2T]
about: [07EXVNF9VP]
sources:
  - url: https://en.wikipedia.org/wiki/Newton%27s_method
---

## Statement

Let $I$ be an open interval, let $f \colon I \to \R$ be [[twice continuously differentiable|0VW90BBSJ4]], and let $r \in I$ with $f(r) = 0$ and $f'(r) \ne 0$.
For $\delta > 0$ with $J = [r - \delta, r + \delta] \subseteq I$ and $f' \ne 0$ on $J$, let
$$M = \frac{\max_{x \in J} \abs{f''(x)}}{2 \min_{x \in J} \abs{f'(x)}}.$$
If $M \delta < 1$, then for every $x_0 \in J$ the iterates of [[Newton's method|07EXVNF9VP]], $x_{k+1} = x_k - f(x_k)/f'(x_k)$, are defined, lie in $J$, converge to $r$, and satisfy
$$\abs{x_{k+1} - r} \le M \abs{x_k - r}^2 \quad \text{for all } k \ge 0.$$
Such a $\delta$ always exists.
If moreover $x_k \ne r$ for all $k$, then
$$\lim_{k \to \infty} \frac{x_{k+1} - r}{(x_k - r)^2} = \frac{f''(r)}{2 f'(r)}.$$

## Remarks

[[Taylor's theorem with the Lagrange remainder|0H5ZAZCX2T]] at $x_k$ gives $0 = f(r) = f(x_k) + f'(x_k)(r - x_k) + \tfrac12 f''(\xi_k)(r - x_k)^2$ for some $\xi_k$ between $x_k$ and $r$.
Dividing by $f'(x_k)$ and using the definition of $x_{k+1}$ gives $x_{k+1} - r = \frac{f''(\xi_k)}{2 f'(x_k)} (x_k - r)^2$, so $\abs{x_{k+1} - r} \le M \abs{x_k - r}^2 \le M\delta \abs{x_k - r}$; this keeps the iterates in $J$ and makes them converge, and the limit follows from $\xi_k, x_k \to r$.
Since $f'(r) \ne 0$ and $f'$ and $f''$ are continuous, $M$ stays bounded as $\delta \to 0$, so a small $\delta$ gives $M\delta < 1$.
Example: for $f(x) = x^2 - 2$ from $x_0 = 1$, the errors are about $4.1 \times 10^{-1}$, $8.6 \times 10^{-2}$, $2.5 \times 10^{-3}$, $2.1 \times 10^{-6}$, $1.6 \times 10^{-12}$; each error is about $0.35$ times the square of the previous one, and $f''(r)/(2f'(r)) = 1/(2\sqrt{2}) \approx 0.35$.
The hypothesis $f'(r) \ne 0$ is needed: for $f(x) = x^2$ the iteration is $x_{k+1} = x_k/2$, which converges only linearly.
Differentiability at $r$ is needed as well: for $f(x) = x^{1/3}$ the iteration is $x_{k+1} = -2x_k$, which diverges from every $x_0 \ne 0$.

## Explanations

### L1 human

Near a simple zero, Newton's method roughly doubles the number of correct digits at each step.
If a guess is right to $3$ digits, the next one is right to about $6$, then $12$.
This holds only once the guess is close enough and the graph crosses the axis at a nonzero slope.

### L2 human

This is the basic local convergence theorem for [[Newton's method|07EXVNF9VP]]: order $2$ in the sense of [[rate of convergence|YWZQC5E54B]], with asymptotic constant $f''(r)/(2f'(r))$.
The same proof works for systems $F(x) = 0$ in $\R^n$ with an invertible Jacobian at the zero, where it is a special case of the Newton–Kantorovich theory.
At a zero of multiplicity $m \ge 2$ the convergence becomes linear with ratio $(m - 1)/m$, and the modified step $x_{k+1} = x_k - m f(x_k)/f'(x_k)$ restores quadratic convergence.
Global convergence is not guaranteed, which is why practical solvers combine Newton steps with bisection or line searches.
