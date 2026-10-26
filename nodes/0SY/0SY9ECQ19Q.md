---
tag: 0SY9ECQ19Q
kind: definition
name: Continuous map of topological spaces
aliases: [continuous-map, continuous-function]
msc: [54C05]
defines: 0VGFHTM75Y
uses: [0CNQXVBHCX, 01ZQQDCERP, 0FGCFY1AZX]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Continuous functions between topological spaces
---

## Definition

Let $(X, \tau_X)$ and $(Y, \tau_Y)$ be [[topological spaces|0CNQXVBHCX]] and let $f \colon X \to Y$ be a function.
The function $f$ is continuous when for each [[open set|01ZQQDCERP]] $V \in \tau_Y$, the [[preimage|0FGCFY1AZX]] $f^{-1}(V)$ is in $\tau_X$.

## Remarks

Equivalently, $f$ is continuous if and only if preimages of closed sets are closed, as in [[continuity via closed sets|0B8GPXFSP7]].
For metric spaces, this is the same as the epsilon-delta condition, by [[continuity via open sets|0YF82GBTND]].
A function is continuous if and only if it is [[continuous at each point|07N7W5C29X]].
Constant maps and identity maps are continuous, and the [[composition of continuous maps is continuous|05NK26G0DR]].

## Explanations

### L1 human

A continuous map does not tear the space apart: the points that go into an open set come from an open set.
This definition uses only open sets, so it works in each topological space.
