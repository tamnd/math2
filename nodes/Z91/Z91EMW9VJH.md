---
tag: Z91EMW9VJH
kind: definition
name: Metamaterial cloaking
msc: [78A48, 78A45, 78A46]
defines: XAKEYEGSTC
uses: [9BWWD4QK8Y, 8BQYB8H5CT, F768YN0P2V, 5MJQ5J5H8Z, CQ9A45JF68, HBCRG5V2BD]
sources:
  - url: https://en.wikipedia.org/wiki/Metamaterial_cloaking
---

## Definition

Let $D \subset \Omega \subset \R^3$ be bounded open sets with $\overline{D} \subset \Omega$, and fix an angular frequency $\omega > 0$.
Let the region outside $\Omega$ be vacuum.
A *cloak* for $D$ at frequency $\omega$ is a linear medium, given by a [[permittivity|F768YN0P2V]] $\varepsilon$ and a [[permeability|5MJQ5J5H8Z]] $\mu$ on $\Omega \setminus \overline{D}$, with this property.
For every linear medium placed in $D$ and every incident time-harmonic field that solves the vacuum [[Maxwell equations|9BWWD4QK8Y]], the [[scattered field|8BQYB8H5CT]] outside $\Omega$ is zero.
In other words, the total field outside $\Omega$ equals the incident field.
*Metamaterial cloaking* is the realisation of a cloak, exactly or approximately, by a [[metamaterial|CQ9A45JF68]].

## Remarks

Example: the spherical cloak of Pendry, Schurig and Smith.
Let $0 < R_1 < R_2$, let $D$ be the ball $\abs{y} < R_1$ and $\Omega$ the ball $\abs{y} < R_2$.
The radial map $r' = R_1 + r (R_2 - R_1)/R_2$ sends the punctured ball $0 < \abs{x} < R_2$ onto the shell $R_1 < \abs{y} < R_2$, and it is the identity on the sphere $\abs{x} = R_2$.
By [[transformation optics|HBCRG5V2BD]], vacuum becomes the medium with, in spherical coordinates and relative to vacuum,
$$\varepsilon_r = \mu_r = \frac{R_2}{R_2 - R_1} \frac{(r' - R_1)^2}{r'^2}, \qquad \varepsilon_\theta = \varepsilon_\phi = \mu_\theta = \mu_\phi = \frac{R_2}{R_2 - R_1}.$$
Outside $\Omega$ the map is the identity, so fields there are those of empty space, and waves never reach $D$.
The radial parameters vanish at $r' = R_1$, so the medium is singular; the claim that it cloaks is made precise with weak solutions, or by a limit of regular approximate cloaks.

Non-example: a perfectly conducting shell hides what is inside it, but its scattered field outside $\Omega$ is not zero, since it scatters the incident wave like any metal ball.

The same construction for electrical impedance tomography was given by Greenleaf, Lassas and Uhlmann.

## Explanations

### L1 human

A cloak is a coat of material around a region such that nothing in the region can be seen from outside.
The definition asks two things: whatever is hidden, and whatever wave is sent, the outside field is that of empty space.
Transformation optics gives such a coat by "blowing up" one point into the whole hidden ball.
