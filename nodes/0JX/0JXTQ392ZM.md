---
tag: 0JXTQ392ZM
kind: statement
role: theorem
name: Legendre's theorem on continued fractions
msc: [11J70]
uses: [0SRWNR42BQ, 0SJ7Z6VKWK]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_continued_fraction
    locator: Legendre's theorem on continued fractions
---

## Statement

Let $\alpha$ be a real number, and let $p$ and $q$ be positive integers such that
$$\left| \alpha - \frac{p}{q} \right| < \frac{1}{2 q^2}.$$
Then $p / q$ is a [[convergent|0SRWNR42BQ]] of the [[continued fraction expansion|0SJ7Z6VKWK]] of $\alpha$.

## Remarks

So the very good rational approximations of $\alpha$ are all convergents.
The constant $\frac{1}{2}$ cannot be replaced by $1$: not every fraction with $\left| \alpha - \frac{p}{q} \right| < \frac{1}{q^2}$ is a convergent.
A use: it shows that the solutions of [[Pell's equation|0AF3DANJ76]] come from the convergents of $\sqrt{d}$.

## History

Adrien-Marie Legendre proved the theorem in his Essai sur la théorie des nombres of 1798.

## Explanations

### L1 human

If a fraction is extremely close to $\alpha$, then the continued fraction algorithm finds it.
So to look for the best approximations of a number, you only need to compute its convergents.
