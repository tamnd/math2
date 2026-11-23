---
tag: ZHDM657G3D
kind: object
name: Small and large Veblen ordinals
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: research
uses: [JQFAE9S2F4, 6QFEVWKE25, CNN7BK5YAW, 8S6CT4TMB7, XVHKCX4F5Y, 7MBX59Y7N9, 01TQB88H4C]
sources:
  - url: https://en.wikipedia.org/wiki/Small_Veblen_ordinal
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Large_Veblen_ordinal
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ackermann_ordinal
    locator: lead section
---

## Description

The finitary [[Veblen function|JQFAE9S2F4]] gives $\varphi(1, 0) = \varepsilon_0$, $\varphi(1, 0, 0) = \Gamma_0$, and $\varphi(1, 0, 0, 0)$, the Ackermann ordinal.
The small Veblen ordinal $\mathrm{SVO}$ is the supremum of $\varphi(1, 0, \ldots, 0)$, with $k$ zeros, over all finite $k$.
It is the least ordinal not reached from $0$ by addition and the Veblen function with finitely many arguments.
The large Veblen ordinal $\mathrm{LVO}$ is the corresponding limit for the transfinite Veblen function, whose arguments are indexed by ordinals with only finitely many nonzero.
The Ackermann ordinal lies between the [[Feferman-Schütte ordinal|CNN7BK5YAW]] and $\mathrm{SVO}$, and all of these are [[countable|01TQB88H4C]].

## Remarks

### The ladder to the small Veblen ordinal

With the [[finitary definition|6QFEVWKE25]], the first values of $\varphi(1, 0, \ldots, 0)$ are these.

1. $\varphi(1) = \omega^1 = \omega$.
2. $\varphi(1, 0) = \varphi_1(0) = \varepsilon_0$.
3. $\varphi(1, 0, 0) = \Gamma_0$, the least fixed point of $\xi \mapsto \varphi(\xi, 0)$.
4. $\varphi(1, 0, 0, 0)$, the Ackermann ordinal, is the least fixed point of $\xi \mapsto \varphi(\xi, 0, 0)$.
5. In general $\varphi(1, 0^{k+1})$ is the least fixed point of $\xi \mapsto \varphi(\xi, 0^k)$, where $0^k$ is a list of $k$ zeros.

Each step adds one argument, and $\mathrm{SVO}$ is the limit of the ladder.

### Other notations

We use Madore's [[collapsing function|8S6CT4TMB7]] $\psi$, whose sets $C(\alpha)$ are generated from $0, 1, \omega, \Omega$ by $+$, $\cdot$, exponentiation and $\psi$.
In it, $\Gamma_0 = \psi(\Omega^\Omega)$ and the Ackermann ordinal is $\psi(\Omega^{\Omega^2})$.
The small Veblen ordinal is $\psi(\Omega^{\Omega^\omega})$, and the large one is $\psi(\Omega^{\Omega^\Omega})$.
Three arguments give the exponent $\Omega^{\Omega}$ and four give $\Omega^{\Omega^2}$; all finite numbers of arguments together lead to $\Omega^{\Omega^\omega}$, and ordinal-indexed arguments to $\Omega^{\Omega^\Omega}$.
Other collapsing functions give other formulas for the same ordinals.

### Role in proof theory and combinatorics

The small Veblen ordinal measures the strength of [[Kruskal's tree theorem|XVHKCX4F5Y]].
It is the maximal order type of finite rooted trees under homeomorphic embedding, a result of Schmidt from 1979.
Ackermann's notation system of 1951 reaches the Ackermann ordinal, and it is weaker than Veblen's system of 1908.
Both Veblen ordinals lie far below the Bachmann-Howard ordinal $\psi(\varepsilon_{\Omega + 1})$, since $\Omega^{\Omega^\Omega} < \varepsilon_{\Omega + 1}$.

### Common errors

Some authors use the name "Ackermann ordinal" for $\mathrm{SVO}$, which is larger, so check which one is meant.

Another error treats $\mathrm{LVO}$ as a small step above $\mathrm{SVO}$.
The step from $\mathrm{SVO}$ to $\mathrm{LVO}$ needs arguments indexed by infinite ordinals, which corresponds to the jump from $\Omega^{\Omega^\omega}$ to $\Omega^{\Omega^\Omega}$ in the exponent.

## Explanations

### L1 human

The Veblen function with two inputs names every ordinal up to $\Gamma_0$.
Allowing three inputs goes further, four inputs further still, and so on.
The small Veblen ordinal is where all these finite versions together stop.
Allowing infinitely many inputs, as long as only finitely many are nonzero, gives a much larger limit, the large Veblen ordinal.

### L2 human

We check that $\Gamma_0 < \varphi(1, 0, 0, 0)$ in the finitary Veblen function.

1. $\varphi(1, 0, 0, 0)$ is the least fixed point of $h(\xi) = \varphi(\xi, 0, 0)$.
2. $h(0) = \varphi(0, 0, 0) = \varphi(0) = 1$, after dropping leading zeros, and $h(1) = \varphi(1, 0, 0) = \Gamma_0$.
3. So neither $0$ nor $1$ is a fixed point of $h$, and the least fixed point $\rho$ satisfies $\rho > 1$.
4. Since $h$ is strictly increasing, $\rho = h(\rho) > h(1) = \Gamma_0$.

The typical use is to place a theory or a combinatorial principle above $\Gamma_0$ on the scale of ordinals.
The trap: the same letter $\psi$ is used by different authors for different collapsing functions, so the expressions above hold only in Madore's system.
