---
tag: 9J1EEAYTXM
kind: statement
role: theorem
name: Uhlmann's theorem
msc: [81P47, 81P40]
uses: [A8D05RKX8M, CDXS11AEW9, V1JTB52E8C, EY0X2NKA3S]
about: [A8D05RKX8M, CDXS11AEW9]
sources:
  - url: https://en.wikipedia.org/wiki/Fidelity_of_quantum_states
---

## Statement

Let $H$ and $K$ be finite-dimensional complex Hilbert spaces with $\dim K \ge \dim H$.
Let $\rho$ and $\sigma$ be [[density operators|V1JTB52E8C]] on $H$.
A purification of $\rho$ on $H \otimes K$ is a unit vector $\psi \in H \otimes K$ with $\tr_K \lvert \psi \rangle \langle \psi \rvert = \rho$.
Then
$$F(\rho, \sigma) = \max \abs{\ip{\psi}{\phi}}^2,$$
where $F$ is the [[fidelity|A8D05RKX8M]] and the maximum runs over all [[purifications|CDXS11AEW9]] $\psi$ of $\rho$ and $\phi$ of $\sigma$ on $H \otimes K$.
Moreover, for any fixed purification $\psi$ of $\rho$, the maximum over the purifications $\phi$ of $\sigma$ alone is already $F(\rho, \sigma)$.

## Remarks

Proof idea: fix an orthonormal basis $(e_i)$ of $H$ and an isometric copy of it in $K$, and let $\Omega = \sum_i e_i \otimes e_i$.
Every purification of $\rho$ has the form $(\sqrt\rho\, U \otimes I)\Omega$ for some unitary $U$, up to an isometry on $K$, and similarly for $\sigma$.
Then $\ip{\psi}{\phi}$ becomes $\tr(\sqrt\rho \sqrt\sigma\, W)$ for a unitary $W$.
The largest modulus of such a trace is the trace norm $\norm{\sqrt\rho\sqrt\sigma}_1$, reached through the polar decomposition, and its square is $F(\rho, \sigma)$.

Example: if $\rho = \lvert a \rangle\langle a \rvert$ and $\sigma = \lvert b \rangle\langle b \rvert$ are pure, every purification is $a \otimes k$ or $b \otimes k'$ with unit vectors $k, k'$, and the maximum of $\abs{\ip{a}{b}}^2 \abs{\ip{k}{k'}}^2$ is $\abs{\ip{a}{b}}^2 = F(\rho, \sigma)$.

## Explanations

### L1 human

Every mixed state can be seen as one part of a larger pure state, called a purification.
Uhlmann's theorem says that the fidelity of two mixed states is the best overlap one can reach between their purifications.
So the fidelity of mixed states reduces to the simple overlap formula for pure states.

### L2 human

Many properties of fidelity follow at once from the theorem.
Symmetry $F(\rho, \sigma) = F(\sigma, \rho)$ and $F \le 1$ are immediate.
Monotonicity under quantum channels follows because a channel has a Stinespring dilation, which maps purifications to purifications.
Joint concavity of $\sqrt F$ also follows.
In quantum cryptography and in the theory of decoupling, the theorem is used to build a purification of a nearby state close to a given one.
