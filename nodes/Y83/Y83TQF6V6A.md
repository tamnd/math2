---
tag: Y83TQF6V6A
kind: concept
name: Rewriting system
msc: [68Q42, 03D03]
sources:
  - url: https://en.wikipedia.org/wiki/Rewriting
---

## Summary

A rewriting system is a set of objects together with one-step rewriting moves between them.
In its abstract form it is just a set with a [[binary relation|05AVARPXA2]], read as "may be rewritten to".
String rewriting systems, [[term rewriting systems|A6J731Y193]] and the reduction of lambda terms are concrete instances.
The main questions are whether rewriting always stops and whether the final result is independent of the choices made.
Together these two properties give unique normal forms.

## Explanations

### L1 human

A rewriting system is a list of simplification steps that may be applied in any order.
For example, in arithmetic one may replace $2 + 3$ by $5$ wherever it occurs.
An object that cannot be simplified further is called a normal form.
Over the letters $a, b$ with the single rule $ba \to ab$, the word $baba$ rewrites to $abba$, then $abab$, then $aabb$, which is a normal form.
