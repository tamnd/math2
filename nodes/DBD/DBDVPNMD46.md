---
tag: DBDVPNMD46
kind: definition
name: Time series
msc: [62M10, 91B84]
defines: EA3MF4VTEH
uses: [0QH5ENKZM1, 0G9EKM0E15]
sources:
  - url: https://en.wikipedia.org/wiki/Time_series
---

## Definition

Let $T$ be a set of time points, usually $T = \Z$, $T = \set{1, \dots, n}$ or an interval of $\R$.
A *time series* is a family of observations $(x_t)_{t \in T}$ indexed by time, together with the order of $T$.
As a statistical model, a time series is a realization of a [[stochastic process|0QH5ENKZM1]] $(X_t)_{t \in T}$.
The same name is often used for the process itself.
The series is in *discrete time* when $T$ is a subset of $\Z$, and in *continuous time* when $T$ is an interval of $\R$.

## Remarks

Example: the yearly maximum temperatures $x_{1990}, \dots, x_{2020}$ at one weather station form a discrete-time series with $T = \set{1990, \dots, 2020}$.
Non-example: the heights of $30$ pupils, listed in alphabetical order of their names, are not a time series.
The index is not time, and its order carries no meaning.
A discrete-time series is a finite or infinite [[sequence|0G9EKM0E15]] of real numbers or vectors; when its values are vectors it is called multivariate.
Many methods assume that the underlying process is stationary, possibly after removing a trend or a seasonal component.
