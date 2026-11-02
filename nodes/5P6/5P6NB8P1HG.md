---
tag: 5P6NB8P1HG
kind: statement
role: theorem
name: Representer theorem
msc: ["46E22", 68Q32, 62G08]
uses: [4CK2GSRAGD, HM2HHE3J51, 56NVR0SS61]
about: [4CK2GSRAGD, 56NVR0SS61]
sources:
  - url: https://en.wikipedia.org/wiki/Representer_theorem
same_as:
  wikidata: Q7314263
  wikipedia: Representer theorem
---

## Statement

Let $\mathcal X$ be a nonempty set and let $k \colon \mathcal X \times \mathcal X \to \R$ be a positive-definite kernel with [[reproducing kernel Hilbert space|4CK2GSRAGD]] $H$ and norm $\norm{\cdot}_H$.
Let $x_1, \dots, x_n \in \mathcal X$, let $c \colon \R^n \to \R \cup \set{\infty}$ be any function, and let $g \colon [0, \infty) \to \R$ be strictly increasing.
Then every minimiser $f \in H$ of
$$c(f(x_1), \dots, f(x_n)) + g(\norm{f}_H)$$
has the form
$$f = \sum_{i=1}^{n} \alpha_i \, k(\cdot, x_i)$$
for some real numbers $\alpha_1, \dots, \alpha_n$.

## Remarks

Proof idea: let $V$ be the span of $k(\cdot, x_1), \dots, k(\cdot, x_n)$ in the [[Hilbert space|HM2HHE3J51]] $H$, and write $f = f_V + f_\perp$ with $f_V \in V$ and $f_\perp \perp V$.
By the reproducing property $f(x_i) = \langle f, k(\cdot, x_i) \rangle_H = f_V(x_i)$, so the first term only depends on $f_V$.
Since $\norm{f}_H^2 = \norm{f_V}_H^2 + \norm{f_\perp}_H^2$ and $g$ is strictly increasing, any $f$ with $f_\perp \ne 0$ is beaten by $f_V$.
If $g$ is only nondecreasing, the same argument shows that, if a minimiser exists, some minimiser has this form.

Example: kernel ridge regression minimises $\frac1n \sum_{i=1}^{n} (y_i - f(x_i))^2 + \lambda \norm{f}_H^2$ with $\lambda > 0$.
By the theorem $f = \sum_i \alpha_i k(\cdot, x_i)$, and with the Gram matrix $K_{ij} = k(x_i, x_j)$ the problem becomes a quadratic problem in $\alpha \in \R^n$, solved by $\alpha = (K + n \lambda I)^{-1} y$.

Without the penalty $g(\norm{f}_H)$ the conclusion fails: if $H$ is infinite-dimensional, adding to a minimiser any nonzero $f_\perp \perp V$ gives another minimiser of $c(f(x_1), \dots, f(x_n))$ that is not in $V$.

## Explanations

### L1 human

Searching for the best function in an infinite-dimensional space looks hopeless.
The representer theorem says that, for this kind of penalised fitting problem, the best function is a combination of $n$ simple bumps, one centred at each data point.
So the problem reduces to finding $n$ numbers.

### L2 human

The theorem is what makes kernel methods computable: support vector machines, kernel ridge regression and smoothing splines all reduce to finite-dimensional problems in $\alpha$ involving only the Gram matrix $K$.
It is a form of regularized [[empirical risk minimization|56NVR0SS61]] in a [[reproducing kernel Hilbert space|4CK2GSRAGD]], where the penalty $\norm{f}_H$ controls smoothness.
The "kernel trick" follows: the solution can be evaluated at a new point $x$ as $\sum_i \alpha_i k(x, x_i)$ without ever working with elements of $H$ explicitly.
Versions of the theorem allow an additional unpenalised finite-dimensional part, such as a constant term.
