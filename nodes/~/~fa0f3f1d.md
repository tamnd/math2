---
tag: ~fa0f3f1d
kind: statement
role: proposition
name: Lipschitz maps are uniformly continuous
msc: [26A16]
uses: [~c2df23c9, ~eddf6490]
sources:
  - url: https://en.wikipedia.org/wiki/Lipschitz_continuity
    locator: Properties
---

## Statement

Let $X$ and $Y$ be [[metric spaces|~200ea42b]] and let $f \colon X \to Y$ be a [[Lipschitz map|~c2df23c9]].
Then $f$ is [[uniformly continuous|~eddf6490]].

## Remarks

Proof: let $K > 0$ be a Lipschitz constant of $f$. For $\varepsilon > 0$, take $\delta = \varepsilon / K$. If $d(x, y) < \delta$, then $d(f(x), f(y)) \le K d(x, y) < \varepsilon$. If $f$ is Lipschitz with $K = 0$, then $f$ is constant.
The converse fails: $x \mapsto \sqrt{x}$ on $[0, 1]$ is uniformly continuous, but it is not Lipschitz.
In particular, each Lipschitz map is continuous.

## Explanations

### L1 human

For a Lipschitz map, you can give an explicit $\delta$ for each $\varepsilon$: divide $\varepsilon$ by the constant $K$.
This $\delta$ does not depend on the point, so the map is uniformly continuous.
