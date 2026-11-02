---
tag: CG7BFJ04YE
kind: statement
role: proposition
name: Mellin transform under a power substitution
msc: [44A15]
uses: [SGZZ4Y0D36, N5PVGRJE1T]
about: [N5PVGRJE1T]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Statement

Let $f \colon (0, \infty) \to \C$ be measurable, let $a \in \R$ with $a \ne 0$, and let $g(x) = f(x^{a})$ for $x > 0$.
Let $s \in \C$.
Then $g$ is [[Mellin convergent|SGZZ4Y0D36]] at $s$ if and only if $f$ is Mellin convergent at $s/a$.
In that case
$$\mathcal{M}g(s) = \frac{1}{\abs{a}} \, \mathcal{M}f\left(\frac{s}{a}\right),$$
where $\mathcal{M}$ is the [[Mellin transform|N5PVGRJE1T]].

## Remarks

For $a > 0$, substitute $u = x^{a}$, so $x = u^{1/a}$ and $dx = \frac{1}{a} u^{1/a - 1} \, du$:
$$\int_0^\infty x^{s-1} f(x^{a}) \, dx = \frac{1}{a} \int_0^\infty u^{(s-1)/a} \, u^{1/a - 1} f(u) \, du = \frac{1}{a} \int_0^\infty u^{s/a - 1} f(u) \, du.$$
For $a < 0$ the substitution reverses the orientation of $(0, \infty)$, which turns the factor $1/a$ into $1/\abs{a}$.
The case $a = -1$ is the rule for the inversion $x \mapsto 1/x$.
Example: $f(x) = e^{-x}$ and $a = 2$ give $\int_0^\infty x^{s-1} e^{-x^2} \, dx = \frac{1}{2} \Gamma(s/2)$ for $\operatorname{Re} s > 0$; at $s = 1$ this is $\int_0^\infty e^{-x^2} \, dx = \frac{1}{2}\Gamma(1/2) = \frac{\sqrt{\pi}}{2}$.
The hypothesis $a \ne 0$ is needed: for $a = 0$, $g$ is the constant $f(1)$, which is Mellin convergent at no $s$ unless $f(1) = 0$.

## Explanations

### L1 human

Replacing $x$ by a power $x^{a}$ rescales the Mellin variable: $s$ becomes $s/a$, and a factor $1/\abs{a}$ appears.
It is the logarithmic version of the rule that stretching a function by a factor rescales its Fourier transform.

### L2 human

This rule computes many transforms from a few, for instance Gaussian integrals from the gamma function.
It is used in the Riemann proof of the functional equation, where the theta function $\sum_n e^{-\pi n^2 x}$ meets $\Gamma(s/2)$ rather than $\Gamma(s)$.
Combined with the rules for dilations and for multiplication by powers, it describes the Mellin transform of $x^{b} f(c x^{a})$ for all $a \ne 0$, $b \in \C$ and $c > 0$.
