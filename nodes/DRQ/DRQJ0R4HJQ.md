---
tag: DRQJ0R4HJQ
kind: example
name: Mercator projection
msc: [86A30, 30C20]
instance_of: [Y2C8D9VC7D]
uses: [Y2C8D9VC7D, 0YYT36R4YD, RCMYJPDMGJ]
sources:
  - url: https://en.wikipedia.org/wiki/Mercator_projection
same_as:
  wikidata: Q309372
  wikipedia: Mercator projection
---

## Example

On the sphere of radius $R$, the *Mercator projection* is
$$x = R(\lambda - \lambda_0), \qquad y = R \ln \tan\left(\frac{\pi}{4} + \frac{\varphi}{2}\right),$$
for latitude $\abs{\varphi} < \pi/2$ and longitude $\lambda_0 - \pi < \lambda < \lambda_0 + \pi$, where $\lambda_0$ is the central meridian.
It is a [[map projection|Y2C8D9VC7D]]: it is smooth, $x$ determines $\lambda$, and $y$ is a strictly increasing function of $\varphi$.
Check of conformality: a small step $d\lambda$ has length $R\cos\varphi\,d\lambda$ on the sphere and $R\,d\lambda$ on the map, so the east-west scale is $\sec\varphi$.
Since $dy/d\varphi = R\sec\varphi$, a small step $d\varphi$ of length $R\,d\varphi$ becomes $R\sec\varphi\,d\varphi$, so the north-south scale is also $\sec\varphi$.
Both scales are equal and the images of meridians and parallels are perpendicular, so the projection is [[conformal|0YYT36R4YD]].
Its [[Tissot indicatrix|RCMYJPDMGJ]] at latitude $\varphi$ is a circle of radius $\sec\varphi$, and the area scale is $\sec^2\varphi$.
The poles have no image, since $y \to \pm\infty$ as $\varphi \to \pm\pi/2$.

## Explanations

### L1 human

The Mercator map wraps a cylinder around the equator and stretches the globe onto it so that shapes stay right in small regions.
To keep shapes, it stretches north-south by the same factor as east-west, and that factor grows towards the poles.
At latitude $60^\circ$ the factor is $2$, so areas look four times too large.
Lines of constant compass bearing are straight on this map, which is why sailors used it.
