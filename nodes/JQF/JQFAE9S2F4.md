---
tag: JQFAE9S2F4
kind: concept
name: Veblen function
msc: ["03E10", "03F15"]
topics: [XTTKZTYDSD]
audience: grad
uses: [ERTAM0SFVB, 0YSCSX5YZC, 6QFEVWKE25, PQSHBKCE7V, KT50SMH3EC, ~0296c06c, ~f8083877, VB6YXF761M, 0ZHQMQ2C1N]
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

The Veblen functions $\varphi_\gamma$, for [[ordinals|0YSCSX5YZC]] $\gamma$, are defined by [[transfinite recursion|0ZHQMQ2C1N]] on $\gamma$: $\varphi_0(\alpha) = \omega^\alpha$; $\varphi_{\gamma + 1}$ enumerates in increasing order the fixed points of $\varphi_\gamma$; and for a limit $\gamma$, $\varphi_\gamma$ enumerates the common fixed points of all $\varphi_\delta$ with $\delta < \gamma$.
Each $\varphi_\gamma$ is a [[normal function|ERTAM0SFVB]], and the two-variable function $\varphi(\gamma, \alpha) = \varphi_\gamma(\alpha)$ is the Veblen function; the [[precise definition|6QFEVWKE25]] is a separate node.
The Veblen function names every ordinal below the Feferman-Schütte ordinal $\Gamma_0$ by a finite term.
So it is the basic tool for the ordinal notations of predicative proof theory.

## Motivation

The map $\alpha \mapsto \omega^\alpha$ names, through [[Cantor normal forms|~f8083877]], every ordinal below its first fixed point $\varepsilon_0$, by [[the least fixed point theorem|~0296c06c]].
To go further, one adds a name for each fixed point, giving $\varepsilon_\alpha$; but then $\alpha \mapsto \varepsilon_\alpha$ has fixed points too.
Oswald Veblen's idea is to repeat this step transfinitely and to index the stages by ordinals.
The index $\gamma$ becomes a second argument, and then a fixed point of $\gamma \mapsto \varphi_\gamma(0)$ is the next ordinal out of reach.

## Notation

Books write $\varphi_\gamma(\alpha)$, $\varphi(\gamma, \alpha)$ or $\varphi \gamma \alpha$ for the same ordinal.
Standard names: $\varphi_1(\alpha) = \varepsilon_\alpha$, the [[epsilon numbers|PQSHBKCE7V]]; $\varphi_2(\alpha) = \zeta_\alpha$; and $\varphi_3(\alpha) = \eta_\alpha$.
The finitary version $\varphi(\alpha_k, \ldots, \alpha_0)$ has more arguments, with $\varphi(\gamma, \alpha)$ as the two-argument case.
In Mathlib, `Ordinal.veblen o a` is $\varphi_o(a)$ with $\varphi_0(a) = \omega^a$.

## Remarks

### Examples

- $\varphi_0(1) = \omega$ and $\varphi_0(\omega) = \omega^\omega$, by the first clause.
- $\varphi_1(0) = \varepsilon_0$, the least fixed point of $\alpha \mapsto \omega^\alpha$; see [[epsilon nought|KT50SMH3EC]].
- $\varphi_2(0) = \zeta_0$, the least $\alpha$ with $\varepsilon_\alpha = \alpha$, is the limit of $\varepsilon_0, \varepsilon_{\varepsilon_0}, \varepsilon_{\varepsilon_{\varepsilon_0}}, \ldots$; see [[small values|~cb123c51]].
- $\varphi_\omega(0) = \sup_n \varphi_n(0)$, the least common fixed point of all $\varphi_n$.
- $\Gamma_0$ is the least $\alpha$ with $\varphi_\alpha(0) = \alpha$; it is the [[Feferman-Schütte ordinal|~5f65c1fc]].

### Non-examples

- [[The successor map cannot start a Veblen hierarchy|~13d45130]]: $\alpha \mapsto \alpha + 1$ has no fixed points.
- The map $\alpha \mapsto \omega^\alpha + 1$ is strictly increasing but not continuous, and it has no fixed points either, so it cannot replace $\varphi_0$.

### Basic properties

