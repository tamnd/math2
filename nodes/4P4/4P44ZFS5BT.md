---
tag: 4P44ZFS5BT
kind: example
name: A proof with a nested claim and two end marks
msc: ["00A35", "11A41"]
topics: [Z2WNQ1DNTX]
audience: school
instance_of: [ET9J6R9T5C]
uses: [01826KMG2H, 0WAY5WX8NY, 0292EPPPT0, ET9J6R9T5C]
sources:
  - url: https://en.wikipedia.org/wiki/Q.E.D.
    locator: Typographical forms used symbolically
  - url: https://en.wikipedia.org/wiki/Tombstone_(typography)
    locator: lead section
---

## Example

*Theorem.* There are infinitely many [[primes|01826KMG2H]] $p$ with $p \equiv 3 \pmod 4$.

*Proof.* Let $p_1, \dots, p_k$ be any finite list of primes with $p_i \equiv 3 \pmod 4$, and put $N = 4 p_1 p_2 \cdots p_k - 1$.

*Claim.* A product of integers that are all $\equiv 1 \pmod 4$ is $\equiv 1 \pmod 4$.

*Proof of the claim.* If $a = 4s + 1$ and $b = 4t + 1$, then
$$ab = 16st + 4s + 4t + 1 = 4(4st + s + t) + 1.$$
Induction on the number of factors gives the claim.
$\square$

Now $N \equiv 3 \pmod 4$, so $N$ is odd, and each prime factor of $N$ is $\equiv 1$ or $\equiv 3 \pmod 4$.
If all prime factors of $N$ were $\equiv 1 \pmod 4$, the claim would give $N \equiv 1 \pmod 4$, which is false.
So $N$ has a prime factor $q \equiv 3 \pmod 4$.
If $q = p_i$ for some $i$, then $q$ divides $4 p_1 \cdots p_k - N = 1$, which is false.
So $q$ is a new prime $\equiv 3 \pmod 4$, and no finite list contains all such primes.
$\blacksquare$

We check the role of each [[end of proof mark|ET9J6R9T5C]], and the proof on one list.

1. The hollow square $\square$ ends the proof of the claim.
   The text after it returns to the main proof.
2. The filled square $\blacksquare$ ends the main proof.
   Nothing after it is part of the proof.
3. For the list $3, 7, 11$ we get
   $$N = 4 \cdot 231 - 1 = 923 = 13 \cdot 71.$$
   Here $13 \equiv 1$ and $71 \equiv 3 \pmod 4$, and $71$ is not in the list, as the proof predicts.

## Remarks

The two marks have different shapes, so the reader can tell the end of the claim from the end of the theorem.
Many authors use the same mark for both and rely on the words "Proof of the claim" to show the nesting.
Either way the marks pair up with the openings like brackets: each "Proof" is closed by exactly one mark, and an inner proof closes before the outer one.

The proof follows the pattern of [[Euclid's theorem|0292EPPPT0]], with [[congruences modulo 4|0WAY5WX8NY]] in place of plain divisibility.
If you try the same argument for primes $\equiv 1 \pmod 4$, with $N = 4 p_1 \cdots p_k + 1$, it breaks: a product of primes $\equiv 3 \pmod 4$ can be $\equiv 1 \pmod 4$, as $3 \cdot 7 = 21$ shows, so the claim no longer forces a new prime of the right form.

## Explanations

### L1 human

A long proof can contain a smaller proof inside it.
Here the small proof shows a fact about remainders, and it ends with a hollow square.
Then the big proof continues, and it ends with a filled square.
The two squares tell you where each proof stops.

### L2 human

To read a proof with nested claims, match each opening with its end mark, the way you match brackets.
"Proof." opens the main proof, and "Proof of the claim." opens the inner proof.
The first square closes the inner proof, and the second square closes the main proof.
So the structure is
$$\text{Proof} \ \big( \ \text{Claim} \ \ldots \ \square \ \big) \ \ldots \ \blacksquare.$$
A nested claim is the usual way to set apart a small lemma that the proof needs only once, and a reader who stops at the first square misses the main argument.
