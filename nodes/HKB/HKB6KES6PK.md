---
tag: HKB6KES6PK
kind: definition
name: Kernel of an integral transform
msc: [44A05]
defines: 9M0NNNFJGM
uses: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_transform
---

## Definition

Let $I$ and $J$ be intervals of $\R$, and let $T$ be an [[integral transform|YCK709QB06]] given by
$$(Tf)(u) = \int_I f(t)\, K(t, u)\, dt \quad (u \in J)$$
for a measurable function $K \colon I \times J \to \C$.
The function $K$ is the *kernel* (or *nucleus*) of $T$.

## Remarks

Example: the Laplace transform $F(s) = \int_0^\infty f(t) e^{-st}\, dt$ has kernel $K(t, s) = e^{-st}$ on $[0, \infty) \times (0, \infty)$; this is read off by comparing with the formula above.
Non-example: the function $f$ itself is not a kernel of $T$; the kernel does not depend on the input $f$, only on the transform.
Suppose the transform is defined on all bounded functions with compact support.
Then the kernel is determined by the transform up to changes on a set of measure zero in $I \times J$.
A kernel is *symmetric* when $I = J$ and $K(t, u) = K(u, t)$.
