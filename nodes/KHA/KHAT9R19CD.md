---
tag: KHAT9R19CD
kind: definition
name: Compressed sensing
msc: [94A12, 41A46, 94A20]
defines: 6V8E0AQNHA
uses: [0VD9ZSWWJG, WC8P971XGW, B0K18PWN2A]
sources:
  - url: https://en.wikipedia.org/wiki/Compressed_sensing
---

## Definition

Let $m < N$ and $s \ge 1$ be integers and let $A$ be a real $m \times N$ [[matrix|0VD9ZSWWJG]], called the *measurement matrix*.
A vector $x \in \R^N$ is *$s$-sparse* if it has at most $s$ nonzero entries.
*Compressed sensing* is the problem of recovering an unknown $s$-sparse vector $x$ from its measurement vector $y = Ax \in \R^m$.
Its standard method is *basis pursuit*: output a solution of
$$\min\set{\norm{z}_1 : z \in \R^N, \ Az = y}, \qquad \norm{z}_1 = \textstyle\sum_{j=1}^N \abs{z_j} .$$
The matrix $A$ *allows recovery of $s$-sparse vectors* if every $s$-sparse $x$ is the unique solution of this problem with $y = Ax$.

## Remarks

It is the case $\varepsilon = 0$ of [[sparse approximation|WC8P971XGW]], restricted to data that come from a sparse vector.
Suppose every $2s$ columns of $A$ are linearly independent.
Then an $s$-sparse $x$ is the only $s$-sparse solution of $Az = Ax$, since two such solutions differ by a $2s$-sparse vector in the kernel of $A$.
A matrix with the [[restricted isometry property|B0K18PWN2A]] of order $2s$ and constant $\delta_{2s} < \sqrt{2} - 1$ allows recovery of $s$-sparse vectors by basis pursuit.
Example: $A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}$, $s = 1$, $x = (0, 0, 2)$, $y = (2, 2)$.
The solutions of $Az = y$ are $z = (2 - t, 2 - t, t)$, and $\norm{z}_1 = 2\abs{2 - t} + \abs{t}$ is minimal exactly at $t = 2$, so basis pursuit returns $x$.
Non-example: for $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ and $s = 1$, the $1$-sparse vectors $e_1$ and $e_2$ give the same $y = (1, 0)$, so no method can recover both.
