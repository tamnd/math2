---
tag: TAKA1DYBNE
kind: definition
name: Tautological one-form
msc: [53D05, 37J39]
defines: ADNHVGY2W4
uses: [F45VQ47GPV, 0E3G0GRPZ6, 6P9PXQDSEN, CAN490EPRT, 004FRCXH6M]
sources:
  - url: https://en.wikipedia.org/wiki/Tautological_one-form
---

## Definition

Let $Q$ be a [[smooth manifold|F45VQ47GPV]] with cotangent bundle $\pi \colon T^*Q \to Q$.
A point of $T^*Q$ is a pair $(q, p)$ with $q \in Q$ and $p \in T_q^* Q$.
The *tautological one-form* is the [[$1$-form|0E3G0GRPZ6]] $\theta$ on $T^*Q$ given by
$$\theta_{(q, p)}(v) = p\big(d\pi_{(q, p)}(v)\big) \quad \text{for } v \in T_{(q,p)}(T^*Q),$$
where $d\pi$ is the [[differential|6P9PXQDSEN]] of $\pi$.

## Remarks

In local coordinates $q^1, \ldots, q^n$ on $Q$ with the induced coordinates $p_1, \ldots, p_n$ on the fibres, $\theta = \sum_i p_i \, dq^i$.
The form $\omega = -d\theta = \sum_i dq^i \wedge dp_i$, with $d$ the [[exterior derivative|004FRCXH6M]], is the canonical [[symplectic form|CAN490EPRT]] of $T^*Q$; some authors use the opposite sign.

Characterization: for every $1$-form $\alpha$ on $Q$, viewed as a section $\alpha \colon Q \to T^*Q$, one has $\alpha^* \theta = \alpha$, and $\theta$ is the only $1$-form on $T^*Q$ with this property.

Example: for $Q = \R$ with coordinate $q$ and fibre coordinate $p$, $\theta = p\, dq$; for $\alpha = c\, dq$ the section is $q \mapsto (q, c)$ and $\alpha^*(p\, dq) = c\, dq = \alpha$.

Non-example: the form $q\, dp$ on $T^*\R$ is not the tautological form.
For the section $\alpha = dq$, that is $q \mapsto (q, 1)$, the pullback of $q\, dp$ is $q \cdot d(1) = 0 \ne dq$.
