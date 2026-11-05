---
tag: HMKY4VCWBQ
kind: statement
role: proposition
name: Liouville's transcendence criterion
sources:
  - wikipedia: en:11826062@r1245763119
    locator: Auxiliary function, section Explicit functions > Liouville's transcendence criterion
    note: adopted
    mention: wikipedia://en/11826062#KFNE
    sections: [Statement]
inventory: [G76C7RMSKH]
---

## Statement

Because of the naming convention mentioned above, auxiliary functions can be dated back to their source simply by looking at the earliest results in transcendence theory. One of these first results was Liouville's proof that transcendental numbers exist when he showed that the so called [[Liouville numbers|0J1R5NP36S]] were transcendental. He did this by discovering a transcendence criterion which these numbers satisfied. To derive this criterion he started with a general [[algebraic number|0MB4TGMXG6]] α and found some property that this number would necessarily satisfy. The auxiliary function he used in the course of proving this criterion was simply the [[minimal polynomial|0VX9EP2GS8]] of α, which is the irreducible polynomial *f* with integer coefficients such that *f*(α) = 0. This function can be used to estimate how well the algebraic number α can be estimated by [[rational numbers|0NCJ5WXN6Z]] *p*/*q*. Specifically if α has degree *d* at least two then he showed that

$$\left|f\left(\frac{p}{q}\right)\right|\geq\frac{1}{q^d},$$

and also, using the [[mean value theorem|0BARQY52N5]], that there is some constant depending on α, say *c*(α), such that

$$\left|f\left(\frac{p}{q}\right)\right| \leq c(\alpha)\left|\alpha-\frac{p}{q}\right|.$$

Combining these results gives a property that the algebraic number must satisfy; therefore any number not satisfying this criterion must be transcendental.

The auxiliary function in Liouville's work is very simple, merely a polynomial that vanishes at a given algebraic number. This kind of property is usually the one that auxiliary functions satisfy. They either vanish or become very small at particular points, which is usually combined with the assumption that they do not vanish or can't be too small to derive a result.
