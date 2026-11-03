---
tag: YK3HD56R3G
kind: concept
name: Multitape Turing machine
msc: [68Q04, 03D10]
specializes: [YFHEG4GYHW]
sources:
  - url: https://en.wikipedia.org/wiki/Multitape_Turing_machine
same_as:
  wikidata: Q1392048
  wikipedia: Multitape Turing machine
---

## Summary

A multitape Turing machine is a [[Turing machine|758EYCN27B]] with a fixed number $k \ge 1$ of tapes, each with its own head.
In one step it reads the $k$ symbols under the heads, writes on each tape and moves each head on its own.
It computes the same functions as a one-tape machine, but often faster, so it is the usual model for measuring time complexity.
A one-tape machine can simulate $t$ steps of a $k$-tape machine in $O(t^2)$ steps.

## Explanations

### L1 human

Think of a clerk with several notebooks open at once, with a finger on one line of each.
At each step the clerk looks at all the fingers, writes in every notebook, and moves each finger as needed.
With one notebook, the clerk would have to flip back and forth a lot to do the same work.
For example, to check that a word is a palindrome, the clerk copies it into a second notebook and then reads the two copies in opposite directions.
This takes a number of steps proportional to the length of the word.
