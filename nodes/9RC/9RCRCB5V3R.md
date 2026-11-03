---
tag: 9RCRCB5V3R
kind: definition
name: Weak gravitational lensing
msc: [85A04, 85A40, 83C99]
defines: ZT312D651W
uses: [C02XZJBFSY, 20XXW00SHF]
sources:
  - url: https://en.wikipedia.org/wiki/Weak_gravitational_lensing
---

## Definition

Consider a thin gravitational lens with [[lens equation|C02XZJBFSY]] $\beta = \theta - \alpha(\theta)$ for $\theta, \beta \in \R^2$, and suppose $\alpha = \nabla \psi$ for a lensing potential $\psi$.
The Jacobian matrix of the lens map is written
$$A(\theta) = \frac{\partial \beta}{\partial \theta} = \begin{pmatrix} 1 - \kappa - \gamma_1 & -\gamma_2 \\ -\gamma_2 & 1 - \kappa + \gamma_1 \end{pmatrix},$$
which defines the *convergence* $\kappa = \tfrac{1}{2} \nabla^2 \psi$ and the *shear* $\gamma = (\gamma_1, \gamma_2)$, with $\gamma_1 = \tfrac{1}{2}(\psi_{11} - \psi_{22})$ and $\gamma_2 = \psi_{12}$.
*Weak gravitational lensing* is the regime $\abs{\kappa} \ll 1$ and $\abs{\gamma} \ll 1$.
There the lens map is one-to-one near $\theta$, and each image is a slightly magnified and sheared copy of its source.

## Remarks

In this regime a small circular source of radius $r$ is imaged, to first order, as an ellipse with semi-axes $r / (1 - \kappa \mp \abs{\gamma})$.
So the ellipticity of the image is close to the reduced shear $g = \gamma / (1 - \kappa)$, and averaging the shapes of many galaxies, whose intrinsic orientations are random, estimates $g$.
The convergence equals $\Sigma / \Sigma_{cr}$, the surface mass density in units of the critical density.

Example: an isothermal sphere lens with Einstein radius $\theta_E$ has $\kappa = \abs{\gamma} = \theta_E / (2 \abs{\theta})$; at $\abs{\theta} = 50 \, \theta_E$ both equal $0.01$, which is weak lensing.

Non-example: images near the Einstein radius of the same lens have $\kappa = \abs{\gamma} = 1/2$, which is not small; this is [[strong lensing|20XXW00SHF]], with large distortions and multiple images.
