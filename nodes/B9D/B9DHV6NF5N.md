---
tag: B9DHV6NF5N
kind: statement
role: fact
name: Poynting–Robertson effect
msc: [70F15, 85A04]
uses: [BXFSBB8Q46, 7147M98XNR, 9636MFFSGC]
about: [BXFSBB8Q46]
sources:
  - url: https://en.wikipedia.org/wiki/Poynting%E2%80%93Robertson_effect
same_as:
  wikidata: Q1127701
  wikipedia: Poynting–Robertson effect
---

## Statement

Let a spherical dust grain of radius $s$ and density $\rho$ orbit a star of luminosity $L$.
The orbit is a circular [[Kepler orbit|BXFSBB8Q46]] of radius $r$, with speed $v \ll c$, where $c$ is the speed of light.
Assume that the grain absorbs all the starlight that falls on it and re-emits it isotropically in its own rest frame.
Assume that the radiation pressure is small compared with the gravity of the star.
Then, to first order in $v/c$, the radiation exerts a drag force on the grain.
The force is opposite to the velocity and has the size
$$F_{\text{PR}} = \frac{v}{c} \cdot \frac{L s^2}{4 r^2 c},$$
and the orbit shrinks slowly while staying nearly circular, with
$$\frac{dr}{dt} = -\frac{3 L}{8 \pi \rho s c^2 \, r}.$$
A grain starting at radius $r_0$ reaches the star after the time
$$t_{\text{PR}} = \frac{4 \pi \rho s c^2 \, r_0^2}{3 L}.$$

## Remarks

Idea: in the frame of the moving grain, the starlight arrives slightly from the front because of the aberration of light.
So the radiation force has a small component against the motion.
Equivalently, in the frame of the star, the light re-emitted by the grain is Doppler shifted forward and carries away momentum along the motion.
The drag gives a [[torque|9636MFFSGC]] $-F_{\text{PR}} \, r$.
It equals the rate of change of the orbital [[angular momentum|7147M98XNR]] $m \sqrt{G M_\star r}$, with $m = \frac{4}{3}\pi s^3 \rho$, and this gives $dr/dt$.
Here $M_\star$ is the mass of the star and $G$ is the gravitational constant.
Integrating $r \, dr$ from $r_0$ to $0$ gives $t_{\text{PR}}$.

Example: for a grain with $s = 1$ mm and $\rho = 2000$ kg/m$^3$ starting at $1$ astronomical unit from the Sun, the formula gives about $4 \times 10^{13}$ s, roughly $1.4$ million years.
Because $t_{\text{PR}}$ grows with $s$, small grains are removed first, which clears dust from the inner Solar System and feeds the zodiacal cloud.

For very small grains the hypothesis on radiation pressure fails: the outward pressure is comparable to gravity and the grain is blown out of the system instead of spiralling in.

John Henry Poynting described the effect in 1903, and Howard P. Robertson gave its relativistic treatment in 1937.

## Explanations

### L1 human

Running through vertical rain, you get wet on the front because the rain seems to come at you at an angle.
A dust grain moving around the Sun meets sunlight in the same way, so the light pushes it slightly backwards.
This brake makes the grain lose orbital speed and spiral slowly into the Sun.

### L2 human

The effect is a first-order relativistic correction to radiation pressure, of relative size $v/c$, but it acts steadily over many orbits and so changes the orbit secularly.
The spiral time is proportional to the size of the grain and to the square of the initial distance.
It sets the lifetime of dust in debris disks and in the Solar System, together with collisions and the outward push of radiation pressure.
