---
tag: RKJBNRKEDT
kind: example
name: Segre embedding
msc: [14N05, "14E25"]
illustrates: [A4H4CZ2V35]
uses: [ZT9A6JK8QF, A4H4CZ2V35, 2C3PAQ7H50, SY2MWC434Z]
sources:
  - url: https://en.wikipedia.org/wiki/Segre_embedding
same_as:
  wikidata: Q3392521
  wikipedia: Segre embedding
---

## Example

Let $k$ be an algebraically closed field and let $m, n \ge 0$.
Let $N = (m + 1)(n + 1) - 1$ and give $\mathbb{P}^N$ the homogeneous coordinates $z_{ij}$ for $0 \le i \le m$ and $0 \le j \le n$.
The *Segre embedding* is the map of [[projective spaces|ZT9A6JK8QF]]
$$\sigma \colon \mathbb{P}^m \times \mathbb{P}^n \to \mathbb{P}^N, \qquad ([x_0 : \dots : x_m], [y_0 : \dots : y_n]) \mapsto [x_i y_j]_{i, j}.$$

Check that it is well defined: scaling $x$ by $\lambda$ and $y$ by $\mu$ scales every $x_i y_j$ by $\lambda \mu \ne 0$, and some $x_i y_j$ is nonzero.

Check that it is injective: the matrix $(x_i y_j)$ is the outer product $x y^T$, of rank $1$.
Its nonzero rows are multiples of $y$ and its nonzero columns are multiples of $x$, so the point determines $[x]$ and $[y]$.

The image is the set of $[z]$ whose $(m+1) \times (n+1)$ matrix $(z_{ij})$ has rank $1$, that is, the zero set of the [[homogeneous polynomials|2C3PAQ7H50]]
$$z_{ij} z_{kl} - z_{il} z_{kj}.$$
This image is [[irreducible|SY2MWC434Z]], so it is a [[projective variety|A4H4CZ2V35]], and it is used to make $\mathbb{P}^m \times \mathbb{P}^n$ into a projective variety of dimension $m + n$.

For $m = n = 1$, the image is the quadric surface $z_{00} z_{11} - z_{01} z_{10} = 0$ in $\mathbb{P}^3$.
The fibres $\sigma(\set{a} \times \mathbb{P}^1)$ and $\sigma(\mathbb{P}^1 \times \set{b})$ are two families of lines on this surface.

## Explanations

### L1 human

A pair of points, one in each projective space, is turned into one point by multiplying all coordinates of the first with all coordinates of the second.
The result is a matrix of rank one, read as a single list of coordinates.
So the product of two projective spaces becomes a subset of a bigger projective space, cut out by the vanishing of all $2 \times 2$ minors.
For two projective lines, this gives the familiar saddle-shaped quadric surface, which is covered by two families of straight lines.
