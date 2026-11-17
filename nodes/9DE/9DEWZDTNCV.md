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
We outline the proof and check that it uses only integers and real inequalities.

1. A lower bound. The [[central binomial coefficient|0JPH2Y4DFV]] $\binom{2n}{n}$ is the largest of the $2n + 1$ terms of $(1 + 1)^{2n} = 4^n$. So $\binom{2n}{n} \ge 4^n/(2n + 1)$. For $n = 5$: $\binom{10}{5} = 252 \ge 4^5/11 \approx 93.09$.
2. Prime powers. By [[Legendre's formula|01WPV9PHN7]], if $p^r$ is the exact power of a prime $p$ in $\binom{2n}{n}$, then $p^r \le 2n$. So $r \le 1$ when $p > \sqrt{2n}$.
3. A gap. If $n \ge 3$ and $2n/3 < p \le n$, then $p$ does not divide $\binom{2n}{n}$. The reason is that $p$ appears twice in $(2n)!$ and twice in $(n!)^2$.
4. An upper bound. The product of all primes $p \le x$ is less than $4^x$. This is a bound on the [[primorial|H19AXAMW3G]], proved by induction with binomial coefficients.
5. Suppose that no prime lies in $(n, 2n]$. By step 3, every prime factor of $\binom{2n}{n}$ is at most $2n/3$. Steps 2 and 4 give $\binom{2n}{n} \le (2n)^{\sqrt{2n}} \cdot 4^{2n/3}$.
6. Steps 1 and 5 give $4^{n/3} \le (2n + 1)(2n)^{\sqrt{2n}}$. A direct computation shows that this inequality fails for every $n \ge 468$.
7. For $n \le 467$, use the primes $2, 3, 5, 7, 13, 23, 43, 83, 163, 317, 631$. Each is less than twice the one before. So for $n$ between two consecutive primes $q \le n < q'$ of the list, the prime $q'$ satisfies $n < q' < 2q \le 2n$.

Every step uses integers, binomial coefficients and inequalities between real numbers, so the proof is elementary.

## Remarks

Chebyshev proved Bertrand's postulate earlier, with longer estimates of the same kind.
The proof of Erdős is elementary, but it is not trivial: step 6 needs care with logarithms, and step 7 needs a finite check.
The finite check in step 7 is part of the proof, not a separate test.

## Explanations

### L1 human

Bertrand's postulate says that between a number and its double, there is always a prime.
Between $10$ and $20$ there are $11$, $13$, $17$ and $19$.
Erdős proved it for all numbers with counting and multiplication only.
His proof studies the number $\binom{2n}{n}$, which counts ways to choose $n$ things out of $2n$.
He shows that this number is too large to be built from small primes alone.

### L2 human

The idea is to compare two estimates of one number.

1. The number $\binom{2n}{n}$ is large: at least $4^n/(2n + 1)$.
2. If no prime lies in $(n, 2n]$, then $\binom{2n}{n}$ is built only from primes at most $2n/3$, and then it is small: at most $(2n)^{\sqrt{2n}} 4^{2n/3}$.
3. For large $n$, the lower bound exceeds the upper bound, which is a contradiction.

The typical pattern of elementary prime number theory is visible here: an identity or a factorization, then real inequalities.
A trap: step 6 only works for large $n$, so the proof is not complete without the finite check of step 7.
