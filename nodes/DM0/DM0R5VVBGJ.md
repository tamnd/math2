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

We use the [[collapsing function|8S6CT4TMB7]] $\psi$ of Madore's system: $C(\alpha)$ contains $0, 1, \omega, \Omega$, is closed under $+$, $\cdot$ and powers, and contains $\psi(\xi)$ for $\xi \in C(\alpha)$ with $\xi < \alpha$.
Let $\varepsilon_\gamma$ be the $\gamma$-th [[epsilon number|PQSHBKCE7V]], and let $\zeta_0 = \varphi_2(0)$ be the least $\gamma$ with $\varepsilon_\gamma = \gamma$, in the notation of the [[Veblen function|JQFAE9S2F4]].
We show two facts.
Part (a) says that $\psi(\gamma) = \varepsilon_\gamma$ for every $\gamma \le \zeta_0$, so $\psi(0) = \varepsilon_0$, $\psi(1) = \varepsilon_1$ and $\psi(\zeta_0) = \zeta_0$.
Part (b) says that $\psi(\alpha) = \zeta_0$ for every $\alpha$ with $\zeta_0 \le \alpha \le \Omega$, so in particular $\psi(\Omega) = \zeta_0$.

Two facts of [[ordinal arithmetic|KAEDCQ8RM6]] are used throughout.
Fact (F1) says that an epsilon number $\varepsilon$ is closed under $+$, $\cdot$ and powers.
For the power with $1 \le \beta < \varepsilon$ and $\gamma < \varepsilon$, we have $\beta^\gamma \le (\omega^\beta)^\gamma = \omega^{\beta \cdot \gamma} < \omega^\varepsilon = \varepsilon$.
Fact (F2) says that if one of $\beta, \gamma$ is at least $\Omega$, then $\beta + \gamma \ge \Omega$.
The same holds for $\beta \cdot \gamma$ when both are nonzero and for $\beta^\gamma$ when $\beta \ge 2$ and $\gamma \ge 1$, and in the remaining cases the result is $0$ or $1$.

### Proof of part (a)

We use induction on $\gamma \le \zeta_0$, and we assume $\psi(\delta) = \varepsilon_\delta$ for all $\delta < \gamma$.

1. For the upper bound, every member of $C(\gamma)$ is below $\varepsilon_\gamma$ or at least $\Omega$.
   The names $0, 1, \omega$ are below $\varepsilon_0 \le \varepsilon_\gamma$, and sums, products and powers keep the property by (F1) and (F2).
2. A value $\psi(\xi)$ in $C(\gamma)$ has $\xi < \gamma \le \zeta_0$, so the induction hypothesis gives $\psi(\xi) = \varepsilon_\xi < \varepsilon_\gamma$.
3. So $\varepsilon_\gamma \notin C(\gamma)$, and $\psi(\gamma) \le \varepsilon_\gamma$.
4. For the lower bound, we show by induction on $\beta$ that every $\beta < \varepsilon_\gamma$ is in $C(\gamma)$.
   The cases $0$ and $1$ are names.
5. If $\beta > 1$ is not an epsilon number, its [[Cantor normal form|6GD30FGYDZ]] $\omega^{\beta_1} c_1 + \dots + \omega^{\beta_k} c_k$ has all exponents below $\beta$, since $\beta_1 = \beta$ would give $\omega^\beta = \beta$.
   The exponents are in $C(\gamma)$ by the induction hypothesis, each $c_i$ is a sum of copies of $1$, so $\beta \in C(\gamma)$.
6. If $\beta = \varepsilon_\delta$, then $\delta < \gamma \le \zeta_0$, so $\delta$ is not a fixed point and $\delta < \varepsilon_\delta = \beta$.
   The induction hypothesis puts $\delta$ in $C(\gamma)$, and since $\delta < \gamma$, the value $\psi(\delta) = \beta$ is in $C(\gamma)$.
7. Steps 3 to 6 show that $\varepsilon_\gamma$ is the least ordinal not in $C(\gamma)$.

### Proof of part (b)

Let $\zeta_0 \le \alpha \le \Omega$.

8. Every $\beta < \zeta_0$ is in $C(\zeta_0)$ by step 7 with $\gamma = \zeta_0$, and $C(\zeta_0) \subseteq C(\alpha)$.
9. Every member of $C(\alpha)$ is below $\zeta_0$ or at least $\Omega$, as in steps 1 and 2.
   The new case is a value $\psi(\xi)$ with $\xi \in C(\alpha)$ and $\xi < \alpha \le \Omega$.
   By the induction hypothesis $\xi < \zeta_0$ or $\xi \ge \Omega$, and $\xi < \Omega$ rules out the second case, so $\psi(\xi) = \varepsilon_\xi < \zeta_0$ by (a).
10. So $\zeta_0 \notin C(\alpha)$, and with step 8, $\psi(\alpha) = \zeta_0$.

## Remarks

As long as the argument is small, $\psi$ is just the epsilon function $\gamma \mapsto \varepsilon_\gamma = \varphi_1(\gamma)$.
In this range $\Omega$ plays no role, because no countable argument at or above $\zeta_0$ can be named from countable material.
At $\zeta_0$ the function gets stuck, and it stays there up to $\Omega$ inclusive.
It grows again only when $\Omega$ itself is an allowed argument, which happens in the [[first impredicative value|3HWF8NBKJE]].

Changing the names changes the values.
The name $1$ can be dropped without any change, because $0^0 = 1$.
The name $\omega$ cannot: without it the countable members of $C(0)$ are the natural numbers, and $\psi(0) = \omega$.

## Explanations

### L1 human

The collapsing function starts by doing something familiar.
Its first value is $\varepsilon_0$, the first ordinal that cannot be written with $\omega$, sums, products and powers.
Its second value is $\varepsilon_1$, the next such ordinal once $\varepsilon_0$ is allowed as a building block.
It goes on listing these ordinals until it reaches $\zeta_0$, where the list catches up with its own index.
There it stops, and only the large ordinal $\Omega$ can push it further.

### L2 human

We check $\psi(2) = \varepsilon_2$ with the steps above.
The set $C(2)$ may use $\psi(0) = \varepsilon_0$ and $\psi(1) = \varepsilon_1$, since $0$ and $1$ are names below $2$.
Every member of $C(2)$ is below $\varepsilon_2$ or at least $\Omega$, because $\varepsilon_2$ is closed under the operations and contains $\varepsilon_0$ and $\varepsilon_1$.
Every ordinal below $\varepsilon_2$ is $\varepsilon_0$, $\varepsilon_1$, or has a Cantor normal form with smaller exponents.
So $\psi(2) = \varepsilon_2$.

Computations like this calibrate a new notation system against the [[Veblen function|JQFAE9S2F4]].
Watch out: $\psi$ is not increasing everywhere, since part (b) gives $\psi(\zeta_0 + 1) = \psi(\Omega) = \zeta_0$.
