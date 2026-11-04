---
tag: CTKD74QERT
kind: proof
name: Proof that the p-adic valuation of a product is the sum of the valuations
msc: [11A51]
proves: 0850JJMJYZ
uses: [04VCPS30ZE, 051VYKA1EX, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/P-adic_valuation
---

## Proof

1. Let $p$ be a prime and let $a$, $b$ be nonzero integers. Put $\alpha = \nu_p(a)$ and $\beta = \nu_p(b)$, where $\nu_p$ is the [[p-adic valuation|04VCPS30ZE]].
2. Since $p^\alpha \mid a$, write $a = p^\alpha a'$ with an integer $a'$. Then $a' \neq 0$.
3. We have $p \nmid a'$. Otherwise $a' = p c$ for an integer $c$, so $a = p^{\alpha + 1} c$ and $p^{\alpha+1} \mid a$. This contradicts the maximality of $\alpha$.
4. In the same way, $b = p^\beta b'$ with an integer $b'$ and $p \nmid b'$.
5. Then $a b = p^{\alpha + \beta} a' b'$. Since $a b \neq 0$, $\nu_p(ab)$ is a natural number. Since $p^{\alpha + \beta} \mid ab$, $\nu_p(ab) \ge \alpha + \beta$.
6. Suppose $p^{\alpha + \beta + 1} \mid ab$. Then $p^{\alpha + \beta} a' b' = p^{\alpha + \beta + 1} d$ for an integer $d$.
7. Cancelling the nonzero factor $p^{\alpha + \beta}$ gives $a' b' = p d$, so $p \mid a' b'$.
8. By [[Euclid's lemma|051VYKA1EX]], $p \mid a'$ or $p \mid b'$. This contradicts steps 3 and 4.
9. So $p^{\alpha + \beta + 1} \nmid ab$. If $k > \alpha + \beta$ and $p^k \mid ab$, then $p^{\alpha + \beta + 1} \mid ab$, since $p^{\alpha+\beta+1}$ [[divides|096PW7Q014]] $p^k$. Hence no such $k$ exists.
10. Therefore $\nu_p(ab) = \alpha + \beta = \nu_p(a) + \nu_p(b)$.

## Idea

Pull out of $a$ and $b$ all the factors $p$ they contain. The parts that remain are not divisible by $p$, and by Euclid's lemma neither is their product. So the product contains exactly $\alpha + \beta$ factors $p$.
