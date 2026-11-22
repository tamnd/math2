---
tag: 9XRWP7QCP8
kind: example
name: Euler's theorem is stronger than Fermat's little theorem
msc: ["00A35", "11A07"]
topics: [Z2WNQ1DNTX]
audience: ug1
instance_of: [KCK4AQ469Q]
uses: [KCK4AQ469Q, 0VC4DVE7DQ, 0M25PRN3WQ, 0DAMHCT17R, 3C53TD]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Descriptive informalities
  - url: https://en.wikipedia.org/wiki/Euler%27s_theorem
    locator: lead section
---

## Example

[[Fermat's little theorem|0M25PRN3WQ]] says: if $p$ is prime and $a$ is an integer not divisible by $p$, then $a^{p-1} \equiv 1 \pmod{p}$.
[[Euler's theorem|0VC4DVE7DQ]] says: if $n \ge 1$ and $\gcd(a, n) = 1$, then $a^{\varphi(n)} \equiv 1 \pmod{n}$, where $\varphi$ is [[Euler's totient function|0DAMHCT17R]].
We check that Euler's theorem is [[stronger|KCK4AQ469Q]] than Fermat's theorem.

1. Assume Euler's theorem.
   Let $p$ be prime and let $a$ be an integer not divisible by $p$.
2. The only positive divisors of $p$ are $1$ and $p$, and $p$ does not divide $a$, so $\gcd(a, p) = 1$.
3. Each of $1, 2, \ldots, p - 1$ is coprime to $p$, and $p$ is not, so $\varphi(p) = p - 1$.
4. Euler's theorem with $n = p$ gives $a^{p-1} \equiv 1 \pmod{p}$, which is Fermat's theorem.
5. Euler's theorem covers cases that Fermat's theorem does not.
   For $n = 8$, the numbers coprime to $8$ in $\{1, \ldots, 8\}$ are $1, 3, 5, 7$, so $\varphi(8) = 4$.
6. With $a = 3$, Euler's theorem gives $3^4 \equiv 1 \pmod{8}$.
   Check: $3^4 = 81 = 10 \cdot 8 + 1$.
   Fermat's theorem says nothing here, because $8$ is not prime.

## Remarks

Steps 1 to 4 show that Euler's theorem gives Fermat's theorem by a short argument.
Steps 5 and 6 show that Euler's theorem has more cases, so it is stronger in the informal sense used for proved theorems.
Both theorems are true, so as bare statements each one implies the other; the comparison is about which one gives the other directly.

[[Lagrange's theorem|3C53TD]] on groups is stronger still.
The units modulo $n$ form a group with $\varphi(n)$ elements, so the order of every unit divides $\varphi(n)$, and that is Euler's theorem.

## Explanations

### L1 human

Fermat's theorem is a rule for remainders when we divide by a prime, such as $7$.
Euler's theorem is a rule of the same kind for division by any number, such as $8$ or $10$.
When the number is prime, Euler's rule becomes Fermat's rule.
So Euler's rule includes Fermat's rule and says more.

### L2 human

Test both theorems on small cases.
Fermat with $p = 5$ and $a = 2$:
$$2^4 = 16 = 3 \cdot 5 + 1, \qquad \text{so } 2^4 \equiv 1 \pmod{5}.$$
Euler with $n = 10$ and $a = 3$: the numbers coprime to $10$ in $\{1, \ldots, 10\}$ are $1, 3, 7, 9$, so $\varphi(10) = 4$, and
$$3^4 = 81 = 8 \cdot 10 + 1, \qquad \text{so } 3^4 \equiv 1 \pmod{10}.$$
The second case is not a case of Fermat's theorem, because $10$ is not prime.

The typical use of Euler's theorem is to compute large powers modulo a composite number.
Watch out: the hypothesis $\gcd(a, n) = 1$ is needed, since $a = 2$ and $n = 10$ give $2^4 = 16 \equiv 6 \pmod{10}$.
