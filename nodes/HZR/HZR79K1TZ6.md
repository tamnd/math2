---
tag: HZR79K1TZ6
kind: example
name: The exchange matrix has no LU decomposition
msc: ["15A23"]
topics: [P8J6QR66TJ]
audience: ug1
not_instance_of:
  - target: 0RKG5YW66Y
    note: the matrix is invertible, but its entry (1, 1) is 0, so no unit lower triangular L and upper triangular U give A = LU
uses: [0RKG5YW66Y, 3PPBWG0B96, 08SP3DF8NB]
sources:
  - url: https://en.wikipedia.org/wiki/LU_decomposition
    locator: Existence and uniqueness
---

## Example

The smallest invertible matrix without an LU decomposition is the $2 \times 2$ exchange matrix, and the obstruction is only the order of its rows.
Let $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, and suppose that $A = LU$ with $L = \begin{pmatrix} 1 & 0 \\ \ell & 1 \end{pmatrix}$ and $U = \begin{pmatrix} p & q \\ 0 & r \end{pmatrix}$.
Multiplying out gives
$$LU = \begin{pmatrix} p & q \\ \ell p & \ell q + r \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.$$
Entry $(1, 1)$ forces $p = 0$, and then entry $(2, 1)$ says $\ell \cdot 0 = 1$, which is false.
So $A$ has no [[LU decomposition|0RKG5YW66Y]].

The matrix $A$ is invertible, because $A \cdot A = I_2$.
Its leading principal minor is $\Delta_1 = 0$, so this agrees with the theorem on [[existence of the LU decomposition|3PPBWG0B96]].
With the [[permutation matrix|08SP3DF8NB]] $P = A$, we get $PA = I_2 = I_2 \cdot I_2$, which is a factorization $PA = LU$.

## Remarks

### No triangular factors at all

The same argument shows more: $A$ has no factorization $A = LU$ with any lower triangular $L$ and upper triangular $U$, unit or not.
Entry $(1, 1)$ gives $\ell_{11} u_{11} = 0$, while entry $(1, 2)$ gives $\ell_{11} u_{12} = 1$ and entry $(2, 1)$ gives $\ell_{21} u_{11} = 1$.
So $\ell_{11} \ne 0$ and $u_{11} \ne 0$, which contradicts $\ell_{11} u_{11} = 0$.

### Watch out

The factorization $A = UL$, with the factors in the other order, fails for this $A$ too, but for a different reason: the zero in position $(2, 2)$.
Indeed, with $U$ upper and $L$ lower triangular, entry $(2, 2)$ of $UL$ is $u_{22} \ell_{22}$, while entries $(2, 1)$ and $(1, 2)$ need $u_{22} \ell_{21} = 1$ and $u_{12} \ell_{22} = 1$, so the same contradiction appears.
A matrix such as $\begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ shows the difference: it has no factorization $A = LU$, since $\Delta_1 = 0$, but it equals $\begin{pmatrix} -1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.
Check: the product is $\begin{pmatrix} -1 + 1 & 1 \\ 1 & 1 \end{pmatrix}$.

## Explanations

### L1 human

Elimination needs a nonzero number in the top left corner to start.
Here that number is $0$, and nothing below can be subtracted to fix it.
A row swap fixes the problem at once.

### L2 human

The failure does not come from singularity: $A$ is its own inverse.
It comes only from the order of the rows.
This is why software computes $PA = LU$ and not $A = LU$.
