---
tag: K8BK5SKY1Y
kind: definition
name: j-invariant
msc: [11F03, 14H52]
defines: FEC2XH822R
uses: [EYREVY31BN, A50Y012RBP, X6XGGH5FPW, VEKV1EM77B, 0ZZ7ZYDR8W]
sources:
  - url: https://en.wikipedia.org/wiki/J-invariant
---

## Definition

Let $\mathbb{H}$ be the [[upper half-plane|X6XGGH5FPW]], let $E_4$ and $E_6$ be the normalized [[Eisenstein series|EYREVY31BN]] of weights $4$ and $6$, and let $\Delta = (E_4^3 - E_6^2)/1728$.
The *$j$-invariant* is the function $j \colon \mathbb{H} \to \C$ given by
$$j(\tau) = \frac{E_4(\tau)^3}{\Delta(\tau)} = \frac{1728\, E_4(\tau)^3}{E_4(\tau)^3 - E_6(\tau)^2}.$$

## Remarks

The [[cusp form|A50Y012RBP]] $\Delta$ has no zeros on $\mathbb{H}$, so $j$ is holomorphic on $\mathbb{H}$.
Both $E_4^3$ and $\Delta$ have weight $12$, so $j(\gamma \tau) = j(\tau)$ for every $\gamma$ in the [[modular group|VEKV1EM77B]].
With $q = e^{2 \pi i \tau}$, $j(\tau) = q^{-1} + 744 + 196884 q + \cdots$, so $j$ is a [[meromorphic|0ZZ7ZYDR8W]] modular function with a simple pole at infinity.
Example: $E_6(i) = 0$, so $j(i) = 1728$; and $E_4(e^{2 \pi i/3}) = 0$, so $j(e^{2 \pi i /3}) = 0$.
Non-example: $j$ is not a [[modular form|GWKN5VG78A]] of weight $0$, because it is unbounded as $\operatorname{Im} \tau \to \infty$.
For the elliptic curve $y^2 = x^3 + ax + b$, the $j$-invariant is $1728 \cdot 4a^3 / (4a^3 + 27b^2)$.
