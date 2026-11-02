---
tag: ZZDMHH8V1K
kind: definition
name: Residue calculus for Laplace inversion
msc: [44A10, "30E20"]
defines: E14W2V09HM
uses: [0NSD1TPHR0, 0JFGKKWWFK, 032HKYS329, 9WRE8KEJJX, 05XT5AVJBK, 0JRW4X1MDC]
sources:
  - url: https://en.wikipedia.org/wiki/Residue_theorem
---

## Definition

Let $F$ be a [[meromorphic function|0NSD1TPHR0]] on $\C$ with finitely many poles $s_1, \ldots, s_n$.
Let $\gamma$ be a real number with $\gamma > \operatorname{Re} s_k$ for every $k$.
Assume that there are constants $C > 0$, $p > 0$ and $R_0 > 0$ with $\abs{F(s)} \le C \abs{s}^{-p}$ for all $s$ with $\abs{s} \ge R_0$ and $\operatorname{Re} s \le \gamma$.
*Residue calculus for Laplace inversion* is the evaluation, for $t > 0$, of the [[Bromwich integral|9WRE8KEJJX]] of $F$ along $\operatorname{Re} s = \gamma$ as
$$\frac{1}{2 \pi i} \int_{\gamma - i \infty}^{\gamma + i \infty} e^{s t} F(s) \, ds = \sum_{k=1}^{n} \operatorname{Res}_{s = s_k} \left( e^{s t} F(s) \right),$$
where $\operatorname{Res}$ is the [[residue|0JFGKKWWFK]].
Under these assumptions the identity holds for every $t > 0$.
Let $F$ also be the [[Laplace transform|05XT5AVJBK]] of a function $f$ as in Mellin's inverse formula.
Then the right side is the [[inverse Laplace transform|0JRW4X1MDC]] $f(t)$ at each $t > 0$ where $f$ is continuous.

## Remarks

The identity follows from the [[residue theorem|032HKYS329]] on the region bounded by the segment from $\gamma - i R$ to $\gamma + i R$ and a left arc of radius about $R$.
A Jordan-type estimate shows that the arc contributes $0$ in the limit when $t > 0$.
The hypotheses hold for every rational $F = P/Q$ with $\deg P < \deg Q$.
Example: $F(s) = 1/(s + 1)^2$ has one double pole, and $\operatorname{Res}_{s=-1} e^{s t}/(s+1)^2 = \frac{d}{ds} e^{s t} \big|_{s = -1} = t e^{-t}$.
Non-example: $F(s) = e^{-s}/s$ is not small on left arcs, because $\abs{e^{-s}} = e^{-\operatorname{Re} s}$ grows there.
The residue sum would give $1$ for all $t > 0$, while the true inverse is the delayed step $u(t - 1)$, which is $0$ for $0 < t < 1$.
Transforms that come from partial differential equations often have infinitely many poles.
For them one uses a sequence of contours that avoid the poles, and one gets a series over all poles.
