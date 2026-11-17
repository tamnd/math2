---
tag: NMEDPPK0CP
kind: example
name: The last two digits of 3^100, found modulo 4 and modulo 25
msc: ["00A35", "11A07"]
topics: [X1NSTVGDNQ]
audience: ug1
instance_of: [KEZPDNM2NH]
uses: [KEZPDNM2NH, 0FNN9B4W64, 0VC4DVE7DQ]
sources:
  - url: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    locator: lead section
---

## Example

Problem: find the last two digits of $3^{100}$, that is, the remainder of $3^{100}$ modulo $100$.
The number $3^{100}$ has $48$ digits, so we do not compute it.
We [[decompose|KEZPDNM2NH]] the modulus: $100 = 4 \cdot 25$, and $4$ and $25$ are coprime.
We solve the problem modulo $4$ and modulo $25$, then recombine.

1. Modulo $4$: $3 \equiv -1$, so $3^{100} \equiv (-1)^{100} = 1 \pmod 4$.
2. Modulo $25$: $3^5 = 243 = 9 \cdot 25 + 18$, so $3^5 \equiv 18 \equiv -7 \pmod{25}$.
3. Then $3^{10} \equiv 49 \equiv -1 \pmod{25}$, and $3^{20} \equiv 1 \pmod{25}$.
4. So $3^{100} = (3^{20})^5 \equiv 1 \pmod{25}$.
5. Recombine: we need $x$ with $0 \leq x < 100$, $x \equiv 1 \pmod 4$ and $x \equiv 1 \pmod{25}$. The number $x = 1$ satisfies both.
6. By the [[Chinese remainder theorem|0FNN9B4W64]], the solution modulo $100$ is unique, so $3^{100} \equiv 1 \pmod{100}$.

The last two digits of $3^{100}$ are $01$.
A direct check by fast modular exponentiation gives the same remainder, $1$.

## Remarks

Step 3 can be replaced by [[Euler's theorem|0VC4DVE7DQ]]: $\varphi(25) = 20$ and $\gcd(3, 25) = 1$, so $3^{20} \equiv 1 \pmod{25}$.
Euler's theorem modulo $100$ gives $3^{40} \equiv 1 \pmod{100}$, since $\varphi(100) = 40$, and this also solves the problem.
The decomposition becomes necessary for a base that is not coprime to $100$.

For $2^{100}$, Euler's theorem modulo $100$ does not apply, since $\gcd(2, 100) = 2$.
The decomposition still works.
Modulo $4$: $2^{100} \equiv 0$, since $4 \mid 2^2$.
Modulo $25$: $2^{10} = 1024 \equiv -1$, so $2^{20} \equiv 1$ and $2^{100} \equiv 1$.
The number between $0$ and $99$ that is $0$ modulo $4$ and $1$ modulo $25$ is found among $1, 26, 51, 76$; only $76$ is divisible by $4$.
So the last two digits of $2^{100}$ are $76$.

## Explanations

### L1 human

The last two digits of a number are its remainder when divided by $100$.
Instead of dividing by $100$, we divide by $4$ and by $25$, which are easier, because $100 = 4 \cdot 25$.
Powers of $3$ repeat their remainders in short cycles for each of these small numbers.
Both remainders turn out to be $1$, and the only two-digit ending with both remainders $1$ is $01$.
So $3^{100}$ ends in $01$.

### L2 human

We state the method for the remainder of $a^n$ modulo $m$, where $m = m_1 m_2$ with $\gcd(m_1, m_2) = 1$.

1. Find $r_1 = a^n \bmod m_1$ and $r_2 = a^n \bmod m_2$. Each modulus is smaller, so the cycles of powers are shorter.
2. Find the unique $x$ with $0 \leq x < m$, $x \equiv r_1 \pmod{m_1}$ and $x \equiv r_2 \pmod{m_2}$. In practice, list the numbers $r_2, r_2 + m_2, r_2 + 2m_2, \ldots$ below $m$ and keep the one that is $r_1$ modulo $m_1$.
3. The Chinese remainder theorem says that this $x$ is unique, so $a^n \equiv x \pmod m$.

For $7^{100}$ modulo $100$: $7^2 = 49 \equiv -1 \pmod{25}$, so $7^{100} = (7^2)^{50} \equiv 1 \pmod{25}$, and $7^{100} \equiv (-1)^{100} = 1 \pmod 4$, so $7^{100}$ ends in $01$.

The typical use: a composite modulus splits into coprime prime powers, and each part is handled separately.

A trap: the parts must be coprime, and the splitting $100 = 10 \cdot 10$ does not work, since a remainder modulo $10$ twice gives only the last digit.
