---
tag: GT4KH0TTYV
kind: example
name: A collapse without an uncountable generator stops at zeta zero
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: research
not_instance_of:
  - target: 8S6CT4TMB7
    note: the generators contain no uncountable ordinal, so nothing is collapsed and the values stop at zeta zero
uses: [8S6CT4TMB7, DM0R5VVBGJ, PQSHBKCE7V]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_collapsing_function
    locator: Predicative start
---

## Example

We define a function $\psi'$ like the [[collapsing function|8S6CT4TMB7]] $\psi$ of Madore's system, but without the name $\Omega$.
Let $C'(\alpha)$ be the least set that contains $0, 1, \omega$, is closed under sums, products and powers, and contains $\psi'(\xi)$ for each $\xi \in C'(\alpha)$ with $\xi < \alpha$.
Let $\psi'(\alpha)$ be the least ordinal not in $C'(\alpha)$.
We show that $\psi'(\alpha) = \varepsilon_\alpha$ for $\alpha \le \zeta_0$, and $\psi'(\alpha) = \zeta_0$ for every $\alpha \ge \zeta_0$, however large.

1. For $\alpha \le \zeta_0$, the proof of part (a) of the [[small values|DM0R5VVBGJ]] works without change.
   The case "at least $\Omega$" in its upper bound never occurs, because every member of $C'(\alpha)$ is countable.
2. So $\psi'(\alpha) = \varepsilon_\alpha$ for $\alpha \le \zeta_0$, and in particular $\psi'(\zeta_0) = \zeta_0$.
3. Let $\alpha \ge \zeta_0$.
   Every $\beta < \zeta_0$ is in $C'(\zeta_0) \subseteq C'(\alpha)$, so $\psi'(\alpha) \ge \zeta_0$.
4. We show that every member of $C'(\alpha)$ is below $\zeta_0$, by induction on the construction.
   The names $0, 1, \omega$ are below $\zeta_0$.
5. The ordinal $\zeta_0$ is an [[epsilon number|PQSHBKCE7V]], so sums, products and powers of members below $\zeta_0$ stay below $\zeta_0$.
6. A value $\psi'(\xi)$ has $\xi \in C'(\alpha)$, so $\xi < \zeta_0$ by the induction hypothesis, and $\psi'(\xi) = \varepsilon_\xi < \zeta_0$ by step 2.
7. So $\zeta_0 \notin C'(\alpha)$, and $\psi'(\alpha) = \zeta_0$.

The function $\psi'$ is not a collapsing function: it has no uncountable name, and its values never pass $\zeta_0$.

## Remarks

The example shows why the uncountable name is needed.
Without $\Omega$, every member of the closure sets is below $\zeta_0$, so a large argument cannot be named inside $C'(\alpha)$ and has no effect.
With $\Omega$, the term $\psi(\Omega)$ names $\zeta_0$, and the real function passes $\zeta_0$ at the argument $\Omega + 1$.

What if we add $\zeta_0$ itself as a name instead of $\Omega$?
The same proof shows that the function then stops at the next fixed point $\zeta_1$.
The same happens for any set of countable names: the set of everything they can ever name is countable, so it is bounded below $\Omega$, and above that bound large arguments add nothing.

## Explanations

### L1 human

Imagine a machine that names ordinals and may use its own earlier answers.
Without a huge helper number, the machine gets stuck at one ordinal, $\zeta_0$.
It cannot name $\zeta_0$, and every later step only uses names below $\zeta_0$.
So feeding it larger inputs does not help.
The huge number $\Omega$ is what lets the real collapsing function escape this trap.

### L2 human

We compare $\psi'(\zeta_0 + 1)$ with the real values.
For $\psi'$, the argument $\zeta_0$ is not in $C'(\zeta_0 + 1)$ by step 4, so $\psi'(\zeta_0)$ is not available, and $\psi'(\zeta_0 + 1) = \zeta_0$.
For $\psi$, the argument $\zeta_0$ is not in $C(\zeta_0 + 1)$ either, and $\psi(\zeta_0 + 1) = \zeta_0$ by the small values.
The difference appears at $\Omega + 1$: the real $\psi$ may use the name $\Omega$, and $\psi(\Omega + 1) = \varepsilon_{\zeta_0 + 1}$, while $\psi'$ has no argument that gives a value above $\zeta_0$.

The example explains the role of $\Omega$ in a first course on ordinal notations.
Watch out: a large argument alone does not give a large value, because the argument must also be named inside the closure set.
