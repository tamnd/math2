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
2. We have $25 = 5 \cdot 5$, $26 = 2 \cdot 13$ and $27 = 3 \cdot 9$, so none of them is a [[prime number|01826KMG2H]].
3. By steps 1 and 2, $A = \varnothing$.
4. So for each integer $n$ the antecedent $n \in A$ is false, and the implication $n \in A \to n \text{ is even}$ is true.
5. So the statement is true, and no number was ever checked for evenness.

## Remarks

The example shows that a universal statement over a set that turns out to be empty is true, whatever its property is.
By the same steps, "every prime number between $24$ and $28$ is odd" is true, and so is "every prime number between $24$ and $28$ is greater than $1000$".

Widen the interval and the truth value changes.
For $22 < n < 28$ the set $A$ becomes $\{23\}$, because $23$ is prime.
Then "every prime number $n$ with $22 < n < 28$ is even" is false, and $n = 23$ is a [[counterexample|0ED72CTBNP]].
The existential statement "some prime number $n$ with $24 < n < 28$ is even" is false in the original range, because it needs an element of $A$.

## Explanations

### L1 human

Look at the whole numbers between $24$ and $28$: they are $25$, $26$ and $27$.
None of them is prime, because $25 = 5 \cdot 5$, $26 = 2 \cdot 13$ and $27 = 3 \cdot 9$.
So the claim "every prime number there is even" talks about nobody.
Nobody can break it, so it counts as true.

### L2 human

Decide the truth value of "every perfect square $n$ with $50 < n < 60$ is divisible by $7$".
The squares on either side of the range are
$$7^2 = 49 \quad \text{and} \quad 8^2 = 64,$$
so no perfect square lies strictly between $50$ and $60$, and the set of such squares is empty.
Each instance has a false antecedent, so the statement is vacuously true.
Ranges and cases with no elements need no work in a proof, but you must first recognize that they are empty.
Watch out: the statement is not false because "there are no examples"; it claims only that no counterexample exists.
