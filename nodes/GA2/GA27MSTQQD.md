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

A student must decide whether the claim "the sum of two odd integers is even" is true, and must convince a classmate.
The student writes the following answer.

> Each odd integer is $2a + 1$ for an integer $a$.
> So two odd integers are $2a + 1$ and $2b + 1$.
> Their sum is $2a + 2b + 2 = 2(a + b + 1)$, and $a + b + 1$ is an integer, so the sum is even.

We check that this answer shows a transformational [[proof scheme|YVNRVXJR68]], a kind of deductive scheme, by the conditions of Harel and Sowder.

1. Generality: the letters $a$ and $b$ stand for arbitrary integers. The argument treats all pairs of odd integers at once.
2. Operations with a goal: the student adds the two expressions and factors out $2$. Each operation aims at the form $2k$, which is the definition of an even integer.
3. Correctness of the operations: $(2a + 1) + (2b + 1) = 2a + 2b + 2 = 2(a + b + 1)$, and the sum of integers $a + b + 1$ is an integer.
4. Persuading: the student offers the general argument to the classmate, not a list of cases. The student expects a general reason to convince.
5. The conviction rests on general operations on the objects, which is the defining condition of a transformational scheme.

## Remarks

The written answer is a [[direct proof|0NTF6DMVAP]].
The scheme is shown by the fact that the student chose this argument to convince, and would not accept four examples instead.
A student with a ritual scheme could copy the same lines without seeing why the factor $2$ matters.
An interview separates the two cases: the student with a transformational scheme can explain each step and can adapt it, for example to show that the sum of three odd integers is odd.
That sum is $(2a + 1) + (2b + 1) + (2c + 1) = 2(a + b + c + 1) + 1$.

## Explanations

### L1 human

This student does not try examples.
Instead, the student uses the fact that each odd number is an even number plus one.
Two odd numbers then give two extra ones, and $1 + 1 = 2$ is even, so the whole sum is even.
This reason works for all odd numbers at once.
The student is convinced by the reason, not by the examples.

### L2 human

1. Represent the objects in general: $2a + 1$ and $2b + 1$.
2. Transform with a goal: add and factor to reach the form $2k$.
3. Check the goal: $k = a + b + 1$ is an integer.
4. Classify: conviction from general operations with anticipation of the result is the transformational scheme.

The typical use of this example is a contrast with the [[empirical scheme|6G5GATCE78]] for the same claim.
A trap is to infer the scheme from the text alone: the [[non-example|6FQKMC0PB2]] of this topic explains why.
