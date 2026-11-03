---
tag: G3SV8PCKHT
kind: statement
role: theorem
name: Monogamy of entanglement
msc: [81P40, 81P42]
uses: [EY0X2NKA3S, V1JTB52E8C, SQ3J7AVMKM, CHNXT8CCK7, XAQCW3D4QQ, A76VV68635]
about: [CHNXT8CCK7]
sources:
  - url: https://en.wikipedia.org/wiki/Monogamy_of_entanglement
same_as:
  wikidata: Q106808950
  wikipedia: Monogamy of entanglement
---

## Statement

Let $H_A$, $H_B$, $H_C$ be finite-dimensional complex Hilbert spaces, and let $\rho_{ABC}$ be a [[density matrix|V1JTB52E8C]] on $H_A \otimes H_B \otimes H_C$.
Write $\rho_{AB}$, $\rho_{AC}$, $\rho_A$ for its [[partial traces|SQ3J7AVMKM]].

1. If $\rho_{AB} = |\varphi\rangle\langle\varphi|$ is a pure state, then $\rho_{ABC} = |\varphi\rangle\langle\varphi| \otimes \rho_C$.
2. (Coffman–Kundu–Wootters inequality) If $H_A = H_B = H_C = \C^2$ and $\rho_{ABC}$ is pure, then
$$C(\rho_{AB})^2 + C(\rho_{AC})^2 \le 4 \det \rho_A.$$

Here $C$ is the concurrence of a two-qubit state $\sigma$: $C(\sigma) = \max(0, \mu_1 - \mu_2 - \mu_3 - \mu_4)$.
The numbers $\mu_1 \ge \mu_2 \ge \mu_3 \ge \mu_4$ are the square roots of the eigenvalues of $\sigma \tilde\sigma$, where $\tilde\sigma = (\sigma_y \otimes \sigma_y) \overline{\sigma} (\sigma_y \otimes \sigma_y)$.
The bar is complex conjugation in the standard basis, and $\sigma_y$ is a [[Pauli matrix|XAQCW3D4QQ]].

## Remarks

For part 1, write $\rho_{ABC} = \sum_k p_k |\psi_k\rangle\langle\psi_k|$ with $p_k > 0$.
The reduced states of the $\psi_k$ on $AB$ average to the pure state $|\varphi\rangle\langle\varphi|$, which is extreme, so each of them equals it.
So each $\psi_k$ has Schmidt rank $1$ across $AB$ versus $C$, that is, $\psi_k = \varphi \otimes \chi_k$.

For a pure three-qubit state, $4 \det \rho_A$ is the squared concurrence between $A$ and the pair $BC$.
The gap $\tau = 4\det\rho_A - C(\rho_{AB})^2 - C(\rho_{AC})^2$ is the three-tangle.
For the [[GHZ state|A76VV68635]], $\rho_A = \tfrac12 I$ and $\rho_{AB}$, $\rho_{AC}$ are separable, so $\tau = 1$.
For the W state $(|001\rangle + |010\rangle + |100\rangle)/\sqrt{3}$, one finds $4\det\rho_A = \tfrac89$ and $C(\rho_{AB})^2 = C(\rho_{AC})^2 = \tfrac49$, so $\tau = 0$.

Classical correlations are not monogamous: three bits that are always equal are perfectly correlated in every pair.

## Explanations

### L1 human

Entanglement cannot be freely shared.
If two qubits are maximally entangled with each other, neither of them can be entangled, or even correlated, with anything else.
More generally, the more $A$ is entangled with $B$, the less it can be entangled with $C$.
This is unlike ordinary correlations, which many parties can share at once.

### L2 human

Monogamy is the reason why entanglement-based quantum key distribution is secure: if Alice and Bob share a nearly maximally entangled state, an eavesdropper holds almost no correlation with it.
The Coffman–Kundu–Wootters inequality makes this quantitative for three qubits.
Osborne and Verstraete extended it to any number of qubits.
Not every entanglement measure is monogamous in this additive form, so the choice of measure matters.
