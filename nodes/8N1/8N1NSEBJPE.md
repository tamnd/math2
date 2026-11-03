---
tag: 8N1NSEBJPE
kind: concept
name: Signal detection theory
msc: ["91E30", 62P15]
sources:
  - url: https://en.wikipedia.org/wiki/Detection_theory
same_as:
  wikidata: Q120811
  wikipedia: Detection theory
---

## Summary

Signal detection theory models how an observer decides whether a weak signal is present in noise.
It separates two things that a raw percentage of correct answers mixes up.
The sensitivity says how well the observer tells signal from noise.
The response bias says how willing the observer is to say "yes".
In the standard model the internal evidence is normally distributed, sensitivity is the index $d'$ and bias is a decision criterion.
The theory is used in psychophysics, medical diagnosis, radar and the evaluation of classifiers.

## Explanations

### L1 human

A radiologist looks at a scan and must say whether a tumour is there.
Some scans without a tumour look suspicious, and some scans with a tumour look clean, so mistakes are unavoidable.
A cautious doctor says "yes" often, catching more tumours but raising more false alarms; a strict doctor does the opposite.
Signal detection theory measures the skill of the doctor in a way that does not depend on this choice of caution.
For example, a hit rate of $84\%$ with a false alarm rate of $16\%$ corresponds to $d' \approx 2$.
