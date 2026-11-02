---
tag: NQC6CRDWFW
kind: statement
role: theorem
name: Bernstein's theorem on absolutely convergent Fourier series
msc: [42A20, 42A16]
uses: [012PBA0FMD, HHBGB5R5S2, 5NN2YZZR3V, 047RFCNVSK]
about: [HHBGB5R5S2]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_of_Fourier_series
---

## Statement

Let $0 < \alpha \le 1$ and let $f \colon \R \to \C$ be a $2\pi$-periodic function that is [[Hölder continuous|012PBA0FMD]] with exponent $\alpha$.
So there is $K \ge 0$ with $\abs{f(x) - f(y)} \le K \abs{x - y}^\alpha$ for all $x, y \in \R$.
Let $\hat f(n)$, $n \in \Z$, be its [[Fourier coefficients|5NN2YZZR3V]].
If $\alpha > 1/2$, then $\sum_{n \in \Z} \abs{\hat f(n)} < \infty$, so the Fourier series of $f$ is [[absolutely convergent|HHBGB5R5S2]].

## Remarks

Proof idea: for $h > 0$ the function $x \mapsto f(x + h) - f(x - h)$ has Fourier coefficients $2i \sin(nh) \hat f(n)$.
By [[Parseval's identity|047RFCNVSK]] and the Hölder bound, $\sum_n 4 \sin^2(nh) \abs{\hat f(n)}^2 \le K^2 (2h)^{2\alpha}$.
Take $h = \pi / (3 \cdot 2^j)$; for $2^j \le \abs{n} < 2^{j+1}$, $\sin^2(nh) \ge 3/4$, so the sum of $\abs{\hat f(n)}^2$ over this block is $O(2^{-2j\alpha})$.
The block has fewer than $2^{j+2}$ terms, so by Cauchy–Schwarz the sum of $\abs{\hat f(n)}$ over it is $O(2^{j(1/2 - \alpha)})$.
These bounds form a convergent geometric series when $\alpha > 1/2$.

Example: every continuously differentiable periodic function is Hölder continuous with exponent $1$, so its Fourier series converges absolutely.

The bound $\alpha > 1/2$ is sharp: there are Hölder continuous functions with exponent $1/2$ whose Fourier series does not converge absolutely.
Mere continuity is far from enough, since there are continuous functions whose Fourier series even diverges at a point.

## Explanations

### L1 human

The smoother a periodic function is, the faster its Fourier coefficients decay.
Bernstein's theorem gives a precise threshold: Hölder continuity with an exponent above one half already makes the coefficients absolutely summable.
Then the Fourier series converges uniformly and without any delicate cancellation.

### L2 human

The proof is a model of a standard technique: estimate the coefficients in dyadic blocks with Parseval's identity, then pass from $\ell^2$ to $\ell^1$ with Cauchy–Schwarz.
The loss of a factor $2^{j/2}$ in the last step explains the threshold $1/2$.
The theorem gives a large class of functions in the [[Wiener algebra|5H8XESYCHQ]].
A related criterion of Zygmund says that a function of bounded variation that is Hölder continuous with some positive exponent also has an absolutely convergent Fourier series.
