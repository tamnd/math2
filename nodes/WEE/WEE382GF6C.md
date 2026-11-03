---
tag: WEE382GF6C
kind: definition
name: Two-body relaxation time
msc: [85A05, 70F10]
defines: GZE6E8XQ7T
uses: [4V8BT1ZD00, 04VZE3FZXF, 29WRN5J730]
sources:
  - url: https://en.wikipedia.org/wiki/Relaxation_(physics)
---

## Definition

Let a stellar system of radius $R$ consist of $N$ stars of equal mass $m$, with typical speed $v$.
Let $t_{\text{cross}} = R/v$ be its crossing time.
A star crosses the system once and meets other stars under [[Newtonian gravity|29WRN5J730]].
Each encounter changes its velocity perpendicular to its motion by a small random amount $\Delta v_\perp$.
These changes add like the steps of a [[random walk|04VZE3FZXF]], with total $\sum (\Delta v_\perp)^2$ per crossing.
The number of crossings $n_{\text{relax}}$ is defined by $n_{\text{relax}} \sum (\Delta v_\perp)^2 = v^2$.
The *two-body relaxation time* is $t_{\text{relax}} = n_{\text{relax}} \, t_{\text{cross}}$.

## Remarks

An encounter with impact parameter $b$ gives $\Delta v_\perp \approx 2 G m/(b v)$, where $G$ is the gravitational constant.
Summing over the encounters of one crossing, with $b$ between a smallest value $b_{\min}$ and $R$, gives $\sum (\Delta v_\perp)^2 \approx 8 N (G m/(R v))^2 \ln \Lambda$ with $\Lambda = R/b_{\min}$.
If the system is in virial equilibrium, $v^2 \approx G N m/R$, and so
$$t_{\text{relax}} \approx \frac{N}{8 \ln \Lambda} \, t_{\text{cross}}, \qquad \Lambda \approx N.$$
The factor $\ln \Lambda$ shows that all ranges of distance contribute equally, so distant weak encounters dominate over close strong ones.

Example: a globular cluster with $N = 10^5$ and $t_{\text{cross}} \approx 10^5$ years has $t_{\text{relax}} \approx 10^5/(8 \cdot 11.5) \cdot 10^5 \approx 10^8$ years, shorter than its age of about $10^{10}$ years.

Non-example: a galaxy with $N = 10^{11}$ and $t_{\text{cross}} \approx 10^8$ years has $t_{\text{relax}}$ of order $10^{17}$ years.
So the galaxy does not relax within the age of the universe, and it is collisionless.
