---
tag: B35K99ADCP
kind: proof
name: Proof of the Fibonacci recurrence from the definition
msc: [11B39]
proves: 0D0SMQYEJA
uses: [0GA9K57A39]
sources:
  - url: https://en.wikipedia.org/wiki/Fibonacci_sequence
    locator: Definition
---

## Proof

1. Let $n$ be a natural number.
2. The node [[Fibonacci sequence|0GA9K57A39]] defines $(F_m)_{m \ge 0}$ by $F_0 = 0$, $F_1 = 1$ and, for every natural number $m$, $F_{m+2} = F_{m+1} + F_m$.
3. Taking $m = n$ in this defining rule gives $F_{n+2} = F_{n+1} + F_n$, which is the claim.

## Idea

The Fibonacci numbers are defined by their two starting values and this rule. So the recurrence holds by definition. Its use is that, with $F_0$ and $F_1$, it fixes every later term.
