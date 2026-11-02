---
tag: XJWC13NY9E
kind: statement
role: theorem
name: Mellin inversion theorem
msc: [44A15]
uses: [SGZZ4Y0D36, N5PVGRJE1T, CHESR1W1CY, X7GTF3D98F]
about: [N5PVGRJE1T, CHESR1W1CY]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_inversion_theorem
same_as:
  wikidata: Q6813106
  wikipedia: Mellin inversion theorem
---

## Statement

Let $f \colon (0, \infty) \to \C$ be measurable and let $c \in \R$.
Assume that $f$ is [[Mellin convergent|SGZZ4Y0D36]] at $c$, so that the [[Mellin transform|N5PVGRJE1T]] $\mathcal{M}f(s) = \int_0^\infty x^{s-1} f(x) \, dx$ is defined on the line $\operatorname{Re} s = c$.
Assume also that $y \mapsto \mathcal{M}f(c + iy)$ is [[integrable|X7GTF3D98F]] on $\R$.
Then, for every $x > 0$ at which $f$ is continuous,
$$f(x) = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} x^{-s} \, \mathcal{M}f(s) \, ds.$$
The right side is the [[inverse Mellin transform|CHESR1W1CY]] of $\mathcal{M}f$ along $\operatorname{Re} s = c$.

## Remarks

Put $x = e^{u}$ and $g(u) = e^{cu} f(e^u)$.
Mellin convergence at $c$ says that $g$ is integrable on $\R$, and $\mathcal{M}f(c + iy) = \int_{\R} g(u) e^{iyu} \, du$ is a Fourier transform of $g$.
The [[Fourier inversion theorem|T4Z8YQZKZV]] then recovers $g$ almost everywhere, hence at every point where $g$ is continuous, and this is the formula above.
Example: $f(x) = e^{-x}$ with $c > 0$ gives $e^{-x} = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} \Gamma(s) x^{-s} \, ds$, the Cahen–Mellin integral.
Continuity at $x$ is needed: if $f(x) = e^{-x}$ is changed at the single point $x = 1/2$, its Mellin transform is still $\Gamma$.
So the formula gives $e^{-1/2}$ there and not the changed value.
For $f = \mathbf{1}_{(0, 1]}$, the transform $\mathcal{M}f(s) = 1/s$ is not integrable on vertical lines, so the integrability hypothesis fails.
The formula still holds at $x \ne 1$ as a limit of integrals over $[c - iT, c + iT]$, but that needs a separate argument.

## Explanations

### L1 human

The Mellin transform loses no information: a reasonable function can be rebuilt from its transform on any single vertical line where the transform is defined.
The rebuilding is an integral of the powers $x^{-s}$ against the transform.

### L2 human

The theorem is the Fourier inversion theorem written on the multiplicative group $(0, \infty)$.
It is how one passes from a Mellin transform back to a function, as in Perron's formula and in [[Barnes integrals|1PDGBGEHM2]].
There the transform is often a product of gamma functions or a Dirichlet series.
In practice one then shifts the line of integration and collects residues, which turns the inversion integral into series or asymptotic expansions.
Without integrability of $\mathcal{M}f$ on the line, as for jump functions, the integral must be taken as a symmetric limit.
For functions of bounded variation near a jump, this limit is the average of the one-sided limits.
