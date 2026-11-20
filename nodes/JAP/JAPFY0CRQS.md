---
tag: JAPFY0CRQS
kind: proof
name: Proof that a matrix is similar to its transpose
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: grad
proves: C708QKZPE6
methods: [0NTF6DMVAP]
uses: [042JWAR3Q0, 0VH1TC1PWF, 0P799D6AMN, 00SPJSDT3Z, PQ1D8FQB3E, 0N28QN4CYA, 0C3CFHDN6R, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose
    locator: Properties
---

## Proof

1. By the [[rational canonical form theorem|042JWAR3Q0]], $A = P R P^{-1}$ with $P \in GL_n(F)$ and $R = C(d_1) \oplus \cdots \oplus C(d_r)$, a block diagonal matrix of [[companion matrices|0VH1TC1PWF]].
2. Let $p = x^m + c_{m-1} x^{m-1} + \cdots + c_0$ be one of the $d_i$, and $C = C(p)$. So $C e_j = e_{j+1}$ for $j < m$, and $C e_m = -\sum_{k=0}^{m-1} c_k e_{k+1}$.
3. Let $Q = F[x]/(p)$. By division with remainder, the classes of $1, x, \dots, x^{m-1}$ are a basis of $Q$. Let $\varphi \colon F^m \to Q$ be the linear bijection with $\varphi(e_j) = x^{j-1}$.
4. Then $\varphi(C u) = x \varphi(u)$ for all $u$. On $e_j$ with $j < m$, both sides are $x^j$. On $e_m$, both sides are $x^m \equiv -\sum_k c_k x^k$ modulo $p$. Both sides are linear in $u$.
5. Let $\lambda \colon Q \to F$ take a class to the coefficient of $x^{m-1}$ in its remainder of degree less than $m$. It is linear. Define $\beta(f, g) = \lambda(fg)$ on $Q$. It is a symmetric [[bilinear form|0P799D6AMN]], because multiplication in $Q$ is commutative and bilinear.
6. For all $f, g \in Q$, $\beta(xf, g) = \lambda(xfg) = \beta(f, xg)$.
7. Let $S$ be the [[Gram matrix|00SPJSDT3Z]] with $S_{ij} = \beta(x^{i-1}, x^{j-1}) = \lambda(x^{i+j-2})$. By bilinearity, $\beta(\varphi u, \varphi v) = u^{\mathsf T} S v$ for $u, v \in F^m$. Also $S$ is [[symmetric|0N28QN4CYA]], since $\beta$ is symmetric.
8. By steps 4, 6 and 7, $u^{\mathsf T} C^{\mathsf T} S v = \beta(x \varphi u, \varphi v) = \beta(\varphi u, x \varphi v) = u^{\mathsf T} S C v$ for all $u, v$. So $C^{\mathsf T} S = S C$.
9. The entry $S_{ij}$ depends only on $i + j$, so $S$ is a [[Hankel matrix|PQ1D8FQB3E]]. If $i + j \le m$, then $x^{i+j-2}$ has degree less than $m - 1$, so $S_{ij} = 0$. If $i + j = m + 1$, then $S_{ij} = \lambda(x^{m-1}) = 1$.
10. Let $J$ be the reversal matrix, with $J_{ij} = 1$ when $i + j = m + 1$ and $0$ otherwise. Then $(SJ)_{ij} = S_{i, m+1-j}$, which is $0$ for $i < j$ and $1$ for $i = j$, by step 9. So $SJ$ is lower triangular with ones on the diagonal.
11. Hence $\det(S) \det(J) = 1$ by the [[determinant|0C3CFHDN6R]] of a triangular matrix and multiplicativity. So $\det S = \pm 1$ and $S$ is invertible, with $C^{\mathsf T} = S C S^{-1}$.
12. Do this for each block $C(d_i)$, with matrix $S_i$. Let $S_R = S_1 \oplus \cdots \oplus S_r$. It is symmetric and invertible, and blockwise multiplication with step 8 gives $R^{\mathsf T} S_R = S_R R$.
13. Let $T = P^{-\mathsf T} S_R P^{-1}$, where $P^{-\mathsf T}$ is the [[transpose|0W809K6AW0]] of $P^{-1}$. Then $T^{\mathsf T} = P^{-\mathsf T} S_R^{\mathsf T} P^{-1} = T$, and $T$ is invertible as a product of invertible matrices.
14. Using $A = P R P^{-1}$ and $A^{\mathsf T} = P^{-\mathsf T} R^{\mathsf T} P^{\mathsf T}$, we get $T A = P^{-\mathsf T} S_R R P^{-1}$ and $A^{\mathsf T} T = P^{-\mathsf T} R^{\mathsf T} S_R P^{-1}$.
15. By step 12 these are equal. So $A^{\mathsf T} T = T A$, that is, $A^{\mathsf T} = T A T^{-1}$ with $T$ symmetric.

## Idea

A companion matrix is multiplication by $x$ on $F[x]/(p)$.
This map is self-adjoint for the symmetric form $\lambda(fg)$, and self-adjoint means $C^{\mathsf T} S = S C$ for the Gram matrix $S$.
The rational canonical form carries this from one block to every matrix.

For $m = 2$ and $p = x^2 + c_1 x + c_0$, $S = \begin{pmatrix} 0 & 1 \\ 1 & -c_1 \end{pmatrix}$.
Both $C^{\mathsf T} S$ and $S C$ are equal to $\begin{pmatrix} 1 & -c_1 \\ -c_1 & c_1^2 - c_0 \end{pmatrix}$.

## Variants

If the similarity need not be symmetric, there is a shorter proof by the [[characteristic matrix|92VZF0QRM8]].
The $k \times k$ minors of $xI - A^{\mathsf T} = (xI - A)^{\mathsf T}$ are the $k \times k$ minors of $xI - A$, so the determinantal divisors agree, and $A$ and $A^{\mathsf T}$ are similar.
A third proof uses the Jordan form over an algebraic closure $\bar F$: the reversal matrix $J$ gives $J_k(\lambda)^{\mathsf T} = J \, J_k(\lambda) \, J$.
Then the theorem on [[similarity over a field extension|5PVFX89NM7]] gives a similarity over $F$, but that similarity need not be symmetric.
