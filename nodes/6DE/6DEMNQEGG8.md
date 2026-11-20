---
tag: 6DEMNQEGG8
kind: example
name: The product of countably many lines is not their direct sum
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
instance_of: [0EX2HPXPJ6]
not_instance_of:
  - target: 0S7W6EG32V
    note: the space of all real sequences contains (1, 1, 1, ...), which has infinitely many nonzero entries
uses: [0MM085RX00, 02WZB422CE, 0HR573CHNM]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_sum_of_modules
    locator: Construction for vector spaces and abelian groups
---

## Example

Let $V_n = \R$ for each $n \in \N$.
The [[direct product|0MM085RX00]] $\R^{\N}$ is the space of all real sequences.
The [[external direct sum|02WZB422CE]] $\R^{(\N)}$ is the subspace of sequences with finitely many nonzero terms.
We check that they are different.

1. The sequence $s = (1, 1, 1, \dots)$ has every entry in $\R$, so $s \in \R^{\N}$.
2. Every entry of $s$ is nonzero, so $s$ has infinitely many nonzero entries, and $s \notin \R^{(\N)}$.
3. So $\R^{(\N)} \ne \R^{\N}$.
4. The unit sequences $e_n$, with $1$ in place $n$ and $0$ elsewhere, lie in both spaces. Their [[span|0HR573CHNM]] is the set of finite linear combinations, which is exactly $\R^{(\N)}$.
5. So the unit sequences are a basis of the direct sum, but they do not span the product: $s$ is not a finite combination of them.

## Remarks

The product $\R^{\N}$ does have a basis, by Zorn's lemma, but no explicit basis is known, and its dimension is uncountable.
For finitely many factors, the product and the direct sum coincide, so the difference appears only for infinite families.

## Explanations

### L1 human

The direct sum allows only lists that end with zeros.
The product allows every list, such as the list of all ones.

### L2 human

A common mistake is to write $s = \sum_{n} e_n$ and conclude that the unit sequences span $\R^{\N}$.
In a vector space without a topology, only finite sums are defined, so this infinite sum has no meaning.
