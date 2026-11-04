---
tag: 8F5WAZJBDY
kind: proof
name: Proof of the addition formula for Fibonacci numbers by induction
msc: [11B39]
proves: 00CN2F997Q
uses: [0GA9K57A39, 0ASJVEFA9J]
sources:
  - url: https://proofwiki.org/wiki/Honsberger's_Identity
    locator: Proof 1
---

## Proof

We argue by [[induction|0ASJVEFA9J]] on $m$, for two consecutive values of $m$ at a time and all $n$ at once.

1. Let $F_k$ be the [[Fibonacci numbers|0GA9K57A39]], with $F_0 = 0$, $F_1 = 1$ and $F_{k+2} = F_{k+1} + F_k$.
2. For a natural number $m$, let $E(m)$ be the claim that $F_{m+n+1} = F_m F_n + F_{m+1} F_{n+1}$ for every natural number $n$.
3. Let $P(m)$ be the claim that $E(m)$ and $E(m + 1)$ both hold.
4. $E(0)$ holds: for every $n$, $F_0 F_n + F_1 F_{n+1} = 0 + F_{n+1} = F_{n+1}$.
5. $E(1)$ holds: $F_2 = F_1 + F_0 = 1$, so for every $n$, $F_1 F_n + F_2 F_{n+1} = F_n + F_{n+1} = F_{n+2}$. Thus $P(0)$ holds.
6. Assume $P(m)$, and let $n$ be a natural number. By the recurrence, $F_{(m+2)+n+1} = F_{m+n+1} + F_{(m+1)+n+1}$.
7. By $E(m)$ and $E(m + 1)$, this is $\left(F_m F_n + F_{m+1} F_{n+1}\right) + \left(F_{m+1} F_n + F_{m+2} F_{n+1}\right)$.
8. Grouping terms, it equals $(F_m + F_{m+1}) F_n + (F_{m+1} + F_{m+2}) F_{n+1} = F_{m+2} F_n + F_{m+3} F_{n+1}$, by the recurrence.
9. So $E(m + 2)$ holds. Together with $E(m + 1)$, this gives $P(m + 1)$.
10. By induction, $P(m)$ holds for every natural number $m$. In particular $F_{m+n+1} = F_m F_n + F_{m+1} F_{n+1}$ for all natural numbers $m$ and $n$.

## Idea

For fixed $n$, both sides satisfy the Fibonacci recurrence in $m$, because they are built linearly from $F_m$ and $F_{m+1}$. The two sides agree for $m = 0$ and $m = 1$, so they agree for every $m$.
