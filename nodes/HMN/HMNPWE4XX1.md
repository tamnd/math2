---
tag: HMNPWE4XX1
kind: definition
name: q-ary entropy function
msc: [94A17, 94B65]
defines: 95CYGNRQQ6
uses: [GW25TGD33J, Y86E072V0V]
sources:
  - url: https://en.wikipedia.org/wiki/Entropy_(information_theory)
---

## Definition

Let $q \ge 2$ be an integer.
The *$q$-ary entropy function* is the function $H_q \colon [0, 1] \to \R$ given by
$$H_q(x) = x \log_q (q - 1) - x \log_q x - (1 - x) \log_q (1 - x),$$
with the convention $0 \log_q 0 = 0$.

## Remarks

For $q = 2$ the first term vanishes, and $H_2$ is the [[binary entropy function|GW25TGD33J]].
In general $H_q(x) = x \log_q (q - 1) + H_2(x) / \log_2 q$.
$H_q(x)$ is the [[Shannon entropy|Y86E072V0V]] in base $q$ of the law on $q$ letters that gives mass $1 - x$ to one letter and mass $x / (q - 1)$ to each other letter.

Example: for $q = 3$ and $x = \frac23$, each of the three letters has mass $\frac13$, and indeed $H_3(\frac23) = \frac23 \log_3 2 - \frac23 \log_3 \frac23 - \frac13 \log_3 \frac13 = \frac23 \log_3 2 - \frac23 \log_3 2 + \frac23 + \frac13 = 1$.

Non-example: for $q = 1$ the formula breaks down, since $\log_1$ is not defined; the definition needs $q \ge 2$.

$H_q$ is continuous and concave on $[0, 1]$, increasing on $[0, 1 - 1/q]$, and its maximum is $H_q(1 - 1/q) = 1$.
Some authors use the natural logarithm, giving $x \ln(q - 1) - x \ln x - (1 - x) \ln(1 - x)$; this is `Real.qaryEntropy` in Mathlib.

## Explanations

### L1 human

It is the binary entropy function with an extra term $x \log_q (q - 1)$ that counts which of the $q - 1$ wrong letters appears.
