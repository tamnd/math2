---
tag: CNN7BK5YAW
kind: object
name: Feferman–Schütte ordinal
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: grad
uses: [JQFAE9S2F4, 6QFEVWKE25, C72RBH0CDR, WXRVDVK1VA, R9YGZQ0ZG3, 7MBX59Y7N9, 01TQB88H4C, PTA0GDJWZQ, XVHKCX4F5Y, 8S6CT4TMB7, 7SQS69T17R]
sources:
  - url: https://en.wikipedia.org/wiki/Feferman–Schütte_ordinal
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Feferman–Schütte_ordinal
    locator: Properties
---

## Description

The Feferman-Schütte ordinal $\Gamma_0$ is the least ordinal $\alpha$ with $\varphi_\alpha(0) = \alpha$, where $\varphi$ is the binary [[Veblen function|JQFAE9S2F4]].
Equivalently, $\Gamma_0 = \varphi(1, 0, 0)$ in the finitary Veblen function, and $\Gamma_0 = \sup \{0, 1, \varepsilon_0, \varphi_{\varepsilon_0}(0), \varphi_{\varphi_{\varepsilon_0}(0)}(0), \ldots\}$.
It is the least ordinal that cannot be reached from $0$ by addition and the binary Veblen function.
It is a [[countable|01TQB88H4C]] ordinal, and it is the [[proof-theoretic ordinal|C72RBH0CDR]] of $\mathrm{ATR}_0$.

## Remarks

### Why the three descriptions agree

1. The map $g(\gamma) = \varphi_\gamma(0)$ is a normal function, so its least fixed point is $\sup_n g^n(0)$. The iterates are $g(0) = 1$, $g(1) = \varepsilon_0$, $g(\varepsilon_0) = \varphi_{\varepsilon_0}(0)$, and so on.
2. In the finitary Veblen function, $\varphi(1, 0, 0)$ is by [[definition|6QFEVWKE25]] the least fixed point of $\xi \mapsto \varphi(\xi, 0) = g(\xi)$.
3. Closure: let $\alpha, \beta < \Gamma_0$. By [[the comparison rule|WXRVDVK1VA]] with $\alpha < \Gamma_0$, $\varphi_\alpha(\beta) < \varphi_{\Gamma_0}(0) = \Gamma_0$ exactly when $\beta < \Gamma_0$, which holds. Also $\alpha + \beta < \Gamma_0$, since $\Gamma_0$ is a fixed point of $\varphi_0$ and hence closed under addition.
4. So every term built from $0$, $+$ and $\varphi$ names an ordinal below $\Gamma_0$, by induction on terms.
5. Conversely, let $0 < \beta < \Gamma_0$. By the Cantor normal form and property 4 of the Veblen function, $\beta = \varphi_{\gamma_1}(\delta_1) + \cdots + \varphi_{\gamma_k}(\delta_k)$ with $\delta_i < \varphi_{\gamma_i}(\delta_i) \le \beta$.
6. Also $\gamma_i \le \varphi_{\gamma_i}(0) \le \varphi_{\gamma_i}(\delta_i)$. Equality throughout would make $\gamma_i$ a fixed point of $g$ below $\Gamma_0$, which step 1 excludes. So $\gamma_i < \beta$.
7. By induction on $\beta$, every ordinal below $\Gamma_0$ has a term.

### Notation system

The terms of steps 5 to 7, with the condition $\delta < \varphi_\gamma(\delta)$ in each term, give a primitive recursive [[ordinal notation system|7MBX59Y7N9]] of order type $\Gamma_0$.
Its fundamental sequence at the top is $\Gamma_0[0] = 0$ and $\Gamma_0[n+1] = \varphi_{\Gamma_0[n]}(0)$; see [[small values|R9YGZQ0ZG3]].
In [[collapsing function|8S6CT4TMB7]] notation, $\Gamma_0 = \psi(\Omega^\Omega)$, and in Feferman's notation $\Gamma_0 = \theta(\Omega)$.
The next ordinals $\Gamma_1, \Gamma_2, \ldots$ are the later fixed points of $g$, so $\Gamma_\alpha = \varphi(1, 0, \alpha)$.

### Role in proof theory

- $\Gamma_0$ is the proof-theoretic ordinal of arithmetical transfinite recursion $\mathrm{ATR}_0$, a system of [[reverse mathematics|7SQS69T17R]].
- Feferman and Schütte, independently in the 1960s, studied autonomous progressions of predicative systems of ramified analysis. They showed that $\Gamma_0$ is the limit of the ordinals that these progressions reach.
- For this reason $\Gamma_0$ is often called the limit of [[predicative|PTA0GDJWZQ]] mathematics.
- [[Kruskal's tree theorem|XVHKCX4F5Y]] is not provable in $\mathrm{ATR}_0$; its strength is measured by the larger [[small Veblen ordinal|ZHDM657G3D]].

### Common errors

- Calling $\Gamma_0$ "the first impredicative ordinal" as a theorem. This reading depends on the analysis of predicativity by Feferman and Schütte, and some authors dispute it.
- Confusing $\Gamma_0$ with $\varphi_\omega(0)$ or with $\varphi_{\varepsilon_0}(0)$. Both are far below $\Gamma_0$, since each is $g(\gamma)$ for some $\gamma < \Gamma_0$.

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
