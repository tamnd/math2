---
tag: 6QFEVWKE25
kind: definition
name: Veblen function
msc: ["03E10", "03F15"]
topics: [XTTKZTYDSD]
audience: grad
defines: JQFAE9S2F4
uses: [0RDJK7EQYY, PXTF18X433, 2C7MBG93AZ, 0ZHQMQ2C1N, ERTAM0SFVB, PQSHBKCE7V]
formal:
  - system: lean4
    library: mathlib
    decl: Ordinal.veblen
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Veblen_function
    locator: Veblen hierarchy
  - url: https://en.wikipedia.org/wiki/Veblen_function
    locator: Finitely many variables
---

## Definition

A function $f$ from [[ordinals|0RDJK7EQYY]] to ordinals is [[normal|PXTF18X433]] if it is strictly increasing and $f(\lambda) = \sup_{\xi < \lambda} f(\xi)$ for every limit $\lambda$.
For a class $C$ of ordinals that is closed and unbounded, its enumeration is the unique strictly increasing map from the ordinals onto $C$.
This enumeration is a normal function.

The Veblen functions $\varphi_\gamma$ are defined by [[transfinite recursion|0ZHQMQ2C1N]] on $\gamma$:

1. $\varphi_0(\alpha) = \omega^\alpha$, with exponentiation from [[ordinal arithmetic|2C7MBG93AZ]].
2. $\varphi_{\gamma + 1}$ is the enumeration of the class $\{ \alpha : \varphi_\gamma(\alpha) = \alpha \}$.
3. For a limit $\gamma$, $\varphi_\gamma$ is the enumeration of the class $\{ \alpha : \varphi_\delta(\alpha) = \alpha \text{ for all } \delta < \gamma \}$.

The Veblen function is the two-variable function $\varphi(\gamma, \alpha) := \varphi_\gamma(\alpha)$.

The definition is sound because of a lemma about [[normal functions|ERTAM0SFVB]], which we cite.
The fixed points of a normal function form a closed unbounded class, and so does the intersection of a set of such classes.
By induction on $\gamma$, each class in clauses 2 and 3 is closed and unbounded, and each $\varphi_\gamma$ is normal.

**Finitary version.** For finitely many arguments, set $\varphi(\alpha) = \omega^\alpha$, drop leading zeros, $\varphi(0, \alpha_{k-1}, \ldots, \alpha_0) = \varphi(\alpha_{k-1}, \ldots, \alpha_0)$, and for $\alpha_i > 0$ with $i \ge 1$ let
$$\varphi(\alpha_k, \ldots, \alpha_{i+1}, \alpha_i, \underbrace{0, \ldots, 0}_{i - 1}, \gamma)$$
be the $\gamma$-th common fixed point of the functions $\xi \mapsto \varphi(\alpha_k, \ldots, \alpha_{i+1}, \beta, \xi, 0, \ldots, 0)$ for all $\beta < \alpha_i$, where $\xi$ is in the place $i - 1$.
For two arguments this is the definition above.

**Transfinite version.** One allows arguments indexed by ordinals, with only finitely many nonzero, and uses the same fixed-point rule.

## Notation

Common forms are $\varphi_\gamma(\alpha)$, $\varphi(\gamma, \alpha)$ and $\varphi \gamma \alpha$.
Special names: $\varphi_1(\alpha) = \varepsilon_\alpha$, the [[epsilon numbers|PQSHBKCE7V]]; $\varphi_2(\alpha) = \zeta_\alpha$; $\Gamma_\alpha = \varphi(1, 0, \alpha)$, the strongly critical ordinals.

## Remarks

- Example: $\varphi_1(\alpha) = \varepsilon_\alpha$. Clause 2 makes $\varphi_1$ the enumeration of the fixed points of $\alpha \mapsto \omega^\alpha$, and these are the epsilon numbers.
- Example: $\varphi(1, 0, 0) = \Gamma_0$. With $i = 2$ and $\alpha_2 = 1$, it is the least fixed point of $\xi \mapsto \varphi(0, \xi, 0) = \varphi_\xi(0)$.
- Non-example: the clauses cannot start from $\alpha \mapsto \alpha + 1$, because it has no fixed points; see [[this non-example|288H8TGQYM]].
- The recursion uses that the earlier classes are nested: if $\delta < \gamma$, every fixed point of $\varphi_\gamma$ is a fixed point of $\varphi_\delta$.
- One may start from any normal function in place of $\alpha \mapsto \omega^\alpha$; the map from a normal function to the enumeration of its fixed points is called the derivative.

## Explanations

### L1 human

Each Veblen function lists, in order, the ordinals that the previous functions leave unchanged.
The first function is $\alpha \mapsto \omega^\alpha$, and the ordinals it leaves unchanged are the epsilon numbers $\varepsilon_0, \varepsilon_1, \ldots$.
So the second function sends $0$ to $\varepsilon_0$, $1$ to $\varepsilon_1$, and so on.

### L2 human

We check $\varphi_1(1) = \varepsilon_1$ and compute it.

1. By clause 2, $\varphi_1(1)$ is the second fixed point of $\alpha \mapsto \omega^\alpha$, the first being $\varepsilon_0$.
2. Iterate from $\varepsilon_0 + 1$: $\omega^{\varepsilon_0 + 1}$, $\omega^{\omega^{\varepsilon_0 + 1}}$, and so on.
3. The supremum is a fixed point by continuity, and every fixed point above $\varepsilon_0$ lies above all these stages.
4. So $\varphi_1(1) = \varepsilon_1$ is this supremum.

The typical use of the definition is to prove facts about all $\varphi_\gamma$ by induction on $\gamma$, using normality at each stage.
The trap: clause 3 takes common fixed points of all earlier functions, not only fixed points of one of them.
