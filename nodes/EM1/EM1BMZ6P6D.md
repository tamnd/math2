---
tag: EM1BMZ6P6D
kind: definition
name: Ray transfer matrix analysis
msc: [78A05]
defines: 9WFT4VY2R7
uses: [N111BHFQ2H, 0VD9ZSWWJG, 032Q9FB8MT, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Ray_transfer_matrix_analysis
---

## Definition

Let an optical system have an optical axis, an input plane and an output plane perpendicular to the axis.
Describe a ray at a plane by the column vector $(y, \theta)^T$.
Here $y$ is its height above the axis and $\theta$ its angle with the axis.
In the [[paraxial approximation|N111BHFQ2H]], the output ray depends linearly on the input ray:
$$\begin{pmatrix} y_2 \\ \theta_2 \end{pmatrix} = \begin{pmatrix} A & B \\ C & D \end{pmatrix} \begin{pmatrix} y_1 \\ \theta_1 \end{pmatrix}.$$
The real [[matrix|0VD9ZSWWJG]] $M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ is the *ray transfer matrix* (ABCD matrix) of the system.
*Ray transfer matrix analysis* computes $M$ as the [[product|032Q9FB8MT]] $M = M_k \cdots M_2 M_1$ of the matrices of the elements.
Here $M_1$ belongs to the element that the light meets first, and $M_k$ to the last one.

## Remarks

Basic matrices: free propagation over a distance $d$ has $\begin{pmatrix} 1 & d \\ 0 & 1 \end{pmatrix}$, and a thin lens of focal length $f$ has $\begin{pmatrix} 1 & 0 \\ -1/f & 1 \end{pmatrix}$.
The [[determinant|00KDZRW4C0]] is $\det M = n_1 / n_2$, where $n_1$ and $n_2$ are the refractive indices at the input and output planes.
With the reduced angle $n\theta$ in place of $\theta$, every ray transfer matrix has determinant $1$.

Example: free space $d$ followed by a thin lens $f$.
Check: $\begin{pmatrix} 1 & 0 \\ -1/f & 1 \end{pmatrix} \begin{pmatrix} 1 & d \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & d \\ -1/f & 1 - d/f \end{pmatrix}$, of determinant $1$.
For $d = f$ the output angle is $-y_1/f$, independent of $\theta_1$: rays from one point of the front focal plane leave parallel.

Non-example: the product written left to right in the order of travel, $M_1 M_2 \cdots M_k$, is in general a different matrix, since matrix multiplication does not commute.
It does not describe the system.
