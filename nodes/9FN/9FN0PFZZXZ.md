---
tag: 9FN0PFZZXZ
kind: statement
role: proposition
name: Derivative of a convolution
msc: [44A35, 42A85]
uses: [2Z29JN3VES, 0VW90BBSJ4, 0AR06W1E1B, BYNV84PF86]
about: [2Z29JN3VES]
sources:
  - url: https://en.wikipedia.org/wiki/Convolution
---

## Statement

Let $n \ge 1$, and let $f \colon \R^n \to \C$ be locally integrable, that is, integrable on every compact set.
Let $g \colon \R^n \to \C$ be a [[continuously differentiable function|0VW90BBSJ4]] with compact support.
Then the [[convolution|2Z29JN3VES]] $f * g$ is defined everywhere and is continuously differentiable, and for $j = 1, \dots, n$
$$\frac{\partial}{\partial x_j} (f * g) = f * \frac{\partial g}{\partial x_j}.$$

## Remarks

Write $(f * g)(x) = \int f(y) g(x - y) \, dy$ and [[differentiate under the integral sign|0AR06W1E1B]].
Let $x$ range over a bounded set and let $0 < \abs{t} \le 1$.
By the mean value theorem, the difference quotients $(g(x + t e_j - y) - g(x - y))/t$ are bounded by $\sup \abs{\partial_j g}$.
They vanish for $y$ outside a fixed compact set $K$.
Since $f$ is integrable on $K$, the [[dominated convergence theorem|BYNV84PF86]] lets the limit pass inside the integral.
Continuity of $f * \partial_j g$ follows in the same way from the uniform continuity of $\partial_j g$.

Example: on $\R$, take $f = \mathbf{1}_{[0, \infty)}$ and $g$ a continuously differentiable function with compact support.
Then $(f * g)(x) = \int_{-\infty}^x g(u) \, du$, and the formula gives $(f * g)' = f * g' = g$, as the fundamental theorem of calculus predicts.

The derivative falls on the smooth factor; $f$ itself need not be differentiable or even continuous.
Without compact support (or some decay) of $g$ the integral need not converge: for $f = 1$ and $g(x) = 1 + x^2$ the convolution is defined nowhere.

## Explanations

### L1 human

To differentiate a convolution, it is enough to differentiate one of the two factors.
You may choose the nicer one.
So a rough function convolved with a smooth one has a derivative, even if the rough function does not.

### L2 human

This is the basic step behind [[smoothing by convolution|4P7KPA3Y7R]]: by induction, $f * g$ is as differentiable as $g$.
It also explains why convolution commutes with constant-coefficient differential operators $P(\partial)$: $P(\partial)(f * g) = f * P(\partial) g$.
In the theory of distributions the same formula holds with $\partial(f * g) = (\partial f) * g = f * (\partial g)$ for any distributions $f, g$ one of which has compact support.
