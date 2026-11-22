---
tag: 9DEWZDTNCV
kind: example
name: Erdős's proof of Bertrand's postulate is elementary
msc: ["00A35", "11N05"]
topics: [Z2WNQ1DNTX]
audience: ug2
instance_of: [84SZZBACP3]
uses: [0FJTGZA4GS, 0JPH2Y4DFV, 01WPV9PHN7, H19AXAMW3G, 84SZZBACP3]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_of_Bertrand%27s_postulate
    locator: Lemmas in the proof
  - url: https://en.wikipedia.org/wiki/Proof_of_Bertrand%27s_postulate
    locator: Proof from the lemmas
---

## Example

[[Bertrand's postulate|0FJTGZA4GS]] states that for every integer $n \ge 1$ there is a prime $p$ with $n < p \le 2n$.
Erdős published an [[elementary proof|84SZZBACP3]] in 1932.
We outline the proof and check that every step uses only integers and real inequalities.

1. A lower bound.
   The [[central binomial coefficient|0JPH2Y4DFV]] $\binom{2n}{n}$ is the largest of the $2n + 1$ terms of $(1 + 1)^{2n} = 4^n$, so
   $$\binom{2n}{n} \ge \frac{4^n}{2n + 1}.$$
   Check: for $n = 5$ we get $\binom{10}{5} = 252$ and $4^5/11 \approx 93.1$.
2. Prime powers are small.
   By [[Legendre's formula|01WPV9PHN7]], if $p^r$ is the exact power of a prime $p$ in $\binom{2n}{n}$, then $p^r \le 2n$.
   So $r \le 1$ when $p > \sqrt{2n}$.
3. A gap in the factorization.
   If $n \ge 3$ and $2n/3 < p \le n$, then $p$ does not divide $\binom{2n}{n}$.
   The reason is that $p$ appears exactly twice in $(2n)!$, from $p$ and $2p$, and exactly twice in $(n!)^2$, so the factors cancel.
4. An upper bound for primes.
   The product of all primes $p \le x$ is less than $4^x$.
   This bound on the [[primorial|H19AXAMW3G]] is proved by induction with binomial coefficients.
5. Suppose that no prime lies in $(n, 2n]$.
   By step 3 every prime factor of $\binom{2n}{n}$ is at most $2n/3$.
   There are at most $\sqrt{2n}$ primes up to $\sqrt{2n}$, and by step 2 each contributes at most $2n$, while by steps 2 and 4 the larger primes contribute at most $4^{2n/3}$ together:
   $$\binom{2n}{n} \le (2n)^{\sqrt{2n}} \cdot 4^{2n/3}.$$
6. Steps 1 and 5 together give
   $$4^{n/3} \le (2n + 1)(2n)^{\sqrt{2n}}.$$
   Taking logarithms shows that this inequality fails for every $n \ge 468$, so the postulate holds for those $n$.
7. For $1 \le n \le 467$ we check directly.
   The prime $2$ handles $n = 1$.
   For larger $n$ use the primes $2, 3, 5, 7, 13, 23, 43, 83, 163, 317, 631$, each less than twice the one before.
   If $q \le n < q'$ for consecutive primes $q, q'$ of the list, then $n < q' < 2q \le 2n$.

Every step uses integers, binomial coefficients, logarithms of real numbers and real inequalities, so the proof is elementary.

## Remarks

The proof is elementary, but it is not short or easy.
Step 6 needs care with logarithms, and step 7 is a finite check that is part of the proof, not a test beside it.
Without step 7 the argument proves the postulate only for $n \ge 468$.

Chebyshev proved Bertrand's postulate earlier, with longer estimates of the same kind.
Both proofs are elementary, and this shows again that "elementary" sorts proofs by their tools and not by their length.
The finite check depends on the estimates: a sharper version of step 5 lowers the threshold $468$ and shortens the list in step 7.

## Explanations

### L1 human

Bertrand's postulate says that between a number and its double there is always a prime.
Between $10$ and $20$ there are $11$, $13$, $17$ and $19$.
Erdős proved it for all numbers with counting and multiplication only.
His proof studies the number $\binom{2n}{n}$, which counts the ways to choose $n$ things out of $2n$.
He shows that this number is too large to be built from small primes alone.

### L2 human

The idea is to compare two estimates of one number, $\binom{2n}{n}$.
It is large, at least $4^n/(2n + 1)$, by step 1.
If no prime lies in $(n, 2n]$, it is built only from primes up to $2n/3$, and then step 5 shows that it is small.
For large $n$ the lower estimate beats the upper one, which is a contradiction.

Check at $n = 500$, using $\log 4 \approx 1.386$ and $\log 1000 \approx 6.908$:
$$\tfrac{500}{3} \log 4 \approx 231.0, \qquad \log 1001 + \sqrt{1000} \, \log 1000 \approx 6.9 + 218.4 = 225.3.$$
The left side is larger, so the inequality of step 6 fails at $n = 500$, as it must.
This pattern, a factorization followed by real inequalities, is typical of elementary prime number theory.
