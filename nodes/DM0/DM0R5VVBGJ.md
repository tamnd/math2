---
tag: DM0R5VVBGJ
kind: example
name: Small values of the ordinal collapsing function
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: research
instance_of: [8S6CT4TMB7]
uses: [8S6CT4TMB7, PQSHBKCE7V, 6GD30FGYDZ, KAEDCQ8RM6, JQFAE9S2F4]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_collapsing_function
    locator: Predicative start
  - url: https://en.wikipedia.org/wiki/Ordinal_collapsing_function
    locator: First impredicative values
---

## Example

We use the [[collapsing function|8S6CT4TMB7]] $\psi$ with generators $0, 1, \omega, \Omega$ and the operations $+$, $\cdot$, exponentiation and $\psi(\xi)$ for $\xi < \alpha$.
Let $\varepsilon_\gamma$ be the $\gamma$-th [[epsilon number|PQSHBKCE7V]], and let $\zeta_0 = \varphi_2(0)$ be the least $\gamma$ with $\varepsilon_\gamma = \gamma$, in the notation of the [[Veblen function|JQFAE9S2F4]].
We show three facts.

- (a) $\psi(\gamma) = \varepsilon_\gamma$ for every $\gamma \le \zeta_0$, so $\psi(0) = \varepsilon_0$ and $\psi(\zeta_0) = \zeta_0$.
- (b) $\psi(\alpha) = \zeta_0$ for every $\alpha$ with $\zeta_0 \le \alpha \le \Omega$.
- (c) In particular, $\psi(\Omega) = \zeta_0$.

Two facts of [[ordinal arithmetic|KAEDCQ8RM6]] are used throughout.

- (F1) An epsilon number $\varepsilon$ is closed under $+$, $\cdot$ and exponentiation: if $\beta, \gamma < \varepsilon$, then $\beta + \gamma$, $\beta \cdot \gamma$ and $\beta^\gamma$ are below $\varepsilon$. For the power, $\beta^\gamma \le (\omega^\beta)^\gamma = \omega^{\beta \cdot \gamma} < \omega^\varepsilon = \varepsilon$.
- (F2) If $\beta, \gamma$ are ordinals and one of them is at least $\Omega$, then $\beta + \gamma$ is at least $\Omega$. The same holds for $\beta \cdot \gamma$ when both are nonzero, and for $\beta^\gamma$ when $\beta \ge 2$ and $\gamma \ge 1$. In the remaining cases ($0 \cdot \gamma$, $\beta^0$, $0^\gamma$, $1^\gamma$) the result is $0$ or $1$.

Proof of (a), by induction on $\gamma \le \zeta_0$.
Fix $\gamma$ and assume $\psi(\delta) = \varepsilon_\delta$ for all $\delta < \gamma$.

1. Upper bound. We show by induction on $n$: every element of $C_n(\gamma)$ is below $\varepsilon_\gamma$ or at least $\Omega$. For $n = 0$, the elements $0, 1, \omega$ are below $\varepsilon_0 \le \varepsilon_\gamma$, and $\Omega \ge \Omega$.
2. Sums, products and powers of elements of $C_n(\gamma)$ keep the property, by (F1) and (F2).
3. A new value $\psi(\xi)$ needs $\xi \in C_n(\gamma)$ and $\xi < \gamma$. Then $\xi < \gamma \le \zeta_0 < \Omega$, and the induction hypothesis gives $\psi(\xi) = \varepsilon_\xi < \varepsilon_\gamma$.
4. So $\varepsilon_\gamma \notin C(\gamma)$, and $\psi(\gamma) \le \varepsilon_\gamma$.
5. Lower bound. We show that every $\beta < \varepsilon_\gamma$ is in $C(\gamma)$, by induction on $\beta$. The cases $\beta = 0$ and $\beta = 1$ are generators.
6. Case 1: $\beta > 1$ is not an epsilon number. Its [[Cantor normal form|6GD30FGYDZ]] $\omega^{\beta_1} c_1 + \dots + \omega^{\beta_k} c_k$ has $\beta_1 \le \beta$, and $\beta_1 = \beta$ would give $\omega^\beta = \beta$. So all exponents are below $\beta$ and lie in $C(\gamma)$ by the induction hypothesis. Each $c_i$ is a sum of copies of $1$. So $\beta \in C(\gamma)$, by the closure under $+$, $\cdot$ and powers.
7. Case 2: $\beta = \varepsilon_\delta$ for some $\delta$. Since $\beta < \varepsilon_\gamma$, we have $\delta < \gamma \le \zeta_0$, so $\varepsilon_\delta \ne \delta$ and $\delta < \varepsilon_\delta = \beta$. The induction hypothesis on $\beta$ gives $\delta \in C(\gamma)$. Since $\delta < \gamma$, the value $\psi(\delta) = \varepsilon_\delta = \beta$ is in $C(\gamma)$.
8. Steps 4 and 7 show that $\varepsilon_\gamma$ is the least ordinal not in $C(\gamma)$, so $\psi(\gamma) = \varepsilon_\gamma$.

