---
tag: MH2WAGERAT
kind: definition
name: Entanglement distillation
msc: [81P48, 81P42]
defines: ZWEGNHHYRB
uses: [EY0X2NKA3S, V1JTB52E8C, F5EB23T03M, CA57HMCRQQ, 2Q85WTJ07A, 7F386TSFRW, H53TSRFWQ4, HRMX4R3C1B]
sources:
  - url: https://en.wikipedia.org/wiki/Entanglement_distillation
---

## Definition

Let $\rho$ be a [[density matrix|V1JTB52E8C]] on $H_A \otimes H_B$, where $H_A$ and $H_B$ are finite-dimensional complex Hilbert spaces.
Let $\Phi^+$ be the projection onto the [[Bell state|CA57HMCRQQ]] $(|00\rangle + |11\rangle)/\sqrt{2}$ of two qubits.
A real number $R \ge 0$ is an *achievable distillation rate* for $\rho$ if there are integers $m_n \ge 0$ and [[LOCC|F5EB23T03M]] channels $\Lambda_n$ such that:

1. $\Lambda_n$ maps states on $(H_A \otimes H_B)^{\otimes n}$ to states on $(\C^2 \otimes \C^2)^{\otimes m_n}$, with $A$ parts to the first party and $B$ parts to the second.
2. $m_n / n \to R$ as $n \to \infty$.
3. The [[trace distance|2Q85WTJ07A]] between $\Lambda_n(\rho^{\otimes n})$ and $(\Phi^+)^{\otimes m_n}$ tends to $0$ as $n \to \infty$.

*Entanglement distillation* is the task of producing such channels.
The *distillable entanglement* $E_D(\rho)$ is the supremum of the achievable rates, and $\rho$ is *distillable* if $E_D(\rho) > 0$.

## Remarks

Example: for a pure state $\psi$ with reduced state $\rho_A$, the distillable entanglement is the [[von Neumann entropy|H53TSRFWQ4]] $S(\rho_A)$.
For a Bell state itself, $\rho_A = \tfrac12 I$, so $E_D = 1$: the channels $\Lambda_n = \id$ with $m_n = n$ achieve rate $1$.

Non-example: a [[separable state|7F386TSFRW]] $\sigma$ has $E_D(\sigma) = 0$.
LOCC maps separable states to separable states.
A separable state has overlap at most $2^{-m}$ with $(\Phi^+)^{\otimes m}$, so for $m \ge 1$ its trace distance to $(\Phi^+)^{\otimes m}$ is at least $\tfrac12$.
So clause 3 fails for every $R > 0$.

LOCC channels map states whose partial transpose is positive semidefinite, as in the [[Peres–Horodecki criterion|HRMX4R3C1B]], to states with the same property.
The same overlap bound holds for such states, so states with positive semidefinite partial transpose are never distillable.
When such a state is entangled, its entanglement is called bound entanglement.
