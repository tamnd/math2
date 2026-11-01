---
tag: ZWJ9G89W3T
kind: definition
name: Local martingale
msc: [60G44, 60G48]
defines: XC2YPC2BSW
uses: [HNK1Y62G7V, YRNFE016FF, WND87FBAKC, NG35MGYDZR, 0CDVK9RQBH]
sources:
  - url: https://en.wikipedia.org/wiki/Local_martingale
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a probability space with a [[filtration|HNK1Y62G7V]] $(\mathcal{F}_t)_{t \ge 0}$.
Let $(X_t)_{t \ge 0}$ be a real [[adapted|YRNFE016FF]] process with càdlàg paths.
$X$ is a *local martingale* if there is a sequence $(\tau_n)_{n \ge 1}$ of [[stopping times|WND87FBAKC]] such that:

1. $\tau_1 \le \tau_2 \le \dots$ almost surely.
2. $\tau_n \to \infty$ almost surely as $n \to \infty$.
3. For each $n$, the [[stopped process|NG35MGYDZR]] $X^{\tau_n} = (X_{t \wedge \tau_n})_{t \ge 0}$ is a [[martingale|0CDVK9RQBH]].

Such a sequence $(\tau_n)$ is called a localising sequence.

## Remarks

Every càdlàg martingale $X$ is a local martingale: take $\tau_n = n$, since a stopped martingale is a martingale by optional stopping.
The deterministic process $X_t = t$ is adapted and continuous but is not a local martingale.
Indeed, clause 3 would give $E[t \wedge \tau_n] = 0$ for all $t$, so $\tau_n = 0$ almost surely, contradicting clause 2.
A local martingale need not be a martingale: if $B$ is a three-dimensional Brownian motion started at $x \ne 0$, then $1/\abs{B_t}$ is a local martingale but not a martingale.
A non-negative local martingale is a [[supermartingale|KYW1PV0SX5]], by Fatou's lemma.
Some authors require clause 3 only for $X^{\tau_n} - X_0$, or for $X^{\tau_n} \mathbf{1}\{\tau_n > 0\}$, so that $X_0$ need not be integrable.
