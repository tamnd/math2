---
tag: CGEPN90SDZ
kind: example
name: Infinitary sentences whose largest models have size beth-alpha
msc: ["03C55", "03C75"]
topics: [W9CHA4PD9H]
audience: research
not_instance_of:
  - target: A9XBRF3A7Z
    note: "for each countable ordinal alpha, beth_alpha is not the Hanf number of L_omega1omega, since phi_alpha has a model of size beth_alpha and no larger model"
uses: [A9XBRF3A7Z, PQG7VAZ1R2, ZC4BHVHWE9, 0YSCSX5YZC, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Beth_number
    locator: lead section
  - book: isbn:9780486488219
    locator: Chapter 7
---

## Example

Fix a countable [[ordinal|0YSCSX5YZC]] $\alpha$.
Let $L_\alpha$ have constants $c_n$ for $n \in \N$, a binary symbol $E$, and unary symbols $P_\beta$ for $\beta \le \alpha$.
Let $\varphi_\alpha$ be the conjunction of the following sentences of the [[infinitary logic|PQG7VAZ1R2]] $L_{\omega_1\omega}$:

- (a) $c_m \ne c_n$ for $m \ne n$, and $\forall x \, (P_0(x) \leftrightarrow \bigvee_n x = c_n)$;
- (b) $\forall x \, (P_\beta(x) \to P_\gamma(x))$ for $\beta \le \gamma \le \alpha$, and $\forall x \, P_\alpha(x)$;
- (c) for $\beta + 1 \le \alpha$: two elements of $P_{\beta+1}$ with the same $E$-predecessors in $P_\beta$ are equal;
- (d) for limit $\delta \le \alpha$: $\forall x \, (P_\delta(x) \to \bigvee_{\beta < \delta} P_\beta(x))$, a countable disjunction.

We show that $\varphi_\alpha$ has a model of size $\beth_\alpha$ and no larger model, so $\beth_\alpha$ is not the [[Hanf number|A9XBRF3A7Z]] of $L_{\omega_1\omega}$.

1. Upper bound, by [[induction|0ASJVEFA9J]] on $\beta \le \alpha$: in a model $\mathcal{M}$, $\abs{P_\beta} \le \beth_\beta$. For $\beta = 0$, (a) gives $\abs{P_0} = \aleph_0 = \beth_0$.
2. For $\beta + 1$: by (c), $x \mapsto \set{z \in P_\beta : z E x}$ is injective on $P_{\beta+1}$, so $\abs{P_{\beta+1}} \le 2^{\beth_\beta} = \beth_{\beta+1}$.
3. For a limit $\delta$: by (d), $P_\delta = \bigcup_{\beta < \delta} P_\beta$, so $\abs{P_\delta} \le \sum_{\beta < \delta} \beth_\beta = \beth_\delta$.
4. By (b), $M = P_\alpha$, so $\abs{M} \le \beth_\alpha$.
5. A model of size $\beth_\alpha$: take $M = V_{\omega + \alpha}$, $P_\beta = V_{\omega + \beta}$, $E$ the membership relation, and $c_n$ an enumeration of the countable set $V_\omega$.
6. Then (a), (b) and (d) hold by the definition of the levels $V_\gamma$, and (c) holds since a set is determined by its members. By the [[beth numbers|ZC4BHVHWE9]], $\abs{V_{\omega+\alpha}} = \beth_\alpha$.

## Remarks

The example shows that the Hanf number of $L_{\omega_1\omega}$ is at least $\sup_{\alpha < \omega_1} \beth_\alpha = \beth_{\omega_1}$.
Indeed, a cardinal $\kappa < \beth_{\omega_1}$ is below some $\beth_\alpha$, and $\varphi_\alpha$ has a model of size at least $\kappa$ but no arbitrarily large models.
Together with Morley's upper bound this gives the value $\beth_{\omega_1}$; see [[this example|QC25K2Y91B]].
For $\alpha = 0$ the sentence says that every element is one of the constants, and its models are countable.
The example needs countable disjunctions only in (a) and (d); for an uncountable $\alpha$ the disjunction in (d) would be uncountable, so the sentence leaves $L_{\omega_1\omega}$.
In first-order logic, (a) and (d) cannot be expressed, and indeed no first-order sentence bounds the size of its infinite models.

## Explanations

### L1 human

Start with a countable set of points.
At the next level, allow every set of points from the level below as a new point: this gives at most $2^{\aleph_0}$ points.
Repeat this, level after level, countably many times.
The sentence describes such a tower with a fixed countable height, and so the tower cannot be larger than a certain size, but it can reach that size.

### L2 human

We compute the bound for $\alpha = 2$.

1. Condition (a) gives $\abs{P_0} = \aleph_0$.
2. Condition (c) with $\beta = 0$ gives $\abs{P_1} \le 2^{\aleph_0} = \beth_1$.
3. Condition (c) with $\beta = 1$ gives $\abs{P_2} \le 2^{\beth_1} = \beth_2$, and (b) gives $M = P_2$.
4. The model $V_{\omega + 2}$ is the set of all sets of subsets of $V_\omega$, and it has size $\beth_2$.

The typical use is to show that a bound for $L_{\omega_1\omega}$ cannot be below $\beth_{\omega_1}$.
The trap is to forget condition (d) at limit levels: without it, $P_\omega$ could contain new elements that are not determined by the lower levels.
