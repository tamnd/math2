---
tag: PJFH51Z48M
kind: statement
role: theorem
name: M. Riesz theorem on the Hilbert transform
msc: [42A50, 44A15]
uses: [NSCEBXM7ZM, SASP14MA1Z, A1H48DDW49]
about: [NSCEBXM7ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_transform
---

## Statement

Let $1 < p < \infty$, and let $H$ be the [[Hilbert transform|NSCEBXM7ZM]] on $\R$.
Then there is a constant $C_p$, depending only on $p$, such that
$$\norm{Hf}_{L^p(\R)} \le C_p \norm{f}_{L^p(\R)} \quad \text{for all } f \in L^p(\R).$$
The same holds for the [[conjugate function|A1H48DDW49]] on the circle: $\norm{\tilde f}_{L^p} \le C_p \norm{f}_{L^p}$ for all $f \in L^p(\R/2\pi\Z)$.

## Remarks

Marcel Riesz's proof for $p = 2k$ an even integer uses complex analysis.
If $f$ is real and $F = f + iHf$ extends holomorphically to the upper half-plane, then $\int F^{2k} = 0$, and taking real parts bounds $\norm{Hf}_{2k}$ by $\norm{f}_{2k}$.
Interpolation then gives $2 \le p < \infty$, and duality gives $1 < p \le 2$, since $H$ is skew-adjoint.
A real-variable proof combines the bound on $L^2$ with a weak type $(1, 1)$ bound, through the Marcinkiewicz interpolation theorem.
The best constant is $C_p = \tan\frac{\pi}{2p}$ for $1 < p \le 2$ and $C_p = \cot\frac{\pi}{2p}$ for $2 \le p < \infty$, a result of Pichorides.

Example: for $p = 2$, $H$ is an isometry, since its multiplier $-i\sgn\xi$ has modulus $1$, and $C_2 = \tan(\pi/4) = 1$.

The theorem fails for $p = 1$ and $p = \infty$.
For $f = \mathbf{1}_{[0, 1]}$, one has $Hf(x) = \frac{1}{\pi} \log\abs{\frac{x}{x - 1}}$.
This is unbounded near $x = 0$ and $x = 1$, and it behaves like $\frac{1}{\pi x}$ at infinity, so it is not integrable.

## Explanations

### L1 human

The Hilbert transform turns each cosine wave into a sine wave, and so turns the real part of a holomorphic function into its imaginary part.
This theorem says it does not make functions much bigger, measured in any $L^p$ norm with $1 < p < \infty$.
At the two ends, $p = 1$ and $p = \infty$, a jump in the function creates a logarithmic blow-up, and the bound fails.

### L2 human

The theorem is equivalent to the convergence of Fourier series in $L^p(\R/2\pi\Z)$ for $1 < p < \infty$.
Indeed, the partial sum operators are combinations of modulated conjugate function operators, so the bound for $\tilde f$ gives uniform bounds for the partial sums.
It is the first case of the theory of singular integrals, which extends it to the [[Riesz transforms|FRNDFJ9WQ5]] and to [[Calderón–Zygmund operators|3SCXCW4AH3]].
