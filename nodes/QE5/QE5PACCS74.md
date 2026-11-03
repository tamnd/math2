---
tag: QE5PACCS74
kind: concept
name: Electrical resistivity tomography
msc: [86A22, 35R30, 35J25]
specializes: [C54MFNX576]
sources:
  - url: https://en.wikipedia.org/wiki/Electrical_resistivity_tomography
same_as:
  wikidata: Q488986
  wikipedia: Electrical resistivity tomography
---

## Summary

Electrical resistivity tomography is a method to image the electrical resistivity of the ground from many measurements with electrodes.
The electrodes are usually placed at the surface or in boreholes.
For each measurement, a current is injected through two electrodes and a voltage is measured between two others.
The data are converted to apparent resistivities and then inverted for a two- or three-dimensional resistivity model.
So it is a [[geophysical inversion|C54MFNX576]] closely related to the [[Calderón problem|R8Y8DDTWBM]].
It is widely used in hydrogeology, environmental and engineering studies and archaeology.

## Explanations

### L1 human

Wet clay conducts electricity well, while dry sand and solid rock conduct it poorly.
Push a small current into the ground through two metal stakes and measure the voltage at two other stakes.
This tells how hard it is for current to flow there.
Repeating this with many stake combinations, near and far apart, gives information at many depths and places.
A computer then builds a picture of the resistivity underground.
In uniform ground of resistivity $\rho$, a current $I$ at a single surface stake makes the voltage $\rho I/(2\pi r)$ at distance $r$.
