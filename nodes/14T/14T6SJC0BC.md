---
tag: 14T6SJC0BC
kind: definition
name: Mehler–Fock transform
msc: [44A15, 44A20, 33C45]
defines: WFQV4R1EMN
uses: [YCK709QB06, 69XMERM6KJ]
sources:
  - url: https://en.wikipedia.org/wiki/Mehler%E2%80%93Fock_transform
---

## Definition

For real $\tau \ge 0$, let $P_{-1/2 + i\tau}$ be the conical [[Legendre function|69XMERM6KJ]] of the first kind on $[1, \infty)$.
Let $f \colon [1, \infty) \to \C$ be a function such that the integral below converges for every $\tau \ge 0$.
The *Mehler–Fock transform* of $f$ is the function
$$F(\tau) = \int_1^\infty f(x)\, P_{-1/2 + i\tau}(x)\, dx, \qquad \tau \ge 0.$$

## Remarks

Under suitable conditions on $f$, the inversion formula is
$$f(x) = \int_0^\infty \tau \tanh(\pi \tau)\, P_{-1/2 + i\tau}(x)\, F(\tau)\, d\tau, \qquad x > 1.$$
The function $P_{-1/2 + i\tau}(x)$ is real for real $\tau$ and $x \ge 1$, and it decays like $x^{-1/2}$ up to a logarithmic factor as $x \to \infty$.

Example: if $f$ is integrable and vanishes outside $[1, 2]$, then the integral is over a compact interval of a continuous kernel, so $F(\tau)$ is defined for every $\tau \ge 0$.

Non-example: $f(x) = x$ has no Mehler–Fock transform, since $x P_{-1/2 + i\tau}(x)$ grows like $x^{1/2}$ up to a logarithmic factor and is not integrable on $[1, \infty)$.

The substitution $x = \cosh t$ turns the transform into an integral over $t \in [0, \infty)$, the form used on the hyperbolic plane.
