---
tag: NBW86C3ZVN
kind: definition
name: Positive-definite kernel
msc: ["46E22", 43A35]
defines: SCMS389SBG
uses: [01MMVW8CKC, 0P17NGQQMQ, 4CK2GSRAGD, 3PRZ02APFA, 2ZB3NFZ94T]
sources:
  - url: https://en.wikipedia.org/wiki/Positive-definite_kernel
---

## Definition

Let $X$ be a nonempty set.
A *positive-definite kernel* on $X$ is a function $K \colon X \times X \to \C$ such that
$$\sum_{i, j = 1}^{n} c_i \overline{c_j}\, K(x_i, x_j) \ge 0$$
for all $n \ge 1$, all $x_1, \dots, x_n \in X$ and all $c_1, \dots, c_n \in \C$.
Equivalently, every matrix $\big(K(x_i, x_j)\big)_{i,j=1}^{n}$ is [[positive semidefinite|01MMVW8CKC]].

## Remarks

Such a kernel is [[Hermitian|2ZB3NFZ94T]]: $K(y, x) = \overline{K(x, y)}$, because each matrix $\big(K(x_i, x_j)\big)$ is a [[Hermitian matrix|0P17NGQQMQ]].
For a real-valued kernel one often uses real coefficients $c_i$ and asks in addition that $K(x, y) = K(y, x)$.
Some authors call these kernels positive semidefinite and keep "positive definite" for the case of strict inequality when the points are distinct and $c \ne 0$.

Example: if $\Phi \colon X \to \mathcal{H}$ is any map into a Hilbert space, then $K(x, y) = \ip{\Phi(x)}{\Phi(y)}$ is positive-definite, where the inner product is linear in the first argument.
Indeed $\sum_{i,j} c_i \overline{c_j} \ip{\Phi(x_i)}{\Phi(x_j)} = \norm{\sum_i c_i \Phi(x_i)}^2 \ge 0$.
By the Moore–Aronszajn theorem every positive-definite kernel arises in this way, from its [[reproducing kernel Hilbert space|4CK2GSRAGD]].

Non-example: the constant kernel $K(x, y) = -1$ is not positive-definite.
With $n = 1$ and $c_1 = 1$, the sum is $K(x_1, x_1) = -1 < 0$.

If $X = G$ is a group and $K(g, h) = \varphi(g^{-1}h)$, then $K$ is positive-definite exactly when $\varphi$ is a [[positive-definite function|3PRZ02APFA]] on $G$.
