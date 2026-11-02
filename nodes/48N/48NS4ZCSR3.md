---
tag: 48NS4ZCSR3
kind: statement
role: theorem
name: Young's inequality for integral operators
msc: [45P05, 47G10, 26D15]
uses: [P15VQS5DJ9, YYNCJSR0PJ, SASP14MA1Z]
about: [SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Young%27s_convolution_inequality
---

## Statement

Let $(X, \mu)$ and $(Y, \nu)$ be $\sigma$-finite [[measure spaces|P15VQS5DJ9]], let $1 \le p \le \infty$ and $C > 0$.
Let $K \colon X \times Y \to \C$ be a [[measurable function|YYNCJSR0PJ]] such that
$$\int_Y \abs{K(x, y)} \, d\nu(y) \le C \quad \text{for almost every } x \in X,$$
$$\int_X \abs{K(x, y)} \, d\mu(x) \le C \quad \text{for almost every } y \in Y.$$
Let $f \in L^p(Y, \nu)$.
Then the integral
$$(T f)(x) = \int_Y K(x, y) \, f(y) \, d\nu(y)$$
converges absolutely for almost every $x \in X$, the function $T f$ lies in $L^p(X, \mu)$, and
$$\norm{T f}_p \le C \norm{f}_p.$$

## Remarks

Proof idea for $1 < p < \infty$: let $p'$ be the conjugate exponent and write $\abs{K} = \abs{K}^{1/p'} \abs{K}^{1/p}$.
Hölder's inequality in $y$ and the first hypothesis give $\abs{T f(x)}^p \le C^{p/p'} \int_Y \abs{K(x, y)} \abs{f(y)}^p \, d\nu(y)$.
Integrating in $x$, Tonelli's theorem and the second hypothesis give $\norm{T f}_p^p \le C^{p/p'} \cdot C \norm{f}_p^p = C^p \norm{f}_p^p$.
The case $p = \infty$ uses only the first hypothesis, and the case $p = 1$ uses only the second.

Example: for $X = Y = \R^n$ with Lebesgue measure and $K(x, y) = g(x - y)$ with $g \in L^1(\R^n)$, both hypotheses hold with $C = \norm{g}_1$.
The result is $\norm{g * f}_p \le \norm{g}_1 \norm{f}_p$, the case $q = 1$ of [[Young's convolution inequality|JXDKJCBXJ8]].

Both hypotheses are needed for the full range of $p$.
On $X = Y = (0, \infty)$, the Hardy kernel $K(x, y) = 1/x$ for $y < x$ and $K(x, y) = 0$ otherwise has $\int_0^\infty K(x, y) \, dy = 1$ for every $x$, but $\int_0^\infty K(x, y) \, dx = \infty$ for every $y$.
The operator $T f(x) = \frac{1}{x} \int_0^x f(y) \, dy$ is bounded on $L^p$ for $1 < p \le \infty$ by [[Hardy's inequality|S7A8YFGG8X]], but not on $L^1$: for $f$ the indicator function of $(0, 1]$, $T f(x) = 1/x$ for $x > 1$, which is not integrable.

## Explanations

### L1 human

An integral operator replaces a function by weighted averages of its values, with weights $K(x, y)$.
Suppose that every row and every column of the weights has total mass at most $C$.
Then the operator enlarges the $L^p$ size of a function by at most the factor $C$, for every $p$.
This is the continuous analogue of the fact that a matrix whose absolute row sums and column sums are at most $C$ has norm at most $C$ on every $\ell^p$.

### L2 human

This result is sometimes called the generalized Young inequality, since it contains the case $\norm{g * f}_p \le \norm{g}_1 \norm{f}_p$ of [[Young's convolution inequality|JXDKJCBXJ8]].
It is the quickest way to show that an integral operator with an integrable kernel acts boundedly on all $L^p$ spaces at once.
For $p = 2$ it is the [[Schur test|25HF1WPPKX]] with constant weights; the Schur test allows other weights and so applies to more kernels.
In the theory of [[integral equations|R3SG1SN7JQ]] it gives the bounds that the contraction principle needs for second-kind equations in $L^p$.
