---
tag: T01DYDHV4C
kind: example
name: Buchholz's psi zero of Omega times two is epsilon one
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: research
instance_of: [E7WEFRMQTB]
uses: [E7WEFRMQTB, TZHC9KJBWF, 7TFCZSVX5R, 6GD30FGYDZ, PQSHBKCE7V]
sources:
  - url: https://en.wikipedia.org/wiki/Buchholz_psi_functions
    locator: Explanation
---

## Example

We use [[Buchholz's functions|E7WEFRMQTB]] with $\Omega = \Omega_1$, and the [[small values|TZHC9KJBWF]] $\psi_0(\Omega) = \varepsilon_0$ and $\psi_0(\alpha) = \omega^\alpha$ for $\alpha \le \varepsilon_0$.
We show two facts, which together give $\psi_0(\Omega \cdot 2) = \varepsilon_1$.
Part (a) says that $\psi_0(\Omega + \eta) = \omega^{\varepsilon_0 + \eta}$ for every $\eta \le \varepsilon_1$.
At $\eta = \varepsilon_1$ the value is $\omega^{\varepsilon_1} = \varepsilon_1$, because $\varepsilon_0 + \varepsilon_1 = \varepsilon_1$.
Part (b) says that $\psi_0(\alpha) = \varepsilon_1$ for every $\alpha$ with $\Omega + \varepsilon_1 \le \alpha \le \Omega \cdot 2$.

Proof of (a), by induction on $\eta$.
The case $\eta = 0$ is $\psi_0(\Omega) = \varepsilon_0$.
Let $\eta \ge 1$, let $\rho = \omega^{\varepsilon_0 + \eta}$, and assume (a) for all $\zeta < \eta$.

1. Every member of $C_0(\Omega + \eta)$ is below $\rho$ or at least $\Omega$, by induction on the construction.
   Sums keep this, because $\rho$ is [[additively indecomposable|7TFCZSVX5R]].
2. A value $\psi_0(\xi)$ with $\xi < \Omega$ is at most $\psi_0(\Omega) = \varepsilon_0 < \rho$, since $\psi_0$ is weakly increasing.
3. A value $\psi_0(\Omega + \zeta)$ with $\zeta < \eta$ is $\omega^{\varepsilon_0 + \zeta} < \rho$, by the induction hypothesis.
4. A value $\psi_\mu(\xi)$ with $\mu \ge 1$ is at least $\Omega$.
   So $\rho \notin C_0(\Omega + \eta)$.
5. For the lower bound, we show by induction on $\beta$ that every $\beta < \rho$ is in $C_0(\Omega + \eta)$.
   Write $\beta$ in [[Cantor normal form|6GD30FGYDZ]] as a sum of powers $\omega^{\beta_i}$ with $\beta_i < \varepsilon_0 + \eta$; it is enough to put each $\omega^{\beta_i}$ in the set.
6. If $\beta_i < \varepsilon_0$, then $\beta_i < \omega^{\beta_i} \le \beta$, because no [[epsilon number|PQSHBKCE7V]] is below $\varepsilon_0$.
   So $\beta_i$ is in the set by the induction hypothesis, and so is $\omega^{\beta_i} = \psi_0(\beta_i)$.
7. If $\beta_i = \varepsilon_0 + \zeta$ with $\zeta < \eta$, then $\zeta \le \beta_i \le \omega^{\beta_i} \le \beta$.
   Equality throughout would make $\zeta$ an epsilon number with $\varepsilon_0 + \zeta = \zeta$, and the only such number up to $\varepsilon_1$ is $\varepsilon_1$, which $\zeta < \eta \le \varepsilon_1$ excludes.
   So $\zeta < \beta$.
8. By the induction hypothesis $\zeta$ is in the set, and so is $\Omega = \psi_1(0)$, hence so is $\Omega + \zeta$, which is below $\Omega + \eta$.
9. So $\psi_0(\Omega + \zeta) = \omega^{\varepsilon_0 + \zeta} = \omega^{\beta_i}$ is in the set, and $\psi_0(\Omega + \eta) = \rho$.

Proof of (b), for $\Omega + \varepsilon_1 \le \alpha \le \Omega \cdot 2$.

10. Every $\beta < \varepsilon_1$ is in $C_0(\Omega + \varepsilon_1) \subseteq C_0(\alpha)$, by (a).
11. Every member of $C_0(\alpha)$ is below $\varepsilon_1$, or equal to $\Omega + \zeta$ with $\zeta < \varepsilon_1$, or at least $\Omega \cdot 2$.
    We check this by induction on the construction, starting from $0$.
12. Sums keep the three cases: a countable ordinal plus $\Omega + \zeta$ is $\Omega + \zeta$, the sum $(\Omega + \zeta) + \beta$ is $\Omega + (\zeta + \beta)$ with $\zeta + \beta < \varepsilon_1$, and two summands at least $\Omega$ give at least $\Omega \cdot 2$.
13. A value $\psi_0(\xi)$ has $\xi < \alpha \le \Omega \cdot 2$, so $\xi$ is in one of the first two cases.
    Then $\psi_0(\xi) \le \omega^{\varepsilon_0 + \zeta} < \varepsilon_1$, by (a) and the small values, with $\zeta = 0$ in the first case.
14. A value $\psi_1(\xi)$ is $\Omega$ for $\xi = 0$, and for $\xi \ge 1$ it exceeds $\Omega \cdot 2$, because $C_1(\xi)$ contains $\Omega + \Omega$.
    For $\mu \ge 2$, $\psi_\mu(\xi) \ge \Omega_2 > \Omega \cdot 2$.
15. So $\varepsilon_1 \notin C_0(\alpha)$, and with step 10, $\psi_0(\alpha) = \varepsilon_1$.

## Remarks

In Buchholz's system the step from $\Omega$ to $\Omega \cdot 2$ in the argument moves the value from $\varepsilon_0$ to the next epsilon number $\varepsilon_1$.
The Wikipedia article continues the list, and gives $\psi_0(\Omega^2) = \zeta_0$.

Compare the Wikipedia [[collapsing function with exponentiation|8S6CT4TMB7]]: there $\psi(\Omega) = \zeta_0$ and $\psi(\Omega \cdot 2) = \zeta_1$.
So the same term $\Omega \cdot 2$ names $\varepsilon_1$ in one system and $\zeta_1$ in the other, which is why every page must fix its system.
Part (b) also shows again that $\psi_0$ is constant on long intervals, here from $\Omega + \varepsilon_1$ to $\Omega \cdot 2$.

## Explanations

### L1 human

In Buchholz's system the large ordinal $\Omega$ is a name for $\varepsilon_0$.
Adding small ordinals to $\Omega$ moves the value up through $\omega^{\varepsilon_0 + 1}$, $\omega^{\varepsilon_0 + 2}$, and so on.
Eventually these powers reach the next epsilon number, $\varepsilon_1$.
After that the value stops again, until the argument reaches $\Omega + \Omega$.
So $\psi_0(\Omega \cdot 2)$ is $\varepsilon_1$, the second epsilon number.

### L2 human

We compute $\psi_0(\Omega + \omega)$ with part (a), where $\eta = \omega$.
The values $\psi_0(\Omega + n) = \omega^{\varepsilon_0 + n}$ for natural $n$ are available, because $\Omega + n$ is named and below $\Omega + \omega$.
Sums of these values and of ordinals below $\varepsilon_0$ give every ordinal below $\omega^{\varepsilon_0 + \omega}$.
No allowed value reaches $\omega^{\varepsilon_0 + \omega}$, so
$$\psi_0(\Omega + \omega) = \omega^{\varepsilon_0 + \omega}.$$

The arguments between $\Omega$ and $\Omega \cdot 2$ thus list the ordinals between $\varepsilon_0$ and $\varepsilon_1$.
Watch out: the formula of (a) stops at $\eta = \varepsilon_1$, and for $\varepsilon_1 \le \eta \le \Omega$ the value stays $\varepsilon_1$.
