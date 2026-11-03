---
tag: ZD2CCNQ3H2
kind: definition
name: Roche lobe
msc: [70F07, 85A05]
defines: W1QRRQA8EZ
uses: [29WRN5J730, BXFSBB8Q46, DCMFQ01QGS, 0B2RZ0778N, 6HZRX3WSQD]
sources:
  - url: https://en.wikipedia.org/wiki/Roche_lobe
---

## Definition

Let two point masses $M_1$ and $M_2$ move on circular orbits about their common centre of mass, at separation $a$.
They move under [[Newtonian gravity|29WRN5J730]], with $G$ the gravitational constant.
Their angular velocity is $\Omega = \sqrt{G(M_1 + M_2)/a^3}$.
Use the frame that rotates with angular velocity $\Omega$, with origin at the centre of mass.
In it the masses are fixed at points $r_1$ and $r_2$ of the plane $z = 0$, and the *Roche potential* is
$$\Phi(r) = -\frac{G M_1}{\abs{r - r_1}} - \frac{G M_2}{\abs{r - r_2}} - \frac{1}{2} \Omega^2 (x^2 + y^2), \qquad r = (x, y, z).$$
Let $L_1$ be the inner Lagrange point, the critical point of $\Phi$ on the segment between $r_1$ and $r_2$.
The *Roche lobe* of $M_1$ is the closure of the connected component containing $r_1$ of the set $\set{r : \Phi(r) < \Phi(L_1)}$.

## Remarks

The two Roche lobes touch at $L_1$, and the [[level set|0B2RZ0778N]] $\Phi = \Phi(L_1)$ that bounds them is a figure-eight in the orbital plane.
The last term of $\Phi$ is the potential of the centrifugal force; the [[Coriolis force|6HZRX3WSQD]] does no work and does not enter $\Phi$.
The *Roche lobe radius* $r_L$ is the radius of the sphere with the same volume as the lobe.
Eggleton's approximation, accurate to about one per cent for all mass ratios, is
$$\frac{r_L}{a} \approx \frac{0.49 \, q^{2/3}}{0.6 \, q^{2/3} + \ln\left(1 + q^{1/3}\right)}, \qquad q = M_1/M_2.$$

Example: for $M_1 = M_2$, the symmetry $r \mapsto -r$ exchanges the two masses and fixes $\Phi$, so $L_1$ is the centre of mass and the two lobes are mirror images.
Eggleton's formula gives $r_L \approx 0.49/(0.6 + \ln 2) \, a \approx 0.38 \, a$.

Non-example: take a value $c > \Phi(L_1)$ slightly above the critical one.
The component of $\set{\Phi < c}$ containing $r_1$ also contains $r_2$, so it is a common envelope around both stars and not the lobe of $M_1$.
