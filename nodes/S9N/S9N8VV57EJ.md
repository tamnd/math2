---
tag: S9N8VV57EJ
kind: proof
name: Proof of the Möbius inversion formula
msc: [11A25]
proves: 07Q4TBTFVB
uses: [0C8QENHYZW, 0ASC73QEQT, 0FCWA16FZE]
sources:
  - url: https://en.wikipedia.org/wiki/M%C3%B6bius_inversion_formula
    locator: Proofs of generalizations
---

## Proof

We rearrange finite double sums and use $\sum_{d \mid k} \mu(d) = [k = 1]$. Here $[k = 1]$ is $1$ if $k = 1$ and $0$ otherwise.

1. By the [[sum of the Möbius function over divisors|0ASC73QEQT]], for each positive integer $k$ we have $\sum_{d \mid k} \mu(d) = [k = 1]$. All divisors here are [[positive divisors|0FCWA16FZE]].
2. Fix a positive integer $n$. Let $T$ be the set of pairs $(d, e)$ of positive integers with $de \mid n$.
3. For positive integers $d$ and $e$, the conditions "$d \mid n$ and $e \mid n/d$", "$de \mid n$" and "$e \mid n$ and $d \mid n/e$" are equivalent. Each one says that $n = dek$ for a positive integer $k$.
4. Assume first that $g(m) = \sum_{e \mid m} f(e)$ for all positive integers $m$. Then
$$\sum_{d \mid n} \mu(d) g\!\left(\frac{n}{d}\right) = \sum_{d \mid n} \sum_{e \mid n/d} \mu(d) f(e) = \sum_{(d, e) \in T} \mu(d) f(e).$$
5. By step 3, we can sum over $e$ first:
$$\sum_{(d, e) \in T} \mu(d) f(e) = \sum_{e \mid n} f(e) \sum_{d \mid n/e} \mu(d) = \sum_{e \mid n} f(e) \, [n/e = 1].$$
The last equality is step 1 with $k = n/e$.
6. Only $e = n$ has $n/e = 1$. So the sum equals $f(n)$. This proves the formula for $f$.
7. Conversely, assume that $f(m) = \sum_{e \mid m} \mu(e) g(m/e)$ for all positive integers $m$. Then
$$\sum_{d \mid n} f(d) = \sum_{d \mid n} \sum_{e \mid d} \mu(e) \, g\!\left(\frac{d}{e}\right).$$
8. The pairs $(d, e)$ with $d \mid n$ and $e \mid d$ correspond one-to-one to the pairs $(e, k)$ with $ek \mid n$, by $k = d/e$ and $d = ek$.
9. So, using step 3 with $(e, k)$ in place of $(d, e)$,
$$\sum_{d \mid n} f(d) = \sum_{(e, k) :\, ek \mid n} \mu(e) g(k) = \sum_{k \mid n} g(k) \sum_{e \mid n/k} \mu(e) = \sum_{k \mid n} g(k) \, [n/k = 1].$$
10. Only $k = n$ contributes, so $\sum_{d \mid n} f(d) = g(n)$. Since $n$ was arbitrary, both directions hold.

## Idea

Substitute one relation into the other and swap the order of the two divisor sums. The inner sum then becomes a sum of $\mu$ over the divisors of a number. That sum is $1$ for the number $1$ and $0$ otherwise, so only one term survives.
