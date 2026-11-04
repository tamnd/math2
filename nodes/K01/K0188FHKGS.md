---
tag: K0188FHKGS
kind: proof
name: Proof of the Chinese remainder theorem for non-coprime moduli
msc: [11A07]
proves: 04SJTX9P4N
uses: [0TPW25CBN6, 096PW7Q014, 02WF878BH1, 09S5SN35DJ, 0DQVHMYAGA, 0CHQKZFK5S]
methods: [01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    locator: Generalization to non-coprime moduli
---

## Proof

1. Let $m$ and $n$ be positive integers and let $a$ and $b$ be integers. Let $g = \gcd(m, n)$ be the [[greatest common divisor|02WF878BH1]] and $M = \operatorname{lcm}(m, n)$ the [[least common multiple|09S5SN35DJ]].
2. Since $m$ and $n$ are positive, $g$ is a positive common divisor of $m$ and $n$. Also, $M$ is the smallest positive common multiple of $m$ and $n$.
3. Necessity. Let $x$ be a solution. By the definition of [[congruence|0TPW25CBN6]], $m$ [[divides|096PW7Q014]] $x - a$ and $n$ divides $x - b$.
4. Since $g$ divides $m$ and $n$, step 3 shows that $g$ divides $x - a$ and $x - b$. So $g$ divides $(x - b) - (x - a) = a - b$, and $a \equiv b \pmod g$.
5. Sufficiency. Assume $a \equiv b \pmod g$, and write $a - b = g t$ with an integer $t$.
6. By [[Bézout's identity|0DQVHMYAGA]], there are integers $u$ and $v$ with $m u + n v = g$.
7. Let $x = a - m u t$. Then $x - a = m (- u t)$, so $x \equiv a \pmod m$.
8. By steps 5 and 6, $x - b = (a - b) - m u t = g t - m u t = (g - m u) t = n v t$. So $x \equiv b \pmod n$, and $x$ is a solution.
9. Uniqueness. Let $x$ and $y$ be two solutions, and let $c = x - y$.
10. The integer $m$ divides $x - a$ and $y - a$, so it divides their difference $c$. In the same way, $n$ divides $c$.
11. By the [[division algorithm|0CHQKZFK5S]], there are integers $q$ and $r$ with $c = q M + r$ and $0 \le r < M$.
12. Since $m$ divides $c$ and $M$, it divides $r = c - q M$. In the same way, $n$ divides $r$. So $r$ is a common multiple of $m$ and $n$.
13. If $r > 0$, then $r$ is a positive common multiple smaller than $M$, which contradicts step 2. So $r = 0$.
14. Hence $M$ divides $c = x - y$, that is, $x \equiv y \pmod M$.
15. By steps 4, 8 and 14, the system has a solution if and only if $a \equiv b \pmod g$, and then two solutions are congruent modulo $M$.

## Idea

A solution forces $a$ and $b$ to agree modulo every common divisor of the moduli. Conversely, Bézout's identity writes $g$ as $m u + n v$. Multiplying by $t = (a - b) / g$ splits $a - b$ into a multiple of $m$ plus a multiple of $n$. Removing the multiple of $m$ from $a$ lands on $b$ plus a multiple of $n$.
