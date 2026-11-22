---
tag: R304WJSMWX
kind: example
name: The matrices with determinant plus or minus one are not the orthogonal group
msc: ["15B10", "20G20"]
topics: [AZS5BPF5H3]
audience: ug2
not_instance_of:
  - target: WWK2E8BRGF
    note: the group contains the shear with rows (1, 1) and (0, 1), which has determinant 1 but is not an orthogonal matrix
uses: [0QRBVFJ50X, 0C3CFHDN6R, 0N0PXCTYA7]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: lead section
---

## Example

Let $G = \{ A \in M_2(\R) : \det A = 1 \text{ or } \det A = -1 \}$, with matrix multiplication.
We show that $G$ is a group and that it is strictly larger than the [[orthogonal group|WWK2E8BRGF]] $O(2)$.

1. The set $G$ is a group, by the product rule for determinants: $\det I_2 = 1$, $\det(AB) = \det A \det B = \pm 1$ and $\det(A^{-1}) = (\det A)^{-1} = \pm 1$.
2. The group $G$ contains $O(2)$, because every orthogonal matrix has [[determinant 1 or -1|QDZJMFATRW]].
3. Let $S$ be the shear
$$S = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad \det S = 1 \cdot 1 - 1 \cdot 0 = 1,$$
so $S \in G$.
4. Compute $S^{\mathsf{T}} S$:
$$S^{\mathsf{T}} S = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \ne I_2.$$
5. So $S$ is not [[orthogonal|0QRBVFJ50X]], and $S \in G$ but $S \notin O(2)$.
6. Check with one length: $S$ sends $(0, 1)$, of length $1$, to $(1, 1)$, of length $\sqrt{2}$.

## Remarks

The example shows what the condition $\det A = \pm 1$ keeps and what it does not keep.
It keeps areas, since $\lvert \det A \rvert$ is the area factor, but it does not keep lengths.

The two groups also differ in size.
The powers of the shear are
$$S^k = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix},$$
and their entries grow without bound, so $G$ is not compact, while every entry of an orthogonal matrix lies in $[-1, 1]$.
A shear $\begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}$ is orthogonal only for $t = 0$, because its second column $(t, 1)$ has length $\sqrt{t^2 + 1}$.
In the same way, the special linear group $SL_2(\R)$ of matrices with determinant $1$ is strictly larger than $SO(2)$.

## Explanations

### L1 human

A shear slides the top edge of a square sideways, and the square becomes a slanted parallelogram.
The area stays the same, but the slanted sides are longer than before.
So the shear does not keep lengths, and it is not in the orthogonal group.
Keeping areas is a weaker property than keeping lengths.

### L2 human

The typical way to show that a matrix is not orthogonal is to find one vector whose length changes.
For the shear one vector is enough: $(0, 1)$ goes to $(1, 1)$, and $1 \ne \sqrt{2}$.
Watch out: determinant $1$ does not make a matrix a rotation.
It says only that areas and orientation stay the same, and a rotation needs orthogonality as well.
