---
tag: TZ1N0HAGW7
kind: concept
name: Neville theta functions
msc: ["33E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Neville_theta_functions
same_as:
  wikidata: Q19514367
  wikipedia: Neville theta functions
---

## Summary

The Neville theta functions $\theta_s$, $\theta_c$, $\theta_d$, $\theta_n$ are rescaled Jacobi [[theta functions|2F5CYQJVAF]].
Their argument is the argument $u$ of the [[Jacobi elliptic functions|P071B692JF]].
With this normalisation the Jacobi functions are simple quotients: $\operatorname{sn} = \theta_s/\theta_n$, $\operatorname{cn} = \theta_c/\theta_n$ and $\operatorname{dn} = \theta_d/\theta_n$.
The letters $s, c, d, n$ match the letters in the names of the twelve Jacobi functions, so any Jacobi function $\operatorname{pq}$ is $\theta_p/\theta_q$.

## Explanations

### L1 human

Theta functions are fast-converging series, and the Jacobi elliptic functions are ratios of them.
In the classical form the theta functions use a rescaled angle $\pi u/(2K)$ and carry awkward constant factors.
Neville chose the scaling so that the constants disappear from the ratios.
Then, for example, $\operatorname{sd} u = \theta_s(u)/\theta_d(u)$, read directly from the letters.
