---
tag: 6ZD2Z78YRM
kind: concept
name: Smith predictor
msc: [93C43, 93B51]
sources:
  - url: https://en.wikipedia.org/wiki/Smith_predictor
same_as:
  wikidata: Q7545392
  wikipedia: Smith predictor
---

## Summary

The Smith predictor is a controller structure for stable plants with a pure time delay.
It uses an internal model of the plant to predict the output without the delay.
It feeds this prediction back to an ordinary controller.
With a perfect model, the delay is moved outside the feedback loop, so the controller can be tuned as if there were no delay.
It matters because time delays in a loop, common in process control, severely limit what plain [[feedback|7NYES2D0Z4]] can achieve.

## Explanations

### L1 human

Imagine adjusting a shower where the water takes ten seconds to reach you.
If you react to what you feel now, you keep overcorrecting, because you feel the effect of your actions too late.
The Smith predictor imagines a shower without the pipe, reacts to that imagined temperature, and checks the imagined one against reality to correct model errors.
The result behaves like the delay-free loop, followed by the unavoidable ten-second wait.
