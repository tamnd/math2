---
tag: 1TAAJQSF8R
kind: proof
name: Proof of the logarithm of a power
msc: [33B10]
proves: 0V948DE5KA
uses: [0044CPHJBV, 0RKW2X63YR, 0RMVS7RXZX, 0K2FNY6DYV]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_logarithmic_identities
    locator: Logarithm of a power
---

## Proof

We argue by induction on $n$.

1. Fix a real number $x > 0$. For a natural number $n$, the power $x^n$ is the product of $n$ factors equal to $x$, with $x^0 = 1$. So $x^n > 0$, and $\ln(x^n)$ is defined by the [[definition of the natural logarithm|0044CPHJBV]].
2. Base case $n = 0$. By the [[definition of the exponential function|0RMVS7RXZX]], $e^0 = 1$, since every term of the series after the first vanishes at $0$.
3. Since [[$\ln(e^y) = y$ for every real $y$|0RKW2X63YR]], we get $\ln(x^0) = \ln 1 = \ln(e^0) = 0 = 0 \cdot \ln x$.
4. Induction step. Assume that $\ln(x^n) = n \ln x$ for some natural number $n$.
5. We have $x^{n+1} = x^n \cdot x$, and both factors are positive.
6. By the [[logarithm of a product|0K2FNY6DYV]], $\ln(x^{n+1}) = \ln(x^n) + \ln x$.
7. By the induction hypothesis, this equals $n \ln x + \ln x = (n+1) \ln x$.
8. By induction, $\ln(x^n) = n \ln x$ for every natural number $n$ and every real $x > 0$.

## Idea

A power $x^n$ is a product of $n$ copies of $x$. The logarithm turns each product into a sum, so it turns $n$ copies of $x$ into $n$ copies of $\ln x$. Induction makes this count precise.
