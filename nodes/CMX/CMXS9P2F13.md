---
tag: CMXS9P2F13
kind: statement
role: theorem
name: Inversion of the Hilbert transform
msc: [44A15, 42A50]
uses: [NSCEBXM7ZM, SASP14MA1Z, PJFH51Z48M, DPVM34ADZV]
about: [NSCEBXM7ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_transform
---

## Statement

Let $1 < p < \infty$ and let $f \in L^p(\R)$, an element of the [[$L^p$ space|SASP14MA1Z]].
Let $H$ denote the [[Hilbert transform|NSCEBXM7ZM]].
Then $Hf \in L^p(\R)$ and
$$H(Hf) = -f$$
almost everywhere.
So $H$ is a bijection of $L^p(\R)$ onto itself, with inverse $H^{-1} = -H$.

## Remarks

For $f \in L^2(\R)$ the [[Fourier transform|DPVM34ADZV]] of $Hf$ is $-i \sgn(\xi)\, \hat f(\xi)$.
Applying this twice multiplies $\hat f$ by $(-i \sgn \xi)^2 = -1$ for $\xi \ne 0$, which gives $H^2 f = -f$ on $L^2$.
For general $p$, [[M. Riesz's theorem|PJFH51Z48M]] says that $H$ is bounded on $L^p$, so $H^2$ is bounded too, and the identity extends from the dense subspace $L^2 \cap L^p$ by continuity.
The hypothesis $p > 1$ is needed: for $f \in L^1(\R)$ the function $Hf$ need not lie in $L^1$.
For example, the indicator function of $[0, 1]$ has $Hf(x) = \frac{1}{\pi} \log \abs{\frac{x}{x - 1}}$, which behaves like $\frac{1}{\pi x}$ as $\abs{x} \to \infty$ and is not integrable.

Example: for $f(x) = \frac{1}{1 + x^2}$ one has $Hf(x) = \frac{x}{1 + x^2}$ and then $H\big[\frac{x}{1 + x^2}\big] = -\frac{1}{1 + x^2}$.

## Explanations

### L1 human

Doing the Hilbert transform twice gives back the original function with a minus sign.
So the transform loses no information, and its inverse is the same operation with a minus sign.
On waves, it is a quarter-period shift, and two quarter-period shifts turn a wave upside down.

### L2 human

The inversion formula says that $H$ is, up to sign, its own inverse; on $L^2$ it is a unitary operator with $H^* = -H$.
It explains the symmetry between the two halves of a Hilbert transform pair.
An example is the pair of real and imaginary parts of the boundary values of a function in the [[Hardy space|PNNNFJVF6W]] of the upper half-plane.
Together with the boundedness on $L^p$ for $1 < p < \infty$, it is the starting point of the theory of singular integral operators.
