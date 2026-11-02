---
tag: 3TGTNRBKW0
kind: definition
name: Hopf module
msc: [16T05]
defines: N8X7XJBKT0
uses: [7XFYP0N84H, 0NZ8JA25WK, 7WEM2E6RTV, NC26CE0Y8B]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_algebra
---

## Definition

Let $K$ be a field and let $H$ be a [[Hopf algebra|7XFYP0N84H]] over $K$ with comultiplication $\Delta$.
A *right Hopf module* over $H$ is a vector space $M$ over $K$ such that:

1. $M$ is a right $H$-[[module|0NZ8JA25WK]], with action $m \otimes h \mapsto m \cdot h$.
2. $M$ is a right $H$-[[comodule|7WEM2E6RTV]], with coaction $\rho \colon M \to M \otimes H$.
3. For all $m \in M$ and $h \in H$, in [[Sweedler notation|NC26CE0Y8B]],
$$\rho(m \cdot h) = \sum m_{(0)} \cdot h_{(1)} \otimes m_{(1)} h_{(2)}.$$

The *coinvariants* of $M$ are the elements of $M^{\mathrm{co}H} = \set{m \in M : \rho(m) = m \otimes 1}$.

## Remarks

Clause 3 says that $\rho$ is a module map when $M \otimes H$ carries the action $(m \otimes x) \cdot h = \sum m \cdot h_{(1)} \otimes x h_{(2)}$.
Example: for a vector space $V$, the space $M = V \otimes H$ with $(v \otimes x) \cdot h = v \otimes xh$ and $\rho(v \otimes x) = \sum v \otimes x_{(1)} \otimes x_{(2)}$.
Clause 3 holds because $\Delta(xh) = \Delta(x)\Delta(h)$.
Non-example: $H = KG$ for a group $G \ne 1$, acting on itself by multiplication, with the coaction $\rho(x) = x \otimes 1$.
This is a module and a comodule, but for $g \ne 1$ in $G$, $\rho(1 \cdot g) = g \otimes 1$ while the right side of clause 3 is $g \otimes g$.
The fundamental theorem of Hopf modules states that the map $M^{\mathrm{co}H} \otimes H \to M$, $m \otimes h \mapsto m \cdot h$, is an isomorphism of Hopf modules.
