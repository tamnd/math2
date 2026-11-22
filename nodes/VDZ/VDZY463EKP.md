---
tag: VDZY463EKP
kind: example
name: Fermat's conjecture on Fermat numbers
msc: ["00A35", "11A41"]
topics: [N4P3E53HM0]
audience: school
instance_of: [WMEMMHZ3BH]
uses: [WMEMMHZ3BH, 0R03B54V4Z, 0N9E4G2P97, 0SN0MAEKYX, 0ED72CTBNP]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat_number
    locator: Primality
---

## Example

The [[Fermat numbers|0R03B54V4Z]] are the numbers $F_n = 2^{2^n} + 1$ for $n = 0, 1, 2, \ldots$.
Pierre de Fermat conjectured that every $F_n$ is [[prime|0SN0MAEKYX]].
We check the evidence that he had, and then the counterexample that Leonhard Euler found.

1. The first three are small enough to see at once.
   $$F_0 = 2^1 + 1 = 3, \qquad F_1 = 2^2 + 1 = 5, \qquad F_2 = 2^4 + 1 = 17.$$
   All three are prime.
2. $F_3 = 2^8 + 1 = 257$ is prime.
   A composite number has a prime factor at most its square root, and $16^2 = 256 < 257 < 17^2$, so it is enough to test $2, 3, 5, 7, 11, 13$, and none of them divides $257$.
3. $F_4 = 2^{16} + 1 = 65537$ is prime too.
   Trial division by the primes up to $256$ confirms this, since $256^2 = 65536 < 65537 < 257^2$.
4. The next one is $F_5 = 2^{32} + 1 = 4294967297$, since $2^{32} = 4294967296$.
5. Euler found the factor $641$, and we check the product $641 \times 6700417$ in two parts.
   $$6700417 \times 600 = 4020250200, \qquad 6700417 \times 41 = 268016680 + 6700417 = 274717097.$$
6. Add the two parts.
   $$4020250200 + 274717097 = 4294967297 = F_5.$$
7. So $F_5 = 641 \times 6700417$ with $1 < 641 < F_5$.
   It is not prime, it is a [[counterexample|0ED72CTBNP]], and the conjecture is false.

The multiplication checks the factor, but it does not explain why $641$ works.
Two facts about $641$ do that, working modulo $641$.

8. Since $641 = 5 \cdot 2^7 + 1$, we have $5 \cdot 2^7 \equiv -1$.
   Raising both sides to the fourth power gives $5^4 \cdot 2^{28} \equiv 1$.
9. Since $641 = 5^4 + 2^4 = 625 + 16$, we have $5^4 \equiv -2^4$.
10. Put step 9 into step 8.
    $$-2^4 \cdot 2^{28} \equiv 1, \quad \text{that is,} \quad 2^{32} \equiv -1 \pmod{641}.$$
11. So $641$ divides $2^{32} + 1 = F_5$.

## Remarks

The example shows a conjecture that five cases supported and that failed at the sixth.
The cases $F_0$ to $F_4$ were evidence, and they were not a proof.

Why is $641$ a natural number to try?
If a prime $p$ divides $F_5$, then $2^{32} \equiv -1 \pmod p$, so $2^{64} \equiv 1$.
The order of $2$ modulo $p$ divides $64$ but not $32$, so it is exactly $64$.
By [[Fermat's little theorem|0M25PRN3WQ]] the order also divides $p - 1$, so $p \equiv 1 \pmod{64}$.
The primes of this form are $193, 257, 449, 577, 641, \ldots$, and $641$ is the fifth one to test.

A [[Fermat prime|0N9E4G2P97]] is a Fermat number that is prime, and no Fermat prime larger than $F_4$ is known.
So the evidence now points the other way, but the statement "only finitely many $F_n$ are prime" is itself an open conjecture.
The numbers grow fast: $F_6 = 2^{64} + 1$ already has $20$ digits, so each new case is much harder to test than the last.

## Explanations

### L1 human

Fermat looked at the numbers $3$, $5$, $17$, $257$ and $65537$.
Each one is $1$ more than a power of $2$, and each one is prime.
He guessed that the next numbers in the list are prime as well.
The next number is $4294967297$, which is too big to test easily by hand.
Euler later showed that it equals $641$ times $6700417$, so the guess was wrong.

### L2 human

Here is a check of the claim that $F_6 = 2^{64} + 1$ has $20$ digits, using only $2^{10} = 1024$.
From below, $1024 > 10^3$ gives
$$2^{64} = 16 \cdot (2^{10})^6 > 16 \cdot 10^{18} = 1.6 \cdot 10^{19}.$$
From above, $1024 < 1.03 \cdot 10^3$ and $1.03^6 < 1.2$ give
$$2^{64} < 16 \cdot 1.2 \cdot 10^{18} < 2 \cdot 10^{19}.$$
So $10^{19} < F_6 < 10^{20}$, and $F_6$ has $20$ digits.
Check: the exact value is $F_6 = 18446744073709551617$, which has $20$ digits.
Watch out: five primes in a row are evidence for a pattern, not a proof of it, and here the sixth case breaks the pattern.
