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
2. In the modern reading A is $\forall x\,(S(x) \to P(x))$. No $x$ satisfies $S(x)$, so the implication holds for every $x$, and A is true.
3. E is $\forall x\,(S(x) \to \neg P(x))$, and it is true for the same reason.
4. I is $\exists x\,(S(x) \land P(x))$. No $x$ satisfies $S(x)$, so I is false.
5. O is $\exists x\,(S(x) \land \neg P(x))$, and it is false for the same reason.
6. Contradictories: A is true and O is false, and E is true and I is false. Both pairs keep the relation.
7. Contraries: A and E are both true. The traditional relation "not both true" fails.
8. Subcontraries: I and O are both false. The traditional relation "not both false" fails.
9. Subalternation: A is true and I is false, and E is true and O is false. The traditional inference from the universal to the particular fails.

## Remarks

The example shows the modern square: with an empty subject term, only the two diagonals of the square remain.
The calculation uses nothing about multiples of $4$, so any predicate term gives the same four truth values.
If $S$ is changed to a non-empty class, for example the even primes, the traditional relations hold again; with $P$ the multiples of $4$, A is false, E true, I false and O true.
The traditional reading avoids the problem by assuming that each term names a non-empty class, so it does not apply to this choice of $S$.
Some traditional authors read A as "all $S$ are $P$, and some $S$ exists"; then A is false here, and the A and O corners are no longer contradictories.

## Explanations

### L1 human

There are no even primes larger than $2$.
In modern logic, "all such primes are multiples of $4$" is true, because there is nothing that could break the rule.
For the same reason "no such prime is a multiple of $4$" is true.
And "some such prime is a multiple of $4$" is false, because there is no such prime at all.
So two sentences that look like opposites, "all ... are" and "no ... is", are true together.

### L2 human

We check the claim in the last remark: if A carries existential import, then A and O are not contradictories.

1. Read A as $\exists x\, S(x) \land \forall x\,(S(x) \to P(x))$ and O as $\exists x\,(S(x) \land \neg P(x))$.
2. For the empty $S$ of the example, $\exists x\, S(x)$ is false, so A is false.
3. O is false, by step 5 of the example.
4. Two contradictories cannot both be false, so A and O are not contradictories in this reading.

The typical use of the example is to decide which reading a text uses: if it lets universal statements be true about nothing, it uses the modern square.
The trap is to mix the readings: the traditional relations need the assumption that $S$ is not empty, and the modern A and E do not give it.
