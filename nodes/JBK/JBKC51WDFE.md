---
tag: JBKC51WDFE
kind: example
name: Bullard disc dynamo
msc: [86A25, 34C60]
illustrates: [AFVDBT0K5C]
uses: [AFVDBT0K5C, 0J0FCWV32D]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamo_theory
---

## Example

A metal disc rotates with angular speed $\Omega$ about its axis.
Sliding contacts on its rim and on its axle connect it to a wire coil wound around the axle.
A current $I$ in the coil makes a magnetic field through the disc.
Let $L$ be the self-inductance of the circuit, $R$ its resistance, and $M > 0$ the mutual inductance between the coil and the disc rim.
The flux through the disc is $MI$, and the rotating disc produces an electromotive force $M \Omega I / (2\pi)$.
So the current obeys
$$L \frac{dI}{dt} = \left( \frac{M \Omega}{2\pi} - R \right) I.$$
At constant $\Omega$, the solution is the [[exponential|0J0FCWV32D]] $I(t) = I_0 \exp\big( (M\Omega/(2\pi) - R) t / L \big)$.
If $\Omega > 2\pi R / M$, any small current $I_0 \neq 0$ grows exponentially: the device is a self-exciting dynamo.
If $\Omega < 2\pi R/M$, the current decays.

When a constant torque $G$ drives the disc, which has moment of inertia $C$, the Lorentz force adds the equation
$$C \frac{d\Omega}{dt} = G - \frac{M I^2}{2\pi}.$$
The steady states with $I \neq 0$ are $\Omega = 2\pi R/M$ and $I^2 = 2\pi G/M$.

## Remarks

The model was studied by Bullard in 1955 as the simplest picture of [[dynamo theory|AFVDBT0K5C]].
The current keeps its initial sign forever, so this single disc cannot reverse.
Rikitake's two-disc dynamo of 1958 couples two such discs, and its current reverses irregularly.
The coil winding makes the device lack mirror symmetry; winding the coil the other way gives $M < 0$ and no dynamo for the same sense of rotation.

## Explanations

### L1 human

Spin a copper disc in a magnetic field and a voltage appears between its axle and its rim.
Feed that voltage into a coil that makes the field, and you have a loop: field makes current, current makes field.
If the disc spins fast enough, a tiny stray current grows until the drive and the braking force balance.
This shows in one line of algebra how a moving conductor can make its own magnetic field.
