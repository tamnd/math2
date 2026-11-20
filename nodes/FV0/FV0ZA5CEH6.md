---
tag: FV0ZA5CEH6
kind: example
name: The three-valued Post logic defines Łukasiewicz negation
msc: ["03B50"]
topics: [WZP584JQ06]
audience: research
instance_of: [YHYSGRE7JV]
illustrates: [8P3Y6T0RZS]
uses: [PHGRJ2D97H, 8P3Y6T0RZS]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
    locator: Post logics Pm
---

## Example

Take $m = 3$ in [[Post's logic|PHGRJ2D97H]], with labels $0, 1, 2$ for the values $0, \tfrac12, 1$.
Negation is $\neg 0 = 2$, $\neg 1 = 0$, $\neg 2 = 1$, and $S = \neg\neg$ is $S0 = 1$, $S1 = 2$, $S2 = 0$.
We build a term for Łukasiewicz negation $f(x) = 2 - x$, following [[the completeness proof|8P3Y6T0RZS]].

1. $M(x) = \max(x, Sx)$: $M(0) = 1$, $M(1) = 2$, $M(2) = 2$.
2. $J_0(x) = S(M(x))$: $J_0(0) = 2$, $J_0(1) = 0$, $J_0(2) = 0$.
3. $J_1(x) = J_0(S^2 x) = J_0(\neg x)$: $J_1(0) = J_0(2) = 0$, $J_1(1) = J_0(0) = 2$, $J_1(2) = J_0(1) = 0$.
4. $f(0) = 2$ and $f(1) = 1$, so $f(x) = \max(K_2(J_0 x), K_1(J_1 x))$, where $K_c(e) = S(\max(S^c e, J_0 e))$.
5. $K_2(2) = S(\max(S^2 2, J_0 2)) = S(\max(1, 0)) = 2$ and $K_2(0) = S(\max(2, 2)) = 0$.
6. $K_1(2) = S(\max(0, 0)) = 1$ and $K_1(0) = S(\max(1, 2)) = 0$.
7. At $x = 0$: $\max(K_2(2), K_1(0)) = \max(2, 0) = 2$. At $x = 1$: $\max(K_2(0), K_1(2)) = \max(0, 1) = 1$. At $x = 2$: $\max(K_2(0), K_1(0)) = 0$.

So the term gives $2, 1, 0$ at $0, 1, 2$, which is $f$.

## Remarks

1. The constant $\tfrac12$, label $1$, is $K_1(J_0 x) \lor K_1(J_1 x) \lor K_1(J_2 x)$ for $J_2 x = J_0(S x)$.
2. Łukasiewicz implication can be built in the same way, as a function of two variables.
3. The term is long; the proof aims at existence, not at short terms.

## Explanations

### L1 human

Post's "not" turns the three values around in a circle.
With "not" and "or" we can build a formula that is high exactly at $0$, and one that is high exactly at $\tfrac12$.
Then we lower each one to the output we want and join them with "or".

### L2 human

1. Compute $S$ and the tests $J_a$ as tables.
2. For each input with a nonzero output, scale its test to that output.
3. Join the scaled tests with $\lor$, and check every input.

The typical use is to turn the existence proof into an explicit formula for a small case.
A trap: the scaling map $K_c$ is correct only on the inputs $0$ and $m - 1$, so apply it to tests, not to arbitrary values.
