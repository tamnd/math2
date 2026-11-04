---
tag: MHZXDEBH6F
kind: proof
name: Proof of Cassini's identity by induction
msc: [11B39]
proves: 01WQZK97Z5
uses: [0GA9K57A39, 0GF6AJEBZ0]
sources:
  - url: https://proofwiki.org/wiki/Cassini's_Identity
    locator: Proof 1
---

## Proof

We argue by [[induction from the base case $n = 1$|0GF6AJEBZ0]].

1. Let $F_m$ be the [[Fibonacci numbers|0GA9K57A39]], with $F_0 = 0$, $F_1 = 1$ and $F_{m+2} = F_{m+1} + F_m$. For $n \ge 1$, let $P(n)$ be the claim $F_{n-1} F_{n+1} - F_n^2 = (-1)^n$.
2. Base case. $F_2 = F_1 + F_0 = 1$, so $F_0 F_2 - F_1^2 = 0 - 1 = -1 = (-1)^1$. Thus $P(1)$ holds.
3. Induction step. Let $n \ge 1$ and assume $P(n)$.
4. By the recurrence, $F_{n+2} = F_{n+1} + F_n$. So $F_n F_{n+2} - F_{n+1}^2 = F_n F_{n+1} + F_n^2 - F_{n+1}^2$.
5. Rearranging, this equals $F_n^2 - F_{n+1}(F_{n+1} - F_n)$.
6. Since $n \ge 1$, the recurrence gives $F_{n+1} = F_n + F_{n-1}$, so $F_{n+1} - F_n = F_{n-1}$.
7. Hence $F_n F_{n+2} - F_{n+1}^2 = F_n^2 - F_{n-1} F_{n+1} = -(F_{n-1} F_{n+1} - F_n^2)$.
8. By $P(n)$, this equals $-(-1)^n = (-1)^{n+1}$. This is $P(n + 1)$.
9. By induction, $F_{n-1} F_{n+1} - F_n^2 = (-1)^n$ for every positive integer $n$.

## Idea

Replace $F_{n+2}$ by $F_{n+1} + F_n$ in the next instance of the identity. After one more use of the recurrence, the expression becomes the previous one with the opposite sign. So the sign alternates, starting from $-1$ at $n = 1$.
