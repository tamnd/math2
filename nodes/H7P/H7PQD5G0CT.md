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

We look at four results that carry the [[label "lemma"|KK5F0F03ZW]] and ask what role each one plays today.

1. [[Euclid's lemma|051VYKA1EX]]: if a prime $p$ divides $ab$, then $p$ divides $a$ or $p$ divides $b$.
   It is Proposition 30 of Book VII of Euclid's Elements.
   It is the main step in the proof of unique prime factorization, and every number theory course also uses it on its own.
2. [[Zorn's lemma|04RXTQA5ZA]]: a nonempty partially ordered set in which every chain has an upper bound has a maximal element.
   Over the other axioms of set theory it is equivalent to the axiom of choice.
   It proves that every vector space has a basis and that every ring with $1 \ne 0$ has a maximal ideal.
3. [[Burnside's lemma|0Z47M1B2VS]]: the number of orbits of a finite group $G$ acting on a finite set $X$ is
   $$\frac{1}{|G|} \sum_{g \in G} |X^g|,$$
   where $X^g$ is the set of points that $g$ fixes.
   It is the main tool for counting objects up to symmetry.
4. The [[Yoneda lemma|D6DF1ARPVD]]: for a functor $F$ from a category to sets and an object $A$, the natural transformations from $\operatorname{Hom}(A, -)$ to $F$ correspond to the elements of $F(A)$.
   It is a basic tool of the whole of category theory.

Each of the four has a full proof, so each is a theorem in the logical sense.
The word "lemma" records where the result started, as a tool inside a larger proof, and not how much it weighs today.

## Remarks

A result keeps the name it received first, even when later work makes it central.
For Zorn's lemma the name still fits one fact: in most proofs it is a single step that produces an object, such as a basis or a maximal ideal.

The person in the name is not always the first author either.
Burnside attributed his lemma to Frobenius, and Cauchy knew the formula earlier still, so the result is sometimes called "the lemma that is not Burnside's".
So a name tells you how a result entered the literature, and you need a history of the subject to learn who found it.

## Explanations

### L1 human

A lemma is usually a small helper result.
Some lemmas became famous on their own.
Zorn's lemma is one of the basic tools of modern mathematics, and it is as strong as one of the axioms of set theory.
Euclid's lemma is more than two thousand years old and is still used every day in number theory.
The word "lemma" in their names is a leftover from history.

### L2 human

Here is Burnside's lemma at work: how many ways are there to color the four corners of a square with two colors, if two colorings that differ by a rotation count as the same?
The rotation group has $4$ elements, the rotations by $0$, $90$, $180$ and $270$ degrees.
The rotation by $0$ degrees fixes all $2^4 = 16$ colorings.
The rotations by $90$ and $270$ degrees move each corner to the next, so they fix only the $2$ colorings with all corners the same color.
The rotation by $180$ degrees swaps opposite corners, so it fixes the $2 \cdot 2 = 4$ colorings with equal colors on opposite corners.
The lemma gives
$$\frac{16 + 2 + 4 + 2}{4} = \frac{24}{4} = 6.$$
Check by listing: all white, all black, one black corner, three black corners, two adjacent black corners, two opposite black corners.
Watch out: dividing $16$ by $4$ gives the wrong answer $4$, because colorings with symmetry, such as all white, have fewer than $4$ distinct rotations.
