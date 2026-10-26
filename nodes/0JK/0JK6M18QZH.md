---
tag: 0JK6M18QZH
kind: definition
name: Kronecker product
msc: [15A69]
defines: 0N7ENQRCXN
uses: [0N1MY1T0W9, 01AXG9KZQF]
sources:
  - url: https://en.wikipedia.org/wiki/Kronecker_product
    locator: Definition
---

## Definition

Let $F$ be a field, let $A = (a_{ij})$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] over $F$, and let $B$ be a $p \times q$ matrix over $F$.
The *Kronecker product* $A \otimes B$ is the $mp \times nq$ [[block matrix|0ASDFEQS6P]]
$$A \otimes B = \begin{pmatrix} a_{11} B & \cdots & a_{1n} B \\ \vdots & \ddots & \vdots \\ a_{m1} B & \cdots & a_{mn} B \end{pmatrix}.$$

## Remarks

It satisfies $(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$ when the products $AC$ and $BD$ are defined.
If $A$ and $B$ are invertible, then $(A \otimes B)^{-1} = A^{-1} \otimes B^{-1}$.
It is not commutative in general, but $A \otimes B$ and $B \otimes A$ are permutation equivalent.
It is the matrix of the tensor product of two linear maps, in the tensor product bases ordered suitably.

## Explanations

### L1 human

The Kronecker product replaces each entry of $A$ with that entry times the whole matrix $B$.
For example, $I_2 \otimes B$ is the block diagonal matrix with two copies of $B$.
It is the matrix form of the tensor product.
