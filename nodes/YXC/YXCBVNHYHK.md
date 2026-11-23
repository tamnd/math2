---
tag: YXCBVNHYHK
kind: proof
name: Proof that epsilon nought is the least fixed point of α ↦ ω^α
msc: ["03E10", "03F15"]
topics: [XTTKZTYDSD]
audience: grad
proves: 9BX0XHX2D5
uses: [KAEDCQ8RM6, 6GD30FGYDZ, 0ZHQMQ2C1N, 0YSCSX5YZC]
methods: [0ASJVEFA9J, 0J0XBKG64S, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Epsilon_number
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ordinal_arithmetic
    locator: Exponentiation
---

## Proof

We show that the tower increases, push the map $\alpha \mapsto \omega^\alpha$ through the supremum by continuity, and then read off the remaining parts.
We use four facts of [[ordinal arithmetic|KAEDCQ8RM6]].

- (A1) The map $\alpha \mapsto \omega^\alpha$ is strictly increasing: $\beta < \gamma$ implies $\omega^\beta < \omega^\gamma$.
- (A2) It is continuous: $\omega^\lambda = \sup_{\xi < \lambda} \omega^\xi$ for every limit ordinal $\lambda$, by the definition of $\omega^\lambda$.
- (A3) Every strictly increasing map $f$ on ordinals satisfies $\alpha \le f(\alpha)$.
  If not, take the least $\alpha$ with $f(\alpha) < \alpha$; then $f(f(\alpha)) < f(\alpha)$, so $f(\alpha)$ is a smaller counterexample.
- (A4) Addition is strictly increasing in its right argument and non-decreasing in its left argument, and $\omega^\gamma \cdot \omega = \omega^{\gamma + 1}$.

First, the tower increases and its supremum is a limit.

1. We have $\tau_0 = 1 < \omega = \tau_1$.
2. If $\tau_n < \tau_{n+1}$, then (A1) gives $\tau_{n+1} = \omega^{\tau_n} < \omega^{\tau_{n+1}} = \tau_{n+2}$.
   By [[induction|0ASJVEFA9J]] on $n$, $\tau_n < \tau_{n+1}$ for all $n$.
3. The supremum of a set of ordinals is its union, so $\xi < \varepsilon_0$ holds exactly when $\xi < \tau_n$ for some $n$.
4. If $\xi < \varepsilon_0$, pick $n$ with $\xi < \tau_n$ by step 3; then $\xi + 1 \le \tau_n < \tau_{n+1} \le \varepsilon_0$ by step 2.
   Also $\varepsilon_0 \ge \tau_1 > 0$, so $\varepsilon_0$ is a limit ordinal.

Part 1.

5. By step 4 and (A2), $\omega^{\varepsilon_0} = \sup_{\xi < \varepsilon_0} \omega^\xi$.
6. Let $\xi < \varepsilon_0$, and choose $n$ with $\xi < \tau_n$ by step 3.
   By (A1), $\omega^\xi < \omega^{\tau_n} = \tau_{n+1} \le \varepsilon_0$.
7. Steps 5 and 6 give $\omega^{\varepsilon_0} \le \varepsilon_0$, and (A3) gives $\varepsilon_0 \le \omega^{\varepsilon_0}$, so $\omega^{\varepsilon_0} = \varepsilon_0$.

Part 2.

8. Let $\omega^\beta = \beta$.
   Since $\omega^0 = 1 \ne 0$, $\beta \ne 0$, so $\tau_0 = 1 \le \beta$.
9. If $\tau_n \le \beta$, then (A1) gives $\tau_{n+1} = \omega^{\tau_n} \le \omega^\beta = \beta$.
   By induction on $n$, $\tau_n \le \beta$ for all $n$.
10. So $\beta$ bounds the tower, and $\varepsilon_0 = \sup_n \tau_n \le \beta$.

Part 3.

11. Let $\alpha < \varepsilon_0$; by (A3), $\alpha \le \omega^\alpha$.
12. If $\alpha = \omega^\alpha$, then part 2 gives $\varepsilon_0 \le \alpha$, which contradicts $\alpha < \varepsilon_0$.
    So $\alpha < \omega^\alpha$.

Part 4.

13. Let $\alpha, \beta < \varepsilon_0$; by steps 2 and 3 there is one $n$ with $\alpha < \tau_n$ and $\beta < \tau_n$.
14. By (A1), $\omega^\alpha < \omega^{\tau_n} = \tau_{n+1} \le \varepsilon_0$.
15. If $n = 0$, then $\alpha = \beta = 0$ and $\alpha + \beta = 0 < \varepsilon_0$.
16. If $n \ge 1$, then (A4) gives $\alpha + \beta < \alpha + \tau_n \le \tau_n + \tau_n = \tau_n \cdot 2 \le \tau_n \cdot \omega$.
17. Since $\tau_n = \omega^{\tau_{n-1}}$, (A4) gives $\tau_n \cdot \omega = \omega^{\tau_{n-1} + 1}$.
18. By step 2, $\tau_{n-1} + 1 \le \tau_n$, so (A1) gives $\omega^{\tau_{n-1} + 1} \le \omega^{\tau_n} = \tau_{n+1} \le \varepsilon_0$.
    With step 16, $\alpha + \beta < \varepsilon_0$.

Part 5.

19. Let $0 < \alpha < \varepsilon_0$.
    By the [[Cantor normal form|6GD30FGYDZ]], $\alpha = \omega^{\beta_1} c_1 + \cdots + \omega^{\beta_k} c_k$ with $\beta_1 > \cdots > \beta_k$ and positive integers $c_i$, and this form is unique.
20. The first term is at most the sum, so (A3) gives $\beta_1 \le \omega^{\beta_1} \le \alpha < \varepsilon_0$.
    Part 3 then gives $\beta_1 < \omega^{\beta_1} \le \alpha$, so every exponent satisfies $\beta_i \le \beta_1 < \alpha$.
21. Define a finite string $t(\alpha)$ by recursion on $\alpha$: $t(0)$ is the symbol $0$, and $t(\alpha)$ is $\omega^{(t(\beta_1))} \cdot c_1 + \cdots + \omega^{(t(\beta_k))} \cdot c_k$ with each $c_i$ in decimal.
    The recursion is well defined because each $\beta_i < \alpha$ by step 20.
22. The map $t$ is injective.
    If $t(\alpha) = t(\alpha')$, the strings show the same number of terms, the same coefficients and the same strings for the exponents.
    By induction on $\alpha$ the exponents are equal, so $\alpha = \alpha'$ by the uniqueness in step 19.
23. The finite strings over a finite alphabet form a countable set, and by step 22 $\varepsilon_0$ injects into it.
    So $\varepsilon_0$ is countable, and with step 4, part 5 holds.

Steps 7, 10, 12, 14, 18 and 23 prove parts 1 to 5, so $\varepsilon_0$ is the least fixed point of $\alpha \mapsto \omega^\alpha$. $\blacksquare$

## Idea

The tower $1, \omega, \omega^\omega, \ldots$ climbs, and the map $\alpha \mapsto \omega^\alpha$ sends each stage to the next one.
By continuity, the map sends the supremum to the supremum of the next stages, and that is the same ordinal.
Any fixed point lies above every stage, because the map preserves order, so it lies above the supremum.
Countability comes from the finite names that the Cantor normal form gives below $\varepsilon_0$.

## Variants

The fixed-point lemma for [[normal functions|ERTAM0SFVB]] gives parts 1 and 2 at once.
For a normal $f$ and any $\gamma$, $\sup_n f^n(\gamma)$ is the least fixed point of $f$ that is at least $\gamma$.
The proof above is this argument with $f(\alpha) = \omega^\alpha$ and $\gamma = 1$.

Countability also follows by induction on $n$: each $\tau_n$ is countable, because $\omega^\gamma$ is countable for countable $\gamma$, and $\varepsilon_0$ is a countable union of countable sets.
As stated, this route needs countable choice to pick the enumerations, while the route by finite names does not.
