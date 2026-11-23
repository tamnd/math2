---
tag: JEW1GKR244
kind: example
name: The square of opposition with an empty subject term
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: school
instance_of: [VYNBSVZ2TH]
uses: [VYNBSVZ2TH, MZBNX2T6Q6, 0ECVK59Y03, 0GHS47PDAQ, 0MSRQHCNN9]
sources:
  - url: https://en.wikipedia.org/wiki/Square_of_opposition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Syllogism
    locator: lead section
---

## Example

Let the subject term $S$ be the even primes greater than $2$ and the predicate term $P$ be the multiples of $4$.
The four corners of the [[square of opposition|VYNBSVZ2TH]] are these sentences.

- A: all even primes greater than $2$ are multiples of $4$.
- E: no even prime greater than $2$ is a multiple of $4$.
- I: some even prime greater than $2$ is a multiple of $4$.
- O: some even prime greater than $2$ is not a multiple of $4$.

We find the truth values in the modern reading and check which relations of the square survive.

1. The only even prime is $2$, so $S$ is [[empty|0ECVK59Y03]].
2. In the modern reading A is $\forall x\,(S(x) \to P(x))$.
   No $x$ satisfies $S(x)$, so the implication holds for every $x$, and A is true.
3. E is $\forall x\,(S(x) \to \neg P(x))$, and it is true for the same reason.
4. I is $\exists x\,(S(x) \land P(x))$, and it is false because no $x$ satisfies $S(x)$.
5. O is $\exists x\,(S(x) \land \neg P(x))$, and it is false for the same reason.
6. The contradictories keep their relation: A is true and O false, and E is true and I false.
7. The contraries A and E are both true, so "not both true" fails.
8. The subcontraries I and O are both false, so "not both false" fails.
9. A is true and I is false, and E is true and O is false, so subalternation fails.

## Remarks

With an empty subject term only the two diagonals of the square remain.
The calculation uses nothing about multiples of $4$, so every predicate term gives the same four truth values.
Take a non-empty subject instead, such as all even primes, and the traditional relations hold again: with $P$ the multiples of $4$, A is false, E true, I false and O true.

The traditional square avoids the case by assuming that every term names a non-empty class.
Another repair reads A as "some $S$ exists and all $S$ are $P$".
Then A is false here, and if O keeps its modern reading, A and O are both false and stop being contradictories.
The square survives this reading only if O is also read as "not every $S$ is $P$", which is true when $S$ is empty.

## Explanations

### L1 human

There are no even primes larger than $2$.
In modern logic, "all such primes are multiples of $4$" is true, because nothing could break the rule.
For the same reason "no such prime is a multiple of $4$" is true.
And "some such prime is a multiple of $4$" is false, because there is no such prime at all.
So the "all" sentence and the "no" sentence, which look like opposites, are true together.

### L2 human

We check the claim in the remarks: if A carries existential import and O keeps its modern reading, then A and O are not contradictories.

1. Read A as $\exists x\, S(x) \land \forall x\,(S(x) \to P(x))$ and O as $\exists x\,(S(x) \land \neg P(x))$.
2. For the empty $S$ of the example, $\exists x\, S(x)$ is false, so A is false.
3. O is false, by step 5 of the example.
4. Contradictories cannot both be false, so A and O are not contradictories in this reading.

To decide which reading a text uses, ask whether it lets a universal statement be true about nothing; if it does, it uses the modern square.
The trap is to mix the readings: the traditional relations need $S$ to be non-empty, and the modern A and E do not promise that.
