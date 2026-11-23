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

The Veblen functions form a sequence of normal functions in which each function lists the common fixed points of all the earlier ones, starting from $\alpha \mapsto \omega^\alpha$.

A function $f$ from [[ordinals|0RDJK7EQYY]] to ordinals is [[normal|PXTF18X433]] if it is strictly increasing and $f(\lambda) = \sup_{\xi < \lambda} f(\xi)$ for every limit $\lambda$.
For a closed unbounded class $C$ of ordinals, its enumeration is the unique strictly increasing map from the ordinals onto $C$, and this map is normal.
The Veblen functions $\varphi_\gamma$ are defined by [[transfinite recursion|0ZHQMQ2C1N]] on $\gamma$:

1. $\varphi_0(\alpha) = \omega^\alpha$, with exponentiation from [[ordinal arithmetic|2C7MBG93AZ]];
2. $\varphi_{\gamma + 1}$ is the enumeration of the class $\{ \alpha : \varphi_\gamma(\alpha) = \alpha \}$;
3. for a limit $\gamma$, $\varphi_\gamma$ is the enumeration of the class $\{ \alpha : \varphi_\delta(\alpha) = \alpha \text{ for all } \delta < \gamma \}$.

The Veblen function is the two-variable function $\varphi(\gamma, \alpha) := \varphi_\gamma(\alpha)$.

The recursion makes sense because of a lemma about [[normal functions|ERTAM0SFVB]], which we cite.
The fixed points of a normal function form a closed unbounded class, and so does the intersection of a set of such classes.
By induction on $\gamma$, each class in clauses 2 and 3 is closed and unbounded, and each $\varphi_\gamma$ is normal.

**Finitary version.**
Set $\varphi(\alpha) = \omega^\alpha$, and drop leading zeros: $\varphi(0, \alpha_{k-1}, \ldots, \alpha_0) = \varphi(\alpha_{k-1}, \ldots, \alpha_0)$.
For $i \ge 1$ and $\alpha_i > 0$, the ordinal
$$\varphi(\alpha_k, \ldots, \alpha_{i+1}, \alpha_i, \underbrace{0, \ldots, 0}_{i - 1}, \gamma)$$
is the $\gamma$-th common fixed point of the functions $\xi \mapsto \varphi(\alpha_k, \ldots, \alpha_{i+1}, \beta, \xi, 0, \ldots, 0)$ for all $\beta < \alpha_i$, where $\xi$ stands in place $i - 1$.
For two arguments this is the definition above.

**Transfinite version.**
The arguments are indexed by ordinals, only finitely many of them are nonzero, and the same fixed-point rule applies.

## Notation

Common forms are $\varphi_\gamma(\alpha)$, $\varphi(\gamma, \alpha)$ and $\varphi \gamma \alpha$.
Special names are $\varphi_1(\alpha) = \varepsilon_\alpha$, the [[epsilon numbers|PQSHBKCE7V]], and $\varphi_2(\alpha) = \zeta_\alpha$.
The strongly critical ordinals are $\Gamma_\alpha = \varphi(1, 0, \alpha)$.

## Remarks

### Why each clause is there

Clause 1 fixes the starting function, and it must be normal.
If we started from $\alpha \mapsto \alpha + 1$, which has no fixed points, clause 2 would have nothing to enumerate; see [[this non-example|288H8TGQYM]].

Clause 2 makes $\varphi_1$ the enumeration of the fixed points of $\alpha \mapsto \omega^\alpha$, and these are the epsilon numbers, so $\varphi_1(\alpha) = \varepsilon_\alpha$.
Clause 3 is needed at limits because there is no single previous function.
At $\gamma = \omega$ it asks for ordinals that every $\varphi_n$ fixes, and a fixed point of $\varphi_5$ alone need not be one of them.

The classes are nested: if $\delta < \gamma$, every value of $\varphi_\gamma$ is a fixed point of $\varphi_\delta$.
So clause 2 could also be read with "all $\delta \le \gamma$", and the result would be the same.

### The finitary version at work

Take $i = 2$ and $\alpha_2 = 1$.
Then $\varphi(1, 0, 0)$ is the least fixed point of $\xi \mapsto \varphi(0, \xi, 0) = \varphi_\xi(0)$, which is $\Gamma_0$.
One may start from any normal function in place of $\alpha \mapsto \omega^\alpha$, and the map from a normal function to the enumeration of its fixed points is called the derivative.

## Explanations

### L1 human

Each Veblen function lists, in order, the ordinals that the previous functions leave unchanged.
The first function is $\alpha \mapsto \omega^\alpha$, and the ordinals it leaves unchanged are the epsilon numbers $\varepsilon_0, \varepsilon_1, \ldots$.
So the second function sends $0$ to $\varepsilon_0$, $1$ to $\varepsilon_1$, and so on.

### L2 human

We compute $\varphi_1(1)$ from the definition.
By clause 2, $\varphi_1(1)$ is the second fixed point of $\alpha \mapsto \omega^\alpha$, the first being $\varepsilon_0$.
Iterate the map from $\varepsilon_0 + 1$:
$$\varepsilon_0 + 1, \quad \omega^{\varepsilon_0 + 1}, \quad \omega^{\omega^{\varepsilon_0 + 1}}, \quad \ldots$$
The supremum is a fixed point by continuity, and every fixed point above $\varepsilon_0$ lies above all these terms.
So $\varphi_1(1) = \varepsilon_1$ is this supremum.

The typical use of the definition is to prove facts about all $\varphi_\gamma$ by induction on $\gamma$, with normality at each stage.
Watch out: clause 3 takes the common fixed points of all earlier functions, not the fixed points of one of them.
