---
tag: QHXWETTMVK
kind: definition
name: Magnetotellurics
msc: [86A25, 86A22, 35Q61]
defines: 1XT0CC79ZJ
uses: [C54MFNX576, 9BWWD4QK8Y, Y8Q6C2W8J6, CH34Y1DWT4]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetotellurics
---

## Definition

Let $\sigma(x) > 0$ be the electrical conductivity of the Earth, and let $\mu_0$ be the magnetic permeability of free space.
Natural electromagnetic fields at angular frequency $\omega > 0$ are recorded at a surface station, giving the horizontal electric field $E_h = (E_x, E_y)$ and the horizontal magnetic field $H_h = (H_x, H_y)$.
Assume that the source fields are uniform horizontal plane waves.
The *impedance tensor* is the $2 \times 2$ complex matrix $Z(\omega)$ with $E_h = Z(\omega)\, H_h$ for all source fields.
The *apparent resistivity* and *phase* of a component $Z_{ij}$ are
$$\rho_{a,ij}(\omega) = \frac{\abs{Z_{ij}(\omega)}^2}{\omega \mu_0}, \qquad \phi_{ij}(\omega) = \arg Z_{ij}(\omega).$$
*Magnetotellurics* is the [[geophysical inversion|C54MFNX576]] that recovers $\sigma$ from $Z(\omega)$ over a range of frequencies and stations.
Its forward map is given by the quasi-static [[Maxwell's equations|9BWWD4QK8Y]].

## Remarks

Example: a homogeneous half-space of resistivity $\rho = 1/\sigma$.
With time dependence $e^{i \omega t}$, the field $E_x = E_0 e^{-kz}$ with $k = \sqrt{i \omega \mu_0 \sigma}$ solves the diffusion equation $\partial_z^2 E_x = i \omega \mu_0 \sigma E_x$, and [[Faraday's law|Y8Q6C2W8J6]] gives $\partial_z E_x = -i \omega \mu_0 H_y$.
So $Z_{xy} = E_x / H_y = \sqrt{i \omega \mu_0 \rho}$, hence $\rho_a = \rho$ at every frequency and the phase is $45^\circ$.
The field decays by $1/e$ over the [[skin depth|CH34Y1DWT4]] $\delta = \sqrt{2\rho/(\omega \mu_0)} \approx 503 \sqrt{\rho T}$ metres, with $T = 2\pi/\omega$ in seconds and $\rho$ in ohm metres.
Non-example: controlled-source electromagnetic methods use a man-made transmitter near the receivers, so the plane-wave assumption fails and the impedance is not the magnetotelluric one.
For a layered Earth $Z$ has the form $\begin{pmatrix} 0 & Z_{xy} \\ -Z_{xy} & 0 \end{pmatrix}$; in two- and three-dimensional structures all four entries carry information.

## Explanations

### L1 human

The station measures how strong the electric field is for a given magnetic field, at many frequencies.
This ratio tells how conductive the ground is down to a depth that grows with the period.
