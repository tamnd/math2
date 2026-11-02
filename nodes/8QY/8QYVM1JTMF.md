---
tag: 8QYVM1JTMF
kind: statement
role: theorem
name: Hartogs–Bochner extension theorem
msc: [32V25, 32D15]
uses: [507C34W0ZT, X7GP9BECD8, 0SPE8WNWFV, 09QSZVVM26]
about: [507C34W0ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Hartogs%27s_extension_theorem
---

## Statement

Let $n \ge 2$ and let $D \subseteq \C^n$ be a [[bounded|09QSZVVM26]] open set with $C^1$ boundary $\partial D$ such that $\C^n \setminus \bar D$ is [[connected|0SPE8WNWFV]].
Let $f \colon \partial D \to \C$ be a $C^1$ function that satisfies the [[tangential Cauchy–Riemann equations|X7GP9BECD8]] on $\partial D$.
Then there is a continuous function $F$ on $\bar D$ that is [[holomorphic|507C34W0ZT]] on $D$ and satisfies $F = f$ on $\partial D$.

## Remarks

The proof uses the [[Bochner–Martinelli formula|YMHYAEJQ80]].
The Bochner–Martinelli integral of $f$ over $\partial D$ defines a function $F_-$ on $D$ and a function $F_+$ on $\C^n \setminus \bar D$.
The tangential Cauchy–Riemann equations make both functions holomorphic, and the jump formula gives $F_- - F_+ = f$ on $\partial D$.
The function $F_+$ tends to $0$ at infinity.
On each complex line that misses $\bar D$ it is an entire function of one variable tending to $0$, hence zero by [[Liouville's theorem|0EHKVRF4J6]].
These lines fill a nonempty open set.
Since $\C^n \setminus \bar D$ is connected, $F_+ = 0$ by the identity theorem, so $F = F_-$ has boundary values $f$.

Example: if $f$ is the restriction to $\partial D$ of a function holomorphic near $\bar D$, then $f$ satisfies the tangential Cauchy–Riemann equations and $F$ is that function.

The hypothesis $n \ge 2$ is necessary.
For $n = 1$ the tangential condition is empty.
The function $f(z) = \bar z$ on the unit circle has no holomorphic extension to the disc that is continuous up to the boundary.
Indeed $\int_{\abs{z} = 1} \bar z \, dz = 2\pi i \ne 0$, whereas Cauchy's theorem would make the integral of such an extension zero.

## Explanations

### L1 human

On the boundary of a domain in $\C^n$ with $n \ge 2$, a function may already satisfy the part of the Cauchy–Riemann equations that only involves directions along the boundary.
The theorem says that such a function is always the boundary value of a holomorphic function inside.
So, in several variables, holomorphic functions on a domain are determined by, and can be built from, suitable functions on its boundary.

### L2 human

The theorem is a boundary version of [[Hartogs's extension theorem|FSGES670AZ]].
Applied to the restriction of a holomorphic function defined near $\partial D$, it gives the extension of that function to $D$.
It is the starting point of the theory of CR functions on real hypersurfaces and of their holomorphic extension.
