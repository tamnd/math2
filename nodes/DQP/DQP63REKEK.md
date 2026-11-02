---
tag: DQP63REKEK
kind: statement
role: theorem
name: Monodromy theorem for singularities
msc: [32S40, 32S55, 14D05]
uses: [VTGYEES3VS, KTFG1S2SMG, C8HD62AB6Q, 0BQAA2BK3Q, 0YV2CKP2AV, 07PH4RX0X5]
about: [KTFG1S2SMG, C8HD62AB6Q]
sources:
  - url: https://en.wikipedia.org/wiki/Milnor_map
---

## Statement

Let $n \ge 1$ and let $f$ be a holomorphic function near $0$ in $\C^{n+1}$ with an [[isolated singularity|VTGYEES3VS]] at $0$.
Let $F$ be the Milnor fibre of the [[Milnor fibration|KTFG1S2SMG]] of $f$ at $0$.
Going once around the base circle gives a diffeomorphism $h \colon F \to F$, defined up to isotopy, and its action $T = h_* \colon H_n(F; \C) \to H_n(F; \C)$ is the *[[monodromy|C8HD62AB6Q]]* of $f$.
Then:

1. every [[eigenvalue|0BQAA2BK3Q]] of $T$ is a [[root of unity|0YV2CKP2AV]];
2. every [[Jordan block|07PH4RX0X5]] of $T$ has size at most $n + 1$.

Equivalently, there is an integer $N \ge 1$ such that $(T^N - \id)^{n+1} = 0$: the monodromy is quasi-unipotent.

## Remarks

One proof uses an embedded resolution of $f^{-1}(0)$, in which the pull-back of $f$ is locally a monomial $u \, x_1^{N_1} \cdots x_k^{N_k}$ with $u$ a unit.
Locally the monodromy then has finite order, and one finds that $T^N$ is unipotent for $N$ the least common multiple of the multiplicities $N_i$.
The nilpotency index of $T^N - \id$ is bounded by the number of divisors that can meet at a point, which is at most $n + 1$.
Other proofs go through the regularity of the Gauss–Manin connection or through Hodge theory.

Example: for $f = x^p + y^q$ with $p, q \ge 2$, the monodromy on $H_1(F; \C)$ is diagonalizable.
Its eigenvalues are the products $\zeta \eta$, where $\zeta \ne 1$ is a $p$-th root of unity and $\eta \ne 1$ is a $q$-th root of unity.
So $T^N = \id$ with $N = \lcm(p, q)$.

## Explanations

### L1 human

Going once around the singular value, the Milnor fibre comes back to itself, but its cycles may be moved around.
The theorem says that this motion is almost periodic: after enough turns, it differs from doing nothing only by a nilpotent part.
In particular, no eigenvalue can be a number like $2$ or $e^{i\sqrt{2}\pi}$; they are all roots of unity.

### L2 human

The monodromy theorem is the local version of a result for families of algebraic varieties over a punctured disc, proved in several ways by Grothendieck, Landman, Clemens and others.
For singularities, the eigenvalues of $T$ are linked to the roots of the [[Bernstein–Sato polynomial|7M5P2A0BZ6]] of $f$.
By results of Malgrange and Kashiwara, the numbers $e^{2\pi i \alpha}$ for the roots $\alpha$ are the eigenvalues of the monodromy at points of $f^{-1}(0)$.
The size of the Jordan blocks is related to the weight filtration of the limit mixed Hodge structure on the cohomology of the Milnor fibre.
