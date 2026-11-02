---
tag: W4E25FVXV1
kind: statement
role: theorem
name: Schmidt's singular value decomposition of a kernel
msc: [45C05, 47B10, 15A18]
uses: [WWMWX7AD4V, CB5G212Q03, 6HSJBJ8TTQ, QSJKPKPM7H, A1G25R99PY, 000NPTMX6J]
about: [WWMWX7AD4V, QSJKPKPM7H]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
---

## Statement

Let $a < b$ and let $K \in L^2([a, b] \times [a, b])$ be a [[square-integrable kernel|WWMWX7AD4V]], with [[Hilbert–Schmidt integral operator|CB5G212Q03]] $T_K$ on $L^2[a, b]$ and [[adjoint|6HSJBJ8TTQ]] $T_K^*$.
Then there are a finite or countable index set $N$ and orthonormal families $(u_n)_{n \in N}$ and $(v_n)_{n \in N}$ in $L^2[a, b]$.
There are also numbers $s_1 \ge s_2 \ge \cdots > 0$, with $s_n \to 0$ if $N$ is infinite, such that:

1. $T_K v_n = s_n u_n$ and $T_K^* u_n = s_n v_n$ for every $n \in N$;
2. $T_K \varphi = \sum_{n \in N} s_n \ip{\varphi}{v_n} u_n$ for every $\varphi \in L^2[a, b]$;
3. $K(x, y) = \sum_{n \in N} s_n \, u_n(x) \overline{v_n(y)}$, with convergence in $L^2([a, b] \times [a, b])$;
4. $\sum_{n \in N} s_n^2 = \int_a^b \int_a^b \abs{K(x, y)}^2 \, dx \, dy$.

The numbers $s_n$ are the [[singular values|QSJKPKPM7H]] of $T_K$: their squares are the nonzero eigenvalues of $T_K^* T_K$, counted with multiplicity.

## Remarks

The operator $T_K^* T_K$ is compact, self-adjoint and has nonnegative eigenvalues; it is the integral operator with the kernel $\int_a^b \overline{K(t, x)} K(t, y) \, dt$.
The [[spectral theorem for compact self-adjoint operators|A1G25R99PY]] gives orthonormal eigenfunctions $v_n$ with eigenvalues $s_n^2 > 0$.
Then $u_n = T_K v_n / s_n$ is an orthonormal family, since $\ip{T_K v_n}{T_K v_m} = \ip{T_K^* T_K v_n}{v_m} = s_n^2 \delta_{nm}$.
Parts 3 and 4 follow as for the bilinear series of a symmetric kernel, using the orthonormal family $u_n(x) \overline{v_m(y)}$.

Example: the Volterra kernel on $[0, 1]$, equal to $1$ for $y \le x$ and $0$ otherwise, has no eigenvalues, but it has singular values $s_n = \frac{1}{(n - \frac12)\pi}$, with $v_n(y) = \sqrt{2} \cos\left((n - \tfrac12)\pi y\right)$ and $u_n(x) = \sqrt{2} \sin\left((n - \tfrac12)\pi x\right)$.
Part 4 gives $\sum_n \frac{1}{(n - \frac12)^2 \pi^2} = \frac12$, the area of the triangle where the kernel is $1$.

For a Hermitian kernel, the $s_n$ are the absolute values of the nonzero eigenvalues, and one may take $u_n = \pm v_n$.

## Explanations

### L1 human

Every square-integrable kernel, symmetric or not, can be written as a sum of simple products $u_n(x) \overline{v_n(y)}$ with decreasing positive weights.
The two families of functions are each orthonormal, but they are different families.
This is the integral version of the [[singular value decomposition|000NPTMX6J]] of a matrix.

### L2 human

The decomposition is the right tool for non-symmetric kernels, where eigenfunctions may fail to exist or to be orthogonal.
Keeping the first $m$ terms gives the best approximation of $K$ in the $L^2$ norm by a degenerate kernel of rank at most $m$, with error $\left(\sum_{n > m} s_n^2\right)^{1/2}$.
For a Fredholm equation of the first kind $T_K \varphi = f$, it gives the formal solution $\varphi = \sum_n s_n^{-1} \ip{f}{u_n} v_n$, and the growth of $1/s_n$ shows why such equations are ill-posed.
