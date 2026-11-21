---
tag: A6P6MMDQBF
kind: example
name: Matrices with the same column space that are not row equivalent
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
not_instance_of:
  - target: 006BHFWMAP
    note: the two matrices have the same column space but different null spaces, so they are not row equivalent
uses: [095DDGZF16, E4GKK727ZM, 03AJKXH1AV, 0PHDYNR24D]
sources:
  - url: https://en.wikipedia.org/wiki/Row_equivalence
    locator: lead section
---

## Example

The column space is not what row operations keep, so equal column spaces prove nothing.
Let
$$P = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \qquad Q = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$$
over $\mathbb{R}$.

1. The columns of $P$ are $e_1$ and $0$, so its [[column space|03AJKXH1AV]] is the span of $e_1$.
2. The columns of $Q$ are $0$ and $e_1$, so its column space is also the span of $e_1$.
3. The equation $Px = 0$ means $x_1 = 0$, so the [[null space|0PHDYNR24D]] of $P$ is the span of $e_2$.
4. The equation $Qx = 0$ means $x_2 = 0$, so the null space of $Q$ is the span of $e_1$.
5. The null spaces differ. Row equivalent matrices have the same null space, by the [[theorem on row equivalence|E4GKK727ZM]], so $P$ and $Q$ are not [[row equivalent|095DDGZF16]].

## Remarks

There is a second proof.
Both matrices are already in reduced row echelon form, and they are different, so by the uniqueness of the RREF they are not row equivalent.

The row spaces differ as well: they are the spans of $(1, 0)$ and of $(0, 1)$.
A column operation, not a row operation, turns $P$ into $Q$: swap the two columns.

## Explanations

### L1 human

Row moves keep the solutions of the equations.
The equation $x_1 = 0$ and the equation $x_2 = 0$ have different solutions.
So no row moves can turn one table into the other, even though both tables use the same column vector.

### L2 human

1. To show that two matrices are not row equivalent, find one invariant that differs.
2. Good invariants are the null space, the row space, the rank and the RREF.
3. The column space is not an invariant of row operations, so it cannot prove row equivalence.

Watch out: equal column spaces do not give row equivalence, and row equivalence does not give equal column spaces.
