---
tag: P1ZMV5NQQJ
kind: statement
role: proposition
name: Wright's formula
sources:
  - wikipedia: en:509009@r1362701401
    locator: Formula for primes, section Wright's formula
    note: adopted
    mention: wikipedia://en/509009#N74G
    sections: [Statement]
inventory: [DJXE62D5X3]
---

## Statement

A tetrationally growing prime-generating formula similar to Mills' comes from a theorem of E. M. Wright. He proved that there exists a real number *α* such that, if

$g_0 = \alpha$ and

$g_{n+1} = 2^{g_n}$ for $n \ge 0$,

then

$$\lfloor g_n \rfloor = \left\lfloor 2^{\dots^{2^{2^\alpha}}} \right\rfloor$$

is prime for all $n \ge 1$. Wright gives the first seven decimal places of such a constant: $\alpha = 1.9287800$. This value gives rise to the primes $\lfloor g_1 \rfloor = \lfloor 2^{\alpha} \rfloor = 3$, $\lfloor g_2 \rfloor = 13$, and $\lfloor g_3 \rfloor = 16381$. $\lfloor g_4 \rfloor$ is even, and so is not prime. However, with $\alpha = 1.9287800 + 8.2843 \cdot 10^{-4933}$, $\lfloor g_1 \rfloor$, $\lfloor g_2 \rfloor$, and $\lfloor g_3 \rfloor$ are unchanged, while $\lfloor g_4 \rfloor$ is a prime with 4932 digits. This [[sequence|0G9EKM0E15]] of primes cannot be extended beyond $\lfloor g_4 \rfloor$ without knowing more digits of $\alpha$. Like Mills' formula, and for the same reasons, Wright's formula cannot be used to find primes.
