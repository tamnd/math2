---
tag: EASHSMA5ZQ
kind: statement
role: theorem
name: Correspondence principle of viscoelasticity
msc: [74D05, 74G05]
uses: [GCX1B3DAJN, JSSYGY0V87, KJ6AAHKJ91, 6W00ZECYT0, 0V49JEZW06, PQ8Z5HS2JR]
about: [GCX1B3DAJN, 6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Viscoelasticity
---

## Statement

Let a body occupy a fixed region $\Omega$ and consist of a homogeneous, isotropic, linear [[viscoelastic|GCX1B3DAJN]] material.
Let its shear and bulk [[relaxation moduli|JSSYGY0V87]] be $G(t)$ and $K(t)$.
Assume that inertia is negligible (quasi-static loading) and that the body is at rest and unloaded for $t < 0$.
Assume that the parts of the boundary where displacements and where tractions are prescribed do not change with time.
Suppose the solution of the corresponding problem of [[linear elasticity|6W00ZECYT0]] is known for every shear modulus $\mu$ and bulk modulus $\kappa$ and for all data.
Then the [[Laplace transforms|0V49JEZW06]] in time of the viscoelastic displacement, strain and stress fields are given by the elastic solution in which:

1. $\mu$ is replaced by $s \hat G(s)$ and $\kappa$ by $s \hat K(s)$;
2. the body forces, prescribed tractions and prescribed displacements are replaced by their Laplace transforms.

The viscoelastic solution is then obtained by inverting the Laplace transform.

## Remarks

By the [[Boltzmann superposition principle|KJ6AAHKJ91]], each viscoelastic constitutive law is a convolution in time, and the Laplace transform turns it into an elastic law with moduli $s \hat G(s)$ and $s \hat K(s)$.
The equilibrium and strain–displacement equations contain no time derivatives in the quasi-static case, so they keep their form after the transform.
So do the boundary conditions when their type at each point is fixed in time.
Example: a bar of a [[Maxwell material|PQ8Z5HS2JR]] in tension, with Young's relaxation modulus $E e^{-t/\tau}$ and $\eta = E\tau$, has the elastic solution $\varepsilon = \sigma_0 / E$.
Replacing $\sigma_0$ by $\sigma_0 / s$ and $E$ by $E s / (s + 1/\tau)$ gives $\hat\varepsilon(s) = \sigma_0 / (E s) + \sigma_0 / (\eta s^2)$, hence the creep law $\varepsilon(t) = \sigma_0/E + \sigma_0 t / \eta$.
The hypothesis on the boundary is necessary.
In indentation by a sphere the contact area changes with time, the type of boundary condition at a point changes, and the simple substitution gives wrong results.
Without negligible inertia the transformed problem is a dynamic one with an extra term $\rho s^2 \hat u$, and the principle needs to be modified accordingly.

## Explanations

### L1 human

Many problems for elastic bodies already have known solutions in handbooks.
The correspondence principle says that you can reuse them for viscoelastic bodies, such as plastics, by a change of variables.
Replace each elastic constant by a certain function of a new variable $s$, and then translate back from $s$ to time.

### L2 human

The principle reduces quasi-static linear viscoelastic boundary value problems to elastic ones, solved once with symbolic moduli.
It explains why the elastic formulas for beams, plates and pressurized cylinders all have viscoelastic counterparts with creeping deflections.
In the frequency domain the same idea replaces the moduli by the complex moduli $G^*(\omega) = i\omega \hat G(i\omega)$, which is how dynamic tests of polymers are analysed.
Its limits, moving boundaries and aging materials, are where genuinely new viscoelastic methods are needed.
