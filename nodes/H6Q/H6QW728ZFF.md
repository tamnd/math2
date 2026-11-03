---
tag: H6QW728ZFF
kind: concept
name: Ensemble Kalman filter
msc: [86A22, "93E11", 62M20]
sources:
  - url: https://en.wikipedia.org/wiki/Ensemble_Kalman_filter
same_as:
  wikidata: Q3072268
  wikipedia: Ensemble Kalman filter
---

## Summary

The ensemble Kalman filter is a method of [[data assimilation|TKT0QAPWW8]].
It replaces the covariance matrix of the Kalman filter by the sample covariance of a finite ensemble of model states.
Each member of the ensemble is run forward by the full, possibly nonlinear, model, and is then corrected with the observations by a Kalman-type update.
It avoids storing and propagating a covariance matrix of the size of the state.
That is impossible for weather and ocean models with millions of variables.
It was introduced by Geir Evensen in 1994 and is now used in operational weather and ocean forecasting.

## Explanations

### L1 human

Instead of one forecast, run a few dozen forecasts that start from slightly different states.
Where the forecasts disagree, the model is uncertain; where they agree, it is confident.
When a new measurement arrives, every forecast is pulled toward it, and more strongly where the ensemble is uncertain.
For example, if forty forecasts of tomorrow's temperature spread between $18$ and $22$ degrees and a thermometer reads $21$, each forecast is moved part of the way toward $21$.
The corrected ensemble is then run forward again to the next measurement.
