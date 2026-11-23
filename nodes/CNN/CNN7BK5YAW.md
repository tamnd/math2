---
tag: CNN7BK5YAW
kind: object
name: Feferman-Schütte ordinal
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: grad
uses: [JQFAE9S2F4, 6QFEVWKE25, C72RBH0CDR, WXRVDVK1VA, R9YGZQ0ZG3, 7MBX59Y7N9, 01TQB88H4C, PTA0GDJWZQ, XVHKCX4F5Y, 8S6CT4TMB7, 7SQS69T17R]
sources:
  - url: https://en.wikipedia.org/wiki/Feferman%E2%80%93Sch%C3%BCtte_ordinal
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Feferman%E2%80%93Sch%C3%BCtte_ordinal
    locator: Properties
---

## Description

Start at $0$ and apply $\gamma \mapsto \varphi_\gamma(0)$ again and again: the values are $1$, $\varepsilon_0$, $\varphi_{\varepsilon_0}(0)$, $\varphi_{\varphi_{\varepsilon_0}(0)}(0)$, and so on.
The supremum of this sequence is the Feferman-Schütte ordinal $\Gamma_0$, where $\varphi$ is the binary [[Veblen function|JQFAE9S2F4]].
It is the least ordinal $\alpha$ with $\varphi_\alpha(0) = \alpha$, and in the finitary Veblen function $\Gamma_0 = \varphi(1, 0, 0)$.
It is also the least ordinal that cannot be reached from $0$ by addition and the binary Veblen function.
It is a [[countable|01TQB88H4C]] ordinal, and it is the [[proof-theoretic ordinal|C72RBH0CDR]] of $\mathrm{ATR}_0$ and of predicative analysis.

## Remarks

### Why the three descriptions agree

1. The map $g(\gamma) = \varphi_\gamma(0)$ is a normal function, so its least fixed point is $\sup_n g^n(0)$.
   The iterates are $g(0) = 1$, $g(1) = \varepsilon_0$, $g(\varepsilon_0) = \varphi_{\varepsilon_0}(0)$, and so on.
2. In the finitary Veblen function, $\varphi(1, 0, 0)$ is by [[definition|6QFEVWKE25]] the least fixed point of $\xi \mapsto \varphi(\xi, 0) = g(\xi)$.
3. Closure: let $\alpha, \beta < \Gamma_0$.
   By [[the comparison rule|WXRVDVK1VA]] with $\alpha < \Gamma_0$, $\varphi_\alpha(\beta) < \varphi_{\Gamma_0}(0) = \Gamma_0$ exactly when $\beta < \Gamma_0$, which holds.
   Also $\alpha + \beta < \Gamma_0$, since $\Gamma_0$ is a fixed point of $\varphi_0$ and so closed under addition.
4. So every term built from $0$, $+$ and $\varphi$ names an ordinal below $\Gamma_0$, by induction on terms.
5. Conversely, let $0 < \beta < \Gamma_0$.
   Each summand $\omega^\eta$ of the Cantor normal form of $\beta$ equals $\varphi_\gamma(\delta)$ for exactly one pair with $\delta < \varphi_\gamma(\delta)$.
   So $\beta = \varphi_{\gamma_1}(\delta_1) + \cdots + \varphi_{\gamma_k}(\delta_k)$ with $\delta_i < \varphi_{\gamma_i}(\delta_i) \le \beta$.
6. Also $\gamma_i \le \varphi_{\gamma_i}(0) \le \varphi_{\gamma_i}(\delta_i) \le \beta$.
   If $\gamma_i = \beta$, equality holds throughout, and $\gamma_i$ is a fixed point of $g$ below $\Gamma_0$, which step 1 excludes.
   So $\gamma_i < \beta$.
7. By induction on $\beta$, every ordinal below $\Gamma_0$ has a term.

### Notation system

The terms of steps 5 to 7, with the condition $\delta < \varphi_\gamma(\delta)$ in each term, give a primitive recursive [[ordinal notation system|7MBX59Y7N9]] of order type $\Gamma_0$.
Its fundamental sequence at the top is $\Gamma_0[0] = 0$ and $\Gamma_0[n+1] = \varphi_{\Gamma_0[n]}(0)$; see [[small values|R9YGZQ0ZG3]].
In Madore's [[collapsing function|8S6CT4TMB7]] $\psi$, with $C(\alpha)$ generated from $0, 1, \omega, \Omega$, we have $\Gamma_0 = \psi(\Omega^\Omega)$.
In Feferman's two-place $\theta$ functions, $\Gamma_0 = \theta(\Omega, 0)$.
The next ordinals $\Gamma_1, \Gamma_2, \ldots$ are the later fixed points of $g$, so $\Gamma_\alpha = \varphi(1, 0, \alpha)$.

### Role in proof theory

The ordinal $\Gamma_0$ is the proof-theoretic ordinal of arithmetical transfinite recursion $\mathrm{ATR}_0$, a system of [[reverse mathematics|7SQS69T17R]].
Feferman and Schütte studied autonomous progressions of systems of ramified analysis, in which a system may use a level only after an earlier system has proved that level well-founded.
They showed, independently, that $\Gamma_0$ is the least ordinal that these progressions cannot reach.
For this reason $\Gamma_0$ is often called the limit of [[predicative|PTA0GDJWZQ]] mathematics.
[[Kruskal's tree theorem|XVHKCX4F5Y]] is not provable in $\mathrm{ATR}_0$, and its strength is measured by the larger [[small Veblen ordinal|ZHDM657G3D]].

### History

Feferman published the analysis in 1964 and Schütte in 1965, and they worked independently.
Both built on Veblen's functions of 1908.

### Common errors

Some texts call $\Gamma_0$ "the first impredicative ordinal" as if it were a theorem.
That reading depends on the Feferman-Schütte analysis of predicativity, and some authors dispute it.

Another error confuses $\Gamma_0$ with $\varphi_\omega(0)$ or with $\varphi_{\varepsilon_0}(0)$.
Both are far below $\Gamma_0$, since each is $g(\gamma)$ for some $\gamma < \Gamma_0$.

## Explanations

### L1 human

With addition and the Veblen functions one can write names for huge countable ordinals, such as $\varepsilon_0$ and $\varphi_{\varepsilon_0}(0)$.
Each name is built from smaller names.
The ordinal $\Gamma_0$ is the first one that has no such name: to name it, one would need $\Gamma_0$ itself as an index.
Logicians found that it also marks the limit of a careful, "predicative" kind of mathematics.

### L2 human

We list the first steps towards $\Gamma_0$ and check that they stay below it.

1. $\Gamma_0[1] = \varphi_0(0) = 1$.
2. $\Gamma_0[2] = \varphi_1(0) = \varepsilon_0$.
3. $\Gamma_0[3] = \varphi_{\varepsilon_0}(0)$, the first common fixed point of all $\varphi_\delta$ with $\delta < \varepsilon_0$.
4. Each term has an index that is a smaller term, so by the comparison rule each is below $\varphi_{\Gamma_0}(0) = \Gamma_0$.

The typical use is as the upper end of the notation system for predicative theories, such as $\mathrm{ATR}_0$.
The trap: the term $\varphi_{\Gamma_0}(0)$ is not a new name, since it equals $\Gamma_0$, and so the Veblen notation stops here.
