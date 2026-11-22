---
tag: HGRAZBCXEQ
kind: example
name: A lemma, a theorem and a corollary on prime factorization
msc: ["00A35", "11A51"]
topics: [N4P3E53HM0]
audience: school
instance_of: [KK5F0F03ZW]
uses: [KK5F0F03ZW, 051VYKA1EX, 084HH1NDCB, 0DZGSDHD92, 0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
    locator: Proof
  - url: https://en.wikipedia.org/wiki/Euclid%27s_lemma
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Square_root_of_2
    locator: Proofs of irrationality
---

## Example

We follow three results of elementary number theory and give each its usual label.
All letters denote positive integers, and $p$, $p_i$, $q_j$ denote [[primes|0SN0MAEKYX]].

1. Lemma ([[Euclid's lemma|051VYKA1EX]]): if $p$ divides $ab$, then $p$ divides $a$ or $p$ divides $b$.
   Its usual proof uses the greatest common divisor of $p$ and $a$, and we take the lemma as proved.
2. A first use of the lemma: if $p$ divides a product $a_1 a_2 \cdots a_k$, then $p$ divides some $a_i$.
   Apply the lemma to $a_1 \cdot (a_2 \cdots a_k)$, and if $p$ divides the second factor, repeat on it.
3. Theorem (uniqueness in the [[fundamental theorem of arithmetic|084HH1NDCB]]): if $p_1 p_2 \cdots p_k = q_1 q_2 \cdots q_l$, then the two lists of primes agree up to order.
4. Proof of the theorem, first part: $p_1$ divides $q_1 \cdots q_l$, so by step 2 it divides some $q_j$.
5. Second part: the only divisors of the prime $q_j$ are $1$ and $q_j$, and $p_1 \ne 1$, so $p_1 = q_j$.
6. Third part: cancel $p_1$ and $q_j$ from the two sides, and repeat with the shorter products.
   When one side becomes $1$, the other side is $1$ too, because a product of primes is larger than $1$.
   So the lists have the same length and the same primes.
7. Corollary (the [[irrationality of the square root of 2|0DZGSDHD92]]): no positive integers $a$ and $b$ satisfy $a^2 = 2b^2$.
8. Proof of the corollary: if $2$ appears $r$ times in the factorization of $a$ and $s$ times in that of $b$, then it appears $2r$ times in $a^2$ and $2s + 1$ times in $2b^2$.
9. By the theorem, two factorizations of one number agree.
   But $2r$ is even and $2s + 1$ is odd, so $a^2 = 2b^2$ is impossible.

## Remarks

The lemma is a tool: it matters mainly because the theorem needs it.
The theorem is the goal: unique factorization is used throughout number theory.
The corollary is a consequence: its proof uses only the theorem and a count of one prime.

The corollary generalizes with no new idea.
Replace $2$ by a positive integer $n$ that is not a perfect square.
Then some prime $q$ appears an odd number of times in $n$, so it appears an odd number of times in $nb^2$ and an even number of times in $a^2$.
So $a^2 = nb^2$ has no solution, and $\sqrt{n}$ is irrational.

## Explanations

### L1 human

Mathematicians label the results in a chain.
First comes a helper fact, a lemma: a prime that divides a product divides one of the factors.
With this helper a big result, a theorem, follows: each number splits into primes in only one way.
From the theorem a small result, a corollary, drops out in a few lines: the square root of $2$ is not a fraction.
The labels show which result is the tool, which is the goal, and which is the bonus.

### L2 human

Check step 8 on small numbers, with $a = 12$ and $b = 6$.
Factor them: $12 = 2^2 \cdot 3$ and $6 = 2 \cdot 3$, so $r = 2$ and $s = 1$.
Then
$$a^2 = 144 = 2^4 \cdot 3^2, \qquad 2b^2 = 72 = 2^3 \cdot 3^2.$$
The prime $2$ appears $4 = 2r$ times on the left and $3 = 2s + 1$ times on the right, so $144 \ne 72$ by this count alone.
Step 9 says the same for every $a$ and $b$, and that is why the count decides the question.
Watch out: the proof of unique factorization must not use the irrationality of $\sqrt{2}$, since that result comes after it in the chain.
