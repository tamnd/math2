---
tag: Q4RHTAS8BV
kind: definition
name: Stable general linear group
msc: [19B14, "20G35"]
defines: G8R9561PXT
uses: [0B1261B5ED, 0FCHE902D7, 0JYTG5K9Y4, X9HEQ29Q49]
sources:
  - url: https://en.wikipedia.org/wiki/General_linear_group
    locator: Stable general linear group
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity, and let $GL_n(R)$ be the [[general linear group|0FCHE902D7]] of invertible $n \times n$ matrices over $R$.
For each $n \ge 1$, let $\iota_n \colon GL_n(R) \to GL_{n+1}(R)$ be the injective [[group homomorphism|0JYTG5K9Y4]]
$$\iota_n(A) = \begin{pmatrix} A & 0 \\ 0 & 1 \end{pmatrix}.$$
The *stable general linear group* $GL(R)$ is the [[direct limit|X9HEQ29Q49]] of the sequence $GL_1(R) \to GL_2(R) \to GL_3(R) \to \cdots$ of these maps.

## Remarks

Equivalently, $GL(R)$ is the group of infinite matrices $(a_{ij})_{i, j \ge 1}$ over $R$ that are invertible and differ from the identity matrix in only finitely many entries.
Each $GL_n(R)$ is a subgroup of $GL(R)$, and $GL(R)$ is their union.
Example: over $\Z$, the matrices $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ give the same element of $GL(\Z)$, since the second is $\iota_2$ of the first.
Non-example: the infinite diagonal matrix with every diagonal entry equal to $-1$ is not in $GL(\Z)$, since it differs from the identity in infinitely many entries.
