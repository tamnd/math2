---
tag: 3HWF8NBKJE
kind: example
name: The first impredicative value of the collapsing function
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: research
instance_of: [8S6CT4TMB7]
uses: [8S6CT4TMB7, DM0R5VVBGJ, PQSHBKCE7V, 6GD30FGYDZ]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_collapsing_function
    locator: First impredicative values
---

## Example

We use the [[collapsing function|8S6CT4TMB7]] $\psi$ of the Wikipedia system, with names $0, 1, \omega, \Omega$, closure under $+$, $\cdot$ and powers, and the values $\psi(\xi)$ for named $\xi < \alpha$.
Let $\zeta_0$ be the least fixed point of $\gamma \mapsto \varepsilon_\gamma$.
We show that
$$\psi(\Omega + 1) = \varepsilon_{\zeta_0 + 1},$$
the next [[epsilon number|PQSHBKCE7V]] after $\zeta_0$.
We use the [[small values|DM0R5VVBGJ]]: $\psi(\gamma) = \varepsilon_\gamma$ for $\gamma \le \zeta_0$, and $\psi(\xi) = \zeta_0$ for $\zeta_0 \le \xi \le \Omega$.
Write $\varepsilon = \varepsilon_{\zeta_0 + 1}$.

1. The name $\Omega$ is in $C(\Omega + 1)$, and $\Omega < \Omega + 1$.
   So $\psi(\Omega) = \zeta_0$ is in $C(\Omega + 1)$.
2. Every allowed value $\psi(\xi)$ has $\xi \le \Omega$, so it is at most $\zeta_0$ by the small values, and in particular below $\varepsilon$.
3. Every member of $C(\Omega + 1)$ is below $\varepsilon$ or at least $\Omega$.
   The four names have this property, step 2 covers the values of $\psi$, and the closure facts (F1) and (F2) of the small values cover sums, products and powers.
4. So $\varepsilon \notin C(\Omega + 1)$, and $\psi(\Omega + 1) \le \varepsilon$.
5. For the lower bound, we show by induction on $\beta$ that every $\beta < \varepsilon$ is in $C(\Omega + 1)$.
   The cases $0$ and $1$ are names.
6. If $\beta > 1$ is not an epsilon number, the exponents of its [[Cantor normal form|6GD30FGYDZ]] are below $\beta$.
   They are in $C(\Omega + 1)$ by the induction hypothesis, so $\beta$ is too.
7. If $\beta = \varepsilon_\delta$ with $\delta < \zeta_0$, then $\delta < \beta$, so $\delta \in C(\Omega + 1)$.
   Since $\delta < \Omega + 1$, the value $\psi(\delta) = \beta$ is in $C(\Omega + 1)$.
8. The only other epsilon number below $\varepsilon$ is $\zeta_0$, which is in $C(\Omega + 1)$ by step 1.
9. So $\varepsilon$ is the least ordinal not in $C(\Omega + 1)$, and $\psi(\Omega + 1) = \varepsilon_{\zeta_0 + 1}$.

## Remarks

The example shows the step that makes $\psi$ a collapsing function.
Below $\Omega$ the value is stuck at $\zeta_0$, because no countable name reaches $\zeta_0$.
The argument $\Omega + 1$ breaks the deadlock, because it allows the name $\psi(\Omega)$, and that name is $\zeta_0$.
So the uncountable term $\Omega$ is used as a name for a countable ordinal.

Change the argument to $\Omega + n$ and the same proof, by induction on $n$, gives $\psi(\Omega + n) = \varepsilon_{\zeta_0 + n}$: at each stage the new name is the previous value.
The Wikipedia article continues the computation to $\psi(\Omega \cdot 2) = \zeta_1$, the second fixed point of $\gamma \mapsto \varepsilon_\gamma$.

## Explanations

### L1 human

Up to the large ordinal $\Omega$, the collapsing function is stuck at one value, $\zeta_0$.
It cannot pass $\zeta_0$, because no small expression names it.
At the argument $\Omega + 1$ the rules allow the name $\psi(\Omega)$, and this name is exactly $\zeta_0$.
With the new name, the function builds all ordinals up to the next epsilon number after $\zeta_0$.
So one step past $\Omega$ sets the function moving again.

### L2 human

We repeat the computation for $\psi(\Omega + 2)$.
In $C(\Omega + 2)$ we may use $\psi(\xi)$ for named $\xi \le \Omega + 1$, and $\Omega + 1$ is named as a sum of two names.
So $\psi(\Omega + 1) = \varepsilon_{\zeta_0 + 1}$ is a new name.
Every allowed value of $\psi$ is at most $\varepsilon_{\zeta_0 + 1}$, so the countable members of $C(\Omega + 2)$ stay below $\varepsilon_{\zeta_0 + 2}$.
Every ordinal below $\varepsilon_{\zeta_0 + 2}$ is built from the names, $\psi(\Omega)$ and $\psi(\Omega + 1)$, so $\psi(\Omega + 2) = \varepsilon_{\zeta_0 + 2}$.

The computation shows how the arguments above $\Omega$ continue the list of epsilon numbers.
Watch out for the condition $\xi < \alpha$: $\psi(\Omega)$ is a name in $C(\Omega + 1)$ but not in $C(\Omega)$, which is why $\psi(\Omega)$ is still $\zeta_0$.
