---
tag: BA3H1Y16TC
kind: statement
role: theorem
name: Ehrenfest theorem
msc: ["81Q05", "81S05"]
uses: [VXDEQB46GV, 7XAKGQQWTP, 5WG6YTAA6J, JNK7GJ3AKE, EPZR6H2WJN, CG9JEATW3Q, HKP9E7N7AB]
about: [JNK7GJ3AKE, VXDEQB46GV]
sources:
  - url: https://en.wikipedia.org/wiki/Ehrenfest_theorem
same_as:
  wikidata: Q908669
  wikipedia: Ehrenfest theorem
---

## Statement

Let $n \ge 1$, $\hbar > 0$ and $m > 0$.
Let $V \colon \R^n \to \R$ be a smooth function such that $V$ and each of its partial derivatives are bounded by a polynomial.
Let $t \mapsto \psi(\cdot, t)$ be a continuously differentiable map from an interval $J \subseteq \R$ into the [[Schwartz space|CG9JEATW3Q]] $\mathcal{S}(\R^n)$ that solves the [[Schrödinger equation|EPZR6H2WJN]]
$$i\hbar\, \partial_t \psi = -\frac{\hbar^2}{2m}\Delta\psi + V\psi,$$
with $\int \abs{\psi(x, t)}^2 \, dx = 1$.
For $j = 1, \dots, n$, let
$$\langle X_j \rangle(t) = \int x_j \abs{\psi}^2 \, dx, \quad \langle P_j \rangle(t) = \int \overline{\psi}\, (-i\hbar\, \partial_j \psi)\, dx, \quad \langle \partial_j V \rangle(t) = \int \partial_j V\, \abs{\psi}^2 \, dx.$$
Then for all $t \in J$,
$$\frac{d}{dt}\langle X_j \rangle = \frac{1}{m}\langle P_j \rangle, \qquad \frac{d}{dt}\langle P_j \rangle = -\langle \partial_j V \rangle.$$

## Remarks

The numbers $\langle X_j \rangle$ and $\langle P_j \rangle$ are the [[expectation values|JNK7GJ3AKE]] of the [[position|7XAKGQQWTP]] and [[momentum|5WG6YTAA6J]] operators, and $H = \frac{1}{2m}\sum_k P_k^2 + V(X)$ is the [[Hamiltonian|VXDEQB46GV]].
For an operator $A$ that maps $\mathcal{S}(\R^n)$ into itself and is symmetric there, differentiating under the integral and using $\partial_t\psi = -\frac{i}{\hbar}H\psi$ gives $\frac{d}{dt}\ip{\psi}{A\psi} = \frac{i}{\hbar}\ip{\psi}{[H, A]\psi}$.
The [[canonical commutation relation|HKP9E7N7AB]] gives $[H, X_j] = -\frac{i\hbar}{m} P_j$ and $[H, P_j] = i\hbar\, \partial_j V$ on $\mathcal{S}(\R^n)$, and the two formulas follow.

Example: for the harmonic potential $V(x) = \frac12 m\omega^2 x^2$ on $\R$, $\partial V = m\omega^2 x$, so $\frac{d^2}{dt^2}\langle X \rangle = -\omega^2 \langle X \rangle$.
The mean position oscillates exactly like a classical oscillator.

In general $\langle \partial_j V \rangle \ne \partial_j V(\langle X \rangle)$, so the mean position does not follow a classical path exactly.
It does so when $V$ is a polynomial of degree at most $2$, or approximately when the wave packet is narrow compared with the scale on which $\partial_j V$ changes.

## Explanations

### L1 human

The averages of position and momentum of a quantum particle move almost like a classical particle.
The rate of change of the average position is the average momentum divided by the mass, and the rate of change of the average momentum is the average force.
This is how Newton's laws reappear, on average, inside quantum mechanics.

### L2 human

The theorem is a special case of the formula $\frac{d}{dt}\langle A \rangle = \frac{i}{\hbar}\langle [H, A] \rangle$, the expectation of the Heisenberg equation of motion.
The commutators with $H$ play the role of the Poisson brackets with the classical Hamiltonian in Hamilton's equations.
The average force is $-\langle \partial_j V \rangle$, not the force at the average position, and the difference measures how far the quantum motion is from classical motion.
The hypotheses here make every step an honest computation with Schwartz functions; for rough potentials or general states one needs a careful choice of domains.
