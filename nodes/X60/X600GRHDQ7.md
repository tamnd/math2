---
tag: X600GRHDQ7
kind: definition
name: Givens rotation
msc: [65F25, 15A23]
defines: NM1KPS6E7Y
uses: [0XNZWJ96HK, 0QRBVFJ50X, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Givens_rotation
---

## Definition

Let $n \ge 2$, let $1 \le i < j \le n$, and let $c, s$ be real numbers with $c^2 + s^2 = 1$.
The *Givens rotation* $G(i, j; c, s)$ is the $n \times n$ real matrix that agrees with the [[identity matrix|06DW9BAWB1]] except in the four entries
$$g_{ii} = c, \qquad g_{ij} = -s, \qquad g_{ji} = s, \qquad g_{jj} = c.$$
Writing $c = \cos\theta$ and $s = \sin\theta$, it is the [[rotation|0XNZWJ96HK]] by the angle $\theta$ in the plane of the coordinates $i$ and $j$.

## Remarks

$G = G(i, j; c, s)$ is an [[orthogonal matrix|0QRBVFJ50X]] with determinant $c^2 + s^2 = 1$.
For $x \in \R^n$, the product $G x$ changes only the entries $i$ and $j$: $(Gx)_i = c x_i - s x_j$ and $(Gx)_j = s x_i + c x_j$.
If $(x_i, x_j) \ne (0, 0)$, put $r = \sqrt{x_i^2 + x_j^2}$, $c = x_i / r$ and $s = -x_j / r$; then $(Gx)_i = r$ and $(Gx)_j = 0$.
Example: for $x = (3, 4)$ in $\R^2$, $r = 5$, $c = 3/5$, $s = -4/5$, and $G x = (9/5 + 16/5, \ -12/5 + 12/5) = (5, 0)$.
Non-example: the matrix with $c = s = 1$ in these four places is not a Givens rotation, since $c^2 + s^2 = 2$, and it is not orthogonal.
Other books put $-s$ in position $(j, i)$ instead; the two conventions differ by the sign of $\theta$.

## Explanations

### L1 human

A Givens rotation turns a vector inside the plane of two coordinate axes and does nothing to the other coordinates.
Its matrix is the identity with a $2 \times 2$ rotation block written into rows and columns $i$ and $j$.
The angle can be chosen so that one of the two entries becomes zero.
