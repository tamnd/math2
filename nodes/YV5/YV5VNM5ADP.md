---
tag: YV5VNM5ADP
kind: statement
role: proposition
name: Mellin transform of a dilation
msc: [44A15]
uses: [SGZZ4Y0D36, N5PVGRJE1T, 0RNGDMHT7M]
about: [N5PVGRJE1T]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Statement

Let $f \colon (0, \infty) \to \C$ be measurable, let $a > 0$ and let $g(x) = f(ax)$ for $x > 0$.
Let $s \in \C$.
Then $g$ is [[Mellin convergent|SGZZ4Y0D36]] at $s$ if and only if $f$ is.
In that case
$$\mathcal{M}g(s) = a^{-s} \, \mathcal{M}f(s),$$
where $\mathcal{M}$ is the [[Mellin transform|N5PVGRJE1T]] and $a^{-s} = e^{-s \log a}$ is a [[complex power|0RNGDMHT7M]].

## Remarks

The proof is the substitution $u = ax$:
$$\int_0^\infty x^{s-1} f(ax) \, dx = \int_0^\infty \left(\frac{u}{a}\right)^{s-1} f(u) \, \frac{du}{a} = a^{-s} \int_0^\infty u^{s-1} f(u) \, du.$$
The same computation with $\abs{f}$ and $\operatorname{Re} s$ gives the equivalence of convergence.
Example: $f(x) = e^{-x}$ gives $\int_0^\infty x^{s-1} e^{-ax} \, dx = a^{-s} \Gamma(s)$ for $\operatorname{Re} s > 0$.
Applied to $a = n$ and summed over $n$, this is the step that links the gamma function with Dirichlet series.
The hypothesis $a > 0$ is needed so that $x \mapsto ax$ maps $(0, \infty)$ onto itself.

## Explanations

### L1 human

Stretching or squeezing the input of $f$ by a factor $a$ multiplies its Mellin transform by $a^{-s}$.
So the Mellin transform turns the scaling of the variable into a simple factor, in the same way the Fourier transform turns a shift into a phase factor.

### L2 human

This is the reason the Mellin transform suits problems with scale invariance, such as homogeneous kernels and harmonic sums $\sum_k \lambda_k f(\mu_k x)$.
For a harmonic sum the rule gives $\mathcal{M}\left[\sum_k \lambda_k f(\mu_k x)\right](s) = \left(\sum_k \lambda_k \mu_k^{-s}\right) \mathcal{M}f(s)$, when the sum and integral can be exchanged.
The factor in brackets is a Dirichlet series, and its poles drive the asymptotic behaviour of the sum.
