---
tag: 6F0TZ1TM4T
kind: definition
name: BCH code
msc: [94B15, 11T71]
defines: YY5ZM93GBY
uses: [E04GGZ1Q91, 0ZXZ82FTX2, 0EHM5ZP5QH, 03NDVCSHSB, M2X88AXM17]
sources:
  - url: https://en.wikipedia.org/wiki/BCH_code
---

## Definition

Let $q$ be a prime power and let $n \ge 2$ be an integer with $\gcd(n, q) = 1$.
Let $m$ be the order of $q$ modulo $n$, and let $\alpha$ be a [[primitive $n$-th root of unity|0EHM5ZP5QH]] in the [[finite field|0ZXZ82FTX2]] $\F_{q^m}$.
Let $b \ge 0$ and $\delta$ be integers with $2 \le \delta \le n$.
For each integer $i$, let $M_i(x) \in \F_q[x]$ be the [[minimal polynomial|03NDVCSHSB]] of $\alpha^i$ over $\F_q$.
The *BCH code* of length $n$ over $\F_q$ with designed distance $\delta$ is the [[cyclic code|E04GGZ1Q91]] of length $n$ over $\F_q$ with generator polynomial
$$g(x) = \lcm\big(M_b(x), M_{b+1}(x), \dots, M_{b+\delta-2}(x)\big).$$
The code is *narrow-sense* if $b = 1$, and *primitive* if $n = q^m - 1$.

## Remarks

The polynomial $g$ divides $x^n - 1$, because each $\alpha^i$ is a root of $x^n - 1$ and $x^n - 1$ has no repeated roots when $\gcd(n, q) = 1$.
So $g$ defines a cyclic code of dimension $n - \deg g \ge n - m(\delta - 1)$, since each $M_i$ has degree at most $m$.
By the [[BCH bound|CT69XTRW2K]], its [[minimum distance|M2X88AXM17]] is at least $\delta$.
In the binary narrow-sense case, $M_{2i} = M_i$, so for $\delta = 2t + 1$ only the odd indices matter and the dimension is at least $n - mt$.

Example: take $q = 2$, $n = 7$, so $m = 3$, and let $\alpha \in \F_8$ be a root of $x^3 + x + 1$.
The conjugates of $\alpha$ are $\alpha, \alpha^2, \alpha^4$, so $M_1 = M_2 = x^3 + x + 1$.
With $b = 1$ and $\delta = 3$, the generator is $g = x^3 + x + 1$, and the code is the $[7, 4, 3]$ [[Hamming code|D68NF1S2NW]].
With $\delta = 5$, one also needs $M_3 = x^3 + x^2 + 1$, so $g = (x^3 + x + 1)(x^3 + x^2 + 1)$ has degree $6$ and the code is the binary repetition code of length $7$.

Non-example: over $\F_2$ the length $n = 6$ is not allowed, since $\gcd(6, 2) \ne 1$.
Then $x^6 - 1 = (x^3 - 1)^2$ has repeated roots, and no field of characteristic $2$ contains a primitive $6$-th root of unity.
