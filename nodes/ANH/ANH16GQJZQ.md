---
tag: ANH16GQJZQ
kind: concept
name: Tensor product of fields
msc: [12F99, 15A69]
sources:
  - url: https://en.wikipedia.org/wiki/Tensor_product_of_fields
same_as:
  wikidata: Q340145
  wikipedia: Tensor product of fields
---

## Summary

Let $E$ and $F$ be extensions of a field $K$.
Their tensor product $E \otimes_K F$ is the [[tensor product of vector spaces|0BF2DE2SYK]] over $K$, with the product $(a \otimes b)(c \otimes d) = ac \otimes bd$.
It is usually not a field.
Each way to put $E$ and $F$ inside one field gives a quotient of $E \otimes_K F$ by a prime ideal.
The field of fractions of this quotient is the [[compositum|T1S29NN8PE]], so the tensor product records all these ways at once.
For a finite separable extension $E = K(\alpha)$ it is a product of fields, one for each irreducible factor over $F$ of the minimal polynomial of $\alpha$.

## Explanations

### L1 human

Given two extensions of $K$, there may be several ways to fit them together in a larger field.
The tensor product keeps track of all of them at once.
For example, $\C \otimes_\R \C$ is isomorphic to $\C \times \C$.
The two factors correspond to the two ways of identifying the second copy of $\C$ with the first: the identity and complex conjugation.
