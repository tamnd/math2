---
tag: NG2J180CHP
kind: definition
name: Reductive Lie algebra
msc: [17B20, 17B05]
defines: T4S70DDW0A
uses: [5JJYBJ6A8K, 54XSPNAM1J, JWMTXQ8A3A, EY9DN7QAX1, JJ9WQWCP9G, G8FEGYDSNE, 1ZB13N78XW, 0ACX5QT8TE]
sources:
  - url: https://en.wikipedia.org/wiki/Reductive_Lie_algebra
---

## Definition

Let $k$ be a field of [[characteristic|1ZB13N78XW]] $0$, and let $\mathfrak g$ be a finite-dimensional [[Lie algebra|5JJYBJ6A8K]] over $k$.
The Lie algebra $\mathfrak g$ is *reductive* if its [[adjoint representation|54XSPNAM1J]] is completely reducible.
That is, every [[ideal|JWMTXQ8A3A]] $\mathfrak a$ of $\mathfrak g$ has a complementary ideal $\mathfrak b$, with $\mathfrak g = \mathfrak a \oplus \mathfrak b$ as vector spaces.

## Remarks

The ideals of $\mathfrak g$ are exactly the subspaces that are [[invariant|0ACX5QT8TE]] under the adjoint representation.
Equivalent conditions, with $\mathfrak z$ the [[center|JJ9WQWCP9G]] of $\mathfrak g$:

1. $\mathfrak g = \mathfrak z \oplus [\mathfrak g, \mathfrak g]$ and $[\mathfrak g, \mathfrak g]$ is [[semisimple|EY9DN7QAX1]];
2. $\mathfrak g$ is the direct sum of an abelian ideal and a semisimple ideal;
3. the radical of $\mathfrak g$ equals $\mathfrak z$.

Example: the [[general linear Lie algebra|G8FEGYDSNE]] $\mathfrak{gl}_n(k)$.
It is the direct sum of the ideal $kI$ of scalar matrices, which is its center, and the semisimple ideal $\mathfrak{sl}_n(k)$, so condition 2 holds.

Non-example: the two-dimensional Lie algebra with basis $x, y$ and $[x, y] = y$.
The line $ky$ is an ideal.
A complementary line is spanned by some $x + cy$, and $[y, x + cy] = -y$ does not lie in it, so it is not an ideal.
Hence the adjoint representation is not completely reducible.
