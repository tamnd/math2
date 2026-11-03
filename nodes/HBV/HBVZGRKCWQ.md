---
tag: HBVZGRKCWQ
kind: example
name: Heisenberg algebra
msc: [17B30, 17B81]
instance_of: [5JJYBJ6A8K]
uses: [G8FEGYDSNE, JJ9WQWCP9G, ZZYCV5EX9J]
sources:
  - url: https://en.wikipedia.org/wiki/Heisenberg_group
---

## Example

Let $k$ be a field.
The three-dimensional *Heisenberg algebra* $\mathfrak h_3$ over $k$ has a basis $x, y, z$ with
$$[x, y] = z, \quad [x, z] = 0, \quad [y, z] = 0.$$
A concrete model is the space of strictly upper triangular $3 \times 3$ matrices in the [[general linear Lie algebra|G8FEGYDSNE]] $\mathfrak{gl}_3(k)$, with
$$x = E_{12}, \quad y = E_{23}, \quad z = E_{13}.$$
Check: $E_{12} E_{23} = E_{13}$ and $E_{23} E_{12} = 0$, so $[x, y] = z$.
Also $E_{13}$ has zero product with $E_{12}$ and $E_{23}$ in both orders, so $[x, z] = [y, z] = 0$.
Since the model is a subspace of $\mathfrak{gl}_3(k)$ closed under brackets, $\mathfrak h_3$ is a Lie algebra.

## Remarks

The [[center|JJ9WQWCP9G]] of $\mathfrak h_3$ is the line $k z$, and $[\mathfrak h_3, \mathfrak h_3] = k z$.
So $\mathfrak h_3$ is nilpotent but not abelian.
More generally, $\mathfrak h_{2n+1}$ has basis $x_1, \dots, x_n, y_1, \dots, y_n, z$ with $[x_i, y_j] = \delta_{ij} z$ and all other brackets of basis elements zero.
For $k = \R$ it is the Lie algebra of the [[Heisenberg group|ZZYCV5EX9J]].
The canonical commutation relation $[\hat q, \hat p] = i\hbar$ of quantum mechanics has the form $[x, y] = z$, with $z$ acting as the scalar $i\hbar$.

## Explanations

### L1 human

The Heisenberg algebra is the simplest Lie algebra that is not abelian but almost is.
Two generators $x$ and $y$ fail to commute, and their bracket $z$ commutes with everything.
It encodes the relation between position and momentum in quantum mechanics.
It can be seen as $3 \times 3$ upper triangular matrices with zeros on the diagonal.
