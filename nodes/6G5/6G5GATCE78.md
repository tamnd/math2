---
tag: 6G5GATCE78
kind: example
name: An empirical proof scheme for the sum of two odd numbers
msc: ["97E50", "97C30"]
topics: [VHGA6J4NZK]
audience: research
instance_of: [YVNRVXJR68]
uses: [YVNRVXJR68, 5V35SGEN1T]
sources:
  - url: https://doi.org/10.1090/cbmath/007/07
    locator: pages 234-283
---

## Example

A student must decide whether the claim "the sum of two odd integers is even" is true, and must convince a classmate.
The student writes the following answer.

> $1 + 3 = 4$, $5 + 7 = 12$, $11 + 13 = 24$, $25 + 49 = 74$.
> All the sums are even, so the claim is true.

We check that this answer shows an empirical [[proof scheme|YVNRVXJR68]], of the inductive kind, by the conditions of Harel and Sowder.

1. Ascertaining: the student became sure of the claim after the four computations. The source of conviction is the examples.
2. Persuading: the student offers the same four computations to the classmate. The student expects examples to convince another person.
3. The arithmetic is correct: $1 + 3 = 4 = 2 \cdot 2$, $5 + 7 = 12 = 2 \cdot 6$, $11 + 13 = 24 = 2 \cdot 12$ and $25 + 49 = 74 = 2 \cdot 37$.
4. No step refers to a property of all odd numbers. The examples are not used to show a general structure, so the argument is not a [[generic proof|SG9XA69J64]].
5. The conviction rests on specific cases, which is the defining condition of an inductive empirical scheme.

## Remarks

The claim is true, and the student's belief is correct.
What the example shows is the standard of conviction, not an error in the conclusion.
The same student would accept the claim "$n^2 + n + 41$ is prime for each natural number $n$" after checking $n = 0$ to $5$, and this claim is false at $n = 40$, where $40^2 + 40 + 41 = 41^2$.
If the student instead wrote "$7 + 9 = 16$: the $7$ is three pairs and one, the $9$ is four pairs and one, and the two ones make a pair", the answer would use a general structure.
That change of one sentence moves the answer from the empirical scheme toward a generic argument.

## Explanations

### L1 human

The student tries a few pairs of odd numbers and sees that each sum is even.
The student then believes that this always happens.
This is how many people become sure of a pattern.
The belief is right in this case, but the reason is weak.
A pattern can hold for the first numbers and fail later.

### L2 human

1. Name the evidence: four sums, each computed and each even.
2. Ask what convinced the student: the student says "it worked every time".
3. Ask what would change the student's mind: only an odd sum, which the student did not find.
4. Classify: conviction from cases is the inductive empirical scheme.

The typical use of this example in teaching is a contrast with the [[transformational scheme|GA27MSTQQD]] for the same claim.
A trap is to judge the scheme only by the conclusion, which is true here.
