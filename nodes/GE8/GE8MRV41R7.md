---
tag: GE8MRV41R7
kind: concept
name: Submultiplicative function
msc: [39B62]
sources:
  - url: https://en.wikipedia.org/wiki/Subadditivity
---

## Summary

A submultiplicative function is a nonnegative function $f$ on a [[semigroup|0XMEM406JM]] with $f(xy) \le f(x) f(y)$ for all $x$ and $y$.
It is the multiplicative twin of a [[subadditive function|3X9DD9J3CV]]: where $f$ is positive, $\log f$ is subadditive.
The [[operator norm|06EKW1AKXF]] on square matrices is submultiplicative.
So is the Frobenius norm, a [[matrix norm|54T6Y6DSY4]] that is not an operator norm.
With Fekete's subadditive lemma this gives the existence of limits such as $\lim_n \norm{T^n}^{1/n}$.

## Explanations

### L1 human

A submultiplicative quantity never grows faster under composition than the product of its values.
Think of a machine that stretches vectors by at most a factor $a$ followed by one that stretches by at most $b$: together they stretch by at most $ab$.
For example, the sequence $a_n = \norm{A^n}$ of norms of powers of a matrix $A$ satisfies $a_{m+n} \le a_m a_n$.
So the growth of $\norm{A^n}$ is controlled by a single number, the limit of $a_n^{1/n}$.
