---
tag: SY0TJ4NCES
kind: statement
role: proposition
name: Commutativity of convolution
msc: [44A35, 42A85]
uses: [2Z29JN3VES, ERP5737VZ1, 2Z2QVWZ262]
about: [2Z29JN3VES]
sources:
  - url: https://en.wikipedia.org/wiki/Convolution
---

## Statement

Let $n \ge 1$, and let $f, g \colon \R^n \to \C$ be Lebesgue measurable.
Let $x \in \R^n$.
Then $\int_{\R^n} \abs{f(y) g(x - y)} \, dy < \infty$ if and only if $\int_{\R^n} \abs{g(y) f(x - y)} \, dy < \infty$.
In that case $(f * g)(x) = (g * f)(x)$, where $*$ is the [[convolution|2Z29JN3VES]].
In particular $f * g = g * f$ for all $f, g \in L^1(\R^n)$.

## Remarks

The proof is the substitution $y = x - z$.
[[Lebesgue measure|2Z2QVWZ262]] is invariant under the reflection $z \mapsto -z$ and under translations, so
$$\int_{\R^n} f(y) g(x - y) \, dy = \int_{\R^n} f(x - z) g(z) \, dz = (g * f)(x),$$
and the same computation with absolute values gives the equivalence of the two convergence conditions.

Example: on $\R$, with $f = \mathbf{1}_{[0, 1]}$ and $g = \mathbf{1}_{[0, 2]}$, both $f * g$ and $g * f$ give at $x$ the length of $[0, 1] \cap [x - 2, x]$ and of $[0, 2] \cap [x - 1, x]$, which are equal: both are $\min(x, 1)$ for $0 \le x \le 2$.

The statement uses that the group $\R^n$ is abelian.
On a non-abelian locally compact group, convolution $f * g$ with $(f * g)(x) = \int f(y) g(y^{-1} x) \, dy$ is in general not commutative.

## Explanations

### L1 human

When you convolve two functions, it does not matter which one you slide and which one stays put.
The answer is the same either way.
This is like the product of two polynomials, which does not depend on the order of the factors.

### L2 human

Commutativity, together with [[associativity|HZ5J8GGS16]] and bilinearity, makes $L^1(\R^n)$ a commutative algebra under convolution.
It is the reason why the [[convolution on the line|ERP5737VZ1]] can be written with either function shifted.
Under the Fourier transform it becomes the commutativity of the pointwise product $\hat f \hat g = \hat g \hat f$.
