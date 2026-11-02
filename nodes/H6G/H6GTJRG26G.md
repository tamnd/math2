---
tag: H6GTJRG26G
kind: concept
name: Weak lower semicontinuity
msc: [49J45, "58E30"]
specializes: [RN4G8SGP6P]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_method_in_the_calculus_of_variations
---

## Summary

A functional on a Banach space is weakly lower semicontinuous if it cannot jump up in a weak limit.
That is, $J(u) \le \liminf_k J(u_k)$ whenever $u_k \to u$ weakly.
It is [[semicontinuity|RN4G8SGP6P]] with respect to the [[weak topology|P6KHVSTPZV]], usually in its sequential form.
Together with coercivity it is the main hypothesis of the [[direct method|TE379HBTY0]].
For integral functionals it is closely tied to convexity of the integrand in the gradient variable.

## Explanations

### L1 human

Weak convergence allows a sequence to oscillate faster and faster while its average settles down.
The functions $\sin(kx)$ on $[0, 2\pi]$ converge weakly to $0$, even though their size does not shrink.
A weakly lower semicontinuous energy may lose value in such a limit, but it cannot gain value.
The norm itself is a typical example: the limit $0$ has norm $0$, below the norms of $\sin(kx)$.
