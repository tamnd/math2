---
tag: 0JC5X4HWR2
kind: statement
role: theorem
name: Vector calculus identities
aliases: [product-rules-for-grad-div-curl]
msc: [26B12]
uses: [0NS2QYVC4Y, 02NSMQVQWK, 0GDNHS9J2X, 0XQ2ZVN1PZ, 0H6DP8CHND, 0M2JRW1J0N, 0F56CMMC5P]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_calculus_identities
    locator: Product rule for multiplication by a scalar
  - url: https://en.wikipedia.org/wiki/Vector_calculus_identities
    locator: Second derivative identities
  - url: https://en.wikipedia.org/wiki/Vector_calculus_identities
    locator: Curl of curl
same_as:
  wikidata: Q1066266
  wikipedia: Vector calculus identities
---

## Statement

Let $U \subseteq \mathbb{R}^3$ be open, let $\phi, \psi \colon U \to \mathbb{R}$ be scalar fields, and let $A \colon U \to \mathbb{R}^3$ be a vector field.
If these fields are of class $C^1$, then
$$\nabla (\phi \psi) = \phi \nabla \psi + \psi \nabla \phi, \qquad \nabla \cdot (\psi A) = \psi \, \nabla \cdot A + \nabla \psi \cdot A, \qquad \nabla \times (\psi A) = \psi \, \nabla \times A + \nabla \psi \times A.$$
If these fields are of class $C^2$, then
$$\nabla \times (\nabla \phi) = 0, \qquad \nabla \cdot (\nabla \times A) = 0, \qquad \nabla \times (\nabla \times A) = \nabla (\nabla \cdot A) - \Delta A,$$
where $\Delta A$ applies the Laplacian to each component of $A$.

## Remarks

Here $\nabla \phi$ is the [[gradient|0NS2QYVC4Y]], $\nabla \cdot A$ the [[divergence|02NSMQVQWK]], $\nabla \times A$ the [[curl|0GDNHS9J2X]], and $\Delta$ the [[Laplacian|0XQ2ZVN1PZ]].
The product rules follow from the product rule for partial derivatives, applied to each component.
The identities [[curl of a gradient is zero|0M2JRW1J0N]] and [[divergence of a curl is zero|0F56CMMC5P]] follow from the symmetry of second derivatives.
Also, $\nabla \cdot (\nabla \phi) = \Delta \phi$ and $\Delta (\phi \psi) = \phi \Delta \psi + 2 \nabla \phi \cdot \nabla \psi + \psi \Delta \phi$.

## Explanations

### L1 human

These identities are the algebra rules of vector calculus.
They let you expand derivatives of products and simplify repeated derivatives, the way the ordinary product rule does in one variable.
