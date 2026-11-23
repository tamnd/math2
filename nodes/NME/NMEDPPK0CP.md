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

We find the last two digits of $3^{100}$, that is, its remainder modulo $100$.
The number $3^{100}$ has $48$ digits, so we do not compute it.
Instead we [[decompose|KEZPDNM2NH]] the modulus as $100 = 4 \cdot 25$, with $4$ and $25$ coprime, solve the problem modulo each factor, and recombine.

1. Modulo $4$ we have $3 \equiv -1$, so $3^{100} \equiv (-1)^{100} = 1 \pmod 4$.
2. Modulo $25$ we have $3^5 = 243 = 9 \cdot 25 + 18$, so $3^5 \equiv 18 \equiv -7 \pmod{25}$.
3. Squaring gives $3^{10} \equiv 49 \equiv -1 \pmod{25}$, and squaring again gives $3^{20} \equiv 1 \pmod{25}$.
4. So $3^{100} = (3^{20})^5 \equiv 1 \pmod{25}$.
5. We need $x$ with $0 \le x < 100$, $x \equiv 1 \pmod 4$ and $x \equiv 1 \pmod{25}$, and $x = 1$ satisfies both.
6. By the [[Chinese remainder theorem|0FNN9B4W64]] the solution modulo $100$ is unique, so $3^{100} \equiv 1 \pmod{100}$.

The last two digits of $3^{100}$ are $01$.
Check modulo $100$ directly: $3^{10} = 59049 \equiv 49$, so $3^{20} \equiv 49^2 = 2401 \equiv 1$, and $3^{100} \equiv 1$.

## Remarks

Step 3 can be replaced by [[Euler's theorem|0VC4DVE7DQ]]: $\varphi(25) = 20$ and $\gcd(3, 25) = 1$, so $3^{20} \equiv 1 \pmod{25}$.
For this base, Euler's theorem modulo $100$ also works directly, since $\varphi(100) = 40$ and $\gcd(3, 100) = 1$.
The decomposition becomes necessary for a base that is not coprime to $100$.

Change the base to $2$, and Euler's theorem modulo $100$ no longer applies, since $\gcd(2, 100) = 2$.
The decomposition still works.
Modulo $4$ the power $2^{100}$ is $0$, and modulo $25$ we have $2^{10} = 1024 \equiv -1$, so $2^{100} \equiv 1$.
Among the numbers $1, 26, 51, 76$ that are $1$ modulo $25$, only $76$ is divisible by $4$, so $2^{100}$ ends in $76$.

## Explanations

### L1 human

The last two digits of a number are its remainder when you divide by $100$.
Instead of dividing by $100$, divide by $4$ and by $25$, which is easier, because $100 = 4 \cdot 25$.
Powers of $3$ repeat their remainders in short cycles for each of these small numbers.
Both remainders turn out to be $1$, and the only two-digit ending with both remainders $1$ is $01$.

### L2 human

Here is the method for the remainder of $a^n$ modulo $m = m_1 m_2$, with $\gcd(m_1, m_2) = 1$.
First find $r_1 = a^n \bmod m_1$ and $r_2 = a^n \bmod m_2$, where the smaller moduli give shorter cycles of powers.
Then list the numbers $r_2, r_2 + m_2, r_2 + 2m_2, \dots$ below $m$ and keep the one that is $r_1$ modulo $m_1$.
The Chinese remainder theorem says that this number is unique, so it is the remainder of $a^n$ modulo $m$.

For $7^{100}$, the square $7^2 = 49 \equiv -1 \pmod{25}$ gives
$$7^{100} = (7^2)^{50} \equiv (-1)^{50} = 1 \pmod{25},$$
and $7^{100} \equiv (-1)^{100} = 1 \pmod 4$, so $7^{100}$ ends in $01$.

The factors must be coprime.
The split $100 = 10 \cdot 10$ fails, since two remainders modulo $10$ give only the last digit.
