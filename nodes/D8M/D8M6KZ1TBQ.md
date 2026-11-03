---
tag: D8M6KZ1TBQ
kind: example
name: Womersley flow
msc: [76Z05, 76D05, 92C35]
illustrates: [18KXZHVF4M]
uses: [18KXZHVF4M, P27AH8WRRC, CZCMRDWDYW, DF0M8YNQ3D]
sources:
  - url: https://en.wikipedia.org/wiki/Pulsatile_flow
---

## Example

Consider a Newtonian fluid of density $\rho$ and viscosity $\mu$ in a rigid straight pipe of circular cross-section with radius $R$, along the $z$-axis.
Drive it by an oscillating pressure gradient $-\partial p / \partial z = \operatorname{Re}(A e^{i \omega t})$ with amplitude $A$ and angular frequency $\omega > 0$.
Let $\alpha = R \sqrt{\omega \rho / \mu}$ be the Womersley number and $J_0$ the [[Bessel function of the first kind|CZCMRDWDYW]] of order $0$.
The *Womersley flow* is the axial velocity
$$u(r, t) = \operatorname{Re} \left\{ \frac{A}{i \omega \rho} \left[ 1 - \frac{J_0(i^{3/2} \alpha \, r / R)}{J_0(i^{3/2} \alpha)} \right] e^{i \omega t} \right\},$$
where $r$ is the distance to the axis and $i^{3/2} = e^{3\pi i/4}$.

Check: for a fully developed axial flow the [[Navier–Stokes equations|18KXZHVF4M]] reduce to $\rho \, \partial_t u = -\partial_z p + \mu (u_{rr} + u_r / r)$.
With $u = \operatorname{Re}(U(r) e^{i\omega t})$ this becomes $i \omega \rho U = A + \mu (U'' + U'/r)$.
The constant $A/(i\omega\rho)$ is a particular solution.
The function $U = J_0(\lambda r)$ satisfies $U'' + U'/r = -\lambda^2 U$, and the choice $\lambda = i^{3/2} \alpha / R$ gives $-\lambda^2 = i \alpha^2 / R^2 = i \omega \rho / \mu$, so it solves the homogeneous equation.
The coefficient is chosen so that $U(R) = 0$, which is the [[no-slip condition|DF0M8YNQ3D]].

## Remarks

For small $\alpha$, the flow at each instant is close to the [[Poiseuille flow|P27AH8WRRC]] for the current pressure gradient.
Viscosity then has time to set up the parabolic profile.
For large $\alpha$, the core moves as a plug that lags the pressure gradient by nearly a quarter period.
Viscous effects are then confined to a wall layer of thickness about $R/\alpha$.
John R. Womersley used this solution to model blood flow in arteries.
There $\alpha$ ranges from small values in small vessels to values above $10$ in the aorta of large mammals.

## Explanations

### L1 human

The heart pushes blood in pulses, not steadily.
In a narrow vessel the blood still flows like a slow steady stream, with a parabolic profile, just going forward and back with each beat.
In a wide artery, like the aorta, the blood in the middle moves almost as one block, and only a thin layer near the wall feels the friction.
The Womersley number says which of these two regimes applies.
