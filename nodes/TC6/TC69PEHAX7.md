---
tag: TC69PEHAX7
kind: object
name: Universal Turing machine
msc: [03D10, 68Q04]
instance_of: [758EYCN27B]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_Turing_machine
same_as:
  wikidata: Q2703890
  wikipedia: Universal Turing machine
---

## Description

Fix an encoding $\langle M, w \rangle$ of a [[Turing machine|758EYCN27B]] $M$ together with an input word $w$ as a single word.
A *universal Turing machine* is a Turing machine $U$ with the following property for every machine $M$ and every input $w$.
The machine $U$ halts on $\langle M, w \rangle$ if and only if $M$ halts on $w$, and then $U$ produces the same output as $M$.
Alan Turing described such a machine in his paper of 1936.

## Remarks

The machine $U$ keeps the description of $M$ on its tape, and the current tape and state of $M$ beside it.
At each step it looks up the matching rule of $M$ in the description and updates the simulated configuration.
In terms of [[computable functions|KZSB5E471K]], it computes the universal function $(e, x) \mapsto \varphi_e(x)$, which is itself partial computable.
Universal machines are the theoretical model of the stored-program computer: one fixed machine runs any program given as data.

## Explanations

### L1 human

A universal Turing machine is a single machine that can imitate every other Turing machine.
You give it, as input, the rule table of another machine and the input for that machine.
It then does whatever that machine would do, step by step.
A modern computer running any program you load is the same idea.
