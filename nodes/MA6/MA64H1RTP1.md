---
tag: MA64H1RTP1
kind: statement
role: proposition
name: Biconjugate gradient stabilized method
msc: [65F10]
uses: [0EB9N0S33C, HGF11AHX5R, QB45PCGQPV, A3FR6PNEPB, KE98SW3SBD, 2RPE77ACER]
about: [2RPE77ACER, HGF11AHX5R]
sources:
  - url: https://en.wikipedia.org/wiki/Biconjugate_gradient_stabilized_method
same_as:
  wikidata: Q4903720
  wikipedia: Biconjugate gradient stabilized method
---

## Statement

Let $A$ be a real [[invertible|0EB9N0S33C]] $n \times n$ matrix, let $b \in \R^n$, and let $x_0 \in \R^n$ with $r_0 = b - A x_0$.
Choose $\hat{r}_0 \in \R^n$ with $\hat{r}_0^T r_0 \ne 0$, and set $p_0 = r_0$.
The *biconjugate gradient stabilized method* (BiCGSTAB) computes, for $k = 0, 1, \dots$,
$$v_k = A p_k, \quad \alpha_k = \frac{\hat{r}_0^T r_k}{\hat{r}_0^T v_k}, \quad s_k = r_k - \alpha_k v_k, \quad t_k = A s_k, \quad \omega_k = \frac{t_k^T s_k}{t_k^T t_k},$$
$$x_{k+1} = x_k + \alpha_k p_k + \omega_k s_k, \quad r_{k+1} = s_k - \omega_k t_k,$$
$$\beta_k = \frac{\hat{r}_0^T r_{k+1}}{\hat{r}_0^T r_k} \cdot \frac{\alpha_k}{\omega_k}, \quad p_{k+1} = r_{k+1} + \beta_k (p_k - \omega_k v_k).$$
Suppose that all denominators are nonzero up to step $m$.
Then in exact arithmetic, for $k \le m$:

1. $r_k = b - A x_k$, and $r_k = Q_k(A) P_k(A) r_0$, where $P_k$ is the residual polynomial of the [[biconjugate gradient method|HGF11AHX5R]] with shadow residual $\hat{r}_0$, and $Q_k(t) = \prod_{j=0}^{k-1} (1 - \omega_j t)$;
2. each $\omega_k$ minimizes $\norm{s_k - \omega t_k}_2$ over $\omega \in \R$;
3. each step uses two products with $A$ and none with $A^T$.

## Remarks

The residual polynomial $P_k$ of BiCG has degree $k$ and value $1$ at $0$, so $r_k$ comes from a polynomial of degree $2k$ in the [[Krylov subspace|QB45PCGQPV]] $\mathcal{K}_{2k+1}(A, r_0)$.
The recurrences come from writing the BiCG coefficients in terms of the inner products $\hat{r}_0^T Q_k(A) P_k(A) r_0$, which needs no $A^T$ because $\hat{r}_0^T Q_k(A) = (Q_k(A^T) \hat{r}_0)^T$.
The factor $Q_k$ is a product of local one-step minimal residual steps, which smooths the erratic convergence of BiCG and of the method CGS.
Example: if $r_0$ is an eigenvector of $A$ for $\lambda$, then $v_0 = \lambda r_0$, $\alpha_0 = 1/\lambda$ and $s_0 = 0$, so $x_0 + \alpha_0 p_0$ already solves the system.
In that case $t_0 = 0$ and $\omega_0$ is undefined, and an implementation stops when $s_k$ is small.
The method can still break down, when $\hat{r}_0^T r_k = 0$ or $\omega_k = 0$.
It can stagnate when the $\omega_k$ are close to $0$, which tends to happen when $A$ has eigenvalues with large imaginary parts.

## Explanations

### L1 human

BiCGSTAB is a fix of the biconjugate gradient method for nonsymmetric systems.
It avoids the transpose of the matrix, and after each BiCG-like step it adds a small step that reduces the residual as much as possible.
The result usually converges more smoothly than BiCG and costs little memory.

### L2 human

BiCGSTAB, due to van der Vorst, is with restarted [[GMRES|A3FR6PNEPB]] one of the default Krylov [[iterative methods|2RPE77ACER]] for nonsymmetric sparse systems.
Its memory and work per step are fixed, in contrast with full GMRES, but it has no global minimization property.
It is used with a [[preconditioner|KE98SW3SBD]], typically an incomplete LU factorization.
Variants such as BiCGSTAB($\ell$) use minimal residual polynomials of higher degree to handle complex eigenvalues better.
