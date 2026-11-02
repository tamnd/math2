---
tag: WNJPRHZ680
kind: statement
role: theorem
name: Szegő limit theorems
msc: [47B35, 42C05, 15B05]
uses: [GKY2WSHE26, 00KDZRW4C0, 5NN2YZZR3V, X7GTF3D98F]
about: [GKY2WSHE26, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Szeg%C5%91_limit_theorems
same_as:
  wikidata: Q3458641
  wikipedia: Szegő limit theorems
---

## Statement

Let $f \colon \R \to [0, \infty)$ be a $2\pi$-periodic function, [[integrable|X7GTF3D98F]] on $[-\pi, \pi]$, with [[Fourier coefficients|5NN2YZZR3V]] $\hat f(k) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(\theta) e^{-ik\theta} \, d\theta$.
For $n \ge 1$ let $T_n(f) = (\hat f(j - k))_{j,k=0}^{n-1}$ be the $n \times n$ [[Toeplitz matrix|GKY2WSHE26]] of $f$, and let $D_n(f) = \det T_n(f)$ be its [[determinant|00KDZRW4C0]].

1. (First Szegő theorem.) If $\log f$ is integrable, then
$$\lim_{n \to \infty} D_n(f)^{1/n} = G(f), \qquad G(f) = \exp\left( \frac{1}{2\pi} \int_{-\pi}^{\pi} \log f(\theta) \, d\theta \right).$$
2. (Strong Szegő theorem.) Assume $f = e^{g}$ with $g$ real-valued and continuous, with Fourier coefficients satisfying $\sum_{k \in \Z} \abs{\hat g(k)} < \infty$ and $\sum_{k \in \Z} \abs{k} \abs{\hat g(k)}^2 < \infty$.
Then
$$\lim_{n \to \infty} \frac{D_n(f)}{G(f)^n} = \exp\left( \sum_{k=1}^{\infty} k \, \hat g(k) \hat g(-k) \right) = \exp\left( \sum_{k=1}^{\infty} k \abs{\hat g(k)}^2 \right).$$

## Remarks

Proof idea for the first theorem: the ratio $D_{n+1}(f) / D_n(f)$ is the minimum of $\frac{1}{2\pi} \int_{-\pi}^{\pi} \abs{p(e^{i\theta})}^2 f(\theta) \, d\theta$ over polynomials $p(z) = 1 + a_1 z + \cdots + a_n z^n$.
These minima decrease to $G(f)$ by [[Szegő's theorem|SZ8ARMDEMY]] on prediction, and then the geometric means $D_n^{1/n}$ have the same limit.
The strong theorem gives the next term of the asymptotics, $D_n(f) \sim E(f) \, G(f)^n$ with the constant $E(f)$ above.

Example: let $f(\theta) = \abs{1 - a e^{i\theta}}^2$ with $\abs{a} < 1$.
Then $T_n(f)$ is tridiagonal with diagonal $1 + \abs{a}^2$, and $D_n(f) = \frac{1 - \abs{a}^{2(n+1)}}{1 - \abs{a}^2}$.
Here $g = \log f$ has $\hat g(0) = 0$ and $\hat g(k) = -a^k / k$ for $k \ge 1$, so $G(f) = 1$ and the strong theorem predicts the limit $\exp\left(\sum_{k \ge 1} \abs{a}^{2k}/k\right) = \frac{1}{1 - \abs{a}^2}$, as the formula confirms.

Szegő proved the first theorem in 1915 and the strong theorem in 1952, motivated by the computation of the spontaneous magnetization of the two-dimensional Ising model.
The strong theorem was later proved under weaker hypotheses, essentially only the condition $\sum \abs{k} \abs{\hat g(k)}^2 < \infty$.

## Explanations

### L1 human

A Toeplitz matrix has constant entries along each diagonal, and these entries are the Fourier coefficients of a function on the circle.
The Szegő theorems say how the determinants of larger and larger such matrices grow.
To first order, they grow like $G^n$, where $G$ is the geometric mean of the function.
The strong theorem gives the precise constant factor in front.

### L2 human

The theorems are the analogue for Toeplitz matrices of the fact that the determinant of a diagonal matrix is the product of its entries.
The first theorem is closely tied to [[orthogonal polynomials on the unit circle|3F9G3DRQ62]] and to prediction theory of stationary sequences.
The strong theorem has applications in statistical mechanics and in random matrix theory, where such determinants compute averages over the unitary group.
