---
tag: MZXHSGFBRF
kind: statement
role: proposition
name: Inverse Mellin transform as inverse Fourier transform
msc: [44A15, 42A38]
uses: [CHESR1W1CY, JB8QMT8DCH, X7GTF3D98F]
about: [CHESR1W1CY, JB8QMT8DCH]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_inversion_theorem
---

## Statement

Let $c \in \R$ and let $\varphi$ be a complex function on the line $\operatorname{Re} s = c$ such that $y \mapsto \varphi(c + iy)$ is [[integrable|X7GTF3D98F]] on $\R$.
Define $\psi \colon \R \to \C$ by $\psi(t) = \varphi(c + 2\pi i t)$.
Then for every $x > 0$,
$$\mathcal{M}^{-1}_c \varphi(x) = x^{-c} \, \check{\psi}(-\log x),$$
where $\mathcal{M}^{-1}_c$ is the [[inverse Mellin transform|CHESR1W1CY]] along $\operatorname{Re} s = c$, and $\check{\psi}(u) = \int_{\R} \psi(t) e^{2\pi i u t} \, dt$ is the [[inverse Fourier transform|JB8QMT8DCH]].

## Remarks

Substitute $y = 2\pi t$ in the definition:
$$\mathcal{M}^{-1}_c \varphi(x) = \frac{1}{2\pi} \int_{\R} x^{-c - iy} \varphi(c + iy) \, dy = x^{-c} \int_{\R} e^{-2\pi i t \log x} \, \psi(t) \, dt,$$
and the last integral is $\check{\psi}(-\log x)$.
The function $\psi$ is integrable because $\int \abs{\psi(t)} \, dt = \frac{1}{2\pi} \int \abs{\varphi(c + iy)} \, dy$.
Example: $\varphi = \Gamma$ and $c = 1$ give $x^{-1} \check{\psi}(-\log x) = e^{-x}$, that is, $\check{\psi}(u) = e^{-u} e^{-e^{-u}}$ for $\psi(t) = \Gamma(1 + 2\pi i t)$.
Combined with the statement that the Mellin transform is a Fourier transform in logarithmic variables, this reduces the Mellin inversion theorem to the [[Fourier inversion theorem|T4Z8YQZKZV]].

## Explanations

### L1 human

The inverse Mellin transform is the inverse Fourier transform in disguise.
One rescales the vertical line so that it becomes the real line, takes the inverse Fourier transform, reads it at the point $-\log x$, and multiplies by the weight $x^{-c}$.

### L2 human

This identity is the inverse half of the dictionary between Mellin and Fourier analysis on $\R$.
It turns questions about the inverse Mellin integral, such as continuity in $x$, decay or behaviour under smoothing, into the corresponding questions for the inverse Fourier transform.
For instance, it shows at once that $x \mapsto x^{c} \mathcal{M}^{-1}_c \varphi(x)$ is bounded and continuous on $(0, \infty)$.
