---
tag: P1ANHAY6XY
kind: concept
name: SIS and SEIR models
msc: [92D30, 34C60]
specializes: [BX5ZA16MM6]
sources:
  - url: https://en.wikipedia.org/wiki/Compartmental_models_(epidemiology)
---

## Summary

The SIS and SEIR models are two basic variants of the [[SIR model|J5FHBDJGJA]].
In the SIS model, infection gives no immunity, so recovered hosts become susceptible again and the disease can persist.
In the SEIR model, newly infected hosts pass through a latent, exposed stage before they become infectious.
SIS suits infections without lasting immunity, and SEIR suits infections with a marked latent period.

## Explanations

### L1 human

Some infections, like many colds, give no lasting protection, so a person goes from sick back to healthy but catchable: this is SIS.
Then the disease can settle at a steady level instead of dying out.
Other infections have a waiting period: a person is infected but cannot yet pass it on; this extra box E gives SEIR.
For example, with the same infection and recovery rates, an SEIR epidemic grows more slowly at first than an SIR epidemic, because of the waiting period.
