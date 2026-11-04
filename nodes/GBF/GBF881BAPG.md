---
tag: GBF881BAPG
kind: proof
name: Proof of the symmetry of binomial coefficients from the factorial formula
msc: [05A10]
proves: 0R7JS3DP3W
uses: [092GEF38YD, 033KTKKRV6]
sources:
  - url: https://proofwiki.org/wiki/Symmetry_Rule_for_Binomial_Coefficients
---

## Proof

We compute both sides with the [[factorial formula|033KTKKRV6]].

1. Let $k \le n$. By the factorial formula, $\binom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$.
2. The number $n - k$ is a natural number with $n - k \le n$. So the factorial formula also applies to $\binom{n}{n-k}$.
3. Since $n - (n - k) = k$, it gives $\binom{n}{n-k} = \dfrac{n!}{(n-k)!\,k!}$.
4. The denominators in steps 1 and 3 are equal, because multiplication is commutative. Hence $\binom{n}{k} = \binom{n}{n-k}$.

## Idea

The factorial formula treats $k$ and $n - k$ in the same way: they appear only through the product $k!\,(n-k)!$.
Swapping them therefore does not change the value.
