---
tag: JQFAE9S2F4
kind: concept
name: Veblen function
msc: ["03E10", "03F15"]
topics: [XTTKZTYDSD]
audience: grad
uses: [ERTAM0SFVB, 0YSCSX5YZC, 6QFEVWKE25, PQSHBKCE7V, KT50SMH3EC, 9BX0XHX2D5, 7MBX59Y7N9, VB6YXF761M, 0ZHQMQ2C1N]
sources:
  - url: https://en.wikipedia.org/wiki/Veblen_function
    locator: Veblen hierarchy
  - url: https://en.wikipedia.org/wiki/Veblen_function
    locator: Finitely many variables
same_as:
  wikidata: Q921930
  wikipedia: Veblen function
---

## Summary

Start with the map $\alpha \mapsto \omega^\alpha$: it sends $0$ to $1$ and $1$ to $\omega$, so $\varphi_0(1) = \omega$.
Its first fixed point is $\varepsilon_0$, and the function that lists all its fixed points in order sends $0$ to $\varepsilon_0$, so $\varphi_1(0) = \varepsilon_0$.
The Veblen functions repeat this step through all the ordinals: each new function lists the fixed points of the earlier ones.
They give finite names to every ordinal below the Feferman-Schütte ordinal $\Gamma_0$, and so they are the basic tool of predicative proof theory.

The functions $\varphi_\gamma$, for [[ordinals|0YSCSX5YZC]] $\gamma$, are defined by [[transfinite recursion|0ZHQMQ2C1N]] on $\gamma$.
First, $\varphi_0(\alpha) = \omega^\alpha$.
Next, $\varphi_{\gamma + 1}$ enumerates in increasing order the fixed points of $\varphi_\gamma$.
For a limit $\gamma$, $\varphi_\gamma$ enumerates the common fixed points of all $\varphi_\delta$ with $\delta < \gamma$.
Each $\varphi_\gamma$ is a [[normal function|ERTAM0SFVB]], and the two-variable function $\varphi(\gamma, \alpha) = \varphi_\gamma(\alpha)$ is the Veblen function; the [[precise definition|6QFEVWKE25]] gives the details.

## Motivation

Cantor normal forms name, through the map $\alpha \mapsto \omega^\alpha$, every ordinal below its first fixed point $\varepsilon_0$, by [[the least fixed point theorem|9BX0XHX2D5]].
To go further, we add a name for each fixed point and get $\varepsilon_\alpha$.
But the map $\alpha \mapsto \varepsilon_\alpha$ has fixed points of its own, such as the limit of $\varepsilon_0, \varepsilon_{\varepsilon_0}, \varepsilon_{\varepsilon_{\varepsilon_0}}, \ldots$.
Veblen's idea is to repeat the step transfinitely and to index the stages by ordinals.

The payoff in proof theory is a [[notation system|7MBX59Y7N9]] of type $\Gamma_0$, built from $0$, addition and $\varphi$.
It is the notation system for the ordinals of predicative theories such as $\mathrm{ATR}_0$, and the [[collapsing functions|8S6CT4TMB7]] used for stronger theories are measured against it.

## Notation

Books write $\varphi_\gamma(\alpha)$, $\varphi(\gamma, \alpha)$ or $\varphi \gamma \alpha$ for the same ordinal.
The first levels have names of their own: $\varphi_1(\alpha) = \varepsilon_\alpha$ are the [[epsilon numbers|PQSHBKCE7V]], $\varphi_2(\alpha) = \zeta_\alpha$, and $\varphi_3(\alpha) = \eta_\alpha$.
The finitary version $\varphi(\alpha_k, \ldots, \alpha_0)$ has more arguments, and $\varphi(\gamma, \alpha)$ is its two-argument case.
In Mathlib, `Ordinal.veblen o a` is $\varphi_o(a)$, with $\varphi_0(a) = \omega^a$.

## Remarks

### A first table of values

The first clause gives $\varphi_0(0) = 1$, $\varphi_0(1) = \omega$ and $\varphi_0(\omega) = \omega^\omega$.
The second clause gives $\varphi_1(0) = \varepsilon_0$, the least fixed point of $\alpha \mapsto \omega^\alpha$; see [[epsilon nought|KT50SMH3EC]].
At the next level, $\varphi_2(0) = \zeta_0$ is the least $\alpha$ with $\varepsilon_\alpha = \alpha$:
$$\zeta_0 = \sup \{ \varepsilon_0, \varepsilon_{\varepsilon_0}, \varepsilon_{\varepsilon_{\varepsilon_0}}, \ldots \}.$$
At the first limit level, $\varphi_\omega(0) = \sup_n \varphi_n(0)$ is the least common fixed point of all $\varphi_n$.
[[Small values of the Veblen function|R9YGZQ0ZG3]] checks these with fundamental sequences.

### Where the hierarchy stops

Since $\gamma \mapsto \varphi_\gamma(0)$ is itself normal, it has fixed points too.
The least one, the least $\alpha$ with $\varphi_\alpha(0) = \alpha$, is the [[Feferman-Schütte ordinal|CNN7BK5YAW]] $\Gamma_0$.
Below $\Gamma_0$ we always have $\varphi_\gamma(0) > \gamma$, so every ordinal there has a name built from smaller names.
At $\Gamma_0$ this fails, and new notation is needed.

### Rules for computing

