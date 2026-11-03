---
tag: PPPSMTJMJP
kind: definition
name: Deflection of the vertical
msc: [86A30]
defines: Y3AWPW7AXM
uses: [R9XX7TNJCH, 6QBV95NG6E, 5Y2BWNY6MF]
sources:
  - url: https://en.wikipedia.org/wiki/Vertical_deflection
---

## Definition

Let $P$ be a point near the Earth's surface.
Let $\Phi$ and $\Lambda$ be the astronomical latitude and longitude of $P$.
They give the direction of the gravity vector $\nabla W$ of the [[geopotential|5Y2BWNY6MF]] at $P$.
Let $\varphi$ and $\lambda$ be the [[geodetic latitude and longitude|6QBV95NG6E]] of $P$, which give the direction of the normal to the [[reference ellipsoid|R9XX7TNJCH]] through $P$.
The *deflection of the vertical* at $P$ is the angle $\theta$ between these two directions.
Its north–south component $\xi$ and east–west component $\eta$ are
$$\xi = \Phi - \varphi, \qquad \eta = (\Lambda - \lambda)\cos\varphi,$$
and for small angles $\theta^2 \approx \xi^2 + \eta^2$.

## Remarks

Example: if $\Phi = 45^\circ 0' 6''$, $\varphi = 45^\circ 0' 0''$ and $\Lambda = \lambda$, then $\xi = 6''$, $\eta = 0$, and the deflection is $6''$ in the north–south direction.
Non-example: the difference $\Lambda - \lambda$ alone is not the east–west component; it must be multiplied by $\cos\varphi$, because meridians converge towards the poles.
The east–west component also links astronomical and geodetic azimuths: the Laplace equation $A - \alpha = \eta\tan\varphi = (\Lambda - \lambda)\sin\varphi$ holds to first order for a line of sight close to the horizon.
It is used to control the azimuths of triangulation networks.
Some authors use the opposite sign convention, with ellipsoid direction minus gravity direction.
