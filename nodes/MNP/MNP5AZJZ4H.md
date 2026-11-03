---
tag: MNP5AZJZ4H
kind: statement
role: theorem
name: Herzenberg dynamo
msc: [76W05, 86A25]
uses: [AFVDBT0K5C, T8JWCBK9M6, JBKC51WDFE]
about: [AFVDBT0K5C]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamo_theory
---

## Statement

Let a large sphere of uniform electrical conductivity be surrounded by an insulator.
Let it contain two small rigid spheres of radius $a$ made of the same conductor, in perfect electrical contact with it.
Let the distance $d$ between their centres satisfy $d \gg a$.
Let each small sphere rotate rigidly with angular speed $\omega$ about an axis through its centre.
Let the rest of the conductor stay at rest.
Consider the magnetic induction equation of [[magnetohydrodynamics|T8JWCBK9M6]] with this velocity field.
For suitable non-parallel orientations of the two axes and for $\omega$ above a critical value, it has a solution with a non-decaying magnetic field.
So kinematic dynamo action is possible in a body of uniform conductivity.

## Remarks

Herzenberg published this example in 1958; in the same year Backus gave another rigorous example with a time-dependent flow.
These were the first rigorous existence proofs for homogeneous kinematic dynamos.
They answered the doubt raised by Cowling's antidynamo theorem, which rules out axisymmetric dynamos.
The proof uses $d \gg a$.
Near each sphere, the field is computed as the response of that sphere to the nearly uniform field produced there by the other sphere.
Then a self-consistent pair of responses is sought.
The arrangement is chiral; if the two axes are parallel, the mutual reinforcement fails.

## Explanations

### L1 human

Can a moving lump of uniform metal make its own magnetic field, with no wires to guide the currents?
Herzenberg showed that the answer is yes with a simple machine: two spinning metal balls inside a big metal ball.
Each spinning ball twists the field made by the other one into a field that helps the other one.
If they spin fast enough, a magnetic field maintains itself.

### L2 human

In [[dynamo theory|AFVDBT0K5C]] the kinematic problem fixes the flow and asks whether the induction equation has growing or steady solutions.
Antidynamo theorems show that flows that are too symmetric fail.
The Herzenberg dynamo is a carefully chosen asymmetric flow for which the answer can be computed by asymptotic analysis.
It is an analogue of the [[Bullard disc dynamo|JBKC51WDFE]] in a body of uniform conductivity, with no insulating wires to direct the current.
