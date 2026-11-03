---
tag: X8W326RJCW
kind: definition
name: Turing completeness
msc: [68Q04, 03D10]
defines: JE3PC89MVM
uses: [HGV3FGKAVX, W6ESDYBF8Z, KZSB5E471K]
sources:
  - url: https://en.wikipedia.org/wiki/Turing_completeness
---

## Definition

Let $\mathcal M$ be a deterministic [[model of computation|HGV3FGKAVX]] over an alphabet $\Sigma$, whose machines compute partial functions $\Sigma^* \rightharpoonup \Sigma^*$.
For each [[Turing machine|W6ESDYBF8Z]] alphabet, fix a total [[computable|KZSB5E471K]] injective map that codes its strings as strings over $\Sigma$.
A machine $M \in \mathcal M$ *simulates* a Turing machine $T$ if two conditions hold for every input $w$ of $T$.

1. $M$ halts on the code of $w$ exactly when $T$ halts on $w$.
2. When both halt, the output of $M$ is the code of the output of $T$.

The model $\mathcal M$ is *Turing complete* if every Turing machine is simulated by some machine of $\mathcal M$.
It is *Turing equivalent* if it is Turing complete and, conversely, every machine of $\mathcal M$ is simulated in the same sense by some Turing machine.

## Remarks

Example: [[register machines|BSPVYC28BY]] are Turing equivalent, with numbers coded in a register and strings coded as numbers.
Every Turing machine can be simulated by a register machine program, and every register machine can be simulated by a Turing machine that keeps the registers on its tape.
Non-example: deterministic finite automata are not Turing complete.
Their output on an input is only accept or reject, and they recognise only regular languages, so no automaton recognises the language $\set{a^n b^n : n \ge 0}$, which a Turing machine decides.
For most models one may take the codes to be very simple, and the notion does not depend on the choice of reasonable codes.
The term is also used for programming languages and other systems that are not formal models; there it is an informal notion.
