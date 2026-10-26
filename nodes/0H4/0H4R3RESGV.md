---
tag: 0H4R3RESGV
kind: definition
name: Limit inferior
aliases: [liminf]
msc: [40A05]
defines: 033RZ32T4Q
uses: [05FQ3VGAR9]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_inferior_and_limit_superior
    locator: The case of sequences of real numbers
---

## Definition

Let $(a_n)$ be a [[bounded sequence|05FQ3VGAR9]] of real numbers.
For each $n \in \mathbb{N}$, let $i_n = \inf \{a_k : k \ge n\}$.
The sequence $(i_n)$ is increasing and bounded above.
The limit inferior of $(a_n)$ is
$$\liminf_{n \to \infty} a_n = \lim_{n \to \infty} i_n = \sup_{n \in \mathbb{N}} \inf_{k \ge n} a_k.$$

## Remarks

The limit exists by the [[monotone convergence theorem|0FM6N4R0VB]].
It satisfies $\liminf a_n = -\limsup (-a_n)$, where $\limsup$ is the [[limit superior|0P8BA7T7S5]].
Always $\inf_n a_n \le \liminf a_n \le \limsup a_n \le \sup_n a_n$.
For $a_n = (-1)^n$, the limit inferior is $-1$ and the limit superior is $1$.

## Explanations

### L1 human

The limit inferior is the lowest value that the sequence keeps coming back to, in the long run.
Each number below it is undercut by only finitely many terms.
