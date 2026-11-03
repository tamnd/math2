---
tag: 42KFAMMBE8
kind: definition
name: Birth–death model of speciation
msc: [92D15, 60J80, 60J85]
defines: 48CJCBEK92
uses: [E8DAD7052E, 0E99F51GVB, TWQFE0FZZS, RK58WSHJSG]
sources:
  - url: https://en.wikipedia.org/wiki/Birth–death_process
---

## Definition

Let $\lambda > 0$ and $\mu \ge 0$.
The *birth–death model of speciation* with speciation rate $\lambda$ and extinction rate $\mu$ is the following random process of lineages in continuous time.
Each living lineage, independently of the others, waits an [[exponentially distributed|0E99F51GVB]] time with rate $\lambda + \mu$.
At the end of this time it splits into two lineages with probability $\lambda/(\lambda + \mu)$, and it goes extinct with probability $\mu/(\lambda + \mu)$.

## Remarks

The number $N(t)$ of living lineages at time $t$ is a linear [[birth–death process|E8DAD7052E]].
This is the [[continuous-time Markov chain|TWQFE0FZZS]] on $\set{0, 1, 2, \dots}$ with birth rate $\lambda n$ and death rate $\mu n$ in state $n$.
Its mean is $\mathbb{E}[N(t)] = N(0) e^{(\lambda - \mu) t}$.
Starting from one lineage, the probability of eventual extinction is $1$ if $\lambda \le \mu$ and $\mu/\lambda$ if $\lambda > \mu$.
Example: the case $\mu = 0$ is the Yule model, in which lineages only split; then $N(t)$ is a pure birth process and $\mathbb{E}[N(t)] = N(0) e^{\lambda t}$.
Non-example: a model whose speciation rate depends on the total number of lineages, as in diversity-dependent models, is not of this form, because the lineages are not independent.
The tree of lineages that survive to the present, with extinct branches removed, is called the reconstructed tree; it is the object compared with [[phylogenetic trees|RK58WSHJSG]] estimated from data.
