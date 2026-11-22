---
tag: 9K7FFF26QR
kind: topic
name: Dual spaces and duality
msc: ["15A03", "15A04"]
topics: [GN8GYSDZFX]
---

## Summary

This topic is a part of [[linear algebra|GN8GYSDZFX]], and it studies the linear forms on a vector space, the maps that turn a vector into one number.
It starts with familiar examples: a row vector acting on columns, the value of a polynomial at a point, an integral and the trace.
A nonzero form is fixed by its kernel up to a scalar, and these kernels are exactly the hyperplanes.
All the forms on $V$ make up a new vector space, the dual space $V^*$, and each basis of $V$ gives a dual basis of coordinate forms.
In finite dimension this shows $\dim V^* = \dim V$, but the resulting isomorphism $V \cong V^*$ depends on the basis.
In infinite dimension the dual is strictly bigger, and the Erdős-Kaplansky theorem gives its exact dimension.
The double dual behaves better: evaluation gives a map $V \to V^{**}$ that needs no choices, and it is an isomorphism exactly when $V$ is finite-dimensional.
The forms that vanish on a subspace form its annihilator, and the dimensions of a subspace and of its annihilator add up to $\dim V$.
Every linear map $f$ has a dual map $f^*$ that goes the other way, and in dual bases its matrix is the transpose.
The topic ends with the kernel and the image of $f^*$, which give a proof that the row rank of a matrix equals its column rank.
Later topics build on this one, such as bilinear forms, inner product spaces through the Riesz representation theorem, and tensor products.

## Remarks

### Reading order

1. [[Linear form|07YQ1C78G0]]: you meet the maps $V \to F$ and learn to write each one as a row of numbers.
2. [[Hyperplanes and linear forms|XR0EQN0H8T]]: you see that a nonzero form is fixed by its kernel up to a scalar, and that these kernels are the hyperplanes.
3. [[Dual space|07JBSZE0V4]]: you learn that the forms on $V$ make up a vector space $V^*$ of their own.
4. [[Dual basis|0ZD2CF6ZS0]]: you compute the coordinate forms of a basis and see why the isomorphism $V \cong V^*$ that they give depends on the basis.
5. [[Dimension of the dual space|00889YD15K]]: you prove $\dim V^* = \dim V$ in finite dimension and see the dual basis fail to span in infinite dimension.
6. [[Erdős-Kaplansky theorem|S5ET1HG2ZX]]: you find the exact dimension $\abs{F}^{\dim V}$ of $V^*$ when $V$ is infinite-dimensional.
7. [[Canonical isomorphism with the double dual|0ZJM9D7NPS]]: you meet the evaluation map $V \to V^{**}$, which needs no choices and is an isomorphism exactly in finite dimension.
8. [[Annihilator|0ASHNYF7AG]]: you study the forms that vanish on a subspace and see that taking annihilators reverses inclusions.
9. [[Dimension of the annihilator|06Q1EFVH0Q]]: you prove $\dim U + \dim U^0 = \dim V$ and identify the duals of quotients and subspaces.
10. [[Dual map|0AZ5ARP287]]: you learn how a linear map $f$ pulls forms back by $f^*(\varphi) = \varphi \circ f$, in the opposite direction.
11. [[Matrix of the dual map is the transpose|0ZPB3180AY]]: you see that the transpose of a matrix is the matrix of the dual map in dual bases.
12. [[Kernel and image of the dual map|7FA499AW3T]]: you prove $\ker f^* = (\im f)^0$ and $\im f^* = (\ker f)^0$, and you get a second proof that row rank equals column rank.

### Prerequisites

- [[Vector spaces, span, independence, bases and dimension|MVH97H8B2J]]: bases, dimension and the extension of independent sets.
- [[Matrices and the operations on them|Y1ESNQ2V52]]: matrix products and the transpose.
- [[Linear maps|9080WQTZ3M]]: kernel, image, rank-nullity and the space $\Hom(V, W)$.
- [[Direct sums, complements and quotient spaces|QHKTJ89V6S]]: quotient spaces, used for the duals of quotients.
- [[Matrices of linear maps, rank and change of basis|S6559D61BP]]: the matrix of a linear map and the change of basis matrix.
