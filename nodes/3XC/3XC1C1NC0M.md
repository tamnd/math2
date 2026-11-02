---
tag: 3XC1C1NC0M
kind: statement
role: theorem
name: Hardy's uncertainty principle
msc: ["42A38", "30D15"]
uses: [DPVM34ADZV, ZNEHMR2CCP, FYR6V2NH6C]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_transform
    locator: Uncertainty principle
---

## Statement

Let $f \colon \R \to \C$ be measurable, and let $a, b > 0$ and $C \ge 0$ be constants.
Suppose that $\abs{f(x)} \le C e^{-\pi a x^2}$ for all $x \in \R$, so that $f$ is integrable.
Let $\hat f(\xi) = \int_\R f(x) e^{-2\pi i x \xi}\, dx$ be the [[Fourier transform|DPVM34ADZV]] of $f$.
Suppose that $\abs{\hat f(\xi)} \le C e^{-\pi b \xi^2}$ for all $\xi \in \R$.

1. If $ab > 1$, then $f = 0$.
2. If $ab = 1$, then $f(x) = c\, e^{-\pi a x^2}$ for some constant $c \in \C$.

## Remarks

By the [[Fourier transform of the Gaussian|ZNEHMR2CCP]], $e^{-\pi a x^2}$ has transform $a^{-1/2} e^{-\pi \xi^2 / a}$, so case 2 cannot be improved.
If $ab < 1$, then $e^{-\pi c x^2}$ satisfies both bounds, with a suitable constant $C$, for every $c$ with $a \le c \le 1/b$, so there are nonzero functions of this kind.

The proof uses complex analysis.
The decay of $f$ makes $\hat f$ extend to an entire function with $\abs{\hat f(\xi + i\eta)} \le C' e^{\pi \eta^2 / a}$.
In case 2, the entire function $g(z) = e^{\pi z^2 / a} \hat f(z)$ is bounded on the real and on the imaginary axis.
The [[Phragmén–Lindelöf principle|FYR6V2NH6C]], applied in each quadrant, shows that $g$ is bounded, hence constant by Liouville's theorem, and Fourier inversion gives $f$.
Case 1 reduces to case 2 with $b$ replaced by $1/a$, and then the bound $\abs{\hat f(\xi)} \le C e^{-\pi b \xi^2}$ with $b > 1/a$ forces the constant to be $0$.

The result is due to G. H. Hardy.
There are versions on $\R^n$, and versions with $L^p$ bounds in place of pointwise bounds.

## Explanations

### L1 human

The bell curve $e^{-\pi x^2}$ and its transform decay at the same Gaussian rate.
Hardy's theorem says that no nonzero function can do better on both sides at once.
If both $f$ and $\hat f$ decay faster than this matched pair of Gaussians, the function must be zero.

### L2 human

Unlike the Heisenberg inequality, which measures spread with variances, Hardy's theorem measures concentration through pointwise decay.
It is a sharp qualitative statement, and the borderline case singles out the Gaussians, just as the equality case of Heisenberg's inequality does.
Its proof is a model for the use of Phragmén–Lindelöf arguments in Fourier analysis.
It has been extended to Lie groups and to the Schrödinger equation, where it gives unique continuation results.