1. Each $\varphi_\gamma$ is normal: strictly increasing and continuous at limits.
2. If $\delta < \gamma$, then $\varphi_\delta(\varphi_\gamma(\alpha)) = \varphi_\gamma(\alpha)$.
3. Comparison: $\varphi_\alpha(\beta) < \varphi_\gamma(\delta)$ if and only if $\alpha = \gamma$ and $\beta < \delta$, or $\alpha < \gamma$ and $\beta < \varphi_\gamma(\delta)$, or $\alpha > \gamma$ and $\varphi_\alpha(\beta) < \delta$. See [[comparing Veblen terms|~1451a79e]].
4. Every ordinal of the form $\omega^\eta$ with $\eta > 0$ equals $\varphi_\gamma(\beta)$ for a unique pair with $\beta < \varphi_\gamma(\beta)$.
5. $\varphi_\gamma(0) \ge \gamma$ for all $\gamma$, and $\varphi_\gamma(0) = \gamma$ first holds at $\gamma = \Gamma_0$.

### History

Oswald Veblen introduced the hierarchy in 1908, as a study of continuous increasing functions of ordinals.
Feferman and Schütte used it in the 1960s to describe the ordinal $\Gamma_0$ of predicative analysis.

### Common errors

- Indexing errors. $\varphi_1$ enumerates the fixed points of $\varphi_0$ from the index $0$, so $\varphi_1(0) = \varepsilon_0$ and $\varphi_1(1) = \varepsilon_1$; counting from $1$ shifts every subscript.
- Confusing $\varepsilon_1$ with $\varepsilon_0 + 1$ or with $\varepsilon_0 \cdot \omega = \omega^{\varepsilon_0 + 1}$. Both lie strictly between $\varepsilon_0$ and $\varepsilon_1$.
- Using fundamental sequences without fixing the convention. Different books choose different sequences, and the values of hierarchies built on them change.

## Explanations

### L1 human

Start with the rule "raise $\omega$ to the power $\alpha$".
Some ordinals do not change under this rule, and the first of them is $\varepsilon_0$.
Listing all such ordinals gives a new rule, $\varphi_1$.
The ordinals that $\varphi_1$ does not change give $\varphi_2$, and so on, also at infinite stages such as $\varphi_\omega$.
For example, $\varphi_2(0)$ is the first ordinal $\alpha$ with $\varepsilon_\alpha = \alpha$.

### L2 human

We compute $\varphi_2(0)$ by iteration.

1. $\varphi_2(0)$ is the least fixed point of $\varphi_1$, which is a normal function.
2. The least fixed point of a normal function $f$ is $\sup_n f^n(0)$, as in [[the proof for epsilon nought|~0296c06c]].
3. $\varphi_1(0) = \varepsilon_0$, $\varphi_1(\varepsilon_0) = \varepsilon_{\varepsilon_0}$, $\varphi_1(\varepsilon_{\varepsilon_0}) = \varepsilon_{\varepsilon_{\varepsilon_0}}$, and so on.
4. So $\varphi_2(0) = \sup \{ \varepsilon_0, \varepsilon_{\varepsilon_0}, \varepsilon_{\varepsilon_{\varepsilon_0}}, \ldots \}$.

The typical use is to give names, and [[fundamental sequences|VB6YXF761M]], to ordinals between $\varepsilon_0$ and $\Gamma_0$.
The trap: $\varphi_2(1)$ is not $\varphi_2(0) + 1$; it is the next fixed point of $\varphi_1$, far above $\varphi_2(0)$.

### L3 human

Veblen's construction works for any normal function in place of $\alpha \mapsto \omega^\alpha$, and the derivative of a normal function, the enumeration of its fixed points, is the basic operation.
The finitary Veblen function $\varphi(\alpha_k, \ldots, \alpha_0)$ adds arguments: $\varphi(1, 0, 0) = \Gamma_0$, $\varphi(1, 0, 0, 0)$ is the Ackermann ordinal, and the supremum over $k$ of $\varphi(1, 0, \ldots, 0)$ is the [[small Veblen ordinal|~fafc7335]].
Transfinitely many arguments with finite support lead to the large Veblen ordinal.
In proof theory, $\Gamma_0$ is the ordinal of $\mathrm{ATR}_0$, and beyond the Veblen functions one uses [[collapsing functions|~766739ea]], which name fixed points by means of uncountable ordinals.
