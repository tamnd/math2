---
tag: C1K05DC7XF
kind: definition
name: Hindmarsh–Rose model
msc: [92C20, 37N25, 34C60]
defines: 87JVMFKR66
uses: [0NT64JV96A, RMWR3MDW0T, DBKXCGDKTD, 0AAQ73WRFB]
sources:
  - url: https://en.wikipedia.org/wiki/Hindmarsh–Rose_model
---

## Definition

Let $a, b, c, d, r, s, x_R, I$ be real parameters with $r > 0$.
The *Hindmarsh–Rose model* is the following system of [[ordinary differential equations|0NT64JV96A]].
$$\frac{dx}{dt} = y - a x^3 + b x^2 - z + I, \qquad \frac{dy}{dt} = c - d x^2 - y, \qquad \frac{dz}{dt} = r\bigl(s (x - x_R) - z\bigr).$$
Here $x(t)$ is the membrane potential, $y(t)$ a fast recovery variable, $z(t)$ a slow adaptation current and $I$ the applied current.

## Remarks

A frequently used choice is $a = 1$, $b = 3$, $c = 1$, $d = 5$, $s = 4$, $x_R = -8/5$, with $r$ of order $10^{-3}$.
Small $r$ makes $z$ slow, so the $(x, y)$ subsystem with $z$ frozen can be studied first.
It has a resting state and a spiking [[limit cycle|0AAQ73WRFB]] that coexist for a range of $z$.
The slow drift of $z$ moves the system back and forth across this range, which gives bursting.
Depending on $I$ and $r$, the model shows tonic spiking, regular bursting or [[chaotic|DBKXCGDKTD]] bursting.
Non-example: with $z$ held fixed ($r = 0$ and constant $z$), the system is planar, so by the Poincaré–Bendixson theorem it cannot be chaotic.
