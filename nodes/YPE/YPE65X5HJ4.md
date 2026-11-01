---
tag: YPE65X5HJ4
kind: problem
name: Integer factorization
msc: [11Y05, 11A51, 68Q25]
uses: [008BH74D7R, 02EKEPPJ3R, 01826KMG2H, 020K0X7HVR, 0HM584C465, 084HH1NDCB, XMHQCDWZW1]
about: [02EKEPPJ3R]
sources:
  - url: https://en.wikipedia.org/wiki/Integer_factorization
same_as:
  wikidata: Q4846249
  wikipedia: Integer factorization
history:
  posed_by: "Carl Friedrich Gauss"
  first_stated: "1801"
---

## Problem

Given a [[composite number|008BH74D7R]] $n$, written in binary, find integers $a$ and $b$ with $1 < a, b < n$ and $n = ab$.
Repeating this step gives the [[prime factorization|02EKEPPJ3R]] of $n$.
The open question is whether there is a classical algorithm that does this in a number of bit operations bounded by a polynomial in $\log n$.

## Remarks

The prime factorization exists and is unique by the [[existence of prime factorization|020K0X7HVR]] and the [[fundamental theorem of arithmetic|084HH1NDCB]], so the problem is about the cost of finding it.
Trial division by all integers up to $\sqrt n$ always works, but it needs about $\sqrt n$ steps, which is exponential in the number of digits.
No polynomial-time classical algorithm is known.
The fastest known general method for large numbers is the general number field sieve, whose heuristic running time is
$$\exp\left( \left( \sqrt[3]{64/9} + o(1) \right) (\ln n)^{1/3} (\ln \ln n)^{2/3} \right).$$
The decision version, which asks whether $n$ has a factor $d$ with $1 < d < k$ for a given $k$, lies in both NP and co-NP.
For this reason it is not expected to be NP-complete, but this is not proved.
On a quantum computer, Shor's algorithm factors $n$ in polynomial time.
Deciding whether $n$ is prime is easier: the [[AKS primality test|XMHQCDWZW1]] does it in deterministic polynomial time, without finding any factor.

## Explanations

### L1 human

Multiplying two large primes is quick, but recovering the two primes from their product seems to be very slow.
For example, $91 = 7 \cdot 13$ is easy to factor by hand, but a product of two primes with three hundred digits each is beyond every known method.
The security of the [[RSA cryptosystem|0HM584C465]] rests on this gap.
Nobody has proved that factoring is really hard, so this remains an open problem.
