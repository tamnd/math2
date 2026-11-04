---
tag: 32T2EECYTC
kind: proof
name: Proof that the sum of the powers of a primitive root of unity is zero
msc: [11R18]
proves: 02PETK9PQ4
uses: [0J817RTVG6, 0FRSR10DWF]
sources:
  - url: https://en.wikipedia.org/wiki/Root_of_unity
    locator: Summation
---

## Proof

We show that multiplying the sum by $\zeta$ does not change it.

1. Let $n \ge 2$ be an integer and let $\zeta$ be a [[primitive $n$th root of unity|0J817RTVG6]].
By definition, $\zeta^n = 1$ and $\zeta^k \neq 1$ for each integer $k$ with $1 \le k < n$.
2. Since $n \ge 2$, the integer $k = 1$ satisfies $1 \le k < n$. So step 1 gives $\zeta \neq 1$.
3. Let $S = \sum_{k=0}^{n-1} \zeta^k = 1 + \zeta + \dots + \zeta^{n-1}$.
4. Multiplication in $\C$ distributes over addition, since [[$\C$ is a field|0FRSR10DWF]]. So $\zeta S = \sum_{k=0}^{n-1} \zeta^{k+1} = \zeta + \zeta^2 + \dots + \zeta^{n}$.
5. By step 1, the last term is $\zeta^n = 1$. So $\zeta S = 1 + \zeta + \dots + \zeta^{n-1} = S$.
6. Subtracting $S$ from both sides of step 5 gives $(\zeta - 1) S = 0$.
7. By step 2, $\zeta - 1 \neq 0$. Since $\C$ is a field, $\zeta - 1$ has an inverse $(\zeta - 1)^{-1}$.
8. Multiplying step 6 by $(\zeta - 1)^{-1}$ gives $S = 0$.
So $1 + \zeta + \zeta^2 + \dots + \zeta^{n-1} = 0$.

## Idea

Multiplying the sum by $\zeta$ shifts every power up by one.
The top power $\zeta^n$ equals $1$ and takes the place of the bottom term, so the sum is unchanged.
A number fixed by multiplication by some $\zeta \neq 1$ must be $0$.
