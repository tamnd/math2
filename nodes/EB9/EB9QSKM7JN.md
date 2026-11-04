---
tag: EB9QSKM7JN
kind: proof
name: Proof that the integers modulo a prime form a field
msc: [11A07]
proves: 0R8YXRC9AJ
uses: [01N3AYAA6N, 0QRV8FPK5M, 0TPW25CBN6, 096PW7Q014, 0SN0MAEKYX, 02WF878BH1, 0DQVHMYAGA, 0QA8CHH8MG]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_arithmetic
    locator: Integers modulo m
---

## Proof

1. Let $p$ be a [[prime number|0SN0MAEKYX]]. For an integer $a$, write $\overline{a}$ for its [[residue class|0QRV8FPK5M]] modulo $p$.
2. By the definition of a residue class, $\overline{a} = \overline{b}$ if and only if $a \equiv b \pmod p$, that is, $p$ [[divides|096PW7Q014]] $a - b$.
3. The ring $\mathbb{Z}/p\mathbb{Z}$ of [[integers modulo p|01N3AYAA6N]] is commutative: $\overline{a} \cdot \overline{b} = \overline{a b} = \overline{b a} = \overline{b} \cdot \overline{a}$.
4. We have $\overline{1} \ne \overline{0}$. Indeed, $p > 1$, so $p$ does not divide $1 - 0 = 1$, and step 2 applies.
5. Let $\overline{a}$ be a nonzero element of $\mathbb{Z}/p\mathbb{Z}$. By step 2, $p$ does not divide $a$.
6. Let $d = \gcd(a, p)$ be the [[greatest common divisor|02WF878BH1]]. It is a positive divisor of $p$, so $d = 1$ or $d = p$, since $p$ is prime.
7. The integer $d$ divides $a$. Since $p$ does not divide $a$ by step 5, $d \ne p$. So $d = 1$.
8. By [[Bézout's identity|0DQVHMYAGA]], there are integers $x$ and $y$ with $a x + p y = 1$.
9. Then $a x - 1 = - p y$, so $p$ divides $a x - 1$. By step 2, $\overline{a x} = \overline{1}$.
10. Hence $\overline{a} \cdot \overline{x} = \overline{a x} = \overline{1}$, and $\overline{x}$ is a multiplicative inverse of $\overline{a}$.
11. By steps 3, 4 and 10, $\mathbb{Z}/p\mathbb{Z}$ is a commutative ring with $1 \ne 0$ in which each nonzero element has an inverse. So it is a [[field|0QA8CHH8MG]].

## Idea

A class $\overline{a}$ is nonzero exactly when $p \nmid a$. For a prime $p$, this forces $\gcd(a, p) = 1$, and Bézout's identity then writes $1$ as $a x$ plus a multiple of $p$, which is an inverse of $\overline{a}$.
