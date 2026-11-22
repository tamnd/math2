---
tag: B9CHNGJV5K
kind: statement
role: lemma
name: Powers and polynomials of a Jordan block
aliases: [powers-of-a-jordan-block, minimal-polynomial-of-a-jordan-block]
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
about: [07PH4RX0X5]
uses: [0PBFS92AJP, 039HF58KQ5, 03NDVCSHSB, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_matrix
    locator: Functions of matrices
  - book: isbn:9780135367971
    locator: Section 7.3
---

## Statement

The lemma computes every power and every polynomial of a Jordan block, and it reads off the polynomials, the eigenvalue and the kernels of the block.
Let $F$ be a field, let $\lambda \in F$ and $k \ge 1$, let $J = J_k(\lambda)$ be the [[Jordan block|0PBFS92AJP]], and let $N = J - \lambda I$.

1. *The shift.* $N e_1 = 0$ and $N e_i = e_{i-1}$ for $2 \le i \le k$. For $0 \le j \le k$, the matrix $N^j$ has the entry $1$ in each position $(i, i + j)$ and $0$ elsewhere, and $\operatorname{rank} N^j = k - j$. In particular $N^k = 0$.
2. *Powers.* For every $m \ge 0$,
$$J^m = \sum_{j=0}^{\min(m, k-1)} \binom{m}{j} \lambda^{m-j} N^j,$$
so the entry $(i, i + j)$ of $J^m$ is $\binom{m}{j} \lambda^{m-j}$.
3. *Polynomials.* If $f \in F[x]$ is written as $f = \sum_{j \ge 0} b_j (x - \lambda)^j$, then $f(J) = \sum_{j=0}^{k-1} b_j N^j$.
4. *Polynomials of the block.* The [[characteristic polynomial|039HF58KQ5]] and the [[minimal polynomial|03NDVCSHSB]] of $J$ are both $(x - \lambda)^k$.
5. *Eigenvalue and kernels.* The only [[eigenvalue|0BQAA2BK3Q]] of $J$ is $\lambda$, its eigenspace is $F e_1$, and $\dim \ker N^j = \min(j, k)$ for all $j \ge 0$.
6. *Cyclic vector.* The vectors $e_k, J e_k, \dots, J^{k-1} e_k$ form a basis of $F^k$.

## Remarks

### Why the hypotheses are so weak

The lemma holds over every field and for every $\lambda$, because the proof uses only the rule $\lambda I \cdot N = N \cdot \lambda I$ and the shape of $N$.
The only place where the field matters is a variant of part 3.
In characteristic $0$ the coefficients are the Taylor coefficients $b_j = f^{(j)}(\lambda) / j!$, but in characteristic $p$ the division by $j!$ fails for $j \ge p$.
The form with the $b_j$, which only expands $f$ in powers of $x - \lambda$, needs no hypothesis.

### What it gives you

Part 5 says that a block of size $k \ge 2$ is not diagonalizable: it has one eigenvalue of algebraic multiplicity $k$ and an eigenspace of dimension $1$.
Over $\mathbb{C}$, part 2 shows that $J_k(\lambda)^m \to 0$ as $m \to \infty$ exactly when $|\lambda| < 1$, since $\binom{m}{j} |\lambda|^{m-j} \to 0$ for each fixed $j$ in that case.
The kernel dimensions in part 5 are the data that the [[normal form of nilpotent endomorphisms|Z2RTKWZZAZ]] uses to count blocks.

For a worked use of part 3, take $f = x^2$ and $J = J_3(\lambda)$.
Write $x^2 = \lambda^2 + 2\lambda (x - \lambda) + (x - \lambda)^2$, so that $b_0 = \lambda^2$, $b_1 = 2\lambda$ and $b_2 = 1$:
$$J^2 = \lambda^2 I + 2 \lambda N + N^2 = \begin{pmatrix} \lambda^2 & 2\lambda & 1 \\ 0 & \lambda^2 & 2\lambda \\ 0 & 0 & \lambda^2 \end{pmatrix}.$$

### The converse

Part 4 has a converse among matrices with one eigenvalue.
If a $k \times k$ matrix has minimal polynomial $(x - \lambda)^k$, then it is similar to $J_k(\lambda)$, because its minimal and characteristic polynomials agree and it is then cyclic.
The [[criterion for cyclic endomorphisms|RK1QVMYW7H]] proves this step.

### Generalizations

For a power series $f$ that converges at $\lambda$ over $\mathbb{C}$, part 3 holds with the Taylor coefficients of $f$ at $\lambda$.
For the exponential this gives
$$\exp(t J_k(\lambda)) = e^{\lambda t} \sum_{j=0}^{k-1} \frac{t^j}{j!} N^j.$$

## History

The block is named after Camille Jordan, who published the normal form in 1870.

## Explanations

### L1 human

A Jordan block is a number times the identity plus a shift.
The shift moves each basis vector one step down the line, and it kills the first one.
So the shift applied $k$ times gives zero, and every power of the block is a short sum that the binomial formula gives.

### L2 human

Take $J = J_3(\lambda)$ and $m = 4$.
Part 2 keeps the terms with $j = 0, 1, 2$:
$$J^4 = \lambda^4 I + 4 \lambda^3 N + 6 \lambda^2 N^2 = \begin{pmatrix} \lambda^4 & 4\lambda^3 & 6\lambda^2 \\ 0 & \lambda^4 & 4\lambda^3 \\ 0 & 0 & \lambda^4 \end{pmatrix}.$$
Check with $\lambda = 1$: $J_3(1)^2 = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}$, and its square has first row $(1, 4, 1 + 4 + 1) = (1, 4, 6)$.
The ranks of $N, N^2, N^3$ are $2, 1, 0$, so the kernels have dimensions $1, 2, 3$.
The trap is to put $\lambda^m$ on the diagonal and leave the rest of the matrix as it was.

### L3 human

The block $J_k(\lambda)$ is the matrix of multiplication by $x$ on $F[x]/((x - \lambda)^k)$ in the basis $(x - \lambda)^{k-1}, \dots, x - \lambda, 1$.
In that language parts 3 and 4 say one thing: a polynomial $f$ acts as zero on the module exactly when $(x - \lambda)^k$ divides $f$.
The formula for $\exp(tJ)$ is the reason why the solutions of $y' = Ay$ contain the terms $t^j e^{\lambda t}$ with $j$ less than the size of a block.
