---
tag: ESN2Y09QGQ
kind: statement
role: theorem
name: No-communication theorem
msc: [81P45, 81P40]
uses: [EY0X2NKA3S, V1JTB52E8C, SQ3J7AVMKM, 10VZYJ4552, SFX7B478FE]
about: [SQ3J7AVMKM, 10VZYJ4552]
sources:
  - url: https://en.wikipedia.org/wiki/No-communication_theorem
same_as:
  wikidata: Q3984056
  wikipedia: No-communication theorem
---

## Statement

Let $H_A$ and $H_B$ be finite-dimensional complex Hilbert spaces, and let $\rho_{AB}$ be a [[density matrix|V1JTB52E8C]] on $H_A \otimes H_B$.
Let $\Phi$ be a [[quantum channel|10VZYJ4552]] on the operators on $H_A$.
Then
$$\tr_A \big( (\Phi \otimes \id)(\rho_{AB}) \big) = \tr_A (\rho_{AB}),$$
where $\tr_A$ is the [[partial trace|SQ3J7AVMKM]] over $H_A$.

## Remarks

By the [[Kraus representation|SFX7B478FE]], $\Phi(\tau) = \sum_k K_k \tau K_k^*$ with $\sum_k K_k^* K_k = I$.
The partial trace over $A$ is unchanged by moving $K_k^*$ from the right to the left inside it, since $K_k$ acts on $A$ only.
So the left side equals $\tr_A \big( (\sum_k K_k^* K_k \otimes I) \rho_{AB} \big) = \tr_A(\rho_{AB})$.

A measurement by Alice whose outcome Bob does not learn is such a channel, $\Phi(\tau) = \sum_j M_j \tau M_j^*$.
For example, if $\rho_{AB}$ is the Bell state $(|00\rangle + |11\rangle)/\sqrt2$, Bob's reduced state is $\tfrac12 I$ before and after any operation of Alice.

The theorem concerns the average state.
Conditioned on Alice's outcome $j$, Bob's state does change, but Bob can only use this after Alice tells him $j$ by a classical message.

## Explanations

### L1 human

Entangled particles show strong correlations, but they cannot be used to send messages.
Whatever Alice does to her particle, the statistics of every measurement Bob can make on his particle stay the same.
So Bob learns nothing about Alice's action until she contacts him by ordinary means.

### L2 human

The theorem shows that quantum theory, despite Bell nonlocality, does not allow signalling faster than light.
It is the reason why teleportation and superdense coding need a classical or quantum channel in addition to shared entanglement.
In the language of channels, it says that the partial trace over $A$ is invariant under every channel acting on $A$.
