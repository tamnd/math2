---
tag: JR1Z7GC7J0
kind: proof
name: Proof of the density of the irrationals
msc: [26A03]
proves: 04J6G4H78J
uses: [0STX0WRDNG, 068BZBXE0C, 0DZGSDHD92, 080T2TXVQV, 0NCJ5WXN6Z, 0QSPNASE50]
sources:
  - url: https://proofwiki.org/wiki/Between_two_Real_Numbers_exists_Irrational_Number
---

## Proof

1. Let $x$ and $y$ be real numbers with $x < y$.
2. By the [[existence of square roots|068BZBXE0C]], there is a real $s \ge 0$ with $s^2 = 2$. Since $s^2 \ne 0$, we have $s \ne 0$, so $s > 0$.
3. The number $s$ is irrational, by the [[irrationality of the square root of 2|0DZGSDHD92]].
4. Dividing by $s > 0$ keeps the order in the [[ordered field|0QSPNASE50]] $\R$. So $x/s < y/s$.
5. By the [[density of the rationals|0STX0WRDNG]], there is a rational $q_1$ with $x/s < q_1 < y/s$. Again by density, there is a rational $q_2$ with $q_1 < q_2 < y/s$.
6. Since $q_1 \ne q_2$, at least one of them is nonzero. Call it $q$. Then $q$ is rational, $q \ne 0$ and $x/s < q < y/s$.
7. Multiply by $s > 0$: $x < q s < y$. Let $z = q s$.
8. Suppose $z$ is a [[rational number|0NCJ5WXN6Z]] $r$. Then $s = r/q$ is a quotient of rationals with $q \ne 0$, so $s$ is rational. This contradicts step 3.
9. So $z$ is an [[irrational number|080T2TXVQV]] with $x < z < y$.

## Idea

A nonzero rational multiple of $\sqrt{2}$ is irrational. Scale the interval by $1/\sqrt{2}$, find a nonzero rational inside it, and scale back.
