---
tag: 0WCPH5Z7FA
kind: statement
role: proposition
name: Trace of a linear map is the trace of its matrix
msc: ["15A04", "15A15"]
topics: [S6559D61BP]
audience: ug1
about: [0KZDNGA561]
uses: [0RPDTWY2JS, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a linear operator
---

## Statement

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$ with a basis $B$, and let $T \colon V \to V$ be a linear map.
Then the [[trace of $T$|0KZDNGA561]] equals the trace of the [[matrix of $T$|0YQSGNYE3K]] in $B$:
$$\tr T = \tr [T]_B.$$
Equivalently, $\tr [T]_{B'} = \tr [T]_B$ for any two bases $B$ and $B'$ of $V$.

## Remarks

### Why each hypothesis is needed

- The same basis must be used for the domain and the codomain. For $\id$ on $\R^2$ with $B = (e_1, e_2)$ and $C = (2e_1, e_2)$, $[\id]_{C,B} = \operatorname{diag}(1/2, 1)$ has diagonal sum $3/2$, but $\tr \id = 2$. This is the [[non-example|VND2T4RZK8]].
- $V$ must be finite-dimensional, so that $T$ has a square matrix with finitely many diagonal entries.

### Consequences

- The trace of $T$ can be computed in the most convenient basis. For a [[projection|033DA1WE8Y]] this gives $\tr P = (\rank P) \cdot 1_F$, by the [[theorem on the trace of a projection|BJTJ41YW55]].
- Similar matrices have the same trace, since they are the matrices of one endomorphism in two bases.
- If $T$ has a basis of eigenvectors with eigenvalues $\lambda_1, \dots, \lambda_n$, then $\tr T = \lambda_1 + \dots + \lambda_n$.

### Converse

Two endomorphisms with the same trace need not be similar.
On $\R^2$, the zero map and the map with matrix $\operatorname{diag}(1, -1)$ both have trace $0$.

### Generalizations

- The same statement holds for a free module of finite rank over a commutative ring, with the same proof.
- The determinant and the characteristic polynomial of $T$ are also independent of the basis, by the [[theorem on similarity invariants|191HBJ7PVZ]].

## History

The trace of a matrix as a similarity invariant is classical.
The basis-free definition through $V^* \otimes V$ came later, with multilinear algebra.

## Explanations

### L1 human

We can compute the trace of a linear map in any basis that we like.
We write the matrix in that basis and add its diagonal entries.
Every basis gives the same number.

### L2 human

A change of basis replaces $[T]_B$ by $P^{-1} [T]_B P$.
The cyclic property $\tr(XY) = \tr(YX)$ moves $P^{-1}$ to the right end, where it cancels $P$.

### L3 human

With a basis-free definition, the trace is the map $\End_F(V) \cong V^* \otimes V \to F$ induced by evaluation $f \otimes v \mapsto f(v)$.
In a basis $B$ with dual basis $B^*$, the endomorphism $T$ is $\sum_{i,j} a_{ij}\, b_j^* \otimes b_i$, and evaluation gives $\sum_i a_{ii}$.
So the statement says that the basis-free trace equals the matrix trace in every basis.
