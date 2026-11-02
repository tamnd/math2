---
tag: V3YTF5WJHY
kind: statement
role: theorem
name: Lerch's uniqueness theorem
msc: [44A10]
uses: [05XT5AVJBK, DWJF7ABPR1]
about: [0V49JEZW06, 07WBTX1MHA]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Statement

Let $f, g \colon [0, \infty) \to \C$ be [[Lebesgue integrable|DWJF7ABPR1]] on each interval $[0, T]$.
Assume that the Laplace integrals of $f$ and $g$ converge at some real number $s_0$.
Let $F$ and $G$ be their [[Laplace transforms|05XT5AVJBK]].
If $F(s) = G(s)$ for every real $s > s_0$, then $f = g$ almost everywhere on $[0, \infty)$.
If in addition $f$ and $g$ are continuous, then $f = g$ everywhere on $[0, \infty)$.

## Remarks

By linearity it suffices to show that $h = f - g$ vanishes almost everywhere when its transform vanishes for $s > s_0$.
Let $\varphi(t) = \int_0^t e^{-s_0 \tau} h(\tau) \, d\tau$; it is continuous and bounded, and integration by parts turns $H(s_0 + n) = 0$, $n = 1, 2, \ldots$, into $\int_0^\infty e^{-n t} \varphi(t) \, dt = 0$.
The substitution $x = e^{-t}$ turns these into $\int_0^1 x^{n-1} \psi(x) \, dx = 0$ for a continuous function $\psi$, so all moments of $\psi$ vanish.
By the Weierstrass approximation theorem $\psi = 0$, hence $\varphi = 0$ and $h = 0$ almost everywhere.
The proof shows that equality at the points $s_0 + n$, $n = 1, 2, \ldots$, is already enough.
Without continuity the conclusion "almost everywhere" cannot be improved: changing $f$ at one point does not change $F$.

## Explanations

### L1 human

Two functions with the same Laplace transform are essentially the same function.
So, when one finds a function with a given transform, one has found the only reasonable one.

### L2 human

This theorem is what makes the [[inverse Laplace transform|07WBTX1MHA]] well defined, up to changes on null sets.
It justifies the table method: once $F$ matches a known transform, the original function is determined.
It does not by itself give a formula for $f$; that is the job of the [[Bromwich integral|5KNAXNHRY6]] and of [[Post's inversion formula|D6QKPBS2EN]].
