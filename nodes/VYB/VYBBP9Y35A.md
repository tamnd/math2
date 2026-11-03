---
tag: VYBBP9Y35A
kind: definition
name: Vector quantization
msc: [94A29, 94A34, 68P30]
defines: WCB9TWJZ31
uses: [H6TFN824YV, V1R1R88GV6, D5PN3G41D6, 0PNRKMRC55, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_quantization
---

## Definition

Let $k \ge 1$ and $N \ge 1$ be integers.
A *vector quantizer* of dimension $k$ and size $N$ is a Borel measurable map $Q \colon \R^k \to \R^k$ with an image of $N$ points.
This image $\set{c_1, \dots, c_N}$ is the *codebook*.
Its *cells* are the sets $S_i = Q^{-1}(c_i)$, which partition $\R^k$.
For a [[random vector|0PNRKMRC55]] $X$ in $\R^k$ with $\mathbb{E}\norm{X}^2 < \infty$, its *distortion* is the [[expected value|0WQNRCNY3M]] $\mathbb{E}\norm{X - Q(X)}^2$.
*Vector quantization* is the representation of $X$ by $Q(X)$, or by the index $i$ with $Q(X) = c_i$, which takes $\log_2 N$ bits.

## Remarks

For $k = 1$ this is a scalar [[quantizer|H6TFN824YV]] with finitely many levels.
Every quantizer with least distortion among those of its size satisfies two conditions.
The first is the *nearest-neighbour condition*: with probability one, $Q(X)$ is a codeword nearest to $X$.
So each cell $S_i$ is the [[Voronoi cell|V1R1R88GV6]] of $c_i$, up to a set of probability zero.
The second is the *centroid condition*: $c_i = \mathbb{E}[X \mid X \in S_i]$ whenever $\Pr(X \in S_i) > 0$.
Lloyd's algorithm alternates these two steps; on a finite data set it is the [[k-means|D5PN3G41D6]] algorithm.
Example: with $k = 2$ and codebook $\set{(1,1), (1,-1), (-1,1), (-1,-1)}$, sending each point to the nearest codeword quantizes $(x, y)$ to $(\sgn x, \sgn y)$ off the axes.
Non-example: a map whose image is the whole unit circle is not a vector quantizer, since its image is infinite.
