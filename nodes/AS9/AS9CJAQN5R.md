---
tag: AS9CJAQN5R
kind: definition
name: Quantum mutual information
msc: [81P17, 94A17, 81P40]
defines: G11KFW51F6
uses: [V1JTB52E8C, SQ3J7AVMKM, H53TSRFWQ4, EY0X2NKA3S, CA57HMCRQQ, 4V9R81KPF7]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_mutual_information
---

## Definition

Let $H_A$ and $H_B$ be finite-dimensional complex Hilbert spaces.
Let $\rho_{AB}$ be a [[density operator|V1JTB52E8C]] on the [[tensor product|EY0X2NKA3S]] $H_A \otimes H_B$.
Let $\rho_A = \tr_B \rho_{AB}$ and $\rho_B = \tr_A \rho_{AB}$ be its [[partial traces|SQ3J7AVMKM]].
The *quantum mutual information* of $\rho_{AB}$ is
$$I(A:B)_\rho = S(\rho_A) + S(\rho_B) - S(\rho_{AB}),$$
where $S(\sigma) = -\tr(\sigma \log \sigma)$ is the [[von Neumann entropy|H53TSRFWQ4]].

## Remarks

Example: let $\rho_{AB} = \lvert \Phi \rangle\langle \Phi \rvert$ with $\lvert \Phi \rangle = (\lvert 00 \rangle + \lvert 11 \rangle)/\sqrt{2}$, a [[Bell state|CA57HMCRQQ]].
The state is pure, so $S(\rho_{AB}) = 0$.
Each marginal is $I/2$, so $S(\rho_A) = S(\rho_B) = \log 2$.
Hence $I(A:B) = 2 \log 2$.

Non-example of correlation: for a product state $\rho_{AB} = \rho_A \otimes \rho_B$, the entropy is additive, $S(\rho_A \otimes \rho_B) = S(\rho_A) + S(\rho_B)$, so $I(A:B) = 0$.

An equivalent form uses the [[quantum relative entropy|4V9R81KPF7]]: $I(A:B)_\rho = D(\rho_{AB} \,\|\, \rho_A \otimes \rho_B)$.
By Klein's inequality this gives $I(A:B)_\rho \ge 0$, with equality exactly for product states.
It also satisfies $I(A:B)_\rho \le 2 \min(\log d_A, \log d_B)$, where $d_A$ and $d_B$ are the dimensions.
With $\log$ to base $2$, the unit is the bit.
