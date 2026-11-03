---
tag: QDBQW0QTR4
kind: statement
role: theorem
name: Rayleigh's principle for natural frequencies
msc: [70J10, 15A18]
uses: [WZGRC78VDB, WKTX3JJHMB, 06WHP8SE98, 0QQCG3JWJ4, 0N28QN4CYA]
about: [JVM27J1FTF, 06WHP8SE98]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient
---

## Statement

Let $M$ and $K$ be real [[symmetric|0N28QN4CYA]] $n \times n$ matrices, both [[positive definite|0QQCG3JWJ4]].
Let $0 < \omega_1 \le \omega_2 \le \cdots \le \omega_n$ be the natural frequencies of the system $M \ddot x + K x = 0$, that is, $\omega_k^2$ are the roots of $\det(K - \lambda M) = 0$ counted with multiplicity.
For $v \in \R^n \setminus \set{0}$ let
$$R(v) = \frac{v^T K v}{v^T M v}$$
be the [[Rayleigh quotient|06WHP8SE98]] of the pair $(K, M)$.
Then $\omega_1^2 \le R(v) \le \omega_n^2$ for every $v \ne 0$, and
$$\omega_1^2 = \min_{v \ne 0} R(v), \qquad \omega_n^2 = \max_{v \ne 0} R(v).$$
Moreover $R(v) = \omega_1^2$ if and only if $v$ is a mode shape of a [[normal mode|WZGRC78VDB]] with frequency $\omega_1$.

## Remarks

Choose mode shapes $v_1, \ldots, v_n$ with $K v_k = \omega_k^2 M v_k$ and $v_j^T M v_k = \delta_{jk}$; they exist by simultaneous diagonalization of $K$ with respect to the inner product $u^T M w$.
Writing $v = \sum_k c_k v_k$ gives $R(v) = \sum_k \omega_k^2 c_k^2 / \sum_k c_k^2$, a weighted average of the $\omega_k^2$, which proves all claims.
In practice a guessed shape $v$ gives the upper bound $\omega_1 \le \sqrt{R(v)}$.
Since $R$ is stationary at mode shapes, an error of order $\varepsilon$ in the shape gives an error of order only $\varepsilon^2$ in $R$.

Example: $M = I_2$ and $K = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$ have $\omega_1^2 = 1$ and $\omega_2^2 = 3$.
The trial shape $v = (1, 0)$ gives $R(v) = 2$, an upper bound for $\omega_1^2$; the trial shape $v = (1, 0.9)$ gives $R(v) = (2 - 1.8 + 1.62)/1.81 \approx 1.006$, already close to $1$.

The hypothesis that $M$ is positive definite is needed.
If $v^T M v = 0$ for some $v \ne 0$, the quotient is not defined there.
If $M$ has a negative eigenvalue, the quotient is unbounded below.

## Explanations

### L1 human

The lowest frequency at which a structure can vibrate is hard to compute exactly, but easy to estimate.
Guess a shape for the vibration, compute its stiffness energy divided by its mass energy, and take the square root.
The answer is never below the true lowest frequency, and a reasonable guess gives a very good estimate.
This is how engineers estimate the fundamental frequency of beams, bridges and buildings.

### L2 human

The statement is the min-max characterization of the smallest and largest eigenvalue of the symmetric pencil $(K, M)$.
After the substitution $v = M^{-1/2} w$, it becomes the usual bound $\lambda_{\min} \le R(A, w) \le \lambda_{\max}$ for the symmetric matrix $A = M^{-1/2} K M^{-1/2}$.
The Courant–Fischer theorem extends it to every natural frequency, and the [[Rayleigh–Ritz method|5YSP8TWD4Q]] applies it on a subspace of trial shapes.
For continuous systems, $R$ becomes a ratio of integrals, such as potential energy over kinetic energy of a vibrating string.
