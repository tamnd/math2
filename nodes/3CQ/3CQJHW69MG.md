---
tag: 3CQJHW69MG
kind: statement
role: proposition
name: Quantum Zeno effect
msc: [81P15, 81Q10]
uses: [HM2HHE3J51, 0NEGN5CRSC, VXDEQB46GV, RMEE72SQME, MF4DYZ4YAX]
about: [RMEE72SQME]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_Zeno_effect
same_as:
  wikidata: Q1897309
  wikipedia: Quantum Zeno effect
---

## Statement

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]] and let $H$ be a [[self-adjoint operator|0NEGN5CRSC]] on $\mathcal{H}$, the [[Hamiltonian|VXDEQB46GV]], in units with $\hbar = 1$.
Let $\psi$ be a unit vector in the domain of $H$, and let $(\Delta H)^2 = \norm{H\psi}^2 - \langle \psi, H\psi \rangle^2$ be the energy variance of $\psi$.
Fix a time $t > 0$ and an integer $N \ge 1$.
Measure the projection onto $\psi$ at the times $t/N, 2t/N, \dots, t$, with the evolution $e^{-isH}$ in between.
The probability $p_N(t)$ that all $N$ measurements give the answer "yes" is
$$p_N(t) = \abs{\langle \psi, e^{-itH/N}\psi \rangle}^{2N}.$$
Then
$$p_N(t) \ge \left(1 - \frac{t^2 (\Delta H)^2}{N^2}\right)^N \text{ when } N > t\,\Delta H, \qquad \text{so} \qquad \lim_{N \to \infty} p_N(t) = 1.$$

## Remarks

The formula for $p_N(t)$ comes from the [[Born rule|MF4DYZ4YAX]] and the [[collapse|RMEE72SQME]] rule: after each "yes" the state is $\psi$ again, and the $N$ factors are independent.
For the bound, let $\mu$ be the spectral measure of $H$ in the state $\psi$, so that $\langle \psi, e^{-i\tau H}\psi \rangle = \int e^{-i\tau\lambda}\, d\mu(\lambda)$.
Then $1 - \abs{\langle \psi, e^{-i\tau H}\psi \rangle}^2 = \iint \big(1 - \cos(\tau(\lambda - \lambda'))\big)\, d\mu(\lambda)\, d\mu(\lambda')$, and $1 - \cos x \le x^2/2$ bounds this by $\tau^2 (\Delta H)^2$.
Taking $\tau = t/N$ and the $N$-th power gives the bound, and the right side tends to $1$.
Example: on $\C^2$ let $H = \omega X$, where $X$ is the Pauli matrix that swaps the two basis vectors, and let $\psi = (1, 0)$.
The survival amplitude is $\cos(\omega t/N)$, so $p_N(t) = \cos^{2N}(\omega t/N) \to 1$.
Without measurements, the state is fully flipped at $t = \pi/(2\omega)$.
The hypothesis that $\psi$ lies in the domain of $H$ matters.
Without a finite energy variance, the short-time decay need not be quadratic, and the limit can fail to be $1$.

## Explanations

### L1 human

A watched quantum system does not change.
If one checks very often whether a system is still in its initial state, the checks keep resetting it, and it stays there.
The reason is that, for short times, the chance of having left the initial state grows like the square of the time, not linearly.
Many short intervals then add up to a total chance of leaving that tends to zero.

### L2 human

The effect combines unitary evolution with the projection postulate, and it shows that frequent measurement is itself a strong dynamical influence.
The key estimate is the quadratic short-time behaviour $1 - \abs{\langle \psi, e^{-i\tau H}\psi \rangle}^2 \le \tau^2 (\Delta H)^2$, which is a form of the energy-time uncertainty relation.
For a subspace instead of a single vector, Misra and Sudarshan studied the limit of the evolution under frequent projections, which leads to a dynamics confined to that subspace.
Exponential decay laws, as for an unstable particle, hold only at intermediate times, which is why the effect does not contradict them.
