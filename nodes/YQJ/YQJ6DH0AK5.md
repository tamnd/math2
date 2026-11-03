---
tag: YQJ6DH0AK5
kind: definition
name: Rigorous coupled-wave analysis
msc: [78A45, 78M22]
defines: 9ZZPJ2R0D8
uses: [9BWWD4QK8Y, G12KXDHPPS, G5Q62JS3JM, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Rigorous_coupled-wave_analysis
---

## Definition

Consider a structure that is periodic in $x$ with period $\Lambda$, invariant in $y$, and made of layers $z_{l-1} < z < z_l$.
In each layer the relative permittivity $\varepsilon(x)$ does not depend on $z$.
Let a $y$-polarized (TE) plane wave of vacuum wave number $k_0$ arrive from above with in-plane wave number $\kappa_0$, and let $\kappa_m = \kappa_0 + 2\pi m / \Lambda$.
Fix a truncation order $M$.
*Rigorous coupled-wave analysis* of order $M$ computes the diffracted field as follows.

1. In each layer, write $E_y = \sum_{\abs{m} \le M} S_m(z) e^{i \kappa_m x}$, and expand $\varepsilon(x) = \sum_p \varepsilon_p e^{2\pi i p x / \Lambda}$ in a [[Fourier series|G12KXDHPPS]].
2. Substitute into $\partial_x^2 E_y + \partial_z^2 E_y + k_0^2 \varepsilon E_y = 0$, which follows from the [[Maxwell equations|9BWWD4QK8Y]], and keep the orders $\abs{m} \le M$; this gives $S'' = A S$ with the [[matrix|0VD9ZSWWJG]] $A = K^2 - k_0^2 E$.
3. Here $K$ is diagonal with entries $\kappa_m$, and $E$ is the Toeplitz matrix with entries $E_{mp} = \varepsilon_{m - p}$.
4. Solve each layer by the eigenvalues and eigenvectors of $A$. Match the tangential fields at the interfaces, and with the plane-wave orders above and below, as in the [[transfer-matrix method|G5Q62JS3JM]].

The output is the amplitude, hence the diffraction efficiency, of each order $m$.

## Remarks

Check for a homogeneous layer: if $\varepsilon$ is a constant $\varepsilon_0$, then $E = \varepsilon_0 I$ and $A$ is diagonal.
The orders decouple, and $S_m'' = (\kappa_m^2 - k_0^2 \varepsilon_0) S_m$, so each order is a plane wave with normal wave number $\sqrt{k_0^2 \varepsilon_0 - \kappa_m^2}$.
The orders that propagate are those with $\kappa_m^2 < k_0^2 \varepsilon_0$, as in the grating equation.

Non-example: a single isolated scatterer, or any structure that is not periodic, has no Fourier series in $x$ of this kind.
RCWA applies to it only after it is made artificially periodic, for example inside a supercell with absorbing layers.

For TM polarization, multiplying the truncated Fourier series of $\varepsilon$ and of the field converges slowly where $\varepsilon$ jumps.
Correct Fourier factorization rules, due to Lifeng Li, fix this by using the inverse of the Toeplitz matrix of $1/\varepsilon$ where the field is discontinuous.

## Explanations

### L1 human

The method treats a grating one layer at a time.
In each layer the field is a sum of a finite number of diffraction orders, and the grating couples them through a matrix.
Solving a matrix eigenvalue problem per layer and gluing the layers gives the power in each order.
