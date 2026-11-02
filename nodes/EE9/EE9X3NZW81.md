---
tag: EE9X3NZW81
kind: concept
name: Bifurcation in a family of maps
msc: [39A28, 37G15, "37E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Bifurcation_theory
---

## Summary

A bifurcation in a family of maps $f_\mu$ is a parameter value $\mu_0$ at which the qualitative behaviour of the iterates of $f_\mu$ changes.
Typical signs are fixed points or periodic orbits that appear, disappear or change their stability.
It is the setting of [[bifurcation theory|D9TW46P19Y]] for [[discrete-time dynamical systems|5AA9AJEARJ]], that is, for difference equations $x_{n+1} = f_\mu(x_n)$.
For one-dimensional maps the basic local types are the saddle-node, the transcritical, the pitchfork and the [[period-doubling bifurcation|NQDTTZ59X8]].

## Explanations

### L1 human

Picture a recursion with a knob, such as the growth rate in a population model.
For most knob settings, turning it a little changes nothing important: the same number of resting states, each attracting or repelling as before.
At a few special settings something new happens, for example a resting state loses its pull and a two-step cycle appears.
Those settings are the bifurcations.
In the logistic map $x \mapsto r x (1 - x)$, the value $r = 3$ is one: below it solutions settle to one value, just above it they alternate between two values.
