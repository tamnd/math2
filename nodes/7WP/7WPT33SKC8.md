---
tag: 7WPT33SKC8
kind: definition
name: Hartree–Fock method
msc: [81V70, 81Q05, 81V55]
defines: 8Q0QS66M7V
uses: [VXDEQB46GV, Y64G7W4BEC, 0MDMZ965VE, EYARCVGB0V]
sources:
  - url: https://en.wikipedia.org/wiki/Hartree%E2%80%93Fock_method
---

## Definition

Let $X = \R^3 \times \set{\uparrow, \downarrow}$ be the one-electron configuration space, with $\int_X f = \sum_{\sigma} \int_{\R^3} f(x, \sigma)\, dx$.
For $N$ electrons in an external potential $v$, let
$$H_N = \sum_{i=1}^{N} \left( -\frac12 \Delta_i + v(x_i) \right) + \sum_{1 \le i < j \le N} \frac{1}{\abs{x_i - x_j}}$$
in atomic units, acting on the antisymmetric functions in $L^2(X^N)$ ([[identical particles|Y64G7W4BEC]] that are fermions).
A *Slater determinant* is a function
$$\Psi(z_1, \ldots, z_N) = \frac{1}{\sqrt{N!}} \det\big( \varphi_i(z_j) \big)_{i,j=1}^{N},$$
where $\varphi_1, \ldots, \varphi_N \in L^2(X)$ are orthonormal orbitals with finite kinetic energy.
The *Hartree–Fock method* approximates the ground state energy of $H_N$ by
$$E^{\mathrm{HF}} = \inf \set{ \ip{\Psi}{H_N \Psi} : \Psi \text{ a Slater determinant} },$$
and the ground state by a minimising Slater determinant, when one exists.

## Remarks

Let $\gamma(z, z') = \sum_i \varphi_i(z)\overline{\varphi_i(z')}$ and $\rho(x) = \sum_\sigma \gamma((x, \sigma), (x, \sigma))$.
A minimiser satisfies, after a unitary change of the orbitals, the *Hartree–Fock equations* $F\varphi_i = \varepsilon_i \varphi_i$, with the Fock operator
$$F\varphi(z) = -\frac12 \Delta\varphi(z) + v(x)\varphi(z) + \left( \int_{\R^3} \frac{\rho(y)}{\abs{x - y}}\, dy \right) \varphi(z) - \int_X \frac{\gamma(z, z')}{\abs{x - y}} \varphi(z')\, dz',$$
where $z = (x, \sigma)$ and $z' = (y, \tau)$.
The third term is the direct (Hartree) term, and the last is the exchange term.
By the [[variational method|EYARCVGB0V]], $E^{\mathrm{HF}}$ is at least the true ground state energy.
For atoms and positive ions, with $v(x) = -Z/\abs{x}$ and $N < Z + 1$, Lieb and Simon proved in 1977 that a minimiser exists.

Example: for helium ($Z = N = 2$) one may take $\varphi_1 = \phi \otimes \uparrow$ and $\varphi_2 = \phi \otimes \downarrow$ with one real spatial orbital $\phi$; then $\Psi = \phi(x_1)\phi(x_2) \cdot \frac{1}{\sqrt2}(\uparrow\downarrow - \downarrow\uparrow)$ is a Slater determinant.

Non-example: in the language of the [[exterior algebra|0MDMZ965VE]], Slater determinants are the decomposable vectors $\varphi_1 \wedge \cdots \wedge \varphi_N$.
For four orthonormal orbitals, $\frac{1}{\sqrt2}(\varphi_1 \wedge \varphi_2 + \varphi_3 \wedge \varphi_4)$ is antisymmetric and normalised but is not a Slater determinant, since its wedge with itself is nonzero.
