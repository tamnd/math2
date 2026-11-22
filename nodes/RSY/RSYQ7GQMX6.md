---
tag: RSYQ7GQMX6
kind: example
name: An algebraic proof of k C(n, k) = n C(n - 1, k - 1) is not a combinatorial proof
msc: ["00A35", "05A19"]
topics: [GB14W4SYPK]
audience: ug1
not_instance_of:
  - target: SS07J9ZAQ7
    note: the proof transforms the factorial formula and never names a set that both sides count, so it proves the identity without counting
uses: [SS07J9ZAQ7, TTQNN6XXQN, 0GBZM0MT0F]
sources:
  - url: https://en.wikipedia.org/wiki/Combinatorial_proof
    locator: lead section
---

## Example

Let $n$ and $k$ be integers with $1 \le k \le n$.
We prove $k\binom{n}{k} = n\binom{n-1}{k-1}$ by algebra, and then we check why this proof is not a [[combinatorial proof|SS07J9ZAQ7]].

1. We use the factorial formula $\binom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$ for the [[binomial coefficient|0GBZM0MT0F]].
2. Since $k! = k \cdot (k-1)!$, the left side is
   $$k\binom{n}{k} = \frac{k \cdot n!}{k!\,(n-k)!} = \frac{n!}{(k-1)!\,(n-k)!}.$$
3. Since $(n-1) - (k-1) = n - k$ and $n \cdot (n-1)! = n!$, the right side is
   $$n\binom{n-1}{k-1} = \frac{n \cdot (n-1)!}{(k-1)!\,(n-k)!} = \frac{n!}{(k-1)!\,(n-k)!}.$$
4. The results of steps 2 and 3 are equal, so the identity holds, and the proof is correct.
5. The proof never names a set.
   No step says what $k\binom{n}{k}$ or $n\binom{n-1}{k-1}$ counts.
6. So the proof is a valid algebraic proof but not a combinatorial proof, because the condition that both sides count one set, or two sets in bijection, is not met.

## Remarks

The algebraic proof and the [[combinatorial proof with a chair|TTQNN6XXQN]] prove the same identity.
The algebraic proof is quicker to check line by line.
The combinatorial proof explains the identity: the left side chooses a committee and then its chair, and the right side chooses the chair first.

The algebraic proof also depends on the factorial formula, which itself needs a proof.
The combinatorial proof uses only the definition of $\binom{n}{k}$ as a number of subsets.
Neither kind of proof is better in general, because they answer different questions: "is it true?" and "why is it true?".

## Explanations

### L1 human

We can prove the identity by writing each binomial coefficient as a fraction of factorials and cancelling.
Both sides turn into the same fraction, so they are equal.
This is a correct proof, but it does not say what the numbers count.
A combinatorial proof would name a set of objects and count it in two ways.
So this proof is a proof by algebra, not a combinatorial proof.

### L2 human

Here are four proofs of identities about binomial coefficients, sorted into the two kinds.
Counting the pairs (committee, chair) in two orders is combinatorial, since it names a set and counts it twice.
Cancelling factorials, as above, is algebraic, since no set appears.
Proving $\sum_k \binom{n}{k} = 2^n$ by putting $x = y = 1$ in the binomial theorem
$$(x + y)^n = \sum_{k} \binom{n}{k} x^k y^{n-k}$$
is algebraic, since it substitutes numbers in a formula.
Proving the same sum by counting the subsets of $[n]$ by size and by "in or out" for each element is combinatorial.
The distinction matters when a problem asks for a combinatorial proof: an algebraic proof, even a correct one, does not answer it.
Watch out: a proof is not combinatorial just because it is about binomial coefficients, and what matters is whether it counts a set.
