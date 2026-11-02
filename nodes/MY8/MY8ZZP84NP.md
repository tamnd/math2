---
tag: MY8ZZP84NP
kind: concept
name: Censoring
msc: [62N01, 62N02]
sources:
  - url: https://en.wikipedia.org/wiki/Censoring_(statistics)
same_as:
  wikidata: Q189813
  wikipedia: Censoring (statistics)
---

## Summary

Censoring is the situation in which the value of a measurement is only partly known.
One learns that it lies in some interval, but not its exact value.
The most common case is right censoring of event times, where one only knows that the event had not happened by the end of follow-up.
Ignoring censored observations, or treating them as exact, biases the estimates.
Methods of [[survival analysis|443ZWDX88P]], such as the [[Kaplan–Meier estimator|B7AJ8RWZRC]], are built to use censored data correctly.

## Explanations

### L1 human

A study of how long marriages last runs for ten years.
For couples still married at the end, we do not know the length of the marriage, only that it is more than their time in the study.
Such a record is censored on the right.
If a scale only reads up to $150$ kg, a reading of "over $150$" is censored in the same way.
If an infection is only detected at a check-up, we know it happened between two visits: that is interval censoring.
