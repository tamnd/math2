---
tag: S4THJVE1AJ
kind: concept
name: Time-variant system
msc: [93A10, 93C05]
sources:
  - url: https://en.wikipedia.org/wiki/Time-variant_system
same_as:
  wikidata: Q7804840
  wikipedia: Time-variant system
---

## Summary

A system is time-invariant if delaying its input only delays its output by the same amount, and time-variant if this fails.
In a time-invariant system the rules do not depend on the clock.
An experiment done today gives the same result as the same experiment done tomorrow.
In a time-variant system the behaviour itself changes with time, as in a rocket whose mass decreases as it burns fuel.
Time invariance is the property that, together with [[linearity|21FN2KSTJZ]], makes transfer functions and frequency methods available.

## Explanations

### L1 human

Imagine pressing a doorbell now or in an hour: if the sound is the same, only later, the doorbell is time-invariant.
A radio whose volume knob is slowly turned while it plays is time-variant: the same song played later comes out at a different volume.
Mathematically, the system $y(t) = 2u(t)$ is time-invariant.
The system $y(t) = t \, u(t)$ is time-variant, because its gain $t$ depends on when the input arrives.
