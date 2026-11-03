---
tag: 2TNXJANSF9
kind: statement
role: proposition
name: Beer–Lambert law
msc: [78A40, 85A25]
uses: [0J0FCWV32D, 0NT64JV96A]
about: [EX9YYRMAJA]
sources:
  - url: https://en.wikipedia.org/wiki/Beer–Lambert_law
same_as:
  wikidata: Q217351
  wikipedia: Beer–Lambert law
---

## Statement

Let a collimated monochromatic beam of light cross a medium along the segment $0 \le z \le \ell$.
Assume that the medium absorbs the light linearly, with an attenuation coefficient $\mu(z) \ge 0$ that is continuous on $[0, \ell]$.
Assume also that the medium neither emits light nor scatters light into the beam.
Then the intensity $I(z)$ of the beam satisfies $I'(z) = -\mu(z) I(z)$, and
$$I(\ell) = I(0) \exp\left(-\int_0^\ell \mu(z) \, dz\right).$$
In particular, let the medium be a solution of one absorbing species of concentration $c$ in a cell of length $\ell$.
Let $\epsilon$ be its molar attenuation coefficient, defined with base-$10$ logarithms.
Then the absorbance satisfies
$$A = \log_{10} \frac{I(0)}{I(\ell)} = \epsilon \, c \, \ell.$$

## Remarks

The idea of the proof: a thin layer of thickness $dz$ removes a fixed fraction $\mu(z) \, dz$ of the light that enters it.
This gives the linear [[differential equation|0NT64JV96A]] $I' = -\mu I$, whose solution is an [[exponential|0J0FCWV32D]] of the integral of $-\mu$.
With $\mu = \ln(10) \, \epsilon c$ constant, taking $\log_{10}$ gives the absorbance form.

Example: if a layer of $1$ cm transmits half of the light, then $\mu = \ln 2$ per cm, and $3$ cm of the same medium transmit $(1/2)^3 = 1/8$ of the light.

The hypotheses are needed.
At very high intensity the absorption becomes nonlinear (saturation), and $\mu$ depends on $I$.
If the medium scatters light into the beam or emits light, the intensity obeys the full [[radiative transfer equation|EX9YYRMAJA]], of which this law is the case with no source terms.
At high concentration, interactions between molecules make the absorbance depend nonlinearly on $c$.

## Explanations

### L1 human

Each thin slice of an absorbing material removes the same fraction of the light that reaches it.
So the light decreases exponentially with the distance it travels.
Doubling the path or doubling the concentration doubles the absorbance.
This is why measuring how much light passes through a sample gives its concentration.

### L2 human

The law is the simplest solution of the radiative transfer equation: a beam along one line, with only extinction.
The quantity $\int_0^\ell \mu \, dz$ is the optical depth of the path, and the law says the transmission is its negative exponential.
In spectroscopy it is used to measure concentrations; in astrophysics and atmospheric physics it describes the extinction of starlight and sunlight.
