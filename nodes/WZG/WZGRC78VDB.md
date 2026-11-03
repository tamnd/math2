---
tag: WZGRC78VDB
kind: definition
name: Normal mode
msc: [70J10, 70J30]
defines: JVM27J1FTF
uses: [WKTX3JJHMB, 0QQCG3JWJ4, 0N28QN4CYA, 8C19QDA99E]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_mode
---

## Definition

Let $M$ and $K$ be real [[symmetric|0N28QN4CYA]] $n \times n$ matrices, with $M$ [[positive definite|0QQCG3JWJ4]], and consider the linear system of [[small oscillations|WKTX3JJHMB]]
$$M \ddot x + K x = 0, \qquad x \colon \R \to \R^n.$$
A *normal mode* of the system is a solution of the form
$$x(t) = A \cos(\omega t + \varphi) \, v,$$
with a vector $v \in \R^n \setminus \set{0}$, the *mode shape*, and constants $A > 0$, $\omega > 0$, $\varphi \in \R$.
The number $\omega$ is the *natural frequency* of the mode.

## Remarks

The function $x(t) = A \cos(\omega t + \varphi) v$ is a solution if and only if $K v = \omega^2 M v$, so the mode shapes and the squared natural frequencies are the generalized eigenvectors and eigenvalues of the pair $(K, M)$.
Each coordinate of a normal mode is a [[simple harmonic motion|8C19QDA99E]] or is identically zero.
If $K$ is positive definite, there are $n$ natural frequencies $0 < \omega_1 \le \cdots \le \omega_n$, counted with multiplicity, with mode shapes $v_1, \ldots, v_n$ that form a basis of $\R^n$ and satisfy $v_i^T M v_j = 0$ for $i \ne j$.

Example: two unit masses joined to walls and to each other by three springs of stiffness $1$: $M = I_2$ and $K = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$.
For $v = (1, 1)$, $K v = v$, so $\omega = 1$; for $v = (1, -1)$, $K v = 3v$, so $\omega = \sqrt 3$.

Non-example: in the same system, $x(t) = \cos(t) \, (1, 0)$ is not a normal mode, since $K (1, 0)^T = (2, -1)^T$ is not a multiple of $(1, 0)^T$, so it is not even a solution.
