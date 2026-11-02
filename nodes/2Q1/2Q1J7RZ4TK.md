---
tag: 2Q1J7RZ4TK
kind: example
name: Irrational rotation
msc: ["37E10", 37A05, 37A25]
instance_of: [556WBDAHNP, AZRPHS478B, NZZE9KCAD8]
uses: [0DZXAXEJQ9, 2Z2QVWZ262, NCCGNTBEYV, 2MGZFRH5PX]
sources:
  - url: https://en.wikipedia.org/wiki/Irrational_rotation
same_as:
  wikidata: Q6073537
  wikipedia: Irrational rotation
---

## Example

Let $\alpha$ be an [[irrational number|0DZXAXEJQ9]] and let $\mathbb{T} = \R/\Z$ be the circle, identified with $[0, 1)$.
The *irrational rotation* by $\alpha$ is
$$R_\alpha \colon \mathbb{T} \to \mathbb{T}, \qquad R_\alpha(x) = x + \alpha \bmod 1.$$

It is a [[measure-preserving transformation|556WBDAHNP]] for [[Lebesgue measure|2Z2QVWZ262]] $\lambda$.
The preimage of an arc is an arc of the same length, and arcs generate the Borel sets.

It is [[ergodic|AZRPHS478B]]: let $f \in L^2(\lambda)$ with $f \circ R_\alpha = f$, with Fourier coefficients $c_k$.
Then $c_k e^{2\pi i k \alpha} = c_k$ for all $k \in \Z$.
Since $k \alpha \notin \Z$ for $k \ne 0$, one gets $c_k = 0$ for $k \ne 0$, so $f$ is constant almost everywhere.

It is even [[uniquely ergodic|NZZE9KCAD8]], and every orbit is dense in $\mathbb{T}$.
By [[Weyl's equidistribution theorem|NCCGNTBEYV]] every orbit $(x + n\alpha \bmod 1)_{n \ge 0}$ is equidistributed.

It is not [[weakly mixing|2MGZFRH5PX]]: $e^{2\pi i x}$ is a nonconstant eigenfunction of the Koopman operator, with eigenvalue $e^{2\pi i \alpha}$.
Its Kolmogorov–Sinai entropy is $0$.
If $\alpha = p/q$ is rational in lowest terms, then $R_\alpha^q$ is the identity and $R_\alpha$ is not ergodic.

## Explanations

### L1 human

Turn a wheel by a fixed angle again and again, where the angle is an irrational fraction of a full turn.
The marked point never comes back exactly to where it started, and over time it visits every part of the rim equally often.
This makes the irrational rotation the simplest ergodic system.
It is orderly rather than chaotic: nearby points stay at the same distance forever, and the system has zero entropy.
