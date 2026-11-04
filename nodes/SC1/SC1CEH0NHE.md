---
tag: SC1CEH0NHE
kind: proof
name: Proof of the existence of inverses modulo n
msc: [11A07]
proves: 0M67FWZWPQ
uses: [00GXTQMY8Z, 0GFKP8F8AG, 02WF878BH1, 0DQVHMYAGA, 0TPW25CBN6, 096PW7Q014]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
    locator: Integers modulo m
---

## Proof

1. Let $n$ be a positive integer and let $a$ be an integer. Let $d = \gcd(a, n)$ be their [[greatest common divisor|02WF878BH1]].
2. Since $n \ne 0$, the integers $a$ and $n$ are not both $0$. So $d$ is a positive common divisor of $a$ and $n$.
3. First assume that $a$ and $n$ are [[coprime|0GFKP8F8AG]], so $d = 1$.
4. By [[Bézout's identity|0DQVHMYAGA]], there are integers $x$ and $y$ with $a x + n y = 1$.
5. Then $a x - 1 = n (-y)$, so $n$ [[divides|096PW7Q014]] $a x - 1$. By the definition of [[congruence|0TPW25CBN6]], $a x \equiv 1 \pmod n$.
6. So $x$ is a [[modular multiplicative inverse|00GXTQMY8Z]] of $a$ modulo $n$.
7. Conversely, assume that $a$ has an inverse $x$ modulo $n$, so $a x \equiv 1 \pmod n$.
8. Then $n$ divides $a x - 1$, so there is an integer $y$ with $a x - 1 = n y$. That is, $a x - n y = 1$.
9. The integer $d$ divides $a$ and $n$, so it divides $a x - n y = 1$.
10. Since $d$ is positive by step 2 and divides $1$, we get $d = 1$. So $a$ and $n$ are coprime.
11. By steps 3 to 10, $a$ has an inverse modulo $n$ if and only if $a$ and $n$ are coprime.

## Idea

An inverse $x$ of $a$ is the same thing as a way to write $1 = a x + n y$. Bézout's identity gives such a way when $\gcd(a, n) = 1$. Conversely, any common divisor of $a$ and $n$ divides $a x + n y = 1$.
