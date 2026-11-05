---
tag: NVEK5W5AFK
kind: statement
role: proposition
name: Landau's inequality
sources:
  - wikipedia: en:9232272@r1307915643
    locator: Geometrical properties of polynomial roots, section Landau's inequality
    note: adopted
    mention: wikipedia://en/9232272#HJP3
    sections: [Statement]
inventory: [3JC4MBD02T]
---

## Statement

The previous bounds are upper bounds for each root separately. **Landau's inequality** provides an upper bound for the absolute values of the product of the roots that have an absolute value greater than one. This inequality, discovered in 1905 by Edmund Landau, has been forgotten and rediscovered at least three times during the 20th century.

This bound of the product of roots is not much greater than the best preceding bounds of each root separately. Let $z_1, \ldots, z_n$ be the $n$ roots of the polynomial $p$. If

$$M(p)=|a_n|\prod_{j=1}^n \max(1,|z_j|)$$

is the Mahler measure of $p$, then

$$M(p)\le \sqrt{\sum_{k=0}^n |a_k|^2}.$$

Surprisingly, this bound of the product of the absolute values larger than 1 of the roots is not much larger than the best bounds of *one* root that have been given above for a single root. This bound is even exactly equal to one of the bounds that are obtained using Hölder's inequality.

This bound is also useful to bound the coefficients of a divisor of a polynomial with integer coefficients: if

$$q= \sum_{k=0}^m b_k x^k$$

is a divisor of $p$, then

$$|b_m|\le|a_n|,$$

and, by [[Vieta's formulas|0M8EWQJ1YV]],

$$\frac{|b_i|}{|b_m|}\le \binom mi \frac{M(p)}{|a_n|},$$

for $i = 0, ..., m$, where $\binom mi$ is a [[binomial coefficient|092GEF38YD]]. Thus

$$|b_i|\le \binom mi M(p)\le \binom mi \sqrt{\sum_{k=0}^n |a_k|^2},$$

and

$$\sum_{i=0}^m |b_i| \le 2^m M(p) \le 2^m \sqrt{\sum_{k=0}^n |a_k|^2}.$$
