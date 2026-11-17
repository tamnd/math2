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

We use [[Buchholz's functions|E7WEFRMQTB]] with $\Omega = \Omega_1$, and the [[small values|TZHC9KJBWF]] of $\psi_0$.
We show two facts.

- (a) $\psi_0(\Omega + \eta) = \omega^{\varepsilon_0 + \eta}$ for every $\eta \le \varepsilon_1$. At $\eta = \varepsilon_1$ the value is $\omega^{\varepsilon_1} = \varepsilon_1$, because $\varepsilon_0 + \varepsilon_1 = \varepsilon_1$.
- (b) $\psi_0(\alpha) = \varepsilon_1$ for every $\alpha$ with $\Omega + \varepsilon_1 \le \alpha \le \Omega \cdot 2$. In particular $\psi_0(\Omega \cdot 2) = \varepsilon_1$.

Proof of (a), by induction on $\eta$.
The case $\eta = 0$ is $\psi_0(\Omega) = \varepsilon_0$.
Let $\eta \ge 1$, let $\rho = \omega^{\varepsilon_0 + \eta}$, and assume (a) for all $\zeta < \eta$.

1. Upper bound. By induction on $n$, every element of $C^n_0(\Omega + \eta)$ is below $\rho$ or at least $\Omega$. Sums keep this, because $\rho$ is [[additively indecomposable|7TFCZSVX5R]].
2. A value $\psi_0(\xi)$ with $\xi < \Omega$ is at most $\psi_0(\Omega) = \varepsilon_0 < \rho$, since $\psi_0$ is weakly increasing.
3. A value $\psi_0(\xi)$ with $\Omega \le \xi < \Omega + \eta$ has $\xi = \Omega + \zeta$ with $\zeta < \eta$. By the induction hypothesis it is $\omega^{\varepsilon_0 + \zeta} < \rho$.
4. A value $\psi_\mu(\xi)$ with $\mu \ge 1$ is at least $\Omega$. So $\rho \notin C_0(\Omega + \eta)$.
5. Lower bound. Every $\beta < \rho$ is in $C_0(\Omega + \eta)$, by induction on $\beta$. Write $\beta$ in [[Cantor normal form|6GD30FGYDZ]] as a sum of powers $\omega^{\beta_i}$ with $\beta_i < \varepsilon_0 + \eta$. It is enough to show that each $\omega^{\beta_i}$ is in the set.
6. Case $\beta_i < \varepsilon_0$. Then $\beta_i < \omega^{\beta_i} \le \beta$, because no [[epsilon number|PQSHBKCE7V]] is below $\varepsilon_0$. So $\beta_i \in C_0(\Omega + \eta)$ by the induction hypothesis, and $\omega^{\beta_i} = \psi_0(\beta_i)$ is in the set.
7. Case $\beta_i = \varepsilon_0 + \zeta$ with $\zeta < \eta$. Then $\zeta \le \beta_i \le \omega^{\beta_i} \le \beta$, and equality throughout would give $\zeta = \varepsilon_0 + \zeta$ and $\omega^\zeta = \zeta$. The only epsilon number $\zeta \le \varepsilon_1$ with $\varepsilon_0 + \zeta = \zeta$ is $\varepsilon_1$, and $\zeta < \eta \le \varepsilon_1$ excludes it. So $\zeta < \beta$.
8. By the induction hypothesis $\zeta \in C_0(\Omega + \eta)$. Also $\Omega = \psi_1(0)$ is in the set, so $\Omega + \zeta$ is in the set, and $\Omega + \zeta < \Omega + \eta$.
9. So $\psi_0(\Omega + \zeta) = \omega^{\varepsilon_0 + \zeta} = \omega^{\beta_i}$ is in the set. Steps 1 to 9 give $\psi_0(\Omega + \eta) = \rho$.

Proof of (b).
Let $\Omega + \varepsilon_1 \le \alpha \le \Omega \cdot 2$.

10. Every $\beta < \varepsilon_1$ is in $C_0(\Omega + \varepsilon_1) \subseteq C_0(\alpha)$, by (a).
11. We show by induction on $n$: every element of $C^n_0(\alpha)$ is below $\varepsilon_1$, or equal to $\Omega + \zeta$ with $\zeta < \varepsilon_1$, or at least $\Omega \cdot 2$. The start $\set{0}$ has this property.
12. Sums. If both summands are below $\varepsilon_1$, so is the sum. A countable ordinal plus $\Omega + \zeta$ is $\Omega + \zeta$. Then $(\Omega + \zeta) + \beta = \Omega + (\zeta + \beta)$ with $\zeta + \beta < \varepsilon_1$. A sum of two elements that are at least $\Omega$ is at least $\Omega \cdot 2$.
13. Values of $\psi_0$. The argument $\xi$ is below $\alpha \le \Omega \cdot 2$, so $\xi < \varepsilon_1$ or $\xi = \Omega + \zeta$ with $\zeta < \varepsilon_1$. In both cases $\psi_0(\xi) \le \omega^{\varepsilon_0 + \zeta} < \varepsilon_1$ (with $\zeta = 0$ in the first case), by (a) and the small values.
14. Values of $\psi_\mu$ with $\mu \ge 1$. We have $\psi_1(0) = \Omega = \Omega + 0$. For $\xi \ge 1$, the set $C_1(\xi)$ contains $\Omega$ and $\Omega + \Omega$, so $\psi_1(\xi) > \Omega \cdot 2$. For $\mu \ge 2$, $\psi_\mu(\xi) \ge \Omega_2 > \Omega \cdot 2$.
15. So $\varepsilon_1 \notin C_0(\alpha)$, because it is countable and not below $\varepsilon_1$. With step 10, $\psi_0(\alpha) = \varepsilon_1$.

## Remarks

The example shows that in Buchholz's system each step $\Omega \cdot k \to \Omega \cdot (k + 1)$ in the argument moves the value to the next epsilon number: $\psi_0(\Omega) = \varepsilon_0$ and $\psi_0(\Omega \cdot 2) = \varepsilon_1$.
The Wikipedia article continues the list and gives $\psi_0(\Omega^2) = \zeta_0$.
Compare the [[collapsing function with exponentiation|8S6CT4TMB7]]: there $\psi(\Omega) = \zeta_0$, and the Wikipedia article on collapsing functions gives $\psi(\Omega \cdot 2) = \zeta_1$.
So the same term $\Omega \cdot 2$ names $\varepsilon_1$ in one system and $\zeta_1$ in the other.
Part (b) shows again that $\psi_0$ is constant on long intervals, here on the interval from $\Omega + \varepsilon_1$ to $\Omega \cdot 2$.

## Explanations

### L1 human

In Buchholz's system the large ordinal $\Omega$ is a name for $\varepsilon_0$.
Adding small ordinals to $\Omega$ moves the value up through the powers $\omega^{\varepsilon_0 + 1}$, $\omega^{\varepsilon_0 + 2}$, and so on.
Eventually these powers reach the next epsilon number, $\varepsilon_1$.
After that the value stops again, until the argument reaches $\Omega + \Omega$.
So $\psi_0(\Omega \cdot 2)$ is $\varepsilon_1$, the second epsilon number.

### L2 human

We compute $\psi_0(\Omega + \omega)$ with part (a).

1. Here $\eta = \omega$, so the claim is $\psi_0(\Omega + \omega) = \omega^{\varepsilon_0 + \omega}$.
2. The values $\psi_0(\Omega + n) = \omega^{\varepsilon_0 + n}$ for natural $n$ are available, because $\Omega + n$ is in the set and below $\Omega + \omega$.
3. Sums of these values and of ordinals below $\varepsilon_0$ give every ordinal below $\omega^{\varepsilon_0 + \omega}$.
4. No allowed value reaches $\omega^{\varepsilon_0 + \omega}$, so $\psi_0(\Omega + \omega) = \omega^{\varepsilon_0 + \omega}$.

The typical use is to see how arguments between $\Omega$ and $\Omega \cdot 2$ list the ordinals between $\varepsilon_0$ and $\varepsilon_1$.
The trap is to apply the formula of (a) past $\eta = \varepsilon_1$: for $\varepsilon_1 \le \eta \le \Omega$, the value stays $\varepsilon_1$.
