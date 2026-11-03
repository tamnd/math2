---
tag: 9YACB2RQ80
kind: statement
role: theorem
name: Onsager reciprocal relations
msc: [82C35, 82B35, 80A17]
uses: [STR73R5MX4, J027RJ924H, SPY89W0RJ7, 0VR671PHE5]
about: [WC6CK8PXPX, STR73R5MX4]
sources:
  - url: https://en.wikipedia.org/wiki/Onsager_reciprocal_relations
same_as:
  wikidata: Q901483
  wikipedia: Onsager reciprocal relations
---

## Statement

Let a macroscopic system near equilibrium be described by variables $\alpha_1, \dots, \alpha_n$ that measure deviations from equilibrium and are even under time reversal.
Let $S(\alpha)$ be its [[entropy|SPY89W0RJ7]], let $X_i = \partial S / \partial \alpha_i$ be the thermodynamic forces and $J_i = d\alpha_i / dt$ the fluxes.
Assume the linear laws
$$J_i = \sum_{k=1}^{n} L_{ik} X_k \qquad (i = 1, \dots, n),$$
with constant coefficients $L_{ik}$.
Assume the microscopic dynamics is invariant under time reversal, and that the mean regression of spontaneous fluctuations of the $\alpha_i$ obeys the same linear laws.
Then the matrix of coefficients is [[symmetric|0VR671PHE5]]:
$$L_{ik} = L_{ki} \quad \text{for all } i, k.$$
If the system is in an external magnetic field $B$, which is odd under time reversal, the relations become $L_{ik}(B) = L_{ki}(-B)$.

## Remarks

The proof uses microscopic reversibility: the equilibrium correlation $\langle \alpha_i(0)\,\alpha_k(\tau) \rangle$ equals $\langle \alpha_k(0)\,\alpha_i(\tau) \rangle$.
Differentiating in $\tau$ and inserting the linear regression law, together with the equilibrium identity $\langle \alpha_i X_k \rangle = -k_B \delta_{ik}$, gives $L_{ki} = L_{ik}$.
Example: in an anisotropic crystal the heat flux is $J_q = -K \nabla T$ for a conductivity tensor $K$, and the relations give $K_{ij} = K_{ji}$, which was confirmed by experiment.
The relations also link the Seebeck and Peltier effects and the Soret and Dufour effects.
For variables that are odd under time reversal, such as momenta, some relations change sign: $L_{ik} = -L_{ki}$ when exactly one of $\alpha_i, \alpha_k$ is odd.

## Explanations

### L1 human

Near equilibrium, each kind of flow is driven by a mix of forces: heat flow mostly by a temperature difference, but also a little by a voltage.
The coefficient that tells how much a voltage drives heat equals the coefficient that tells how much a temperature difference drives electric current.
This symmetry comes from the fact that the laws of motion of molecules look the same when time runs backwards.

### L2 human

The relations reduce the number of independent transport coefficients from $n^2$ to $n(n+1)/2$.
Together with the [[entropy production|STR73R5MX4]] $\sigma = \sum_{i,k} L_{ik} X_i X_k \ge 0$, they make $L$ a symmetric positive semidefinite matrix.
They are the main structural result of linear irreversible thermodynamics, and they underlie the Kelvin relations of thermoelectricity and Prigogine's minimum entropy production principle.
They hold only in the linear regime near equilibrium.
