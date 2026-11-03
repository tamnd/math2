---
tag: HHX77HQZ7F
kind: concept
name: Numerical weather prediction
msc: [86A10, 65M06, 35Q86]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_weather_prediction
same_as:
  wikidata: Q837552
  wikipedia: Numerical weather prediction
---

## Summary

Numerical weather prediction is the forecasting of the weather by solving the equations of atmospheric motion on a computer.
It treats the forecast as an [[initial value problem|0FXDW992DS]].
An estimate of the present state, obtained by [[data assimilation|TKT0QAPWW8]], is advanced in time by a discretised model such as the [[primitive equations|QANHETP404]].
The first successful numerical forecast, with the barotropic vorticity equation, was made in 1950, and today it is the basis of all weather forecasts.
Its skill is limited by model errors, by errors in the initial state and by the chaotic growth of those errors.

## Explanations

### L1 human

The atmosphere obeys the laws of physics: conservation of mass, momentum, energy and water.
Numerical weather prediction cuts the atmosphere into millions of boxes and estimates the weather in each box now.
Then it uses the laws of physics to step forward a few minutes at a time.
Repeating this step thousands of times gives a forecast several days ahead.
Because small errors in the starting state grow, forecasters run many slightly different forecasts, an ensemble, to see how certain the forecast is.
