---
tag: 19SZD9XAFX
kind: definition
name: Random matrix
msc: [15B52, 60B20]
defines: 1HS4RT7HK5
uses: [0NFPJVJJHX, 0PNRKMRC55, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Random_matrix
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0NFPJVJJHX]] and let $m, n \ge 1$ be integers.
Let $\mathbb{K}$ be $\R$ or $\C$, and give the space $\mathbb{K}^{m \times n}$ of $m \times n$ [[matrices|0VD9ZSWWJG]] the Borel $\sigma$-algebra of $\mathbb{K}^{mn}$.
A *random $m \times n$ matrix* is a measurable map $X \colon \Omega \to \mathbb{K}^{m \times n}$.

## Remarks

Equivalently, $X = (X_{ij})$ where each entry $X_{ij}$ is a [[random variable|0PNRKMRC55]] on the same space $(\Omega, \mathcal{F}, P)$.
The law of $X$ is the probability measure $P \circ X^{-1}$ on $\mathbb{K}^{m \times n}$.
Example: let $G$ be an $n \times n$ matrix whose entries are independent standard normal random variables, and let $H = (G + G^T)/\sqrt{2}$.
Each entry of $H$ is a sum of measurable functions, so $H$ is a random symmetric matrix; it is a Wigner matrix with Gaussian entries.
Non-example: $n^2$ random variables defined on different probability spaces do not form a random matrix, because the entries need one common probability space.
