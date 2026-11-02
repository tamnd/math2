---
tag: 25HF1WPPKX
kind: statement
role: theorem
name: Schur test
msc: [45P05, 47G10, 47B38]
uses: [P15VQS5DJ9, YYNCJSR0PJ, SASP14MA1Z, 03TM135G0N]
about: [SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_test
same_as:
  wikidata: Q4456448
  wikipedia: Schur test
---

## Statement

Let $(X, \mu)$ and $(Y, \nu)$ be $\sigma$-finite [[measure spaces|P15VQS5DJ9]], and let $K \colon X \times Y \to \C$ be a [[measurable function|YYNCJSR0PJ]].
Assume that there are measurable functions $p \colon X \to (0, \infty)$ and $q \colon Y \to (0, \infty)$ and constants $\alpha, \beta > 0$ such that
$$\int_Y \abs{K(x, y)} \, q(y) \, d\nu(y) \le \alpha \, p(x) \quad \text{for almost every } x \in X,$$
$$\int_X \abs{K(x, y)} \, p(x) \, d\mu(x) \le \beta \, q(y) \quad \text{for almost every } y \in Y.$$
Then for every $f \in L^2(Y, \nu)$ the integral
$$(T f)(x) = \int_Y K(x, y) \, f(y) \, d\nu(y)$$
converges absolutely for almost every $x$.
Moreover, $T$ is a [[bounded linear operator|03TM135G0N]] from $L^2(Y, \nu)$ to $L^2(X, \mu)$ with operator norm $\norm{T} \le \sqrt{\alpha \beta}$.

## Remarks

Proof idea: write $\abs{K} \abs{f} = \big(\abs{K} q\big)^{1/2} \big(\abs{K} \abs{f}^2 / q\big)^{1/2}$ and apply the Cauchy–Schwarz inequality in $y$.
The first hypothesis gives $\abs{T f(x)}^2 \le \alpha \, p(x) \int_Y \abs{K(x, y)} \abs{f(y)}^2 q(y)^{-1} \, d\nu(y)$.
Integrating in $x$ and exchanging the integrals by Tonelli's theorem, the second hypothesis gives $\norm{T f}_2^2 \le \alpha \beta \norm{f}_2^2$.

With $p = q = 1$ the test says: if $\int_Y \abs{K(x, y)} \, d\nu(y) \le \alpha$ for almost every $x$ and $\int_X \abs{K(x, y)} \, d\mu(x) \le \beta$ for almost every $y$, then $\norm{T} \le \sqrt{\alpha \beta}$ on $L^2$.
For $\alpha = \beta$ this is the case $p = 2$ of [[Young's inequality for integral operators|48NS4ZCSR3]].
The freedom to choose the weights $p$ and $q$ is what makes the test useful for kernels such as $1/(x + y)$, which have no finite row or column integrals.

Example: let $X = Y = (0, \infty)$ with Lebesgue measure and $K(x, y) = 1/(x + y)$.
Take $p(x) = x^{-1/2}$ and $q(y) = y^{-1/2}$.
The substitution $y = x u$ gives $\int_0^\infty \frac{y^{-1/2}}{x + y} \, dy = x^{-1/2} \int_0^\infty \frac{u^{-1/2}}{1 + u} \, du = \pi x^{-1/2}$, and by symmetry the same holds for the second hypothesis.
So $\alpha = \beta = \pi$ and $\norm{T} \le \pi$, which is the continuous form of [[Hilbert's inequality|G4R4MWWP3C]].

## Explanations

### L1 human

An integral operator acts on a function by averaging it against a kernel $K(x, y)$.
The Schur test gives a simple way to see that such an operator does not blow up the size of functions, measured in $L^2$.
One only has to find one positive test function for the rows and one for the columns of the kernel, and check two integral inequalities.

### L2 human

The Schur test is the main elementary tool to prove that an integral operator is bounded on $L^2$ when its kernel is not square-integrable.
Such an operator is not [[Hilbert–Schmidt|W3BX66Y47G]].
It is used for kernels with a singularity or slow decay, such as homogeneous kernels on $(0, \infty)$ and kernels in the study of Bergman projections.
It is the continuous analogue of the bound of the norm of a matrix by the geometric mean of the largest row sum and the largest column sum.
For $L^p$ with $p \ne 2$, the same idea with Hölder's inequality in place of Cauchy–Schwarz gives a version with weights.
