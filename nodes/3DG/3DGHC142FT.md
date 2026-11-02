---
tag: 3DGHC142FT
kind: statement
role: theorem
name: L2 convergence of Fourier series
msc: [42A20, 42A16]
uses: [NXQX1KFMDB, 5NN2YZZR3V, G12KXDHPPS, SASP14MA1Z]
about: [G12KXDHPPS]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_of_Fourier_series
---

## Statement

Let $\mathbb{T} = \R / 2\pi\Z$ and let $f \in L^2(\mathbb{T})$, the [[Lebesgue space|SASP14MA1Z]] of square integrable functions with the norm $\norm{g}_2 = \left( \frac{1}{2\pi} \int_{-\pi}^{\pi} \abs{g(x)}^2 \, dx \right)^{1/2}$.
Let $\hat f(n)$ be the [[Fourier coefficients|5NN2YZZR3V]] of $f$ and let $S_N f(x) = \sum_{n=-N}^{N} \hat f(n) e^{inx}$ be the partial sums of its [[Fourier series|G12KXDHPPS]].
Then
$$\lim_{N \to \infty} \norm{f - S_N f}_2 = 0 \qquad \text{and} \qquad \frac{1}{2\pi} \int_{-\pi}^{\pi} \abs{f(x)}^2 \, dx = \sum_{n=-\infty}^{\infty} \abs{\hat f(n)}^2.$$

## Remarks

Both claims follow from the [[Fourier basis theorem|NXQX1KFMDB]], which says that the monomials $e_n$ form an orthonormal basis of $L^2(\mathbb{T})$.
$S_N f$ is the orthogonal projection of $f$ onto the span of $e_{-N}, \dots, e_N$, so $\norm{f - S_N f}_2^2 = \norm{f}_2^2 - \sum_{\abs{n} \le N} \abs{\hat f(n)}^2$.
Completeness of the basis makes the right side tend to $0$; the second formula is Parseval's identity for this basis.
Example: for $f(x) = x$ on $(-\pi, \pi)$, $\hat f(0) = 0$ and $\abs{\hat f(n)} = 1/\abs{n}$ for $n \ne 0$, and Parseval gives $\frac{\pi^2}{3} = 2 \sum_{n \ge 1} \frac{1}{n^2}$, which is the value $\frac{\pi^2}{6}$ of the [[Basel problem|0DMY75D6FV]].
Convergence in $L^2$ does not give convergence at each point; pointwise convergence almost everywhere for $L^2$ functions is the much deeper [[Carleson's theorem|FBH6KG484Z]].
The converse direction is the Riesz–Fischer theorem: every sequence $(c_n) \in \ell^2(\Z)$ is the sequence of Fourier coefficients of some $f \in L^2(\mathbb{T})$.

## Explanations

### L1 human

The finite sums of the Fourier series of a square integrable function get closer and closer to the function, when distance is measured by the average of the squared error.
The energy of the function, the average of $\abs{f}^2$, equals the sum of the energies of its frequency components.

### L2 human

This is the simplest and most robust convergence theorem for Fourier series.
It needs no smoothness, only square integrability, and it holds for every function in $L^2(\mathbb{T})$.
The analogous statement in $L^p(\mathbb{T})$ for $1 < p < \infty$ is true but harder; it rests on the boundedness of the conjugate function, a theorem of M. Riesz.
For $p = 1$ and in $C(\mathbb{T})$ with the supremum norm the analogous statement is false, because the Lebesgue constants of the Dirichlet kernel are unbounded.
