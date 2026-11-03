---
tag: SJHSM3KKPC
kind: concept
name: Pierson–Moskowitz spectrum
msc: [86A05, 76B15]
specializes: [GYQCDP4VN8]
sources:
  - url: https://en.wikipedia.org/wiki/Sea_state
---

## Summary

The Pierson–Moskowitz spectrum is a model [[ocean wave spectrum|GYQCDP4VN8]] for a fully developed sea.
This is the state reached when a steady wind has blown long enough over a long enough stretch of water.
It was proposed by Willard Pierson and Lionel Moskowitz from measurements in the North Atlantic.
Its only parameter is the wind speed, and it decays like $\omega^{-5}$ at high frequencies.
It is a standard design spectrum in ocean engineering and the starting point for spectra of growing seas such as JONSWAP.

## Explanations

### L1 human

If the wind blows steadily for a long time over open ocean, the waves stop growing: they lose as much energy by breaking as they gain from the wind.
The Pierson–Moskowitz spectrum describes this final state.
Its single peak moves to longer periods as the wind gets stronger, and the wave height grows like the square of the wind speed.
For a wind of $20$ m/s, the formula gives a significant wave height of about $0.21 \cdot 20^2 / 9.8 \approx 8.5$ metres.
