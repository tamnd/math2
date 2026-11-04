---
tag: N8W7EW15GD
kind: proof
name: Proof of Binet's formula by induction
msc: [11B39]
proves: 0404D8TN7Y
uses: [0GA9K57A39, 0SC8T7548D, 0ASJVEFA9J]
sources:
  - url: https://proofwiki.org/wiki/Euler-Binet_Formula
    locator: Proof 1
---

## Proof

We argue by [[induction|0ASJVEFA9J]] on $n$, for two consecutive terms at a time.

1. Let $\varphi = \frac{1 + \sqrt{5}}{2}$ and $\psi = \frac{1 - \sqrt{5}}{2}$. For a natural number $n$, let $G_n = \frac{\varphi^n - \psi^n}{\sqrt{5}}$.
2. By the description of the [[golden ratio|0SC8T7548D]], $\varphi$ and $\psi$ are the roots of $x^2 - x - 1$. So $\varphi^2 = \varphi + 1$ and $\psi^2 = \psi + 1$.
3. Directly, $\psi^2 = \frac{1 - 2\sqrt{5} + 5}{4} = \frac{3 - \sqrt{5}}{2} = \psi + 1$, and the same computation with $+\sqrt{5}$ checks $\varphi^2 = \varphi + 1$.
4. We have $G_0 = \frac{1 - 1}{\sqrt{5}} = 0$ and $G_1 = \frac{\varphi - \psi}{\sqrt{5}} = \frac{\sqrt{5}}{\sqrt{5}} = 1$.
5. For every natural number $n$, step 2 gives $\varphi^{n+2} = \varphi^{n+1} + \varphi^n$ and $\psi^{n+2} = \psi^{n+1} + \psi^n$. Subtracting and dividing by $\sqrt{5}$ gives $G_{n+2} = G_{n+1} + G_n$.
6. Let $P(n)$ be the claim that $G_n = F_n$ and $G_{n+1} = F_{n+1}$, where $F_m$ are the [[Fibonacci numbers|0GA9K57A39]].
7. $P(0)$ holds by step 4, since $F_0 = 0$ and $F_1 = 1$.
8. Assume $P(n)$. Then $G_{n+1} = F_{n+1}$, and by step 5, $G_{n+2} = G_{n+1} + G_n = F_{n+1} + F_n = F_{n+2}$. So $P(n + 1)$ holds.
9. By induction, $P(n)$ holds for every natural number $n$. In particular $F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}}$ for every $n$.

## Idea

Since $\varphi$ and $\psi$ satisfy $x^2 = x + 1$, their powers obey the Fibonacci rule. So does every combination $a \varphi^n + b \psi^n$. The choice $a = -b = \frac{1}{\sqrt{5}}$ matches the starting values $0$ and $1$, so it gives the Fibonacci numbers.
