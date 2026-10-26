---
tag: 000NPTMX6J
kind: statement
role: theorem
name: Singular value decomposition
msc: [15A18, 15A23]
uses: [0K2TX12X58, 0D6RMJ10M9]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: lead section
same_as:
  wikidata: Q420904
  wikipedia: Singular value decomposition
---

## Statement

Let $A$ be an $m \times n$ complex matrix.
Then there are a [[unitary matrix|0AR68JTMDT]] $U$ of size $m \times m$, a unitary matrix $V$ of size $n \times n$, and an $m \times n$ matrix $\Sigma$ with
$$A = U \Sigma V^*.$$
Here $\Sigma_{ij} = 0$ for $i \ne j$, and $\Sigma_{11} \ge \Sigma_{22} \ge \cdots \ge 0$ are the [[singular values|09VMDSRXWJ]] of $A$.

## Remarks

If $A$ is real, then $U$ and $V$ can be chosen real orthogonal.
The columns of $V$ are eigenvectors of $A^* A$, and the columns of $U$ are eigenvectors of $A A^*$.
The matrix $\Sigma$ is unique; $U$ and $V$ are not unique in general.
Keeping the $k$ largest singular values gives the best approximation of $A$ of rank $k$, for the Frobenius and operator norms.

## Explanations

### L1 human

Every matrix is a rotation, then a stretch along the axes, then another rotation.
The stretch factors are the singular values.
This decomposition is a central tool in data analysis and numerical computation.
