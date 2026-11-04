---
tag: BZKSH32NRV
kind: proof
name: Proof that Fermat numbers are pairwise coprime
msc: [11A41]
proves: 05598J0Y8R
uses: [0R03B54V4Z, 0GFKP8F8AG, 0ASJVEFA9J, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat_number
    locator: Basic properties
---

## Proof

1. Let $F_k = 2^{2^k} + 1$ be the [[Fermat numbers|0R03B54V4Z]]. We first show, by [[induction|0ASJVEFA9J]] on $k \ge 1$, that $F_0 F_1 \cdots F_{k-1} = F_k - 2$.
2. For $k = 1$: $F_0 = 3$ and $F_1 - 2 = 5 - 2 = 3$.
3. Assume $F_0 \cdots F_{k-1} = F_k - 2$ for some $k \ge 1$. Then
$$F_0 \cdots F_k = (F_k - 2) F_k = (2^{2^k} - 1)(2^{2^k} + 1) = 2^{2^{k+1}} - 1 = F_{k+1} - 2.$$
This completes the induction.
4. Now let $m \ne n$ be natural numbers. We may assume $m < n$. Then $n \ge 1$, and $F_m$ is one of the factors $F_0, \dots, F_{n-1}$.
5. Let $d$ be a positive common divisor of $F_m$ and $F_n$. Then $d$ [[divides|096PW7Q014]] $F_0 \cdots F_{n-1} = F_n - 2$, by steps 1 and 4.
6. So $d$ divides $F_n - (F_n - 2) = 2$. Hence $d = 1$ or $d = 2$.
7. Every Fermat number is odd, since $2^{2^k}$ is even. So $d \ne 2$, and $d = 1$.
8. So the only positive common divisor of $F_m$ and $F_n$ is $1$. That is, $F_m$ and $F_n$ are [[coprime|0GFKP8F8AG]].

## Idea

The product of all earlier Fermat numbers is $2$ less than the next one. So a common divisor of two Fermat numbers must divide $2$. Fermat numbers are odd, so that divisor is $1$.
