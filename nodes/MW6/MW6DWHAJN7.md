---
tag: MW6DWHAJN7
kind: definition
name: Substitution matrix
msc: [92D20, 62P10]
defines: Q7MXCRQR8X
uses: [G42Y4TPD4N]
sources:
  - url: https://en.wikipedia.org/wiki/Substitution_matrix
---

## Definition

Let $\Sigma$ be a finite alphabet.
A *substitution matrix* on $\Sigma$ is a symmetric function $S \colon \Sigma \times \Sigma \to \R$, written as a $\abs{\Sigma} \times \abs{\Sigma}$ matrix.
The entry $S(x, y)$ is the score of a column of a pairwise [[alignment|G42Y4TPD4N]] containing $x$ and $y$.
Let $p_x > 0$ be background frequencies of the letters, and $q_{xy} = q_{yx} > 0$ target frequencies of aligned pairs in related sequences.
The matrix is a *log-odds* matrix if for some constant $\lambda > 0$
$$S(x, y) = \frac{1}{\lambda} \log \frac{q_{xy}}{p_x p_y} \quad \text{for all } x, y \in \Sigma.$$

## Remarks

In a log-odds matrix, a positive score means that the pair is seen in related sequences more often than by chance.
The score of an ungapped alignment is then a log-likelihood ratio, up to the factor $1/\lambda$.
It compares a model of related sequences with a model of independent ones.
Example: on $\Sigma = \set{A, C, G, T}$, $S(x, x) = 1$ and $S(x, y) = -1$ for $x \ne y$ is a substitution matrix, since it is symmetric.
Non-example: a table with $S(A, G) = 1$ and $S(G, A) = -1$ is not symmetric, so the score of an alignment would change when the two sequences are swapped.
The PAM matrices of Dayhoff are built from an evolutionary model of point mutations; the BLOSUM matrices of Henikoff and Henikoff are counted from conserved blocks of aligned proteins.
