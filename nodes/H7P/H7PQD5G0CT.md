---
tag: H7PQD5G0CT
kind: example
name: Named lemmas that are major results
msc: ["00A35"]
topics: [N4P3E53HM0]
audience: ug1
instance_of: [KK5F0F03ZW]
uses: [KK5F0F03ZW, 04RXTQA5ZA, 0Z47M1B2VS, 051VYKA1EX, D6DF1ARPVD]
sources:
  - url: https://en.wikipedia.org/wiki/Lemma_(mathematics)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Burnside%27s_lemma
    locator: History
  - url: https://en.wikipedia.org/wiki/Zorn%27s_lemma
    locator: lead section
---

## Example

We look at four results that carry the label "lemma" and check what role each one plays today.

1. [[Euclid's lemma|051VYKA1EX]]: if a prime $p$ divides $ab$, then $p$ divides $a$ or $b$. It is Proposition 30 of Book VII of Euclid's Elements. It is the main step in the proof of unique prime factorization, and it is also used on its own in each course of number theory.
2. [[Zorn's lemma|04RXTQA5ZA]]: a nonempty partially ordered set in which each chain has an upper bound has a maximal element. Over the other axioms of set theory, it is equivalent to the axiom of choice. It proves that each vector space has a basis.
3. [[Burnside's lemma|0Z47M1B2VS]]: the number of orbits of a finite group $G$ on a finite set $X$ is $\frac{1}{|G|}\sum_{g \in G} |X^g|$. It is a main tool for counting objects up to symmetry. Burnside attributed it to Frobenius, and Cauchy knew the formula earlier.
4. [[Yoneda lemma|D6DF1ARPVD]]: in category theory, natural transformations from a representable functor $\operatorname{Hom}(A, -)$ to a functor $F$ correspond to the elements of $F(A)$. It is a basic tool of the whole subject.
5. In each case the result has a full proof, so it is a theorem in the logical sense. The word "lemma" records its origin as a tool, not its weight.

## Remarks

The example shows that the label of a result does not measure its importance.
A result keeps the name that it received first, even when later work makes it central.
In Zorn's case, the name "lemma" fits a different fact: in many proofs it is a step that produces an object, such as a basis or a maximal ideal.

The names also show that the person in the name is not always the first author.
Burnside's lemma is the best-known case, and it is sometimes called "the lemma that is not Burnside's".

## Explanations

### L1 human

A lemma is usually a small helper result.
But some lemmas became famous on their own.
Zorn's lemma, for example, is one of the basic tools of modern mathematics, and it is as strong as one of the axioms of set theory.
Euclid's lemma is more than two thousand years old and is still used every day in number theory.
The word "lemma" in their names is a leftover from history.

### L2 human

We use Burnside's lemma to count the ways to colour the four corners of a square with two colours, up to rotation.

1. The rotation group has $4$ elements: the rotations by $0$, $90$, $180$ and $270$ degrees.
2. The rotation by $0$ degrees fixes all $2^4 = 16$ colourings.
3. The rotations by $90$ and by $270$ degrees fix only the $2$ colourings with all corners of one colour.
4. The rotation by $180$ degrees fixes the colourings with equal colours on opposite corners. There are $2 \cdot 2 = 4$ of them.
5. The lemma gives $(16 + 2 + 4 + 2) / 4 = 24 / 4 = 6$ colourings up to rotation.

The typical use of the lemma is to count objects up to symmetry, as in this example.
A trap is to divide the number of all colourings by the size of the group: $16 / 4 = 4$ is wrong, because some colourings have symmetries.
