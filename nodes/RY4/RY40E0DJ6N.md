---
tag: RY40E0DJ6N
kind: definition
name: Mueller calculus
msc: [78A10]
defines: X17R7F1QH5
uses: [1WA9ASC6NF, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Mueller_calculus
---

## Definition

Let an optical element act linearly on the [[Stokes vectors|1WA9ASC6NF]] of light, for light of a fixed frequency and direction.
Its *Mueller matrix* is the real $4 \times 4$ [[matrix|0VD9ZSWWJG]] $M$ such that the output Stokes vector is $S_{\mathrm{out}} = M S_{\mathrm{in}}$ for every input Stokes vector $S_{\mathrm{in}}$.
If light passes through elements with Mueller matrices $M_1, M_2, \dots, M_k$ in this order, the whole system has Mueller matrix $M_k \cdots M_2 M_1$.
*Mueller calculus* is the computation of polarization states with these matrices.

## Remarks

Example: an ideal linear polarizer with horizontal transmission axis has
$$M = \frac{1}{2}\begin{pmatrix} 1 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
For unpolarized light $S_{\mathrm{in}} = (1, 0, 0, 0)$, it gives $S_{\mathrm{out}} = (1/2, 1/2, 0, 0)$: half the intensity, fully polarized horizontally.

Non-example: the matrix $\mathrm{diag}(1, 2, 0, 0)$ is not the Mueller matrix of a physical element.
It sends the Stokes vector $(1, 1, 0, 0)$ to $(1, 2, 0, 0)$, which fails $S_0^2 \ge S_1^2 + S_2^2 + S_3^2$.

The ideal depolarizer has Mueller matrix $\mathrm{diag}(1, 0, 0, 0)$.
Every Jones matrix gives a Mueller matrix, but the depolarizer shows that the converse fails.
