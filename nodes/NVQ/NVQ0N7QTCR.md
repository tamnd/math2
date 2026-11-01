---
tag: NVQ0N7QTCR
kind: definition
name: Transcendence degree
msc: [12F20]
defines: D7TR0YWR9H
uses: [0WQ1A8SHTZ, E45PA267S4, W635VBXEXG, 0JTGRV4WT4, 09EYMKMSB9, 08ZDRN6H41]
sources:
  - url: https://en.wikipedia.org/wiki/Transcendental_extension
---

## Definition

Let $L/K$ be a [[field extension|0WQ1A8SHTZ]].
The *transcendence degree* of $L/K$, written $\operatorname{trdeg}_K L$, is the [[cardinality|0JTGRV4WT4]] of a [[transcendence basis|E45PA267S4]] of $L/K$.

## Remarks

The definition makes sense because [[a transcendence basis exists|W635VBXEXG]] and any two transcendence bases have the same cardinality; the proof uses an exchange argument like the [[Steinitz exchange lemma|08ZDRN6H41]].
Example: $\operatorname{trdeg}_K K(x_1, \dots, x_n) = n$, with transcendence basis $\set{x_1, \dots, x_n}$.
Example: $\operatorname{trdeg}_\Q \R$ is the cardinality of the continuum, since $\R$ is uncountable and the algebraic closure of a countable field is countable.
Non-example: for $L = \Q(\pi, \pi^2)$, the transcendence degree over $\Q$ is $1$, not $2$, because $\set{\pi, \pi^2}$ is dependent and $\set{\pi}$ is a transcendence basis.
It is additive in towers: $\operatorname{trdeg}_K M = \operatorname{trdeg}_L M + \operatorname{trdeg}_K L$ for $K \subseteq L \subseteq M$.
The transcendence degree is $0$ if and only if the extension is [[algebraic|09EYMKMSB9]].
