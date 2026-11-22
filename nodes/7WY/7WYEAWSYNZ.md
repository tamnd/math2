---
tag: 7WYEAWSYNZ
kind: example
name: The union of two eigenspaces is not a subspace
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
not_instance_of:
  - target: 0G0RFPG8HR
    note: The union of the eigenspaces of diag(1, 2) is not closed under addition, so it is not an eigenspace and not a subspace
uses: [0AYEPBQMAW, 0B5H4208Z9]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenspaces, geometric multiplicities, and eigenbasis for a matrix
---

## Example

Let $A = \operatorname{diag}(1, 2)$ over $\mathbb{R}$, so that $A(x, y) = (x, 2y)$.
Its [[eigenspaces|0AYEPBQMAW]] are the two axes, $E_1 = \operatorname{span}\{e_1\}$ and $E_2 = \operatorname{span}\{e_2\}$.
Let $U = E_1 \cup E_2$, the set of all [[eigenvectors|0B5H4208Z9]] of $A$ together with $0$.
We show that $U$ is not a subspace of $\mathbb{R}^2$.

1. We have $Ae_1 = e_1$ and $Ae_2 = 2e_2$, so $e_1 \in E_1 \subseteq U$ and $e_2 \in E_2 \subseteq U$.
2. Their sum is $e_1 + e_2 = (1, 1)$, and
$$A(1, 1) = (1, 2).$$
3. The vector $(1, 2)$ is not a multiple of $(1, 1)$, because its two entries differ.
   So $(1, 1)$ is not an eigenvector, and $(1, 1) \notin U$.
4. So $U$ is not closed under addition, and it is not a subspace.

## Remarks

Each single eigenspace $E_\lambda = \ker(A - \lambda I)$ is a subspace, because it is a kernel.
The failure comes only from joining two of them.
The right way to combine eigenspaces is the sum $E_1 + E_2 = \{ u + w : u \in E_1, w \in E_2 \}$, which is a subspace, here all of $\mathbb{R}^2$.
This sum is direct, because eigenvectors with distinct eigenvalues are linearly independent.

Change $A$ to $2I$, so that both diagonal entries agree.
Then $E_2$ is the whole plane, and the union of the eigenspaces is a subspace.
So the union fails to be a subspace exactly because two different eigenvalues each have their own line.

## Explanations

### L1 human

The eigenvectors for $1$ lie on the horizontal axis, and those for $2$ lie on the vertical axis.
Adding one arrow from each axis gives an arrow that points between the axes.
The map stretches its two parts by different amounts, so the new arrow gets turned, and it is not an eigenvector.

### L2 human

The lesson is to use the sum of eigenspaces, not their union.
Watch out: for a matrix with several eigenvalues, "the set of all eigenvectors" is not a subspace, so it has no dimension and no basis.
Each eigenspace has a basis, and joining these bases gives an independent set, which is the start of diagonalization.
