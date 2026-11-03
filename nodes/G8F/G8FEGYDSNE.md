---
tag: G8FEGYDSNE
kind: example
name: General linear Lie algebra
msc: [17B45, 17B05, "22E60"]
instance_of: [5JJYBJ6A8K]
uses: [WCJYA7CJ83, 0VD9ZSWWJG, 0J7H0YBFDJ, 0FCHE902D7]
sources:
  - url: https://en.wikipedia.org/wiki/General_linear_group
---

## Example

Let $k$ be a field and $n \ge 1$.
The *general linear Lie algebra* $\mathfrak{gl}_n(k)$ is the vector space of all $n \times n$ [[matrices|0VD9ZSWWJG]] over $k$ with the bracket
$$[X, Y] = XY - YX.$$
It is the [[Lie algebra of the associative algebra|WCJYA7CJ83]] $M_n(k)$, so it is a [[Lie algebra|5JJYBJ6A8K]].
More generally, for a vector space $V$, $\mathfrak{gl}(V)$ is the space of linear [[endomorphisms|0J7H0YBFDJ]] of $V$ with the same bracket.

Check in a small case: in $\mathfrak{gl}_2(k)$, with the matrix units $E_{ij}$, one has $[E_{12}, E_{21}] = E_{11} - E_{22}$ and $[E_{11}, E_{12}] = E_{12}$.
In general $[E_{ij}, E_{kl}] = \delta_{jk} E_{il} - \delta_{li} E_{kj}$.
The $n^2$ matrix units form a basis, so $\dim \mathfrak{gl}_n(k) = n^2$.

## Remarks

For $k = \R$ or $\C$, $\mathfrak{gl}_n(k)$ is the Lie algebra of the [[general linear group|0FCHE902D7]] $GL_n(k)$.
Indeed $GL_n(k)$ is open in $M_n(k)$, so its tangent space at $I$ is all of $M_n(k)$.
A representation of a Lie algebra $\mathfrak g$ on $V$ is a homomorphism $\mathfrak g \to \mathfrak{gl}(V)$.
By [[Ado's theorem|33E7PK3Z71]], every finite-dimensional Lie algebra over a field of characteristic $0$ is isomorphic to a subalgebra of some $\mathfrak{gl}_n(k)$.
The center of $\mathfrak{gl}_n(k)$ is the line of scalar matrices.

## Explanations

### L1 human

Take all square matrices of a fixed size and use $XY - YX$ as the bracket.
This is the general linear Lie algebra, the model for all others.
It describes the infinitesimal changes of an invertible matrix near the identity.
Most Lie algebras met in practice sit inside it as subalgebras.
