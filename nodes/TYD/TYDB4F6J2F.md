---
tag: TYDB4F6J2F
kind: example
name: An induction step without a base case, for n^2 + n odd
msc: ["97E50", "00A35"]
topics: [EEH2F76CYQ]
audience: school
instance_of: [V52HDTMPV5]
uses: [V52HDTMPV5, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Description
---

## Example

False claim: for every natural number $n$, the number $n^2 + n$ is odd.
Here is a "proof" with a correct induction step and no base case.
It is an instance of the first [[error in induction proofs|V52HDTMPV5]], the missing base case.

1. Let $P(n)$ be the statement "$n^2 + n$ is odd".
2. Step.
   Let $n$ be a natural number, and assume $P(n)$, so that $n^2 + n = 2m + 1$ for some integer $m$.
3. Expand the next value and use the hypothesis:
   $$(n + 1)^2 + (n + 1) = (n^2 + n) + 2(n + 1) = 2m + 1 + 2(n + 1) = 2(m + n + 1) + 1.$$
   This is odd, so $P(n + 1)$ holds.
4. "By induction", $P(n)$ holds for every $n$.

Now we check each part.
The step in steps 2 and 3 is correct, since each equality is algebra or the assumption $P(n)$.
The base case is missing, and when we test it, $0^2 + 0 = 0$ is even, so $P(0)$ is false.
In fact the claim is false for every $n$: we have $n^2 + n = n(n + 1)$, one of the consecutive integers $n$ and $n + 1$ is even, and so the product is even.
So the step proves "if $P(n)$, then $P(n + 1)$" about statements that are all false, and an implication with a false premise is true but gives no information.

## Remarks

The step of [[mathematical induction|0ASJVEFA9J]] alone proves nothing, and the example makes that concrete.
What the step does show is that $n^2 + n$ and $(n + 1)^2 + (n + 1)$ have the same parity.
Together with one known value this fixes the parity of all values, and without a value it fixes nothing.

Change the claim and the same step becomes a proof.
For "$n^2 + n$ is even", the step works word for word with "even" in place of "odd", and the base case $0^2 + 0 = 0$ holds, so induction proves it.
For "$n^2 + n + 1$ is odd", the base case is $0 + 0 + 1 = 1$, the same step works, and that claim is true as well.

## Explanations

### L1 human

Imagine a row of dominoes set up so that each one would knock over the next.
If nobody pushes the first domino, nothing falls.
The "proof" above sets up the dominoes well but never pushes the first one.
In fact $0 \cdot 0 + 0 = 0$ is even, and $1 \cdot 1 + 1 = 2$ is even, so the claim is false from the start.

### L2 human

We test the claim on small values: $0^2 + 0 = 0$, $1^2 + 1 = 2$, $2^2 + 2 = 6$ and $3^2 + 3 = 12$.
All four values are even.
The step says that if one value is odd, then the next value is odd, and it never applies, because no value is odd.

The lesson is to prove the base case before you write the step, because the base case is often where a false claim fails.
Watch out for the feeling that a correct step makes a claim "almost proved": here the step is correct and the claim is false for every $n$.
