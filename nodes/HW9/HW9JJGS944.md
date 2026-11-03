---
tag: HW9JJGS944
kind: concept
name: Passivity
msc: [93D30, 93C10, 93D25]
specializes: [RSZFWWYP9E]
sources:
  - url: https://en.wikipedia.org/wiki/Passivity_(engineering)
---

## Summary

A system is passive if it cannot produce more energy than it receives through its input.
Here the power supplied is the product $u^T y$ of input and output.
Formally, some nonnegative storage function of the state grows at most by the energy supplied.
Passivity is the special case of [[dissipativity|RSZFWWYP9E]] with supply rate $u^T y$.
Negative feedback connections of passive systems are again passive, which makes passivity a modular tool for proving stability of nonlinear systems.

## Explanations

### L1 human

Electric circuits made of resistors, capacitors and inductors are passive: they can store energy and burn it as heat, but they cannot create it.
The power going into such a circuit is voltage times current, the product of input and output.
A passive system is one where the energy stored at any time is at most the energy stored at the start plus the energy pumped in.
A spring with a damper is a mechanical example, with force as input and velocity as output.
