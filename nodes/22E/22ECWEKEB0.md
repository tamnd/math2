---
tag: 22ECWEKEB0
kind: proof
name: Proof that log x is at most x - 1
msc: [33B10, 26D15]
proves: 04CBRA4JRK
uses: [012C7GFF20, 0044CPHJBV, 0RKW2X63YR, 0RMVS7RXZX]
sources:
  - url: https://proofwiki.org/wiki/Bounds_of_Natural_Logarithm
---

## Proof

1. Let $x > 0$, and let $y = \ln x$, where $\ln$ is the [[natural logarithm|0044CPHJBV]].
2. By the inequality [[$1 + y \le e^y$|012C7GFF20]], we get $1 + \ln x \le e^{\ln x}$.
3. By [[the inverse relation of $\ln$ and $\exp$|0RKW2X63YR]], $e^{\ln x} = x$. So $1 + \ln x \le x$, that is, $\ln x \le x - 1$.
4. The same inequality says that $1 + y = e^y$ holds if and only if $y = 0$. So $\ln x = x - 1$ holds if and only if $\ln x = 0$.
5. If $\ln x = 0$, then $x = e^{\ln x} = e^0 = 1$. Here $e^0 = 1$ by the [[series of the exponential|0RMVS7RXZX]], since all terms after the first vanish at $0$.
6. Conversely, if $x = 1$, then $\ln x = \ln(e^0) = 0$, since $\ln(e^y) = y$ for every real $y$.
7. So $\ln x \le x - 1$ for every $x > 0$, with equality if and only if $x = 1$.

## Idea

The line $y = 1 + t$ lies below the graph of $e^t$ and touches it only at $t = 0$. Substituting $t = \ln x$ moves this fact over to the logarithm. The line $y = x - 1$ is the tangent to $\ln$ at $x = 1$.
