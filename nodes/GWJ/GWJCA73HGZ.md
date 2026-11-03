---
tag: GWJCA73HGZ
kind: definition
name: Realization of a transfer function
msc: [93B15, 93C05]
defines: WDVJXWV3RF
uses: [86JKV3TRFD, 6J9MPVHSMF, 0XDK9CGYKJ]
sources:
  - url: https://en.wikipedia.org/wiki/Realization_(systems)
---

## Definition

Let $m, p \ge 1$, and let $G$ be a $p \times m$ matrix whose entries are real [[rational functions|0XDK9CGYKJ]] of $s$.
Let $n \ge 0$.
Let $A \in \R^{n \times n}$, $B \in \R^{n \times m}$, $C \in \R^{p \times n}$ and $D \in \R^{p \times m}$ be real matrices.
The quadruple $(A, B, C, D)$ is a *realization* of $G$ if
$$G(s) = C (sI - A)^{-1} B + D$$
for every $s \in \C$ that is not an eigenvalue of $A$.
The number $n$ is the *dimension*, or *order*, of the realization.
The corresponding [[linear time-invariant system|6J9MPVHSMF]] $x' = Ax + Bu$, $y = Cx + Du$ then has [[transfer function|86JKV3TRFD]] $G$.

## Remarks

A rational matrix $G$ has a realization if and only if it is proper, that is, $G(s)$ has a finite limit as $\abs{s} \to \infty$; this limit is then $D$.

Example: $G(s) = 1/(s + 1)$ has the realization $A = -1$, $B = 1$, $C = 1$, $D = 0$ of dimension $1$, since $C(s - A)^{-1}B = 1/(s + 1)$.
It also has the realization $A = \begin{pmatrix} -1 & 0 \\ 0 & -2 \end{pmatrix}$, $B = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $C = (1, 0)$, $D = 0$ of dimension $2$, since $C (sI - A)^{-1} B = 1/(s + 1)$.

Non-example: $G(s) = s$ has no realization, because $C(sI - A)^{-1}B + D$ tends to $D$ as $\abs{s} \to \infty$, while $s$ does not have a finite limit.

If $(A, B, C, D)$ is a realization and $T$ is an invertible $n \times n$ matrix, then $(TAT^{-1}, TB, CT^{-1}, D)$ is a realization of the same $G$.
The same definition is used in discrete time, with the variable $z$ of the Z-transform in place of $s$.
