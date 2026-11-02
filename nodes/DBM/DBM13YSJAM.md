---
tag: DBM13YSJAM
kind: statement
role: proposition
name: Differentiation operator as inverse of integration
msc: [44A40]
uses: [82YAXZMMQ1, BDBDJSP6DF, 0NHGY0N0JB]
about: [82YAXZMMQ1, TD5XK5AHNV]
sources:
  - url: https://en.wikipedia.org/wiki/Operational_calculus
---

## Statement

Let $\mathcal{M}$ be the [[Mikusiński field of operators|82YAXZMMQ1]], the field of fractions of the convolution ring of locally integrable functions on $[0, \infty)$.
Let $h$ be the constant function $1$ on $[0, \infty)$, and let $s = 1/h$ be its inverse in $\mathcal{M}$.
For a complex number $c$, write $c$ also for the numerical operator $c \cdot 1$ of $\mathcal{M}$, which corresponds to the function $c\,h$ divided by $h$.
Let $f$ be continuously differentiable on $[0, \infty)$.
Then
$$s f = f' + f(0)$$
in $\mathcal{M}$.
More generally, if $f$ is $n$ times continuously differentiable on $[0, \infty)$, then
$$s^n f = f^{(n)} + \sum_{k=0}^{n-1} f^{(k)}(0) \, s^{n-1-k}.$$

## Remarks

By the [[fundamental theorem of calculus|0NHGY0N0JB]], $\int_0^t f'(\tau) \, d\tau = f(t) - f(0)$.
By the [[integration operator result|BDBDJSP6DF]] this reads $h f' = f - f(0) h$ in the convolution ring.
Multiplying both sides by $s$ gives $f' = s f - f(0)$, which is the first formula.
The general formula follows by induction on $n$.
For example, with $f(t) = e^{a t}$, one gets $s f = a f + 1$, so $f = 1/(s - a)$ in $\mathcal{M}$.
The operator $s$ is not a function: it is a quotient of functions, and $s f$ equals the function $f'$ only when $f(0) = 0$.

## Explanations

### L1 human

Integration from $0$ is multiplication by the constant function $1$.
Its inverse in the field of operators is an operator $s$ that acts like differentiation.
It differs from plain differentiation by a term that remembers the starting value $f(0)$.

### L2 human

This formula has the same shape as the rule $\mathcal{L}\{f'\}(s) = s F(s) - f(0)$ for the Laplace transform.
Mikusiński's calculus gets it with no condition on the growth of $f$ and no convergence of integrals.
A linear differential equation with constant coefficients and initial values becomes an algebraic equation in $s$ in the field $\mathcal{M}$.
One then solves for the unknown and reads off a function, often after a partial fraction expansion in $s$.