Each $\varphi_\gamma$ is normal: strictly increasing and continuous at limits.
If $\delta < \gamma$, then $\varphi_\delta(\varphi_\gamma(\alpha)) = \varphi_\gamma(\alpha)$, because the values of $\varphi_\gamma$ are fixed points of every earlier function.
This gives the comparison rule: $\varphi_\alpha(\beta) < \varphi_\gamma(\delta)$ exactly when $\alpha = \gamma$ and $\beta < \delta$, or $\alpha < \gamma$ and $\beta < \varphi_\gamma(\delta)$, or $\alpha > \gamma$ and $\varphi_\alpha(\beta) < \delta$.
[[Comparing Veblen terms|WXRVDVK1VA]] proves it and runs it on examples.
Every ordinal of the form $\omega^\eta$ equals $\varphi_\gamma(\beta)$ for exactly one pair with $\beta < \varphi_\gamma(\beta)$, and this gives unique normal forms.

### What cannot start a hierarchy

[[The successor map|288H8TGQYM]] $\alpha \mapsto \alpha + 1$ has no fixed points, so there is nothing for $\varphi_1$ to list.
The map $\alpha \mapsto \omega^\alpha + 1$ is strictly increasing but not continuous: at $\omega$ the values $\omega^n + 1$ climb to $\omega^\omega$, but the value at $\omega$ is $\omega^\omega + 1$.
It has no fixed points either, since $\omega^\alpha + 1 > \omega^\alpha \ge \alpha$.
So the construction needs a normal function at the start.

### Watch out

The indexing starts at $0$.
The function $\varphi_1$ lists the fixed points of $\varphi_0$ from index $0$, so $\varphi_1(0) = \varepsilon_0$ and $\varphi_1(1) = \varepsilon_1$.
Counting from $1$ shifts every subscript by one.

The ordinal $\varepsilon_1$ is far above $\varepsilon_0 + 1$ and above $\varepsilon_0 \cdot \omega = \omega^{\varepsilon_0 + 1}$.
Both of these lie strictly between $\varepsilon_0$ and $\varepsilon_1$.

Fundamental sequences are a choice, not part of the definition.
Different books choose different sequences, and hierarchies of functions built on them change their values.

### History

Oswald Veblen introduced the hierarchy in 1908, in a study of continuous increasing functions of ordinals.
Feferman and Schütte used it in the 1960s to describe $\Gamma_0$, the ordinal of predicative analysis.

### Try it

Is $\varphi_1(\varphi_2(0))$ larger than $\varphi_2(0)$?
No, they are equal: $\varphi_2(0) = \zeta_0$ is a fixed point of $\varphi_1$, so $\varepsilon_{\zeta_0} = \zeta_0$.

Which is larger, $\varphi_2(1)$ or $\varphi_2(0) + 1$?
$\varphi_2(1)$ is the next fixed point of $\varphi_1$ after $\zeta_0$, and it is an epsilon number, so it is far larger than $\zeta_0 + 1$.

## Explanations

### L1 human

Start with the rule "raise $\omega$ to the power $\alpha$".
Some ordinals do not change under this rule, and the first of them is $\varepsilon_0$.
Listing all such ordinals in order gives a new rule, $\varphi_1$.
The ordinals that $\varphi_1$ does not change give $\varphi_2$, and so on, also at infinite stages such as $\varphi_\omega$.
For example, $\varphi_2(0)$ is the first ordinal $\alpha$ with $\varepsilon_\alpha = \alpha$.

### L2 human

We compute $\varphi_2(0)$ by iteration.
It is the least fixed point of $\varphi_1$, which is a normal function.
The least fixed point of a normal function $f$ is $\sup_n f^n(0)$, as in [[the proof for epsilon nought|9BX0XHX2D5]].
Apply $\varphi_1$ again and again, starting from $0$:
$$\varphi_1(0) = \varepsilon_0, \qquad \varphi_1(\varepsilon_0) = \varepsilon_{\varepsilon_0}, \qquad \varphi_1(\varepsilon_{\varepsilon_0}) = \varepsilon_{\varepsilon_{\varepsilon_0}}.$$
So $\varphi_2(0)$ is the supremum of this sequence.
Check: by continuity, $\varphi_1$ of the supremum is the supremum of the next terms, which is the same supremum.

The typical use is to give names, and [[fundamental sequences|VB6YXF761M]], to the ordinals between $\varepsilon_0$ and $\Gamma_0$.
Watch out: $\varphi_2(1)$ is not $\varphi_2(0) + 1$, but the next fixed point of $\varphi_1$, far above $\varphi_2(0)$.

### L3 human

Veblen's construction works for any normal function in place of $\alpha \mapsto \omega^\alpha$.
The enumeration of the fixed points of a normal function is called its derivative, and it is the basic operation of the theory.
The finitary Veblen function $\varphi(\alpha_k, \ldots, \alpha_0)$ adds arguments: $\varphi(1, 0, 0) = \Gamma_0$, and $\varphi(1, 0, 0, 0)$ is the Ackermann ordinal.
The supremum over $k$ of $\varphi(1, 0, \ldots, 0)$ is the [[small Veblen ordinal|ZHDM657G3D]], and arguments indexed by ordinals lead to the large Veblen ordinal.
In proof theory $\Gamma_0$ is the ordinal of $\mathrm{ATR}_0$, and beyond the Veblen functions one uses collapsing functions, which name fixed points with the help of uncountable ordinals.
