---
tag: EQ6DCTV902
kind: example
name: Werner state
msc: [81P42, 81P40]
illustrates: [7F386TSFRW, CHNXT8CCK7]
uses: [EY0X2NKA3S, V1JTB52E8C, 7F386TSFRW, CHNXT8CCK7, CA57HMCRQQ]
sources:
  - url: https://en.wikipedia.org/wiki/Werner_state
same_as:
  wikidata: Q7983528
  wikipedia: Werner state
---

## Example

Let $d \ge 2$ and let $F$ be the swap operator on $\C^d \otimes \C^d$, defined by $F(u \otimes v) = v \otimes u$.
Let $P_{s} = \tfrac12(I + F)$ and $P_{a} = \tfrac12(I - F)$ be the projections onto the symmetric and antisymmetric subspaces.
Their ranks are $d(d+1)/2$ and $d(d-1)/2$.
For $0 \le p \le 1$, the *Werner state* with parameter $p$ is the [[density matrix|V1JTB52E8C]]
$$\rho_p = p \, \frac{2 P_a}{d(d-1)} + (1 - p) \, \frac{2 P_s}{d(d+1)}.$$
It commutes with $U \otimes U$ for every unitary $U$ on $\C^d$, and every state with this symmetry is of this form.

Werner states are [[separable|7F386TSFRW]] exactly when $p \le \tfrac12$, and [[entangled|CHNXT8CCK7]] when $p > \tfrac12$.
A quick check of the trace of $F \rho_p$: $\tr(F P_a) = -\tr P_a$ and $\tr(F P_s) = \tr P_s$, so $\tr(F \rho_p) = 1 - 2p$.
For a product state, $\tr(F \, \sigma \otimes \tau) = \tr(\sigma \tau) \ge 0$, so every separable state $\rho$ has $\tr(F\rho) \ge 0$.
Hence $\rho_p$ is entangled for $p > \tfrac12$.
For $p \le \tfrac12$ one shows separability by averaging a suitable product state over the group of all $U \otimes U$.

## Remarks

For $d = 2$, the antisymmetric subspace is spanned by the [[Bell state|CA57HMCRQQ]] $|\Psi^-\rangle$.
Then $\rho_p = q \, |\Psi^-\rangle\langle\Psi^-| + (1 - q) \tfrac14 I$ with $p = (1 + 3q)/4$.
In this form the state is entangled exactly when $q > \tfrac13$.
Werner introduced these states in 1989.
He showed that some of the entangled ones admit a local hidden-variable model for all projective measurements.

## Explanations

### L1 human

A Werner state mixes the antisymmetric states with symmetric noise; for two qubits, the antisymmetric part is the singlet.
The mixture looks the same in every common basis of the two parties.
One number $p$ controls the mixture.
When the antisymmetric part is large enough, the state is entangled; below a sharp threshold, the noise destroys the entanglement.
This makes Werner states the standard test case for separability criteria.
