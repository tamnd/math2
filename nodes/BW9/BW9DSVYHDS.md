---
tag: BW9DSVYHDS
kind: definition
name: Quadratic residue code
msc: [94B15, 11T71]
defines: SS8ZNM2TG7
uses: [E04GGZ1Q91, 0DKCECSYCF, 0EHM5ZP5QH, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_residue_code
---

## Definition

Let $p$ be an odd prime and let $q$ be a prime with $q \ne p$ such that $q$ is a [[quadratic residue|0DKCECSYCF]] modulo $p$.
Let $Q \subseteq \set{1, \dots, p - 1}$ be the set of nonzero quadratic residues modulo $p$.
Let $\beta$ be a [[primitive $p$-th root of unity|0EHM5ZP5QH]] in an extension field of the [[finite field|0ZXZ82FTX2]] $\F_q$, and put
$$g_Q(x) = \prod_{r \in Q} (x - \beta^r).$$
The *quadratic residue code* of length $p$ over $\F_q$ is the [[cyclic code|E04GGZ1Q91]] of length $p$ over $\F_q$ with generator polynomial $g_Q$.

## Remarks

The coefficients of $g_Q$ lie in $\F_q$: the Frobenius map sends $\beta^r$ to $\beta^{qr}$, and $qr$ is again a quadratic residue because $q$ is one.
Since $\abs{Q} = (p - 1)/2$, the code has dimension $p - (p - 1)/2 = (p + 1)/2$.
Its minimum distance $d$ satisfies $d^2 \ge p$, and $d^2 - d + 1 \ge p$ when $p \equiv -1 \pmod 4$.
Using the non-residues instead of $Q$ gives an equivalent code.
For $q = 2$, the condition on $q$ means $p \equiv \pm 1 \pmod 8$.

Example: $q = 2$ and $p = 7$.
The squares modulo $7$ are $Q = \set{1, 2, 4}$, and $2 \in Q$.
For a root $\beta$ of $x^3 + x + 1$ in $\F_8$, the roots of $x^3 + x + 1$ are $\beta, \beta^2, \beta^4$, so $g_Q = x^3 + x + 1$ and the code is the $[7, 4, 3]$ [[Hamming code|D68NF1S2NW]].
Here $d^2 - d + 1 = 7 \ge p$, with equality.
Other examples: $q = 2$, $p = 23$ gives the binary Golay code $[23, 12, 7]$, and $q = 3$, $p = 11$ gives the [[ternary Golay code|ERXD4K3GHG]] $[11, 6, 5]$.

Non-example: $q = 2$ and $p = 5$.
The squares modulo $5$ are $1, 4$, so $2$ is not a quadratic residue.
Indeed $(x - \beta)(x - \beta^4)$ is not fixed by the Frobenius map, which sends $\beta$ to $\beta^2$, so it does not have coefficients in $\F_2$.
