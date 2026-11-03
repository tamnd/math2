---
tag: EB1DQP2E0K
kind: concept
name: Lumped-element thermal model
msc: [80A19, 34A30]
sources:
  - url: https://en.wikipedia.org/wiki/Lumped-element_model
---

## Summary

The lumped-element thermal model treats a body as having one uniform temperature that changes with time.
This replaces the [[heat equation|VP2HN86VAG]] by an ordinary differential equation.
It is accurate when the [[Biot number|ZYJRK1RVP5]] is small, so that heat moves inside the body much faster than it leaves the surface.
Its solution is the exponential approach of [[Newton's law of cooling|02HB5F40VR]].

## Explanations

### L1 human

A small metal ball dropped into cold water cools almost evenly, so one thermometer reading describes the whole ball.
The model keeps only this single temperature.
The ball loses heat at a rate proportional to how much hotter it is than the water.
So its excess temperature shrinks by the same factor in each equal time step, like radioactive decay.
Networks of such lumps, joined by [[thermal resistances|1CB45W4GA6]], model whole buildings and electronic devices.
