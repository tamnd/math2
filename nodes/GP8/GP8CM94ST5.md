---
tag: GP8CM94ST5
kind: concept
name: Optimal job scheduling
msc: [90B35, 68M20, 90C27]
specializes: [FJPER80BJC]
sources:
  - url: https://en.wikipedia.org/wiki/Optimal_job_scheduling
same_as:
  wikidata: Q7062516
  wikipedia: Optimal job scheduling
---

## Summary

Optimal job scheduling is a family of [[combinatorial optimization|FJPER80BJC]] problems.
Jobs must be assigned to machines and to time intervals so as to optimize an objective, such as the completion time of the last job.
The problems differ in the machine environment, in the constraints on the jobs, and in the objective.
They are classified by the three-field notation $\alpha \mid \beta \mid \gamma$ of Graham, Lawler, Lenstra and Rinnooy Kan.
Some cases have fast exact algorithms, while many others are [[NP-hard|MHA48AWBXN]] and are attacked by [[approximation algorithms|4WEVBDQ8SR]].

## Explanations

### L1 human

A print shop has several printers and a pile of print jobs, each needing a known time.
It must decide which printer handles which job and in what order.
One goal is to finish all jobs as early as possible; another is to keep the average waiting time of customers low.
For example, with one printer, doing short jobs first makes the average finishing time smallest.
