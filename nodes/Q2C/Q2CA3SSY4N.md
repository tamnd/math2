---
tag: Q2CA3SSY4N
kind: definition
name: Time complexity
msc: [68Q25, 68Q15, 68W40]
defines: T00W8RQT8E
uses: [758EYCN27B, YK3HD56R3G, P74SXXT7DX, 1P6EP01HZF, 0TGV80E6A4]
sources:
  - url: https://en.wikipedia.org/wiki/Time_complexity
---

## Definition

Let $M$ be a deterministic [[multitape Turing machine|YK3HD56R3G]] with input alphabet $\Sigma$ that halts on every input.
The *running time*, or *time complexity*, of $M$ is the function $t_M \colon \N \to \N$ given by
$$t_M(n) = \max \set{\text{number of steps of } M \text{ on input } w : w \in \Sigma^*, \ \abs{w} = n},$$
where $\abs{w}$ is the length of the [[string|1P6EP01HZF]] $w$.
For a function $f \colon \N \to \N$, $\mathrm{DTIME}(f(n))$ is the class of [[languages decided|P74SXXT7DX]] by some such machine $M$ with $t_M(n) = O(f(n))$, in [[big O notation|0TGV80E6A4]].

## Remarks

Example: the language $\set{0^k 1^k : k \ge 0}$ is in $\mathrm{DTIME}(n)$.
A two-tape machine checks that the input has the form $0^* 1^*$ and copies the $0$s to its second tape.
Then it crosses off one of them for each $1$, so it uses $O(n)$ steps.
On a single-tape [[Turing machine|758EYCN27B]] this language can be decided in time $O(n \log n)$ but not in time $O(n)$.
In fact every language decided by a single-tape machine in time $o(n \log n)$ is regular.
Non-example: a machine that does not halt on some input has no time complexity in this sense.
The same definitions apply to other models, such as random-access machines, where each instruction counts as one step.
