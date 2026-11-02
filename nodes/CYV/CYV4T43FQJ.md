---
tag: CYV4T43FQJ
kind: statement
role: theorem
name: Gauss–Newton algorithm
msc: [65K10, 90C30, 62J02]
uses: [047NDTEPCV, 0BYTQ4X1HC, 07EXVNF9VP, 0QNVQ4VD9T, YWZQC5E54B]
about: [C7E69V030F]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton_algorithm
same_as:
  wikidata: Q1496373
  wikipedia: Gauss–Newton algorithm
---

## Statement

Let $D \subseteq \R^n$ be open, let $m \ge n$, and let $r \colon D \to \R^m$ be continuously differentiable with [[Jacobian matrix|047NDTEPCV]] $J(x)$.
The aim is to minimize $S(x) = \tfrac12 \norm{r(x)}_2^2$.
The *Gauss–Newton algorithm* starts from $x_0 \in D$ and sets
$$x_{k+1} = x_k - \bigl( J(x_k)^T J(x_k) \bigr)^{-1} J(x_k)^T r(x_k),$$
as long as $J(x_k)$ has full column rank.
Suppose that $x^* \in D$ satisfies $r(x^*) = 0$, that $J(x^*)$ has full column rank, and that $J$ is [[Lipschitz continuous|0QNVQ4VD9T]] near $x^*$.
Then there are $\delta > 0$ and $C > 0$ such that, for every $x_0$ with $\norm{x_0 - x^*} < \delta$, the iterates are defined, converge to $x^*$, and satisfy
$$\norm{x_{k+1} - x^*} \le C \norm{x_k - x^*}^2.$$

## Remarks

The step $p_k = x_{k+1} - x_k$ is the [[least squares|0BYTQ4X1HC]] solution of the linearized problem $\min_p \norm{r(x_k) + J(x_k) p}_2$.
In practice one computes it by a QR factorization of $J(x_k)$ rather than by forming $J^T J$.
The Hessian of $S$ is $J^T J + \sum_i r_i \nabla^2 r_i$.
Gauss–Newton drops the second term, so near a zero-residual solution it behaves like [[Newton's method|07EXVNF9VP]], which gives the quadratic rate.

If $r(x^*) \ne 0$, the dropped term need not vanish, and the convergence is then in general only linear.
For large residuals or strongly nonlinear $r_i$, the iteration may diverge even from good starting points.
A line search or the [[Levenberg–Marquardt algorithm|TH54SPVN1N]] makes the method robust.
Example: fitting $y = e^{c t}$ to the data $(0, 1)$, $(1, e)$ has zero residual at $c = 1$, so Gauss–Newton converges quadratically from any $c_0$ near $1$.

## Explanations

### L1 human

Many fitting problems ask for parameters that make a nonlinear model match data as closely as possible in the least squares sense.
Gauss–Newton replaces the model by its linear approximation at the current guess, solves the resulting linear least squares problem, and repeats.
When the model can fit the data exactly, it converges very fast near the answer.

### L2 human

The method needs only first derivatives of the residuals, unlike Newton's method for $S$, which needs second derivatives.
It is the basic method of [[nonlinear regression|C7E69V030F]] and of many calibration and inverse problems.
The rank condition on $J(x^*)$ is needed: without it the linearized problems have no unique solution, and the convergence theory fails.
