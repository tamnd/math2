---
tag: TQWGW9X8VF
kind: concept
name: Tree automaton
msc: [68Q45, 68Q42]
sources:
  - url: https://en.wikipedia.org/wiki/Tree_automaton
same_as:
  wikidata: Q2872598
  wikipedia: Tree automaton
---

## Summary

A tree automaton is a finite automaton that reads finite labelled trees, such as terms or syntax trees, instead of words.
A bottom-up tree automaton assigns states to the leaves, and then to each node from the states of its children.
It accepts when the root gets an accepting state.
The tree languages recognized in this way, the regular tree languages, keep most good properties of [[regular languages|18WVBDCS38]] of words.
Tree automata are used for XML schemas, term rewriting, program analysis and decision procedures in logic.

## Explanations

### L1 human

A word is a tree in which every node has at most one child, so tree automata generalize the [[finite automata|SFMYM96C1B]] that read words.
Think of evaluating an arithmetic or logical expression written as a tree: each leaf gets a value, and each inner node computes its value from its children.
A tree automaton does the same with finitely many possible "values", its states.
For example, it can check whether a Boolean expression built from $0$, $1$, $\land$ and $\lor$ evaluates to $1$.
