---
tag: TZHC9KJBWF
kind: example
name: Small values of Buchholz's psi zero
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: research
instance_of: [E7WEFRMQTB]
uses: [E7WEFRMQTB, 7TFCZSVX5R, 6GD30FGYDZ, PQSHBKCE7V]
sources:
  - url: https://en.wikipedia.org/wiki/Buchholz_psi_functions
    locator: Explanation
  - url: https://en.wikipedia.org/wiki/Buchholz_psi_functions
    locator: Properties
---

## Example

We use [[Buchholz's functions|E7WEFRMQTB]] $\psi_\nu$, with $\Omega_0 = 1$ and $\Omega = \Omega_1$.
We prove four values.
Part (a) is $\psi_\nu(0) = \Omega_\nu$ for each $\nu \le \omega$, so $\psi_0(0) = 1$ and $\psi_1(0) = \Omega$.
Part (b) is $\psi_0(\alpha) = \omega^\alpha$ for each $\alpha \le \varepsilon_0$, so $\psi_0(1) = \omega$, $\psi_0(2) = \omega^2$, $\psi_0(\omega) = \omega^\omega$ and $\psi_0(\varepsilon_0) = \varepsilon_0$.
Part (c) is $\psi_0(\alpha) = \varepsilon_0$ for each $\alpha$ with $\varepsilon_0 \le \alpha \le \Omega$.
Part (d) is $\psi_0(\Omega + 1) = \omega^{\varepsilon_0 + 1} = \varepsilon_0 \cdot \omega$.
We use one fact (F): if $\rho$ is [[additively indecomposable|7TFCZSVX5R]] and $\beta, \gamma < \rho$, then $\beta + \gamma < \rho$, and a sum with a summand at least $\Omega$ is at least $\Omega$.

### Proof of parts (a) and (b)

Part (a) comes first.

1. $C_\nu(0)$ allows no value of $\psi$, since no $\xi$ is below $0$.
   So $C_\nu(0)$ is the closure of the set of ordinals below $\Omega_\nu$ under addition.
2. For $\nu = 0$ this set is $\{ 0 \}$, since $0 + 0 = 0$, so $\psi_0(0) = 1$.
3. For $\nu \ge 1$, $\Omega_\nu$ is an infinite cardinal, so a sum of two smaller ordinals is smaller, and $\psi_\nu(0) = \Omega_\nu$.

Part (b) is proved by induction on $\alpha \le \varepsilon_0$, and we assume $\psi_0(\xi) = \omega^\xi$ for all $\xi < \alpha$.

4. Every member of $C_0(\alpha)$ is below $\omega^\alpha$ or at least $\Omega$, by induction on the construction from $\{ 0 \}$.
   Sums keep this by (F), since $\omega^\alpha$ is additively indecomposable.
5. A value $\psi_0(\xi)$ with $\xi < \alpha$ is $\omega^\xi < \omega^\alpha$, and a value $\psi_\mu(\xi)$ with $\mu \ge 1$ is at least $\Omega$.
   So $\psi_0(\alpha) \le \omega^\alpha$.
6. For the lower bound, take $0 < \beta < \omega^\alpha$ and assume every smaller ordinal is in $C_0(\alpha)$.
   Write $\beta = \omega^{\beta_1} + \dots + \omega^{\beta_k}$ in [[Cantor normal form|6GD30FGYDZ]] with $\beta_1 \ge \dots \ge \beta_k$, so each $\beta_i \le \beta_1 < \alpha$.
7. Each $\beta_i$ is below $\beta$: if $\beta_i = \beta$, then $\omega^\beta \le \beta$, so $\beta$ is an [[epsilon number|PQSHBKCE7V]] below $\omega^\alpha \le \varepsilon_0$, and none exists.
8. So each $\beta_i$ is in $C_0(\alpha)$, and since $\beta_i < \alpha$, so is $\psi_0(\beta_i) = \omega^{\beta_i}$, and so is the sum $\beta$.
   Hence $\psi_0(\alpha) = \omega^\alpha$.

### Proof of parts (c) and (d)

For part (c), let $\varepsilon_0 \le \alpha \le \Omega$.

9. Every $\beta < \varepsilon_0$ is in $C_0(\varepsilon_0) \subseteq C_0(\alpha)$, by (b).
10. Every member of $C_0(\alpha)$ is below $\varepsilon_0$ or at least $\Omega$.
    For a value $\psi_0(\xi)$, the argument has $\xi < \alpha \le \Omega$, so $\xi < \varepsilon_0$ by the induction hypothesis, and $\psi_0(\xi) = \omega^\xi < \varepsilon_0$.
11. So $\varepsilon_0 \notin C_0(\alpha)$, and $\psi_0(\alpha) = \varepsilon_0$.

Part (d) follows.

12. $\Omega = \psi_1(0)$ is in $C_0(\Omega + 1)$, and $\Omega < \Omega + 1$, so $\psi_0(\Omega) = \varepsilon_0$ is in $C_0(\Omega + 1)$.
13. Every ordinal below $\varepsilon_0 \cdot \omega$ is $\varepsilon_0 \cdot m + \gamma$ with $m$ natural and $\gamma < \varepsilon_0$, a sum of members by step 9, so it is in $C_0(\Omega + 1)$.
14. Every allowed value $\psi_0(\xi)$ has $\xi \le \Omega$, so it is at most $\varepsilon_0$ by (b) and (c), and the values $\psi_\mu(\xi)$ with $\mu \ge 1$ are at least $\Omega$.
15. By (F) with $\rho = \omega^{\varepsilon_0 + 1}$, every countable member of $C_0(\Omega + 1)$ is below $\varepsilon_0 \cdot \omega$, so $\psi_0(\Omega + 1) = \varepsilon_0 \cdot \omega$.

## Remarks

Below $\varepsilon_0$, Buchholz's $\psi_0$ is the function $\alpha \mapsto \omega^\alpha$.
So it produces powers of $\omega$ although the definition only uses addition.
At $\varepsilon_0$ it gets stuck, because the argument of $\psi_0$ must already be named, and every argument named from countable material is below $\varepsilon_0$.
The name $\Omega = \psi_1(0)$ gives $\varepsilon_0$ as $\psi_0(\Omega)$, and from $\Omega + 1$ on the function grows again.

Compare Madore's [[collapsing function with exponentiation|8S6CT4TMB7]].
There the stopping point below $\Omega$ is $\zeta_0$ instead of $\varepsilon_0$, because exponentiation is one of the operations.

## Explanations

### L1 human

Buchholz's first function starts at $1$, then gives $\omega$, then $\omega^2$, $\omega^3$, and so on.
It only knows how to add, but it can feed its own answers back in, and this produces all powers of $\omega$.
It gets stuck at $\varepsilon_0$, the first ordinal that equals $\omega$ to its own power.
The huge ordinal $\Omega$ gives the missing name: $\psi_0(\Omega) = \varepsilon_0$.
One step past $\Omega$, the function moves on to $\varepsilon_0 \cdot \omega$.

### L2 human

We compute $\psi_0(\omega + 1)$.
The argument $\omega$ is named, because $\omega = \psi_0(1)$ and $1 = \psi_0(0)$, with $0 < 1 < \omega + 1$.
So $\psi_0(\omega) = \omega^\omega$ is a member, and so are all $\psi_0(n) = \omega^n$.
Sums of copies of $\omega^\omega$ and of smaller powers give every ordinal below
$$\omega^\omega \cdot \omega = \omega^{\omega + 1},$$
and no allowed value reaches it, so $\psi_0(\omega + 1) = \omega^{\omega + 1}$.
Check: this agrees with part (b) for $\alpha = \omega + 1$.

Such computations test a notation against known ordinals before the impredicative part starts.
Watch out: $\Omega = \psi_1(0)$ is a member of $C_0(\alpha)$ for every $\alpha > 0$, but it is a name, not a countable ordinal, and sums with it stay uncountable.
