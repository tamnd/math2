---
tag: 0ZEPNS9BXK
kind: statement
role: theorem
name: g to the power of the group order is 1
aliases: [power-of-the-group-order-is-identity, g-to-the-order-of-the-group-is-the-identity]
msc: ["20D60"]
topics: [1VHQWXC64D]
audience: ug1
about: [0B85S2V2DR, 0WE2NHZJ7B]
uses: [G5S1M9, 0B85S2V2DR, 0WE2NHZJ7B, 08V7JHS3QZ, 0F5QC101Q7]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange's_theorem_(group_theory)
    locator: Applications
  - url: https://en.wikipedia.org/wiki/Euler%27s_theorem
    locator: Proofs
  - book: isbn:9780471433347
    locator: Section 3.2
---

## Statement

Let $G$ be a finite [[group|G5S1M9]] with identity element $e$, and let $g \in G$.
Then $g^{|G|} = e$, where $|G|$ is the [[order|0B85S2V2DR]] of $G$.
In multiplicative notation the identity is often written $1$, as in the name of this theorem.

## Remarks

### Why each hypothesis is needed

- The group $G$ must be finite. In $(\mathbb{Z}, +)$, no multiple $n \cdot 1$ with $n \geq 1$ is $0$, and $|\mathbb{Z}|$ is not a natural number.
- The structure must be a group. In the finite monoid $(\{0, 1, 2, 3\}, \cdot)$ of residues modulo $4$ under multiplication, $2^4 = 16 \equiv 0$, which is not the identity $1$.

### Consequences

- [[Fermat's little theorem|0M25PRN3WQ]]: if $p$ is prime and $p \nmid a$, then $a^{p - 1} \equiv 1 \pmod p$. Apply the theorem to the [[group of units|0F8X8ZRQ53]] $(\mathbb{Z}/p\mathbb{Z})^\times$, of order $p - 1$.
- [[Euler's theorem|0VC4DVE7DQ]]: if $\gcd(a, n) = 1$, then $a^{\varphi(n)} \equiv 1 \pmod n$. Apply the theorem to $(\mathbb{Z}/n\mathbb{Z})^\times$, whose [[order is $\varphi(n)$|0S7495H4HM]], where $\varphi$ is [[Euler's totient function|0DAMHCT17R]].
- For each integer $k$, $g^k = g^{k \bmod |G|}$. So a large power can be computed with a small exponent.
- The inverse of $g$ is $g^{|G| - 1}$.

### Converse

The converse asks: if $n \geq 1$ and $g^n = e$ for each $g \in G$, is $n$ a multiple of $|G|$?
This is false.
In the [[Klein four-group|0PMRQJVTME]], $g^2 = e$ for each $g$, but $2$ is not a multiple of $4$.
The least such $n$ is the [[exponent|0ZDW0H0VX4]] of $G$, and it divides $|G|$, but it can be smaller.

### Generalizations

- If $\exp(G)$ is the exponent of $G$, then $g^{\exp(G)} = e$ for each $g$. This is stronger, because $\exp(G)$ divides $|G|$.
- For the units modulo $n$, the exponent is the Carmichael function $\lambda(n)$. Thus $a^{\lambda(n)} \equiv 1 \pmod n$ when $\gcd(a, n) = 1$. For example, $\lambda(8) = 2$, while $\varphi(8) = 4$.

## History

Fermat stated his little theorem without proof in a letter of 1640.
Euler published a proof in 1736.
In a paper of 1763, Euler proved the generalization to a modulus $n$ that is not prime, with $\varphi(n)$ in place of $p - 1$.

## Explanations

### L1 human

If a group has $n$ elements, then the $n$-th power of each element is the identity.
For example, the numbers $1$ to $6$ form a group under multiplication modulo $7$.
This group has $6$ elements.
So $3^6$ leaves remainder $1$ after division by $7$.
Indeed $3^6 = 729 = 104 \cdot 7 + 1$.

### L2 human

We compute $5^{100} \bmod 7$.

1. The number $5$ is a unit modulo $7$, and $(\mathbb{Z}/7\mathbb{Z})^\times$ has order $6$.
2. By the theorem, $5^6 \equiv 1 \pmod 7$.
3. We divide: $100 = 16 \cdot 6 + 4$.
4. So $5^{100} = (5^6)^{16} \cdot 5^4 \equiv 5^4 \pmod 7$.
5. We compute $5^2 = 25 \equiv 4$ and $5^4 \equiv 4^2 = 16 \equiv 2 \pmod 7$.
6. Thus $5^{100} \equiv 2 \pmod 7$.

The typical use is to reduce large exponents, as in the RSA cryptosystem.
A trap is to use the theorem for an element that is not in the group.
The number $2$ is not a unit modulo $4$, and $2^{\varphi(4)} = 2^2 = 4 \equiv 0 \pmod 4$.

### L3 human

The theorem says that the exponent of a finite group divides its order.
For finite abelian groups, the exponent equals the order exactly when the group is cyclic.
For the units modulo $n$, this is the question of a primitive root: $(\mathbb{Z}/n\mathbb{Z})^\times$ is cyclic exactly when $n$ is $1$, $2$, $4$, $p^k$ or $2p^k$ for an odd prime $p$.
In a finite field $\mathbb{F}_q$, the theorem for the group $\mathbb{F}_q^\times$ of order $q - 1$ gives $x^q = x$ for each $x \in \mathbb{F}_q$.
So the elements of $\mathbb{F}_q$ are exactly the roots of $x^q - x$.
