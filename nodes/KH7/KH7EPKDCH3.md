---
tag: KH7EPKDCH3
kind: statement
role: theorem
name: Lie–Trotter product formula
msc: [47D03, 47B25, 81Q10]
uses: [HM2HHE3J51, 0NEGN5CRSC, DT49GKR9AS, DVGQB92HPJ]
about: [0NEGN5CRSC]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_product_formula
---

## Statement

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]].
Let $A$ and $B$ be [[self-adjoint operators|0NEGN5CRSC]] on $H$, with domains $D(A)$ and $D(B)$.
Assume that $A + B$ is [[essentially self-adjoint|DT49GKR9AS]] on $D(A) \cap D(B)$, and let $C$ be its closure.
Then for every $t \in \R$ and every $x \in H$,
$$e^{itC}x = \lim_{n \to \infty} \left( e^{itA/n} e^{itB/n} \right)^n x,$$
where the unitary groups $e^{itA}$, $e^{itB}$ and $e^{itC}$ are those of [[Stone's theorem|DVGQB92HPJ]].

## Remarks

For $n \times n$ matrices this is the [[Lie product formula|HK3BRMK912]], and the proof idea is the same.
The difference $e^{isA}e^{isB} - e^{isC}$ is $o(s)$ as $s \to 0$ when applied to a vector of $D(A) \cap D(B)$.
A telescoping sum turns $n$ such errors of size $o(1/n)$ into a total error that tends to $0$.
In infinite dimensions, the convergence is in the strong sense, vector by vector, and the essential self-adjointness of $A + B$ is used to pass from $D(A) \cap D(B)$ to general $x$.
A similar formula holds for the semigroups $e^{-tA}$ and $e^{-tB}$ with $t \ge 0$, when $A$ and $B$ are bounded below and $A + B$ is essentially self-adjoint on $D(A) \cap D(B)$.

Example: in quantum mechanics with $A = -\Delta$ and $B = V$ a suitable potential, $e^{-itA/n}$ acts by a Fourier multiplier and $e^{-itV/n}$ by multiplication.
The formula approximates the Schrödinger evolution by alternating free motion and potential kicks; this is the basis of split-step methods.

## Explanations

### L1 human

For numbers, $e^{a + b} = e^{a}e^{b}$, but for operators that do not commute this fails.
The product formula repairs this: alternating many small steps of $A$ and of $B$ gives the evolution of $A + B$ in the limit.
It is like crossing a field diagonally by many tiny steps east and north in turn.

### L2 human

The result is due to Trotter, who extended Lie's formula for matrices to unbounded operators.
It is used to build the Feynman–Kac formula: for $-\Delta + V$, the alternating products become integrals over paths of Brownian motion.
In numerical analysis it justifies operator splitting, where a hard evolution is approximated by easy ones.
The hypothesis that $A + B$ is essentially self-adjoint on $D(A) \cap D(B)$ ensures that the limit is the evolution of a well-defined Hamiltonian.
