---
tag: 1VXZHAHT6K
kind: concept
name: CUSUM
msc: [62L10, 62P30]
sources:
  - url: https://en.wikipedia.org/wiki/CUSUM
same_as:
  wikidata: Q1024555
  wikipedia: CUSUM
---

## Summary

CUSUM, short for cumulative sum, is a sequential procedure for detecting a change in the distribution of a stream of observations.
It adds up evidence for a change and resets the sum to zero whenever it becomes negative.
It raises an alarm when the sum crosses a threshold.
E. S. Page introduced it in 1954, and it is the standard solution of the [[change detection|Z5H8ZZHVMC]] problem in quality control.

## Explanations

### L1 human

Picture a machine that fills bottles with $500$ ml on average, and suppose a fault would raise the average.
After each bottle, add how much it exceeds $500$ ml plus a small allowance, and subtract when it falls short, but never let the running total go below zero.
While the machine is fine, the total keeps hitting zero and stays small.
After a fault, the excesses pile up and the total soon crosses the alarm level.
