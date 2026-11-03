---
tag: EPHETG6TCT
kind: example
name: RLC circuit
msc: [94C05, 34A30]
illustrates: [9B0V41V2F8]
uses: [9B0V41V2F8, 0NT64JV96A, 0RNXVVTJTJ]
sources:
  - url: https://en.wikipedia.org/wiki/RLC_circuit
same_as:
  wikidata: Q323477
  wikipedia: RLC circuit
---

## Example

A *series RLC circuit* is a single loop made of a resistor $R > 0$, an inductor $L > 0$, a capacitor $C > 0$ and a voltage source $V(t)$.
Let $q(t)$ be the charge on the capacitor and $i = q'$ the loop current.
The voltage drops are $R i$ across the resistor, $L i'$ across the inductor and $q / C$ across the capacitor.
The voltage law of [[Kirchhoff's circuit laws|9B0V41V2F8]] around the loop gives the [[ordinary differential equation|0NT64JV96A]]
$$L q'' + R q' + \frac{q}{C} = V(t).$$
This is the equation of a [[damped harmonic oscillator|0RNXVVTJTJ]], with $L$ as mass, $R$ as friction and $1/C$ as spring constant.
For $V = 0$, the characteristic equation $L s^2 + R s + 1/C = 0$ has roots $s = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$ with $\alpha = R/(2L)$ and $\omega_0 = 1/\sqrt{LC}$.
The circuit is overdamped if $\alpha > \omega_0$, critically damped if $\alpha = \omega_0$, and underdamped, with decaying oscillations of angular frequency $\sqrt{\omega_0^2 - \alpha^2}$, if $\alpha < \omega_0$.

## Remarks

For a sinusoidal source of angular frequency $\omega > 0$, the steady state has impedance $Z(\omega) = R + \mathrm{i}\left(\omega L - \frac{1}{\omega C}\right)$, where $\mathrm{i}$ is the imaginary unit.
Its modulus is smallest at the resonant frequency $\omega = \omega_0$, where $Z = R$ and the current amplitude is largest.
For example, $L = 1$ henry and $C = 1$ microfarad give $\omega_0 = 1000$ radians per second.

## Explanations

### L1 human

An RLC circuit is the electrical version of a mass on a spring with friction.
The inductor resists changes of current like a mass resists changes of speed, the capacitor stores energy like a spring, and the resistor turns energy into heat like friction.
Charge put on the capacitor sloshes back and forth through the inductor, and the resistor makes the swings die out.
Driven at the right frequency, the circuit resonates, which is how a radio tunes to one station.
