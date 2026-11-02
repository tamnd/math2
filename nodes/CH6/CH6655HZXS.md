---
tag: CH6655HZXS
kind: statement
role: theorem
name: Existence of an eigenvalue for a nonzero symmetric kernel
msc: [45C05, 47A75]
uses: [WWMWX7AD4V, 2ZB3NFZ94T, CB5G212Q03, 4NSACSWRJZ, DC7HMHVREP, M2NEP1K5AE]
about: [2ZB3NFZ94T, DC7HMHVREP]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Schmidt_theorem
---

## Statement

Let $a < b$ and let $K \in L^2([a, b] \times [a, b])$ be a [[square-integrable kernel|WWMWX7AD4V]] that is [[Hermitian|2ZB3NFZ94T]], that is, $K(y, x) = \overline{K(x, y)}$ for almost all $x, y$.
Assume that $K$ is not $0$ almost everywhere.
Let $T_K$ be its [[Hilbert–Schmidt integral operator|CB5G212Q03]] on $L^2[a, b]$.
Then $T_K$ has an [[eigenfunction|4NSACSWRJZ]] with a real eigenvalue $\mu$ such that $\abs{\mu} = \norm{T_K} > 0$.
In particular $K$ has at least one [[characteristic value|DC7HMHVREP]], namely $1/\mu$.

## Remarks

Since $T_K$ is self-adjoint, $\norm{T_K} = \sup_{\norm{\varphi} = 1} \abs{\ip{T_K \varphi}{\varphi}}$, and $\norm{T_K} > 0$ because a kernel whose operator is $0$ is $0$ almost everywhere.
Take unit vectors $\varphi_k$ with $\ip{T_K \varphi_k}{\varphi_k} \to \mu$, where $\mu = \pm \norm{T_K}$.
Then $\norm{T_K \varphi_k - \mu \varphi_k}^2 \le 2\mu^2 - 2\mu \ip{T_K \varphi_k}{\varphi_k} \to 0$.
Since $T_K$ is [[compact|M2NEP1K5AE]], a subsequence of $T_K \varphi_k$ converges, so $\varphi_k$ converges to some unit vector $\varphi$, and $T_K \varphi = \mu \varphi$.

Example: for $K(x, y) = \min(x, y)$ on $[0, 1]$, the largest eigenvalue is $4 / \pi^2$, with eigenfunction $\sin(\pi x / 2)$, and $\norm{T_K} = 4 / \pi^2$.

Symmetry is necessary.
The Volterra kernel, equal to $1$ for $y \le x$ and $0$ otherwise, is square-integrable and not zero.
But its operator $\varphi \mapsto \int_a^x \varphi$ has no eigenfunction at all, so this kernel has no characteristic value.
In finite dimension, the statement is the fact that a nonzero Hermitian matrix has an eigenvalue whose absolute value is its operator norm.

## Explanations

### L1 human

A symmetric kernel that is not zero always has at least one natural mode: a function that the integral operator only stretches.
The stretching factor of the best mode equals the largest amount by which the operator can stretch any function.
Without symmetry this can fail completely.

### L2 human

This is the first step of the Hilbert–Schmidt theory.
Applying it again on the orthogonal complement of the eigenfunctions already found produces the whole sequence of eigenvalues and eigenfunctions, and leads to the [[Hilbert–Schmidt expansion theorem|3CXAZ1G5RJ]].
The variational form $\abs{\mu} = \max \abs{\ip{T_K \varphi}{\varphi}}$ is the starting point of the min-max characterization of the further characteristic values.
