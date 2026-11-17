---
tag: VF1QJPSDG5
kind: example
name: Euclid's proof that there are infinitely many primes is elementary
msc: ["00A35", "11A41"]
topics: [Z2WNQ1DNTX]
audience: ug1
instance_of: [84SZZBACP3]
uses: [0292EPPPT0, 01826KMG2H, 084HH1NDCB, 84SZZBACP3]
sources:
  - url: https://en.wikipedia.org/wiki/Euclid%27s_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Elementary_proof
    locator: lead section
---

## Example

[[Euclid's theorem|0292EPPPT0]] states that there are infinitely many [[prime numbers|01826KMG2H]].
It is Proposition 20 of Book IX of [[Euclid's Elements|83WHDAV68J]].
We give the proof and check that every step is [[elementary|84SZZBACP3]].

1. Let $p_1, \dots, p_k$ be a finite list of primes. Put $N = p_1 p_2 \cdots p_k + 1$. This step uses only multiplication and addition of integers.
2. Each $p_i$ divides $N - 1$. If $p_i$ also divided $N$, then $p_i$ would divide $N - (N - 1) = 1$, which is false. This step uses only divisibility.
3. Since $N \ge 2$, $N$ has a prime factor $q$. This follows from the [[fundamental theorem of arithmetic|084HH1NDCB]], or from the fact that the least divisor $d > 1$ of $N$ is prime.
4. By step 2, $q$ is not in the list. So no finite list contains all primes.
5. A numerical check. For the list $2, 3, 5, 7$, we get $N = 211$, which is prime. For the list $2, 3, 5, 7, 11, 13$, we get $N = 30031 = 59 \cdot 509$, and the new primes $59$ and $509$ are not in the list.

No step uses real analysis, complex numbers or limits, so the proof is elementary in every usual sense.

## Remarks

Step 5 shows a common misreading of the proof: $N$ itself need not be prime.
The proof only says that a prime factor of $N$ is new.
The proof is also short, but shortness is not the reason it is elementary.
Euler's proof that $\sum_p 1/p$ [[diverges|00RA98X2CP]] proves the same theorem with infinite series and logarithms, so it is not elementary in the same strict sense.

## Explanations

### L1 human

Take any list of primes, multiply them, and add $1$.
The new number leaves remainder $1$ when we divide it by any prime in the list.
So its prime factors are new primes.
The proof uses only multiplying, adding and dividing whole numbers.
That is why we call it elementary.

### L2 human

To decide whether a proof is elementary, list the tools in each step and compare them with the allowed tools.

1. The allowed tools in number theory are the arithmetic of integers, real numbers and real inequalities.
2. The tools of Euclid's proof are products, the remainder of a division, and the existence of a prime factor.
3. Every tool in step 2 is in the list of step 1.

A trap: the proof is not "by contradiction" in an essential way, since it starts from any finite list and constructs a prime outside it.
