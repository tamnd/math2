---
tag: MHSBP40HDC
kind: statement
role: proposition
name: Shift operator as an exponential of differentiation
msc: [44A45, 47B39, "26E05"]
uses: [0Z49YH6ZWY, 081WKEDK6C, 0V1EJCT8G6]
about: [0Z49YH6ZWY]
sources:
  - url: https://en.wikipedia.org/wiki/Shift_operator
---

## Statement

Let $f \colon \R \to \C$ be given by a power series $f(x) = \sum_{n \ge 0} c_n x^n$ that converges for every $x \in \R$; for example, $f$ may be a polynomial.
For $h \in \R$, let $T_h f$ be the shifted function $(T_h f)(x) = f(x + h)$, and let $D = d/dx$.
Then for all $x, h \in \R$
$$(T_h f)(x) = \sum_{n=0}^\infty \frac{h^n}{n!} \, (D^n f)(x).$$
In operator notation, $T_h = e^{hD}$ on such functions.

## Remarks

The right side is the [[Taylor series|0Z49YH6ZWY]] of $f$ at $x$, evaluated at the increment $h$.
A power series that converges on all of $\R$ is an [[analytic function|081WKEDK6C]] whose Taylor series at every point converges to it on all of $\R$, which gives the identity.
For a polynomial of degree $d$ the sum stops at $n = d$, and the identity is exact algebra.

Example: $f(x) = x^2$.
Then $f + h f' + \frac{h^2}{2} f'' = x^2 + 2hx + h^2 = (x + h)^2$.

The hypothesis of analyticity is needed.
For the [[smooth non-analytic function|09RTYYHXKA]] $f(x) = e^{-1/x^2}$ for $x \ne 0$, $f(0) = 0$, all derivatives vanish at $0$, so the right side at $x = 0$ is $0$, while $f(h) > 0$ for $h \ne 0$.

## Explanations

### L1 human

Knowing all derivatives of a nice function at one point determines its values nearby.
The formula packages this as "shifting by $h$ equals the exponential of $h$ times differentiation".
It is Taylor's formula written as an identity between operators.

### L2 human

Since $e^{hD} e^{kD} = e^{(h+k)D}$, the identity explains why shifts compose by adding the steps.
In the calculus of finite differences, the forward difference $\Delta = T_1 - \id$ becomes $e^D - 1$, and on polynomials this gives formal identities such as $D = \log(1 + \Delta) = \Delta - \Delta^2/2 + \Delta^3/3 - \cdots$, a finite sum on each polynomial.
In quantum mechanics the same identity says that the momentum operator generates translations.
