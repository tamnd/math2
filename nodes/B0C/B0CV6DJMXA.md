---
tag: B0CV6DJMXA
kind: definition
name: Detectability
msc: [93B07, 93D15, 93C05]
defines: PE9HCFHXB5
uses: [0BQAA2BK3Q, C4HN3EAQWM, C2KM20J9DZ, 3RJZAP1KQG, 1ZD7GE643S]
sources:
  - url: https://en.wikipedia.org/wiki/Observability
---

## Definition

Let $n, p \ge 1$, let $A$ be a real $n \times n$ matrix and let $C$ be a real $p \times n$ matrix.
Consider the system $x' = Ax$, $y = Cx$.
The pair $(C, A)$ is *detectable* if some real $n \times p$ matrix $L$ makes every [[eigenvalue|0BQAA2BK3Q]] of $A - LC$ have negative real part.

## Remarks

Since $(A - LC)^T = A^T + C^T (-L^T)$, the pair $(C, A)$ is detectable if and only if $(A^T, C^T)$ is [[stabilizable|C2KM20J9DZ]]; this is the [[duality|3RJZAP1KQG]] of the two notions.
By the [[Hautus lemma|1ZD7GE643S]] argument, $(C, A)$ is detectable if and only if the matrix with blocks $\lambda I - A$ above $C$ has rank $n$ for every $\lambda \in \C$ with $\operatorname{Re} \lambda \ge 0$.
Every [[observable|C4HN3EAQWM]] system is detectable.
For the observer $\hat{x}' = A \hat{x} + L(y - C \hat{x})$, the error $e = x - \hat{x}$ satisfies $e' = (A - LC) e$, so it tends to $0$ when $L$ is as in the definition.
Example: $A = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ and $C = \begin{pmatrix} 0 & 1 \end{pmatrix}$; with $L = \begin{pmatrix} 0 \\ 2 \end{pmatrix}$ one gets $A - LC = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$, so the pair is detectable.
Non-example: $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ and the same $C$; for every $L$ the matrix $A - LC = \begin{pmatrix} 1 & -l_1 \\ 0 & -1 - l_2 \end{pmatrix}$ is upper triangular with the eigenvalue $1$.
