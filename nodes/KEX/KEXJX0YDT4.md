---
tag: KEXJX0YDT4
kind: problem
name: Zermelo's navigation problem
msc: [49K15, 49N90, 93C15]
uses: [YTR959CYMX, 7RPV2T29CF, 0NT64JV96A]
about: [T3V6ZNAMDN]
sources:
  - url: https://en.wikipedia.org/wiki/Zermelo%27s_navigation_problem
same_as:
  wikidata: Q28134370
  wikipedia: Zermelo's navigation problem
history:
  posed_by: "Ernst Zermelo"
  first_stated: "1931"
---

## Problem

A boat moves in the plane with constant speed $V > 0$ relative to the water.
The water moves with a velocity field $w = (w_1, w_2) \colon \R^2 \to \R^2$ of class $C^1$ with $\abs{w} < V$ everywhere.
The captain controls the heading $\theta(t)$, so that the position $(x(t), y(t))$ obeys the [[ordinary differential equations|0NT64JV96A]]
$$x' = V \cos \theta + w_1(x, y), \qquad y' = V \sin \theta + w_2(x, y).$$
Given two points $P$ and $Q$, find a heading $t \mapsto \theta(t)$ that brings the boat from $P$ to $Q$ in the least time.

## Remarks

It is a [[time-optimal control|YTR959CYMX]] problem, and the [[Pontryagin maximum principle|7RPV2T29CF]] gives necessary conditions on optimal headings.
Zermelo derived a differential equation for the optimal heading along the path, known as Zermelo's navigation formula.
For a constant current $w$, the optimal heading is constant and the boat moves along the straight segment from $P$ to $Q$.
One aims so that the sum of $V(\cos\theta, \sin\theta)$ and $w$ points from $P$ to $Q$.
The condition $\abs{w} < V$ ensures that the boat can make headway in every direction.

## Explanations

### L1 human

A boat crosses a river or a sea with currents, and the captain wants to arrive as soon as possible.
Pointing straight at the target is not best, because the current pushes the boat off course.
The problem asks how to steer at each moment, and it is one of the first problems of optimal control.
