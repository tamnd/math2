---
tag: TJGNFQC2BY
kind: definition
name: Nyquist plot
msc: [93C80, 93D10]
defines: Z7SPHAWMDX
uses: [BMY8QZSD9H, 86JKV3TRFD, 0CTE7A31XQ, 0XDK9CGYKJ]
sources:
  - url: https://en.wikipedia.org/wiki/Nyquist_stability_criterion
---

## Definition

Let $G$ be the [[transfer function|86JKV3TRFD]] of a single-input single-output linear time-invariant system.
Assume that $G$ is a proper [[rational function|0XDK9CGYKJ]] with real coefficients and no pole on the imaginary axis.
The *Nyquist plot* of $G$ is the curve $\omega \mapsto G(i\omega)$, $\omega \in \R$, in the [[complex plane|0CTE7A31XQ]].
It is closed up at $\omega = \pm\infty$ by the point $G(\infty) = \lim_{\abs{s} \to \infty} G(s)$.

## Remarks

Because $G$ has real coefficients, $G(-i\omega) = \overline{G(i\omega)}$, so the part for $\omega < 0$ is the mirror image of the part for $\omega > 0$ in the real axis.
When $G$ has poles on the imaginary axis, one replaces the imaginary axis by an indented contour.
It goes around each such pole on a small half-circle in the right half-plane, and the plot is the image of this contour.

Example: for $G(s) = 1/(s + 1)$, $G(i\omega) = (1 - i\omega)/(1 + \omega^2)$.
One checks $\abs{G(i\omega) - 1/2} = 1/2$, so the Nyquist plot is the circle with centre $1/2$ and radius $1/2$, run clockwise from $G(\infty) = 0$ through $G(0) = 1$ back to $0$.

Non-example: for $G(s) = 1/s$ the formula $G(i\omega)$ is not defined at $\omega = 0$, so the definition above does not apply directly; one needs the indented contour.
