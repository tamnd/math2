---
tag: M60QTW5EBV
kind: proof
name: Proof that the geometric multiplicity is at most the algebraic multiplicity
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: FWY8A9M5HK
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0ZND7NQ970, 0AYEPBQMAW, 0S7A0EMPF4, C98TZ6ZAXC, 0M4SXE5WW3, 0YYMY95FWS, 0K1KKMFHYH]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenspaces, geometric multiplicity, and the eigenbasis
  - book: isbn:9780134860244
---

## Proof

We choose a basis that starts with a basis of the eigenspace, so that the matrix of $T$ has a block $\lambda I_g$ in its corner, and then we read the factor $(t - \lambda)^g$ off the characteristic polynomial.
Write $g = \dim E_\lambda$ and let $m$ be the algebraic multiplicity of $\lambda$.

*Lower bound.*

1. By the definition of an [[eigenvalue|0ZND7NQ970]], there is a vector $v \ne 0$ with $T(v) = \lambda v$.
2. This $v$ lies in $E_\lambda$, by the definition of the [[eigenspace|0AYEPBQMAW]].
   So $E_\lambda \ne 0$ and $g \ge 1$.

*Upper bound.*

3. Choose a basis $u_1, \dots, u_g$ of $E_\lambda$.
   It is an independent list in $V$, so it [[extends to a basis|0M4SXE5WW3]] $B = (u_1, \dots, u_g, w_1, \dots, w_{n-g})$ of $V$.
4. For $j \le g$ we have $T(u_j) = \lambda u_j$, because $u_j \in E_\lambda$.
5. Column $j$ of the [[matrix of the linear map|0YYMY95FWS]] $[T]_B$ holds the coordinates of $T(u_j)$, so for $j \le g$ it is $\lambda e_j$.
6. So $[T]_B$ has the block form
$$[T]_B = \begin{pmatrix} \lambda I_g & C \\ 0 & D \end{pmatrix},$$
   with a $g \times (n - g)$ block $C$ and an $(n - g) \times (n - g)$ block $D$.
7. If $g = n$, then $[T]_B = \lambda I_n$ and $p_T = (t - \lambda)^n$, so $m = n = g$.
8. If $g < n$, part 2 of the theorem on the [[characteristic polynomial of an endomorphism|C98TZ6ZAXC]] gives $p_T = p_{\lambda I_g} \cdot p_D$ for this block triangular matrix.
9. The matrix $t I_g - \lambda I_g$ is diagonal with every diagonal entry $t - \lambda$, so the [[determinant of a triangular matrix|0K1KKMFHYH]] gives $p_{\lambda I_g} = (t - \lambda)^g$.
10. So $p_T = (t - \lambda)^g \, p_D$, and $(t - \lambda)^g$ divides $p_T$.
11. By the definition of the [[algebraic multiplicity|0S7A0EMPF4]], $m$ is the largest $k$ with $(t - \lambda)^k \mid p_T$, so $g \le m$.

The matrix case follows by applying this to the map $x \mapsto Ax$ on $F^n$.

## Idea

Put the eigenvectors first in the basis.
On them the map is multiplication by $\lambda$, so the matrix has $\lambda I_g$ in the top left corner and zeros below it.
The determinant of a block triangular matrix is the product of the determinants of the diagonal blocks, so the characteristic polynomial contains $(t - \lambda)^g$.
The other block $D$ may contain more factors $t - \lambda$, and that is why the inequality can be strict.
For the [[shear|HTAWRAC3QE]], $g = 1$ and the basis $(e_1, e_2)$ already has this form, with $D = (1)$ giving the second factor $t - 1$.

## Variants

A second proof uses the generalized eigenspace $G_\lambda = \ker(T - \lambda \operatorname{id}_V)^n$.
It contains $E_\lambda$, and it has dimension $m$, by the [[decomposition into generalized eigenspaces|0Z3GDY89T5]], so $g \le m$.
This needs the decomposition, which is a later and longer result.

Over an algebraically closed field, the [[Jordan normal form|085HQ5G5TE]] gives a third view.
There $g$ is the number of Jordan blocks for $\lambda$ and $m$ is their total size, and each block has size at least $1$.
