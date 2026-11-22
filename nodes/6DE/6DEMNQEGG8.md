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
The [[external direct sum|02WZB422CE]] $\R^{(\N)}$ is the subspace of sequences with only finitely many nonzero terms.
We check that the two spaces are different, and that the unit sequences span only the smaller one.

1. The sequence $s = (1, 1, 1, \dots)$ has every entry in $\R$, so $s \in \R^{\N}$.
2. Every entry of $s$ is nonzero, so $s$ has infinitely many nonzero entries, and $s \notin \R^{(\N)}$.
3. So $\R^{(\N)} \ne \R^{\N}$.
4. Let $e_n$ be the unit sequence with $1$ in place $n$ and $0$ elsewhere.
   Each $e_n$ lies in both spaces.
5. A finite combination $c_1 e_{n_1} + \cdots + c_k e_{n_k}$ has nonzero entries only in the places $n_1, \dots, n_k$, so it lies in $\R^{(\N)}$.
   Conversely, a sequence $(a_0, a_1, \dots)$ in $\R^{(\N)}$ with $a_n = 0$ for $n > N$ equals $a_0 e_0 + \cdots + a_N e_N$.
   So the [[span|0HR573CHNM]] of the unit sequences is exactly $\R^{(\N)}$.
6. Hence the unit sequences form a basis of the direct sum, and they do not span the product, since $s$ is not a finite combination of them.

## Remarks

The example shows that the product and the direct sum part ways as soon as the family is infinite.
For finitely many factors, say $\R^k$, every sequence of length $k$ has finite support, and the two spaces coincide.

The product $\R^{\N}$ still has a basis, because [[every vector space has a basis|00MS9VMQ9Z]], but the proof uses Zorn's lemma and gives no formula for one.
Its dimension is uncountable, so no countable family, such as the unit sequences, can span it.

## Explanations

### L1 human

The direct sum allows only lists that end in zeros, such as $(5, 0, 2, 0, 0, \dots)$.
The product allows every list, such as the list of all ones.
So the product is the bigger space.

### L2 human

A common mistake is to write $s = \sum_{n} e_n$ and conclude that the unit sequences span $\R^{\N}$.
In a vector space without a topology only finite sums are defined, so this infinite sum has no meaning.
The span of a family is the set of its finite combinations, and step 5 shows that these all end in zeros.
In analysis, where sequences carry a norm or a topology, infinite sums can make sense, and that leads to the different notion of a Schauder basis.
