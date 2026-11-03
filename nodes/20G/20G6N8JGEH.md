---
tag: 20G6N8JGEH
kind: concept
name: Transonic flow
msc: [76H05, 35M10]
specializes: [FJC2GMVARF]
sources:
  - url: https://en.wikipedia.org/wiki/Transonic
---

## Summary

A transonic flow is a [[compressible flow|FJC2GMVARF]] that contains both subsonic and supersonic regions.
This happens when the flight speed is close to the [[speed of sound|SN4J6KP03C]].
Consider a wing at a free stream Mach number of about $0.8$.
A pocket of supersonic flow forms over its upper surface and usually ends in a shock wave.
The steady equations of transonic flow are of mixed type, elliptic in the subsonic part and hyperbolic in the supersonic part, like the [[Tricomi equation|21DD2334NR]].
This makes transonic flow hard both in theory and in computation, and it governs the design of modern airliner wings.

## Explanations

### L1 human

An airliner cruises a little below the speed of sound.
The air speeds up as it passes over the curved top of the wing, and in a region there it moves faster than sound.
Behind that region the air must slow down again, and it usually does so abruptly in a weak shock wave, which costs drag.
The flow is thus partly slower and partly faster than sound, and both kinds of behaviour must be handled at once.
