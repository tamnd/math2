---
tag: ~0fc1eddf
kind: example
name: An induction step without a base case, for n^2 + n odd
msc: ["97E50", "00A35"]
topics: [EEH2F76CYQ]
audience: school
instance_of: [~43bd251e]
uses: [~43bd251e, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Description
---

## Example

False claim: for every natural number $n$, the number $n^2 + n$ is odd.
Here is a "proof" with a correct induction step and no base case.
It is an instance of the first [[error in induction proofs|~43bd251e]]: the missing base case.

1. Let $P(n)$ be the statement "$n^2 + n$ is odd".
2. Step: let $n \in \mathbb{N}$ and assume $P(n)$, so $n^2 + n = 2m + 1$ for some integer $m$.
3. We expand: $(n + 1)^2 + (n + 1) = n^2 + 2n + 1 + n + 1 = (n^2 + n) + 2(n + 1)$.
4. By step 2, this is $2m + 1 + 2(n + 1) = 2(m + n + 1) + 1$, which is odd. So $P(n + 1)$ holds.
5. "By induction", $P(n)$ holds for every $n$.

We check each part.

1. The step (steps 2 to 4) is correct: each line follows from the previous one by algebra or by the assumption $P(n)$.
2. The base case is missing. We test it: $0^2 + 0 = 0$, which is even. So $P(0)$ is false.
3. The claim is false for every $n$. We have $n^2 + n = n(n + 1)$, and one of the two consecutive integers $n$ and $n + 1$ is even, so the product is even.
4. So the step proves "if $P(n)$, then $P(n + 1)$" about statements that are all false. An implication with a false premise is true, and it gives no information.

## Remarks

1. The example shows that the step of [[mathematical induction|0ASJVEFA9J]] alone proves nothing. The step and the base case are both needed.
2. The same step proves "if $n^2 + n$ is even, then $(n + 1)^2 + (n + 1)$ is even", and this time the base case $0^2 + 0 = 0$ holds. So induction proves the true claim "$n^2 + n$ is even for every $n$".
3. If the claim changes to "$n^2 + n + 1$ is odd", then the base case holds ($0 + 0 + 1 = 1$) and the same step works. So that claim is true.
4. The step shows that $n^2 + n$ and $(n + 1)^2 + (n + 1)$ have the same parity. Together with one value, this fixes the parity of all values; without a value, it fixes nothing.

## Explanations

### L1 human

Imagine a row of dominoes set up so that each one would knock over the next.
If nobody pushes the first domino, nothing falls.
The "proof" above sets up the dominoes well but never pushes the first one.
In fact $0 \cdot 0 + 0 = 0$ is even, and $1 \cdot 1 + 1 = 2$ is even, so the claim is false from the start.

### L2 human

We test the claim and the step on small values.

1. $n = 0$: $0^2 + 0 = 0$, even.
2. $n = 1$: $1 + 1 = 2$, even.
3. $n = 2$: $4 + 2 = 6$, even.
4. $n = 3$: $9 + 3 = 12$, even.
5. The step says: if one value is odd, the next is odd. It never applies, because no value is odd.

The typical lesson: before writing the step, prove the base case, because it is often where a false claim fails.
A trap is to think that a correct step makes the claim "almost proved": here the claim is false for every $n$.
