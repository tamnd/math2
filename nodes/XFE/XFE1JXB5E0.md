---
tag: XFE1JXB5E0
kind: proof
name: Proof of the vector calculus identities
msc: ["26B12"]
proves: 0JC5X4HWR2
uses: [0NS2QYVC4Y, 02NSMQVQWK, 0GDNHS9J2X, 0XQ2ZVN1PZ, 0SEDGXG9S3, 0V9A43H7WV, 0TCBZMEYGN, 0KXSK8TEEB, 0NNQY8WCW6, 0M2JRW1J0N, 0F56CMMC5P, 05RCT1522R, 02RSXVM1ZN]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_calculus_identities
    locator: Product rule for multiplication by a scalar
---

## Proof

We compute each identity in coordinates.

1. Write $(x_1, x_2, x_3)$ for $(x, y, z)$, $\partial_i = \partial / \partial x_i$, and $A = (A_1, A_2, A_3)$. For a function $g$, $\partial_i \partial_j g$ is the [[second partial derivative|02RSXVM1ZN]] $\partial_i (\partial_j g)$.
2. A function on $U$ of [[class $C^1$|0TCBZMEYGN]] is differentiable by [[continuous partial derivatives imply differentiability|0KXSK8TEEB]]. So its [[gradient|0NS2QYVC4Y]] is $(\partial_1 g, \partial_2 g, \partial_3 g)$.
3. Let $\phi, \psi, A$ be $C^1$. A partial derivative $\partial_i$ at a point is the derivative of a function of one variable on an open interval. So the [[product rule|0V9A43H7WV]] gives $\partial_i (\phi \psi) = \phi \, \partial_i \psi + \psi \, \partial_i \phi$ and $\partial_i (\psi A_k) = \psi \, \partial_i A_k + A_k \, \partial_i \psi$.
4. The right sides in step 3 are continuous, so $\phi \psi$ and $\psi A$ are $C^1$. By step 2, the $i$-th component of $\nabla (\phi \psi)$ is $\phi \, \partial_i \psi + \psi \, \partial_i \phi$. So $\nabla (\phi \psi) = \phi \nabla \psi + \psi \nabla \phi$.
5. By the definition of the [[divergence|02NSMQVQWK]] and step 3, $\nabla \cdot (\psi A) = \sum_i \partial_i (\psi A_i) = \psi \sum_i \partial_i A_i + \sum_i A_i \, \partial_i \psi = \psi \, \nabla \cdot A + \nabla \psi \cdot A$.
6. By the definition of the [[curl|0GDNHS9J2X]] and step 3, the first component of $\nabla \times (\psi A)$ is $\partial_2 (\psi A_3) - \partial_3 (\psi A_2) = \psi (\partial_2 A_3 - \partial_3 A_2) + (\partial_2 \psi \, A_3 - \partial_3 \psi \, A_2)$.
7. The second component is $\partial_3 (\psi A_1) - \partial_1 (\psi A_3) = \psi (\partial_3 A_1 - \partial_1 A_3) + (\partial_3 \psi \, A_1 - \partial_1 \psi \, A_3)$.
8. The third component is $\partial_1 (\psi A_2) - \partial_2 (\psi A_1) = \psi (\partial_1 A_2 - \partial_2 A_1) + (\partial_1 \psi \, A_2 - \partial_2 \psi \, A_1)$.
9. In steps 6 to 8, the first brackets are the components of $\nabla \times A$. By the definition of the [[cross product|0SEDGXG9S3]], the second brackets are the components of $\nabla \psi \times A$. So $\nabla \times (\psi A) = \psi \, \nabla \times A + \nabla \psi \times A$.
10. Now let $\phi$ and $A$ be $C^2$. Then $\nabla \times (\nabla \phi) = 0$, because the [[curl of a gradient is zero|0M2JRW1J0N]].
11. Also $\nabla \cdot (\nabla \times A) = 0$, because the [[divergence of a curl is zero|0F56CMMC5P]].
12. Let $B = \nabla \times A$, so $B = (\partial_2 A_3 - \partial_3 A_2, \ \partial_3 A_1 - \partial_1 A_3, \ \partial_1 A_2 - \partial_2 A_1)$, a $C^1$ field. The first component of $\nabla \times B$ is $\partial_2 B_3 - \partial_3 B_2 = \partial_2 \partial_1 A_2 + \partial_3 \partial_1 A_3 - \partial_2 \partial_2 A_1 - \partial_3 \partial_3 A_1$.
13. The second component is $\partial_3 B_1 - \partial_1 B_3 = \partial_3 \partial_2 A_3 + \partial_1 \partial_2 A_1 - \partial_3 \partial_3 A_2 - \partial_1 \partial_1 A_2$.
14. The third component is $\partial_1 B_2 - \partial_2 B_1 = \partial_1 \partial_3 A_1 + \partial_2 \partial_3 A_2 - \partial_1 \partial_1 A_3 - \partial_2 \partial_2 A_3$.
15. Each $A_k$ is $C^2$, hence twice differentiable. By the formula for the [[Laplacian|0XQ2ZVN1PZ]] as a [[sum of second partial derivatives|05RCT1522R]], $\Delta A_k = \partial_1 \partial_1 A_k + \partial_2 \partial_2 A_k + \partial_3 \partial_3 A_k$.
16. The function $\nabla \cdot A = \partial_1 A_1 + \partial_2 A_2 + \partial_3 A_3$ is $C^1$. So the $k$-th component of $\nabla (\nabla \cdot A) - \Delta A$ is $\sum_{j \ne k} \partial_k \partial_j A_j - \sum_{j \ne k} \partial_j \partial_j A_k$, since the terms $\partial_k \partial_k A_k$ cancel.
17. For $k = 1, 2, 3$, step 16 agrees with steps 12, 13 and 14, once each $\partial_j \partial_k A_j$ there is replaced by $\partial_k \partial_j A_j$. This is allowed by [[Schwarz's theorem|0NNQY8WCW6]], since $A_j$ is $C^2$.
18. Hence $\nabla \times (\nabla \times A) = \nabla (\nabla \cdot A) - \Delta A$.

## Idea

The product rules come from the one-variable product rule, applied to each partial derivative of each component. The second-order identities are bookkeeping of mixed partial derivatives. They hold because, for $C^2$ functions, the order of differentiation does not matter.
