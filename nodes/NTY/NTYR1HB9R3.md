---
tag: NTYR1HB9R3
kind: proof
name: Proof of simultaneous unitary diagonalization
msc: ["15A21", "47B15"]
topics: [3YM9EK6VMB]
audience: ug2
proves: BFQQDA489F
uses: [04CW1P44VD, 06J4PXRG22, 0JHGAV9H25, D5KVBA1K9R, 0Y85GYEGSF, 0AYEPBQMAW, 0ENZN5G4CV, 0MB8HQW495, 0JWM6GJNQW, 096V7H13H9]
methods: [0KMVFSHFGZ, 0WCP0PVET6, TFQ1845T84]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_matrix
    locator: Consequences
---

## Proof

We use strong induction on $n = \dim V$, and we split $V$ into the eigenspaces of one member of $\mathcal{F}$ that is not a scalar multiple of $I$.

1. Direction "if". Let $e_1, \dots, e_n$ be a common orthonormal eigenbasis. In this basis every member of $\mathcal{F}$ has a diagonal matrix, and diagonal matrices commute, so the members commute.
2. Direction "only if", setting. Let $\mathbb{K}$ be $\mathbb{C}$ with normal members, or $\mathbb{R}$ with self-adjoint members. For $n \geq 0$, let $P(n)$ say that parts 1 and 2 hold for every commuting family on every space of dimension $n$. Fix $n$ and assume $P(d)$ for all $d < n$.
3. Case 1: every member of $\mathcal{F}$ is a scalar multiple of $I$. Then every nonzero vector is an eigenvector of every member, so [[any orthonormal basis|0Y85GYEGSF]] of $V$ works. This case includes $n = 0$ and $n = 1$.
4. Case 2: some $A \in \mathcal{F}$ is not a scalar multiple of $I$. By the [[complex spectral theorem|04CW1P44VD]] or the [[real spectral theorem|06J4PXRG22]], $A$ has an orthonormal eigenbasis.
5. The eigenspaces of $A$. Let $\lambda_1, \dots, \lambda_m$ be the distinct eigenvalues of $A$, with [[eigenspaces|0AYEPBQMAW]] $E_1, \dots, E_m$. The eigenbasis lies in their union, so $V = E_1 + \dots + E_m$, and the $E_i$ are pairwise orthogonal by [[orthogonality of eigenspaces|0JHGAV9H25]].
6. Each piece is smaller. If $m = 1$, then $A = \lambda_1 I$, which Case 2 excludes, so $m \geq 2$. Each $E_i$ is nonzero, so $\dim E_i < n$.
7. Invariance under $B$. Let $B \in \mathcal{F}$ and $v \in E_i$. Since $AB = BA$,
$$A(Bv) = B(Av) = B(\lambda_i v) = \lambda_i\, Bv,$$
so $Bv \in E_i$.
8. Invariance under $B^*$. By the [[spectral decomposition|D5KVBA1K9R]] applied to $B$, its adjoint is a polynomial in $B$, $B^* = g(B)$. So $B^*$ commutes with $A$ as well, and step 7 with $B^*$ in place of $B$ shows that $B^* v \in E_i$ for $v \in E_i$.
9. The restriction. Let $B_i$ be the restriction of $B$ to $E_i$. For $v, w \in E_i$ we have $\ip{B_i v}{w} = \ip{v}{B^* w}$ with $B^* w \in E_i$, so the adjoint of $B_i$ on $E_i$ is the restriction of $B^*$.
10. The restricted family. So $B_i$ is [[normal|0ENZN5G4CV]] when $B$ is normal, and [[self-adjoint|0MB8HQW495]] when $B$ is self-adjoint. For $B, C \in \mathcal{F}$, the restrictions commute, because $BC = CB$ on all of $V$.
11. Induction. By $P(\dim E_i)$, each $E_i$ has an orthonormal basis of common eigenvectors of all the $B_i$. Each of these vectors is an eigenvector of every $B \in \mathcal{F}$, because $Bv = B_i v$ for $v \in E_i$.
12. Joining the bases. Vectors from different $E_i$ are orthogonal by step 5, so the joined family is orthonormal. It spans each $E_i$, so it spans $V$ by step 5. An orthonormal family is [[linearly independent|0JWM6GJNQW]], so the joined family is a [[basis|096V7H13H9]] of $V$, and $P(n)$ holds.
13. Part 3. Apply parts 1 and 2 to the maps $x \mapsto A_j x$ with the standard inner product, which are normal or self-adjoint by the matrix of the adjoint. Put the common orthonormal eigenvectors as the columns of $U$. Then $U$ is unitary, or real orthogonal in the real case, and $A_j U = U D_j$ with $D_j$ diagonal, so every $U^* A_j U = D_j$ is diagonal.

## Idea

Choose one member $A$ that is not a scalar and cut the space into its eigenspaces.
Every member that commutes with $A$ maps each eigenspace into itself, and so does its adjoint, because for a normal operator the adjoint is a polynomial in the operator.
So the problem breaks into smaller problems of the same kind, one on each eigenspace.
Induction solves each smaller problem, and the orthogonality of the eigenspaces glues the answers into one orthonormal basis.

## Variants

Step 8 is the finite-dimensional case of [[Fuglede's theorem|V1C28937NX]]: if $AB = BA$ and $B$ is normal, then $AB^* = B^* A$.
For bounded operators on a Hilbert space, $B^*$ need not be a polynomial in $B$, and the proof of that theorem is harder.

For a finite family $A_1, \dots, A_k$, one can split without induction on the dimension.
Cut $V$ by the eigenspaces of $A_1$, then cut each piece by the eigenspaces of $A_2$, and so on.
The final pieces are the intersections $E^{(1)}_{i_1} \cap \dots \cap E^{(k)}_{i_k}$ of eigenspaces, they are pairwise orthogonal, and they add up to $V$, so orthonormal bases of the pieces give the common eigenbasis.
