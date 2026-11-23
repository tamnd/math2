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

[[Euclid's theorem|0292EPPPT0]] is the $\Pi^0_2$ sentence $\forall n \, \exists p \, (p > n \wedge p \text{ is prime})$.
Its proof is often told as a proof by contradiction, but we read a bound on $p$ off it, in the manner of [[proof mining|XR1JXQG1CD]].

**Claim.** For every $n \ge 1$ there is a prime $p$ with $n < p \le n! + 1$.

We check the claim in four steps.

1. Let $N = n! + 1$.
   Then $N \ge 2$, so $N$ has a prime factor $p$, and $p \le N$ because a factor of a positive number is at most that number.
2. Suppose that $p \le n$.
   Then $p$ divides $n!$, since $n! = 1 \cdot 2 \cdots n$ has $p$ as one of its factors.
3. Then $p$ divides the difference $N - n! = 1$.
   No prime divides $1$, so the assumption $p \le n$ is false.
4. So $p > n$, and together with step 1 we get $n < p \le n! + 1$.

The bound gives an algorithm: test the numbers $n + 1, n + 2, \dots, n! + 1$ for primality, and stop at the first prime.

## Remarks

The version "suppose there are only finitely many primes" hides the bound, but the bound is there, because the contradiction is reached by looking at one explicit number.
The witness, the least prime factor of $n! + 1$, is a primitive recursive function of $n$.
So the theorem is a $\Pi^0_2$ sentence with a primitive recursive witness, which is what [[Parsons's theorem|2VYJXZZDGB]] predicts for theorems of $\mathrm{I}\Sigma_1$.
The [[elementary character of Euclid's proof|VF1QJPSDG5]] is what makes the extracted bound so simple.

Different proofs give different bounds.
Bertrand's postulate gives a prime $p$ with $n < p \le 2n$, which is far better, but it needs a different proof.
Proof mining returns the bound of the given proof, not the best bound.
If we replace $n!$ by the product of the primes up to $n$, the same argument works and gives a smaller bound, since that product divides $n!$.

## Explanations

### L1 human

Euclid's proof says: multiply the numbers up to $n$, add $1$, and look at a prime factor of the result.
That prime cannot divide any number up to $n$, so it is larger than $n$.
It is also at most the number we built.
For $n = 3$ we get $3! + 1 = 7$, which is prime, so $p = 7$ and $3 < 7 \le 7$.

### L2 human

We compute the witness for $n = 4$ and $n = 5$.
For $n = 4$ the number factors as follows:
$$4! + 1 = 25 = 5 \cdot 5.$$
So $p = 5$ and $4 < 5 \le 25$.
For $n = 5$ the number factors as follows:
$$5! + 1 = 121 = 11 \cdot 11.$$
So $p = 11$ and $5 < 11 \le 121$.
Check: $121 / 11 = 11$, and no prime up to $5$ divides $121$.

The typical use is as the simplest case of a bound read off an existence proof.
Watch out: $n! + 1$ need not be prime itself, as $25$ and $121$ show; only its prime factors are guaranteed to be larger than $n$.
