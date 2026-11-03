---
tag: SDVM01S0X6
kind: definition
name: Monte Carlo method for radiative transfer
msc: ["80M31", "80A21", 65C05]
defines: FAC4PR0NAE
uses: [W4MT7K2QTF, EX9YYRMAJA, 028Z8WC5Y9, 2KX7W1TG7T, 2TNXJANSF9]
sources:
  - url: https://en.wikipedia.org/wiki/Monte_Carlo_method_for_photon_transport
---

## Definition

Let $D \subseteq \R^3$ be a region filled with a medium with absorption coefficient $\kappa \ge 0$ and scattering coefficient $\sigma \ge 0$, where $\kappa + \sigma > 0$.
Let $p$ be a scattering phase function, normalized as in the [[radiative transfer equation|EX9YYRMAJA]].
Assume for simplicity that $\kappa$ and $\sigma$ are constant, and put $\beta = \kappa + \sigma$.
The *Monte Carlo method for radiative transfer* estimates radiative quantities by simulating $N$ independent bundle histories, each as follows.

1. Draw the emission point and the initial direction from the distribution of the emitted radiation.
2. Draw the free path length $s = -\ln(\xi)/\beta$ with $\xi$ uniform on $(0, 1)$, and move the bundle a distance $s$ along its direction.
3. If the bundle leaves $D$, record where it hits the boundary and stop.
4. Otherwise, with probability $\kappa / \beta$, record an absorption at that point and stop.
   With probability $\sigma / \beta$, draw a new direction $\Omega$ with density $p(\Omega' \cdot \Omega)/(4\pi)$, where $\Omega'$ is the old direction, and go to step 2.

A quantity of interest is, for example, the energy absorbed in a subregion or reaching a part of the boundary.
It is estimated by the fraction of the $N$ histories that end there, times the total emitted power.
This is an instance of the [[Monte Carlo method|W4MT7K2QTF]].

## Remarks

Step 2 is [[inverse transform sampling|2KX7W1TG7T]] of the [[exponential distribution|028Z8WC5Y9]] with rate $\beta$, which is the law of the distance to the first interaction in a homogeneous medium.
Each estimate is an average of independent bounded random variables, so its standard deviation is $O(N^{-1/2})$.
Example: a purely absorbing slab of thickness $d$ ($\sigma = 0$) is hit by bundles at normal incidence.
A bundle is transmitted exactly when $s > d$, which has probability $P(s > d) = e^{-\kappa d}$.
So the transmitted fraction tends to $e^{-\kappa d}$ as $N \to \infty$, which agrees with the [[Beer–Lambert law|2TNXJANSF9]].
Non-example: the discrete ordinates method also solves the radiative transfer equation, but it discretises the directions and solves the resulting deterministic equations, without random sampling.
In nonhomogeneous media, the path length is drawn so that the optical depth $\int_0^s \beta$ along the path is exponentially distributed with mean $1$.
