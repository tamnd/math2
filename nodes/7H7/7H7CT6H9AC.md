---
tag: 7H7CT6H9AC
kind: definition
name: Modular representation theory
msc: [20C20, 20C05]
defines: G28W7J8G2D
uses: [WYGRXCG2RN, 0F6ES3BRYP, MNP2HBWB5Q, 0NZ8JA25WK, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_representation_theory
---

## Definition

Let $G$ be a finite group and let $K$ be a field whose [[characteristic|0F6ES3BRYP]] is a prime $p$ that divides $\abs{G}$.
A *modular representation* of $G$ over $K$ is a [[representation|WYGRXCG2RN]] $\rho \colon G \to GL(V)$ on a finite-dimensional vector space $V$ over $K$.
Equivalently, it is a finitely generated [[module|0NZ8JA25WK]] over the [[group algebra|MNP2HBWB5Q]] $KG$.
*Modular representation theory* is the study of these representations and modules.

## Remarks

Example: $G = \Z/p\Z$ with generator $g$, $K = \F_p$, and $\rho(g) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
This is a representation because $\rho(g)^p = \begin{pmatrix} 1 & p \\ 0 & 1 \end{pmatrix} = I$ in characteristic $p$.
The line $K e_1$ is invariant, but any other line $K(a e_1 + e_2)$ is sent to $K((a+1) e_1 + e_2)$, a different line, so $V$ is not a direct sum of invariant lines.
Non-example: representations of $G$ over $\C$, or over a [[finite field|0ZXZ82FTX2]] whose characteristic does not divide $\abs{G}$, are ordinary representations; there Maschke's theorem makes every representation semisimple.
Let $K$ be a splitting field for $G$.
Brauer showed that the number of simple $KG$-modules is the number of conjugacy classes of elements of $G$ of order prime to $p$.