Proof of (b).
Let $\zeta_0 \le \alpha \le \Omega$.

9. Every $\beta < \zeta_0$ is in $C(\zeta_0) \subseteq C(\alpha)$, by step 8 with $\gamma = \zeta_0$ and the monotonicity of $C$.
10. Every element of $C_n(\alpha)$ is below $\zeta_0$ or at least $\Omega$, by induction on $n$ as in steps 1 to 3. The new case is $\psi(\xi)$ with $\xi \in C_n(\alpha)$ and $\xi < \alpha \le \Omega$. By the induction hypothesis $\xi < \zeta_0$ or $\xi \ge \Omega$, and $\xi < \Omega$ excludes the second case. So $\psi(\xi) = \varepsilon_\xi < \zeta_0$ by (a).
11. So $\zeta_0 \notin C(\alpha)$, and with step 9, $\psi(\alpha) = \zeta_0$. Taking $\alpha = \Omega$ gives (c).

## Remarks

The example shows that $\psi$ is the epsilon function $\gamma \mapsto \varepsilon_\gamma = \varphi_1(\gamma)$ as long as the argument is small.
In this range the uncountable $\Omega$ plays no role, because no argument above $\zeta_0$ can be formed from countable material.
At $\zeta_0$ the function gets stuck, and it stays at $\zeta_0$ up to $\Omega$ inclusive.
Only above $\Omega$ does $\psi$ grow again, because then $\Omega$ is an allowed argument: see [[the first impredicative value|3HWF8NBKJE]].
The generator $1$ can be dropped without a change, because $0^0 = 1$.
The generator $\omega$ cannot be dropped: without it, the countable elements of $C(0)$ are the natural numbers, and $\psi(0) = \omega$.

## Explanations

### L1 human

The collapsing function starts by doing something familiar.
Its first value is $\varepsilon_0$, the first ordinal that cannot be written with $\omega$, sums, products and powers.
Its second value is $\varepsilon_1$, the next such ordinal once $\varepsilon_0$ is allowed as a building block.
It goes on listing these ordinals until it reaches $\zeta_0$, a point where the list catches up with its own index.
There it stops, and only the large ordinal $\Omega$ can push it further.

### L2 human

We check $\psi(2) = \varepsilon_2$ by the steps above.

1. $C(2)$ may use $\psi(0) = \varepsilon_0$ and $\psi(1) = \varepsilon_1$, since $0, 1 \in C_0(2)$ and both are below $2$.
2. Every element of $C(2)$ is below $\varepsilon_2$ or at least $\Omega$, because $\varepsilon_2$ is closed under the operations and contains $\varepsilon_0$ and $\varepsilon_1$.
3. Every ordinal below $\varepsilon_2$ is either an epsilon number ($\varepsilon_0$ or $\varepsilon_1$, both in $C(2)$) or has a Cantor normal form with smaller exponents.
4. So $\psi(2) = \varepsilon_2$.

The typical use of such computations is to calibrate a new notation system against the [[Veblen function|JQFAE9S2F4]].
The trap is to think that $\psi$ is increasing everywhere: by (b), $\psi(\zeta_0 + 1) = \psi(\Omega) = \zeta_0$.
