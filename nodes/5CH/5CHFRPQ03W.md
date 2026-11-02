---
tag: 5CHFRPQ03W
kind: statement
role: theorem
name: Hardy inequality in Sobolev spaces
msc: [26D10, "46E35", 35A23]
uses: [M4CEZ5K9HP, S7A8YFGG8X, SASP14MA1Z]
about: [M4CEZ5K9HP]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy%27s_inequality
---

## Statement

Let $n \ge 2$ and $1 \le p < n$.
Then every continuously differentiable function $u \colon \R^n \to \R$ with compact support satisfies
$$\int_{\R^n} \frac{\abs{u(x)}^p}{\abs{x}^p} \, dx \le \Big( \frac{p}{n - p} \Big)^p \int_{\R^n} \abs{\nabla u(x)}^p \, dx.$$

## Remarks

For $p = 2$ and $n \ge 3$ there is a short proof.
Let $a = (n - 2)/2$ and expand $0 \le \int \abs{\nabla u + a u \, x / \abs{x}^2}^2 \, dx$.
The cross term is $a \int \nabla (u^2) \cdot x / \abs{x}^2 \, dx = -a (n - 2) \int u^2 / \abs{x}^2 \, dx$ by integration by parts, since $\operatorname{div}(x / \abs{x}^2) = (n - 2) / \abs{x}^2$.
Collecting terms gives $\frac{(n-2)^2}{4} \int u^2 / \abs{x}^2 \, dx \le \int \abs{\nabla u}^2 \, dx$, which is the statement.

The constant $\big( \frac{p}{n - p} \big)^p$ is the best possible, but there is no nonzero function for which equality holds.
By density, the inequality extends to every $u$ in the [[Sobolev space|M4CEZ5K9HP]] $W^{1,p}(\R^n)$.
It is the $n$-dimensional analogue of the one-dimensional [[Hardy's inequality|S7A8YFGG8X]].

The hypothesis $p < n$ is needed.
For $p = n$, take $u$ smooth with compact support and $u(0) \ne 0$: then $\abs{u}^n / \abs{x}^n$ is not integrable near $0$, while the right side is finite.

## Explanations

### L1 human

The weight $1/\abs{x}^p$ is large near the origin, so the left side punishes functions that are large near $0$.
The inequality says that the gradient energy alone pays for this, as long as the dimension is larger than $p$.
In space with $p = 2$, it says that $\int u^2 / \abs{x}^2 \le 4 \int \abs{\nabla u}^2$.

### L2 human

Hardy's inequality controls singular potentials by kinetic energy.
In quantum mechanics it shows that the operator $-\Delta - c / \abs{x}^2$ on $\R^n$ is bounded below when $c \le (n-2)^2 / 4$.
In partial differential equations it is used to treat lower-order terms with singular coefficients and to study equations with critical singular weights.
