---
tag: 9KT4NGVX2F
kind: definition
name: Lindblad equation
msc: [81S22, 81P16, 47D07]
defines: 8KA04VC7G6
uses: [HM2HHE3J51, V1JTB52E8C, 0NEGN5CRSC, 0XC1RDBY7A]
sources:
  - url: https://en.wikipedia.org/wiki/Lindbladian
---

## Definition

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]] of finite dimension $d$, and let $B(H)$ be the space of linear operators on $H$.
A *Lindbladian* is a linear map $\mathcal{L} \colon B(H) \to B(H)$ of the form
$$\mathcal{L}(\rho) = -i [K, \rho] + \sum_{k=1}^{m} \gamma_k \left( L_k \rho L_k^* - \tfrac{1}{2} \left( L_k^* L_k \rho + \rho L_k^* L_k \right) \right),$$
where:

1. $K$ is a [[self-adjoint operator|0NEGN5CRSC]] on $H$, the Hamiltonian, and $[K, \rho] = K\rho - \rho K$.
2. $L_1, \dots, L_m$ are operators on $H$, the jump operators, and $L_k^*$ is the adjoint of $L_k$.
3. $\gamma_1, \dots, \gamma_m$ are real numbers with $\gamma_k \ge 0$, the rates.

The *Lindblad equation* is the linear differential equation $\frac{d\rho}{dt} = \mathcal{L}(\rho)$ for a curve $t \mapsto \rho(t)$ of [[density matrices|V1JTB52E8C]] on $H$.
Units are chosen so that the reduced Planck constant is $1$.

## Remarks

Example: let $H = \C^2$ with basis $|0\rangle, |1\rangle$, let $K = 0$, $m = 1$, $L_1 = |0\rangle\langle 1|$ and $\gamma_1 = \gamma > 0$.
Then $L_1 \rho L_1^* = \rho_{11} |0\rangle\langle 0|$ and $L_1^* L_1 = |1\rangle\langle 1|$, so the $(1,1)$ entry of $\mathcal{L}(\rho)$ is $-\gamma \rho_{11}$.
Hence $\rho_{11}(t) = e^{-\gamma t} \rho_{11}(0)$: the excited level decays at rate $\gamma$.

Non-example: the equation $\frac{d\rho}{dt} = -\gamma \rho$ with $\gamma > 0$ is not a Lindblad equation.
Every Lindbladian satisfies $\tr \mathcal{L}(\rho) = 0$, by cyclicity of the [[trace|0XC1RDBY7A]], so the Lindblad equation preserves the trace.
The solution $e^{-\gamma t} \rho$ loses trace, so no choice of $K$, $L_k$ and $\gamma_k$ gives this map.

The rates can be absorbed into the jump operators by replacing $L_k$ by $\sqrt{\gamma_k} L_k$.
The equation is also called the GKSL equation, after Gorini, Kossakowski, Sudarshan and Lindblad, who found it independently in 1976.
Their theorem says that a linear map $\mathcal{L}$ generates a semigroup $e^{t\mathcal{L}}$, $t \ge 0$, of completely positive trace-preserving maps if and only if $\mathcal{L}$ has the form above.
