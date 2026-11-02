---
tag: P4DFMJTD09
kind: definition
name: Empirical risk minimization
msc: [68Q32, 62H30, 68T05]
defines: 56NVR0SS61
uses: [3BTG6VVCGZ, N26TSVRH2S, 0BYTQ4X1HC]
sources:
  - url: https://en.wikipedia.org/wiki/Empirical_risk_minimization
---

## Definition

Let $\mathcal X$ and $\mathcal Y$ be sets, let $L \colon \mathcal Y \times \mathcal Y \to [0, \infty)$ be a [[loss function|3BTG6VVCGZ]], and let $\mathcal F$ be a class of functions $f \colon \mathcal X \to \mathcal Y$.
Let $(x_1, y_1), \dots, (x_n, y_n) \in \mathcal X \times \mathcal Y$ be data.
The *empirical risk* of $f \in \mathcal F$ is
$$R_n(f) = \frac1n \sum_{i=1}^{n} L(f(x_i), y_i).$$
*Empirical risk minimization* over $\mathcal F$ selects a function $\hat f \in \mathcal F$ with $R_n(\hat f) = \inf_{f \in \mathcal F} R_n(f)$, when such a function exists.

## Remarks

When the data are a random sample from a distribution $P$, $R_n(f)$ is an unbiased estimate of the [[risk|N26TSVRH2S]] $R(f) = E[L(f(X), Y)]$ for each fixed $f$.
For the selected $\hat f$, however, $R_n(\hat f)$ tends to underestimate $R(\hat f)$, because $\hat f$ was chosen to fit the same data.

Example: with $\mathcal X = \R$, $\mathcal Y = \R$, the squared loss $L(a, y) = (a - y)^2$ and $\mathcal F = \set{x \mapsto a + bx : a, b \in \R}$, empirical risk minimization is fitting a line by [[least squares|0BYTQ4X1HC]].

Non-example: ridge regression minimises $R_n(f) + \lambda \norm{\beta}^2$ with $\lambda > 0$ over linear functions $f(x) = \beta^T x$.
Its minimiser is in general not a minimiser of $R_n$ alone, so it is regularized empirical risk minimization, not empirical risk minimization.
