---
tag: GA27MSTQQD
kind: example
name: A transformational proof scheme for the sum of two odd numbers
msc: ["97E50", "97C30"]
topics: [VHGA6J4NZK]
audience: research
instance_of: [YVNRVXJR68]
uses: [YVNRVXJR68, 0NTF6DMVAP]
sources:
  - url: https://doi.org/10.1090/cbmath/007/07
    locator: pages 234-283
---

## Example

A student must decide whether "the sum of two odd integers is even" is true, and must convince a classmate.
The student writes this answer.

> Each odd integer is $2a + 1$ for an integer $a$.
> So two odd integers are $2a + 1$ and $2b + 1$.
> Their sum is $2a + 2b + 2 = 2(a + b + 1)$, and $a + b + 1$ is an integer, so the sum is even.

We check that the answer shows a transformational [[proof scheme|YVNRVXJR68]], which is one kind of deductive scheme in the sense of Harel and Sowder.

1. Generality: the letters $a$ and $b$ stand for arbitrary integers, so the argument treats all pairs of odd integers at once.
2. Operations aimed at a goal: the student adds the two expressions and takes out the factor $2$.
   Each move aims at the form $2k$, which is the definition of an even integer.
3. The operations are correct:
   $$(2a + 1) + (2b + 1) = 2a + 2b + 2 = 2(a + b + 1),$$
   and $a + b + 1$ is an integer because integers are closed under addition.
4. Persuading: the student offers the general argument to the classmate, not a list of cases, so the student expects a general reason to convince.
5. Conviction from general operations on the objects, with the result anticipated, is the defining condition of a transformational scheme, so the answer is an instance of it.

## Remarks

The written answer is a [[direct proof|0NTF6DMVAP]].
The scheme shows in the student's choice: this is the argument the student chose to convince, and four examples would not have satisfied the student.

The same text does not prove the same scheme in every writer.
A student with a ritual scheme could copy these lines without seeing why the factor $2$ matters.
An interview separates the two cases, since a student with a transformational scheme can explain each step and adapt the argument.
For example, asked about three odd integers, such a student writes
$$(2a + 1) + (2b + 1) + (2c + 1) = 2(a + b + c + 1) + 1,$$
and concludes that the sum is odd.

## Explanations

### L1 human

This student does not try examples.
Instead, the student uses the fact that each odd number is an even number plus one.
Two odd numbers then give two extra ones, and $1 + 1 = 2$ is even, so the whole sum is even.
That reason works for all odd numbers at once, and it is the reason, not a list of cases, that convinces the student.

### L2 human

Read the answer as four moves.
The student first represents the objects in general, as $2a + 1$ and $2b + 1$.
Then the student transforms them with a goal in view, adding and factoring to reach the form $2k$.
Next the student checks that $k = a + b + 1$ is an integer.
Finally the student uses the result to persuade, which is what makes it a scheme and not only a text.
Set it beside the [[empirical answer|6G5GATCE78]] to the same claim to see the contrast.
Watch out: the scheme cannot be read from the text alone, as [[the non-example|6FQKMC0PB2]] explains.
