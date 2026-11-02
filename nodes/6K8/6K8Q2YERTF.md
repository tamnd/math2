---
tag: 6K8Q2YERTF
kind: concept
name: Chattering control
msc: [49J15, 49K15, 93C15]
sources:
  - url: https://en.wikipedia.org/wiki/Bang–bang_control
---

## Summary

A chattering control is a control that switches between values infinitely many times in a bounded time interval.
Its switching times accumulate at some point.
Chattering controls can be optimal, as in [[Fuller's phenomenon|RSZS9SFFZ7]], and they also appear as approximations of [[relaxed controls|SFMD8RKRSE]].
They show that the [[bang–bang|GK1Z3Q1WRZ]] structure of an optimal control may involve infinitely many switches.

## Explanations

### L1 human

Imagine a heater that must be fully on or fully off, and that should bring a room to an exact temperature as well as possible.
The best strategy may switch on and off more and more often as the target gets close, with shorter and shorter periods.
The switching times pile up at one moment, like the points $1/2, 3/4, 7/8, \ldots$ piling up at $1$.
A control with such infinitely many switches before a finite time is called chattering.
