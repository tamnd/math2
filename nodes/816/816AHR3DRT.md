---
tag: 816AHR3DRT
kind: statement
role: theorem
name: Hard Lefschetz theorem
msc: [14F45, 14C30, 14F25]
uses: [A4H4CZ2V35, 6N7BC70CX0, JX47MS1R1H]
about: [A4H4CZ2V35, 6N7BC70CX0]
sources:
  - url: https://en.wikipedia.org/wiki/Lefschetz_hyperplane_theorem
---

## Statement

Let $X \subset \mathbb{P}^N_{\C}$ be a smooth complex [[projective variety|A4H4CZ2V35]] of dimension $n$.
Let $\omega \in H^2(X, \Q)$ be the class of a hyperplane section $X \cap H$, in [[singular cohomology|6N7BC70CX0]].
Let $L \colon H^j(X, \Q) \to H^{j+2}(X, \Q)$ be the map $\alpha \mapsto \omega \smile \alpha$, given by the [[cup product|JX47MS1R1H]].
Then for each integer $k$ with $0 \le k \le n$, the map
$$L^k \colon H^{n-k}(X, \Q) \to H^{n+k}(X, \Q)$$
is an isomorphism.

## Remarks

The classical proof uses [[Hodge theory|32YJXG30MF]] on the [[Kähler manifold|X60JG9AEQJ]] $X(\C)$.
The operator $L$, its adjoint $\Lambda$ and the degree operator form a representation of $\mathfrak{sl}_2$ on harmonic forms, and $L^k$ is an isomorphism by the representation theory of $\mathfrak{sl}_2$.
For $X = \mathbb{P}^n$, $H^{2i}(X, \Q) = \Q \, \omega^i$ for $0 \le i \le n$ and the odd groups vanish, so $L^k$ sends $\omega^{(n-k)/2}$ to $\omega^{(n+k)/2}$, which is a basis.
The theorem shows that $L \colon H^j \to H^{j+2}$ is injective for $j < n$, so the Betti numbers satisfy $b_j \le b_{j+2}$ for $j < n$, and also $b_j = b_{2n-j}$.
Over a field of positive characteristic, Deligne proved the analogue for $\ell$-adic cohomology.
The hypothesis that $\omega$ comes from an ample class matters: for a class $\omega$ with $\omega^n = 0$, such as $0$, the map $L^n \colon H^0 \to H^{2n}$ is zero.

## Explanations

### L1 human

A smooth projective variety of dimension $n$ has cohomology groups in degrees $0$ to $2n$.
Cutting by a hyperplane again and again gives a map from degree $n-k$ to degree $n+k$.
The theorem says that this map loses nothing and adds nothing: it is a bijection.
So the cohomology is symmetric around the middle degree in a very rigid way.

### L2 human

The theorem gives the Lefschetz decomposition of $H^*(X, \Q)$ into primitive parts, and together with the Hodge–Riemann bilinear relations it shows that the cohomology carries a polarized Hodge structure.
It is one of the standard tools that restrict which manifolds can be projective varieties: for example, the sequences $b_0, b_2, b_4, \ldots$ and $b_1, b_3, b_5, \ldots$ cannot decrease before the middle degree.
It complements the [[Lefschetz hyperplane theorem|EX6YSYN7B4]], which compares the cohomology of $X$ with that of a hyperplane section below the middle degree.
Grothendieck's Lefschetz-type standard conjecture asks that the inverse of $L^k$ come from an algebraic cycle.
