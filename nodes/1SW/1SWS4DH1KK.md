---
tag: 1SWS4DH1KK
kind: example
name: Every prime number between 24 and 28 is even
msc: ["03B10", "97E30"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0V4QXPGJQK]
uses: [0V4QXPGJQK, 0B88PQTJ66, 01826KMG2H]
sources:
  - url: https://en.wikipedia.org/wiki/Vacuous_truth
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.2
---

## Example

Consider the statement "every prime number $n$ with $24 < n < 28$ is even".
Let $A = \{n \in \mathbb{Z} \mid 24 < n < 28 \text{ and } n \text{ is prime}\}$.
The statement is the restricted [[universal statement|0B88PQTJ66]] $\forall n \in A \; (n \text{ is even})$, that is, $\forall n \in \mathbb{Z} \; (n \in A \to n \text{ is even})$.
We show that it is a [[vacuous truth|0V4QXPGJQK]].

1. The integers $n$ with $24 < n < 28$ are $25$, $26$ and $27$.
2. $25 = 5 \cdot 5$, so $25$ is not a [[prime number|01826KMG2H]].
3. $26 = 2 \cdot 13$, so $26$ is not prime.
4. $27 = 3 \cdot 9$, so $27$ is not prime.
5. By steps 1 to 4, $A = \varnothing$.
6. So for each integer $n$, the antecedent $n \in A$ is false, and the implication $n \in A \to n \text{ is even}$ is true.
7. So the statement is true, and it is true without a check of evenness for any number.

## Remarks

The example shows that a universal statement over a set that turns out to be empty is true, whatever its property is.
By the same steps, "every prime number between $24$ and $28$ is odd" is also true, and so is "every prime number between $24$ and $28$ is greater than $1000$".

The truth value changes when the interval changes.
For $22 < n < 28$, the set $A$ becomes $\{23\}$, because $23$ is prime.
Then "every prime number $n$ with $22 < n < 28$ is even" is false, and $n = 23$ is a [[counterexample|0ED72CTBNP]].
The statement "some prime number $n$ with $24 < n < 28$ is even" is false, because an existential statement needs an element of $A$.

## Explanations

### L1 human

Look at the whole numbers between $24$ and $28$: they are $25$, $26$ and $27$.
None of them is prime: $25 = 5 \cdot 5$, $26 = 2 \cdot 13$ and $27 = 3 \cdot 9$.
So the claim "every prime number there is even" talks about nobody.
Nobody can break it, so it counts as true.

### L2 human

We decide the truth value of "every perfect square $n$ with $50 < n < 60$ is divisible by $7$".

1. The squares near the interval are $7^2 = 49$ and $8^2 = 64$.
2. So no perfect square lies strictly between $50$ and $60$, and the set of such squares is empty.
3. So each instance has a false antecedent, and the statement is vacuously true.

The typical use of this check is in a proof that treats ranges or cases: a range with no elements needs no work, but it must be recognized as empty.
A trap is to call such a statement false because "there are no examples"; the statement claims only that no counterexample exists.
