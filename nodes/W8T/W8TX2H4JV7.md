---
tag: W8TX2H4JV7
kind: definition
name: Sinai–Ruelle–Bowen measure
msc: ["37D20", "37C40", "37D35"]
defines: 256NP6JBEQ
uses: [F45VQ47GPV, 0KZZ70ZHXP, B232EZ1FMB, NJ1FJSNK6A, ZHKS81A7QN, P0P21KDV6E]
sources:
  - url: https://en.wikipedia.org/wiki/Sinai%E2%80%93Ruelle%E2%80%93Bowen_measure
---

## Definition

Let $M$ be a compact Riemannian [[manifold|F45VQ47GPV]] and let $f \colon M \to M$ be a $C^2$ [[diffeomorphism|0KZZ70ZHXP]].
Let $\mu$ be an $f$-[[invariant|B232EZ1FMB]] Borel probability measure on $M$.
The measure $\mu$ is a *Sinai–Ruelle–Bowen measure* (an *SRB measure*) if both conditions hold:

1. For $\mu$-almost every $x$, at least one [[Lyapunov exponent|NJ1FJSNK6A]] of $f$ at $x$ is positive.
2. The conditional measures of $\mu$ on the local unstable manifolds given by [[Pesin theory|ZHKS81A7QN]] are [[absolutely continuous|P0P21KDV6E]] with respect to their Riemannian volume.

## Remarks

Example: let $f$ be the map of $\R^2 / \Z^2$ given by the matrix $\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ and $\mu$ Lebesgue measure.
The exponent $\log \frac{3 + \sqrt 5}{2}$ is positive at every point.
The unstable manifolds are the lines of the expanding eigendirection, and the conditional measures of $\mu$ on them are multiples of length.
So $\mu$ is an SRB measure.

Non-example: for the same map, the Dirac measure at the fixed point $0$ is invariant and has a positive exponent.
Its conditional measure on the unstable line through $0$ is a point mass, which is not absolutely continuous with respect to length, so clause 2 fails.

Some authors use a different definition: $\mu$ is SRB, or *physical*, if the set of points $x$ with $\frac{1}{n} \sum_{k=0}^{n-1} \varphi(f^k x) \to \int \varphi \, d\mu$ for every continuous $\varphi$ has positive volume.
For an Axiom A attractor of a $C^2$ diffeomorphism, there is a unique SRB measure on each basic piece of the attractor, and it is physical in this sense.
Ledrappier and Young proved a characterization for $C^2$ diffeomorphisms.
An invariant measure $\mu$ that satisfies clause 1 is SRB in the sense above if and only if its entropy equals the integral of the sum of its positive exponents.
