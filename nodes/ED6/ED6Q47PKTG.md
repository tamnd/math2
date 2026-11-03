---
tag: ED6Q47PKTG
kind: definition
name: Numerical weather prediction
msc: [86A10, 65M06, 35Q86]
defines: HHX77HQZ7F
uses: [0FXDW992DS, QANHETP404, TKT0QAPWW8, B6E54YTR64, G0ZT1SDQGS]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_weather_prediction
---

## Definition

Let $M$ be a numerical model of the atmosphere.
It is a discretisation in space and time, by the methods of [[numerical analysis|B6E54YTR64]], of partial differential equations for the atmospheric state.
Typical equations are the [[primitive equations|QANHETP404]], together with parametrisations of unresolved processes.
The model state is a vector $x \in \R^n$ of grid-point or spectral values, and one step of the model maps $x_k$ to $x_{k+1} = M(x_k)$.
*Numerical weather prediction* is the forecasting of the weather by the following procedure.

1. An analysis $x_0^a$ of the current state is computed from observations and a previous forecast by [[data assimilation|TKT0QAPWW8]].
2. The [[initial value problem|0FXDW992DS]] is solved forward: $x_{k+1} = M(x_k)$ with $x_0 = x_0^a$, up to the forecast range.
3. The forecast fields $x_k$ are converted into weather variables at the times and places of interest.

## Remarks

The procedure is repeated in cycles, typically every $6$ or $12$ hours, and the short-range forecast of one cycle is the background for the next analysis.
In ensemble prediction, step 2 is repeated from several perturbed analyses, and the spread of the forecasts estimates their uncertainty.

Example: the first successful numerical forecast, in 1950, used the barotropic vorticity equation on a grid over North America and was computed on the ENIAC computer.

Non-example: a statistical forecast that predicts tomorrow's temperature by regression on past observations, without integrating equations of motion, is not numerical weather prediction in this sense.

Because the atmosphere is chaotic, errors in $x_0^a$ grow with time, the [[butterfly effect|G0ZT1SDQGS]], and this limits the useful range of deterministic forecasts to about two weeks.
