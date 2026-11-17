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

1. Claim $C$: "$91$ is prime". This part is present.
2. Data $D$: none. The student gives no fact in support of the claim.
3. Warrant $W$: none. A warrant links data to a claim, and there are no data to link.
4. Qualifier and rebuttal: none are stated.
5. The model needs at least a claim, data and a warrant for one step. The data are missing, so the utterance has no Toulmin layout.

## Remarks

The claim is also false: $91 = 7 \cdot 13$.
The bare assertion gives the class no way to see this, because it offers no step to check.
If the student had said "$91$ is prime, because it is odd and not divisible by $3$ or $5$", the utterance would have data and an implicit warrant ("an odd number not divisible by $3$ or $5$ is prime").
That argument has a layout, and the layout shows the error: the warrant is false, as $91$ and $49 = 7^2$ show.
So the model helps a teacher only after a student gives reasons.

## Explanations

### L1 human

Saying "$91$ is prime" is a claim with no reason.
Without a reason, there is nothing to check except the claim itself.
The Toulmin model describes reasons, so it has nothing to describe here.
In fact $91 = 7 \times 13$, so the claim is false.

### L2 human

1. List the parts: only a claim.
2. Recall the minimal layout: claim, data and warrant.
3. Conclude: not a Toulmin argument.

A teacher's typical response is to ask "why?", which turns the assertion into an argument that the class can analyse.
