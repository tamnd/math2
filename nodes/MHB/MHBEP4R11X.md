---
tag: MHBEP4R11X
kind: proof
name: Proof of the freshman's dream
msc: [13A35]
proves: 0396VGFA78
uses: [0GYGHKX834, 0P7CH1CND5, 0EHWPWGHB2, 092GEF38YD, 033KTKKRV6, 051VYKA1EX, 0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Freshman%27s_dream
    locator: Prime characteristic
---

## Proof

1. Let $p$ be a [[prime number|0SN0MAEKYX]] and let $R$ be a [[commutative ring|0GYGHKX834]] of [[characteristic|0P7CH1CND5]] $p$. So $p \cdot 1 = 0$ in $R$. Let $x, y \in R$.
2. By the [[binomial theorem|0EHWPWGHB2]], $(x + y)^p = \sum_{k=0}^{p} \binom{p}{k} x^k y^{p-k}$.
3. Fix an integer $k$ with $0 < k < p$. By the [[factorial formula|033KTKKRV6]], $\binom{p}{k} \cdot k! \cdot (p-k)! = p!$.
4. The prime $p$ divides $p!$. So $p$ divides the product $\binom{p}{k} \cdot k! \cdot (p-k)!$.
5. The number $k! \, (p-k)!$ is a product of integers from $1$ to $p - 1$. None of these factors is divisible by $p$.
6. So $p \nmid k! \, (p-k)!$, by [[Euclid's lemma|051VYKA1EX]] applied to one factor at a time.
7. By Euclid's lemma and steps 4 and 6, $p$ divides the [[binomial coefficient|092GEF38YD]] $\binom{p}{k}$. Write $\binom{p}{k} = p t$ with an integer $t \ge 1$.
8. Let $z = x^k y^{p-k}$. Then $\binom{p}{k} z = t \cdot (p \cdot z)$, a sum of $t$ copies of $p \cdot z$.
9. By the distributive law, $p \cdot z = (p \cdot 1) z = 0 \cdot z = 0$. So $\binom{p}{k} x^k y^{p-k} = 0$.
10. Thus only the terms with $k = 0$ and $k = p$ remain in step 2. Their coefficients are $\binom{p}{0} = \binom{p}{p} = 1$.
11. Hence $(x + y)^p = y^p + x^p = x^p + y^p$.

## Idea

Expand with the binomial theorem. Every middle coefficient $\binom{p}{k}$ is a multiple of $p$, because $p$ appears in $p!$ but not in $k! \, (p-k)!$. In characteristic $p$, multiples of $p$ act as zero, so only $x^p$ and $y^p$ survive.
