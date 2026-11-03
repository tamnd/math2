---
tag: QTEWT0Z0EF
kind: concept
name: Enthalpy method for phase change
msc: ["80A22", "80M20", 35R35]
sources:
  - url: https://en.wikipedia.org/wiki/Stefan_problem
---

## Summary

The enthalpy method rewrites a melting or freezing problem as a single heat conduction equation for the [[enthalpy|722RZK72P5]] on the whole domain.
The temperature is a function of the enthalpy that stays flat at the melting point while the [[latent heat|FN6Z9QKAH5]] is absorbed or released.
The moving boundary between solid and liquid is not tracked; it is read off afterwards as the place where the temperature equals the melting point.
This gives a weak formulation of the [[Stefan problem|3B0HB3DHW1]] and a simple numerical method on a fixed grid.
The method also handles several space dimensions and changes in the topology of the front.
See the [[definition|NWTYMKXCCB]].

## Explanations

### L1 human

Melting ice in a glass needs heat even though the temperature stays at $0$ degrees until all the ice is gone.
The enthalpy keeps count of all the heat a piece of material has received, including the heat spent on melting.
So the enthalpy keeps rising during the melting while the temperature waits.
The method follows the enthalpy of each small cell of the material, and a cell is solid, liquid or partly melted according to its enthalpy.
No one has to say in advance where the ice ends and the water begins.
