---
tag: NDC0E9BZ94
kind: concept
name: Finite-state machine
msc: [68Q45]
sources:
  - url: https://en.wikipedia.org/wiki/Finite-state_machine
same_as:
  wikidata: Q176452
  wikipedia: Finite-state machine
---

## Summary

A finite-state machine is an abstract machine that is in one of finitely many states at each moment.
It changes state each time it reads an input symbol.
With a set of accepting states it becomes a [[deterministic finite automaton|W65B6BKZRY]], which accepts or rejects words.
With an output function it becomes a [[Mealy machine|BDWD5J39DJ]] or a [[Moore machine|6VAZ66YNCA]], which translates input words into output words.
Finite-state machines are the simplest models of computation in [[automata theory|2ZSYVRGQ05]] and model many real devices, such as vending machines and network protocols.

## Explanations

### L1 human

Think of a turnstile.
It is either locked or unlocked, and these are its two states.
A coin moves it from locked to unlocked, and a push moves it from unlocked to locked.
A finite-state machine is any system of this kind: finitely many states, and a rule that says which state comes next for each input.
Its memory is only the current state, so it cannot count without bound.
