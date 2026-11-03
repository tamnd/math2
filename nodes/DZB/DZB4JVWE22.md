---
tag: DZB4JVWE22
kind: definition
name: BIBO stability
msc: [93D25, 93C05]
defines: DH8950CRZ3
uses: [6J9MPVHSMF, 3X3SYVM7R5, 86JKV3TRFD, WPC2XRMB9Y, 2Z29JN3VES]
sources:
  - url: https://en.wikipedia.org/wiki/BIBO_stability
---

## Definition

Let $H$ be a system with inputs and outputs that maps each input signal $u \colon [0, \infty) \to \R^m$ to an output signal $y = Hu \colon [0, \infty) \to \R^p$, with zero initial state.
A signal $u$ is *bounded* if $\norm{u}_\infty = \sup_{t \ge 0} \norm{u(t)} < \infty$, where the supremum is an [[essential supremum|WPC2XRMB9Y]] for measurable signals.
The system $H$ is *BIBO stable* (bounded-input bounded-output stable) if for every bounded input $u$ the output $Hu$ is bounded.

## Remarks

A stronger requirement is a constant $C$ with $\norm{Hu}_\infty \le C \norm{u}_\infty$ for all bounded $u$; for the convolution systems below the two notions agree.
A single-input single-output [[linear time-invariant system|6J9MPVHSMF]] with [[impulse response|3X3SYVM7R5]] $h$, so that $y = h * u$ is a [[convolution|2Z29JN3VES]], is BIBO stable if and only if $\int_0^\infty \abs{h(t)} \, dt < \infty$.
If its [[transfer function|86JKV3TRFD]] is a proper rational function in lowest terms, this holds if and only if every pole has negative real part.
The discrete-time version uses sequences and the condition $\sum_k \abs{h_k} < \infty$.

Example: $h(t) = e^{-t}$, with transfer function $1/(s + 1)$.
Then $\int_0^\infty \abs{h} = 1$, and $\abs{y(t)} \le \int_0^t e^{-(t - \tau)} \abs{u(\tau)} \, d\tau \le \norm{u}_\infty$.

Non-example: the integrator, with $h(t) = 1$ for $t \ge 0$ and transfer function $1/s$.
The bounded input $u = 1$ gives $y(t) = t$, which is unbounded.
