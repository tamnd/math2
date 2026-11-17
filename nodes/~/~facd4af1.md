---
tag: ~facd4af1
kind: example
name: Proving the inverse instead of the contrapositive
msc: ["00A35", "11A05"]
topics: [958EF46EYJ]
audience: school
not_instance_of:
  - target: 0BB5TPGQ1N
    note: the argument proves not P implies not Q, the inverse, which is equivalent to the converse and not to the claim
uses: [0BB5TPGQ1N, 09A3N7ZN5G]
sources:
  - url: https://en.wikipedia.org/wiki/Contraposition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Inverse_(logic)
    locator: lead section
---

## Example

Claim: for all integers $a$ and $b$, if $4 \mid ab$, then $4 \mid a$ or $4 \mid b$.
A student writes: "We prove the contrapositive; assume $4 \nmid ab$; then $4$ divides neither $a$ nor $b$, because a multiple of $4$ times any integer is a multiple of $4$."
This is not a [[proof by contrapositive|0BB5TPGQ1N]].
We check the condition that fails.

1. The claim has the form $P \Rightarrow Q$ with $P$: "$4 \mid ab$" and $Q$: "$4 \mid a$ or $4 \mid b$".
2. The contrapositive is $\neg Q \Rightarrow \neg P$: if $4 \nmid a$ and $4 \nmid b$, then $4 \nmid ab$.
3. The student assumed $\neg P$ and concluded $\neg Q$. This is the inverse $\neg P \Rightarrow \neg Q$.
4. The inverse is the contrapositive of the [[converse|09A3N7ZN5G]] $Q \Rightarrow P$, so it is equivalent to the converse, not to the claim.
5. The student's argument is a correct proof of the converse: if $4 \mid a$ or $4 \mid b$, then $4 \mid ab$.
6. The claim itself is false: $a = b = 2$ gives $ab = 4$, so $4 \mid ab$, but $4 \nmid 2$.

## Remarks

The example shows why the order of the negations matters.
The contrapositive negates both parts and swaps them; the inverse negates both parts and keeps the order.

A true claim of the same shape uses a prime instead of $4$.
For a prime $p$, if $p \mid ab$, then $p \mid a$ or $p \mid b$: this is [[Euclid's lemma|051VYKA1EX]].
Its correct contrapositive is "if $p \nmid a$ and $p \nmid b$, then $p \nmid ab$".
The number $4$ is not prime, and $a = b = 2$ shows that the claim fails for it.

## Explanations

### L1 human

Take the sentence "if an animal is a dog, then it has four legs".
Its contrapositive is "if an animal does not have four legs, then it is not a dog", and this says the same thing.
Its inverse is "if an animal is not a dog, then it does not have four legs".
The inverse is a different sentence, and it is false: a cat has four legs.
A proof of the inverse does not prove the original sentence.

### L2 human

We sort four statements about an integer $n$ into equivalent pairs.

1. Original: if $n$ is a multiple of $6$, then $n$ is even. This is true.
2. Contrapositive: if $n$ is odd, then $n$ is not a multiple of $6$. True, and equivalent to 1.
3. Converse: if $n$ is even, then $n$ is a multiple of $6$. False, since $n = 2$.
4. Inverse: if $n$ is not a multiple of $6$, then $n$ is odd. False, since $n = 2$, and equivalent to 3.

The typical use of this check: before writing "we prove the contrapositive", write out $\neg Q \Rightarrow \neg P$ and compare it with the claim.

A trap: when the converse happens to be true, a proof of the inverse looks correct, and the error stays hidden until a case where the converse fails.
