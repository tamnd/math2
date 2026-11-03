---
tag: C2A51P3NHQ
kind: example
name: Rankine cycle
msc: [80A10]
instance_of: [AGRGCDWQF8]
uses: [722RZK72P5, ECAXF3AWWX, WYAY33ZVYQ, Z686C32X8S, 4Y41F2C3P9]
sources:
  - url: https://en.wikipedia.org/wiki/Rankine_cycle
same_as:
  wikidata: Q215612
  wikipedia: Rankine cycle
---

## Example

The ideal *Rankine cycle* is a [[thermodynamic cycle|AGRGCDWQF8]] of a working fluid, usually water, that flows steadily through four devices.

1. State $1 \to 2$: a pump compresses saturated liquid along an [[isentropic process|ECAXF3AWWX]] from the low pressure $p_L$ to the high pressure $p_H$.
2. State $2 \to 3$: a boiler heats the fluid along an [[isobaric process|WYAY33ZVYQ]] at $p_H$ until it is vapour, possibly superheated.
3. State $3 \to 4$: a turbine expands the vapour isentropically from $p_H$ back to $p_L$.
4. State $4 \to 1$: a condenser cools the fluid at constant pressure $p_L$ until it is saturated liquid again.

The fluid returns to state $1$, so every state function returns to its initial value and the process is a cycle.
Let $h_i$ be the specific [[enthalpy|722RZK72P5]] at state $i$.
Neglect changes of kinetic and potential energy in the steady flow.
Then the heat taken in per unit mass is $q_{in} = h_3 - h_2$ and the heat given off is $q_{out} = h_4 - h_1$.
The net work per unit mass is $w = q_{in} - q_{out}$, by the first law over one cycle.
So the [[thermal efficiency|Z686C32X8S]] is
$$\eta = 1 - \frac{h_4 - h_1}{h_3 - h_2}.$$

## Remarks

In the boiler, the fluid takes in heat at temperatures below the highest temperature of the cycle.
So, by [[Carnot's theorem|4Y41F2C3P9]], the efficiency is lower than the Carnot efficiency between the highest and lowest temperatures of the cycle.
The pump work $h_2 - h_1$ is small because a liquid is nearly incompressible, and this is an advantage over a gas cycle.
In a gas cycle the compressor takes a large part of the turbine work.

## Explanations

### L1 human

The Rankine cycle is the idealised cycle of a steam power plant.
Water is pumped to high pressure, boiled, run through a turbine, and condensed back to water.
The turbine gives much more work than the pump needs, and the difference is the useful output.
Its efficiency is read off from four enthalpy values in steam tables.
