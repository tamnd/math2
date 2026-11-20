---
tag: V9MKVNQ207
kind: example
name: The identity matrix is a sum of matrix units, not a matrix unit
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
not_instance_of:
  - target: A4HTT7JFD1
    note: I_2 = E_11 + E_22 has two entries equal to 1, while a matrix unit has exactly one nonzero entry
uses: [4H93XF4RVH, 6NHZRCKJNW]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_unit
    locator: lead section
---

## Example

Let $I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, the [[identity matrix|6NHZRCKJNW]].

1. A [[matrix unit|4H93XF4RVH]] $E_{ij}$ has exactly one nonzero entry, the entry $1$ at $(i, j)$.
2. $I_2$ has two nonzero entries, at $(1, 1)$ and at $(2, 2)$.
3. So $I_2$ is not equal to any of $E_{11}$, $E_{12}$, $E_{21}$ and $E_{22}$.
4. But $E_{11} + E_{22} = \begin{pmatrix} 1 + 0 & 0 + 0 \\ 0 + 0 & 0 + 1 \end{pmatrix} = I_2$.

## Remarks

The identity is a unit of the ring $M_2(R)$, since it is invertible, but it is not a matrix unit.
Conversely, no matrix unit is a unit of $M_n(R)$ for $n \ge 2$, because each has a zero row.
The decomposition $I_n = E_{11} + \dots + E_{nn}$ splits $I_n$ into $n$ idempotents with pairwise products $0$.

## Explanations

### L1 human

The identity matrix has a $1$ in two places, so it is not a matrix unit.
It is the sum of the two diagonal matrix units.

### L2 human

The words "unit" in "matrix unit" and in "unit of a ring" have different meanings.
This example separates them.
