---
tag: S0GAFZK93F
kind: example
name: A bound on the next prime from Euclid's proof
msc: ["03F10", "11A41"]
topics: [8XY7JYZKFW]
audience: grad
instance_of: [XR1JXQG1CD]
uses: [XR1JXQG1CD, 0292EPPPT0, VF1QJPSDG5]
sources:
  - url: https://en.wikipedia.org/wiki/Euclid%27s_theorem
    locator: Euclid's proof
  - url: https://en.wikipedia.org/wiki/Proof_mining
    locator: lead section
---

## Example

[[Euclid's theorem|0292EPPPT0]] says $\forall n\, \exists p\, (p > n \wedge p \text{ prime})$.
Its proof is often given by contradiction, but we read off a bound on $p$, as in [[proof mining|XR1JXQG1CD]].

**Claim.** For every $n \ge 1$ there is a prime $p$ with $n < p \le n! + 1$.

1. Let $N = n! + 1$. Then $N \ge 2$, so $N$ has a prime factor $p$, and $p \le N$.
2. Suppose $p \le n$. Then $p$ divides $n!$, since $n!$ is the product $1 \cdot 2 \cdots n$.
3. Then $p$ divides $N - n! = 1$, which is false for a prime.
4. So $p > n$, and $n < p \le n! + 1$.

The bound gives an algorithm: test the numbers from $n + 1$ to $n! + 1$ for primality, and stop at the first prime.

## Remarks

The proof by contradiction, "suppose there are only finitely many primes", hides the bound, but the bound is there.
The witness $p$ is the least prime factor of $n! + 1$, a primitive recursive function of $n$.
So the theorem is a $\Pi^0_2$ statement with a primitive recursive witness, as [[Parsons's theorem|2VYJXZZDGB]] predicts for theorems of $\mathrm{I}\Sigma_1$.
Better bounds exist, such as Bertrand's postulate $p \le 2n$, but they need other proofs; proof mining gives the bound of the given proof.
The [[elementary character of Euclid's proof|VF1QJPSDG5]] is what makes the bound simple.

## Explanations

### L1 human

Euclid's proof says: multiply numbers up to $n$, add $1$, and look at a prime factor of the result.
That prime cannot divide any number up to $n$, so it is larger than $n$.
It is also at most the number we built.
For $n = 3$: $3! + 1 = 7$, which is prime, so $p = 7$ and $3 < 7 \le 7$.

### L2 human

We compute the witness for $n = 4$ and $n = 5$.

1. $n = 4$: $4! + 1 = 25 = 5 \cdot 5$, so $p = 5$, and $4 < 5 \le 25$.
2. $n = 5$: $5! + 1 = 121 = 11 \cdot 11$, so $p = 11$, and $5 < 11 \le 121$.

The typical use is as the simplest example of a bound read off from an existence proof.
A trap is to think that $n! + 1$ itself is prime; for $n = 4$ it is $25$.
