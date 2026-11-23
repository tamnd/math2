---
tag: GF25NRYH94
kind: example
name: A bare assertion has no Toulmin layout
msc: ["97E50", "97C70"]
topics: [VHGA6J4NZK]
audience: research
not_instance_of:
  - target: RVZCSFDB2Y
    note: the utterance has a claim but no data, so there is nothing that a warrant could link to the claim
uses: [RVZCSFDB2Y]
sources:
  - url: https://en.wikipedia.org/wiki/Stephen_Toulmin
    locator: Toulmin model of argument
---

## Example

In a lesson on primes, a student says only: "$91$ is prime."
The student gives no reason, and the teacher moves on.
We check the parts of the [[Toulmin model|RVZCSFDB2Y]] and find that the utterance is not a Toulmin argument.

1. Claim $C$: "$91$ is prime", which is present.
2. Data $D$: none, because the student offers no fact in support of the claim.
3. Warrant $W$: none, because a warrant links data to a claim and there are no data to link.
4. Qualifier and rebuttal: none stated.
5. One step of the model needs at least a claim, data and a warrant.
   The data are missing, so the utterance has no Toulmin layout.

## Remarks

The claim is also false, since $91 = 7 \cdot 13$.
The bare assertion gives the class no way to see this, because it offers no step to check.

Suppose the student had said "$91$ is prime, because it is odd and not divisible by $3$ or $5$".
Then the utterance has data and an implicit warrant: an odd number not divisible by $3$ or $5$ is prime.
That argument has a layout, and the layout exposes the error, because the warrant is false, as $49 = 7^2$ and $91$ itself show.
So the model helps a teacher only after a student gives reasons.

## Explanations

### L1 human

Saying "$91$ is prime" is a claim with no reason.
Without a reason, there is nothing to check except the claim itself.
The Toulmin model describes reasons, so it has nothing to describe here.
In fact $91 = 7 \times 13$, so the claim is false.

### L2 human

List the parts that are present, and only the claim remains.
Compare with the minimal layout of claim, data and warrant, and the utterance falls short.
So it is not a Toulmin argument.
A teacher's typical response is to ask "why?", which turns the assertion into an argument that the class can analyze.
