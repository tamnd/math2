---
tag: PQPDQCCD02
kind: statement
role: theorem
name: von Neumann mean ergodic theorem
msc: [47A35, 37A30]
uses: [HM2HHE3J51, MM0EJ2GDE4, 0B8KZRT28M, 0XJXTBCB2T, 556WBDAHNP, SASP14MA1Z]
about: [MM0EJ2GDE4]
sources:
  - url: https://en.wikipedia.org/wiki/Ergodic_theory
    locator: Mean ergodic theorem
---

## Statement

Let $H$ be a [[Hilbert space|HM2HHE3J51]] and let $U \colon H \to H$ be a bounded linear operator with $\norm{U} \le 1$, for example a [[unitary operator|MM0EJ2GDE4]].
Let $P$ be the [[orthogonal projection|0B8KZRT28M]] of $H$ onto the closed subspace $\set{v \in H : Uv = v}$.
Then for every $v \in H$,
$$\lim_{n \to \infty} \norm{\frac{1}{n} \sum_{k=0}^{n-1} U^k v - P v} = 0.$$

## Remarks

Proof idea: let $F = \set{v : Uv = v}$ and $B = \set{w - Uw : w \in H}$.
For $\norm{U} \le 1$ one shows that $Uv = v$ if and only if $U^* v = v$, and this gives $H = F \oplus \overline{B}$, an [[orthogonal decomposition|0XJXTBCB2T]].
On $F$ the averages are constantly $v$.
On $B$ they telescope: $\frac{1}{n} \sum_{k=0}^{n-1} U^k (w - Uw) = \frac{1}{n}(w - U^n w)$, of norm at most $2\norm{w}/n$.
Since all averaging operators have norm at most $1$, the convergence to $0$ extends from $B$ to its closure.

Main application: let $T$ be a [[measure-preserving transformation|556WBDAHNP]] of a probability space $(X, \mathcal{A}, \mu)$, and let $U f = f \circ T$ on [[$L^2(\mu)$|SASP14MA1Z]].
Then $U$ is an isometry, and the theorem says that the Birkhoff averages of every $f \in L^2(\mu)$ converge in $L^2$ to the projection of $f$ onto the $T$-invariant functions.
If $T$ is ergodic, the invariant functions are the constants, and the limit is the constant $\int_X f \, d\mu$.

Example: for $U = -\id$ on $H = \C$, the fixed space is $\set{0}$.
The averages of $v$ equal $v/n$ for odd $n$ and $0$ for even $n$, so they tend to $0 = Pv$.

## Explanations

### L1 human

Apply a norm-non-increasing operator again and again to a vector and average the results.
The averages always settle down, and the limit is the part of the vector that the operator does not move.
The parts that move get averaged out.

### L2 human

This is the Hilbert space form of the ergodic theorem, proved by von Neumann in 1932, and it gives convergence in mean rather than at almost every point.
Through the composition operator $f \mapsto f \circ T$, it turns questions about a measure-preserving map into questions about a linear operator, which is the starting point of the spectral theory of dynamical systems.
Birkhoff's theorem gives almost-everywhere convergence and needs a different, harder argument based on a maximal inequality.
