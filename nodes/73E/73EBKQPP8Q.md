---
tag: 73EBKQPP8Q
kind: example
name: Hawaiian earring
msc: [55Q52, 54G20]
uses: [060W5CBZP6, 0TVJZYB6SH, 0WB6DH499T]
sources:
  - url: https://en.wikipedia.org/wiki/Hawaiian_earring
---

## Example

For $n \ge 1$ let $C_n \subseteq \R^2$ be the [[circle|060W5CBZP6]] with centre $(1/n, 0)$ and radius $1/n$.
The Hawaiian earring is $H = \bigcup_{n \ge 1} C_n$ with the subspace topology from $\R^2$.
All circles pass through the origin $0$.
The space $H$ is [[compact|0TVJZYB6SH]] and [[path-connected|0WB6DH499T]], but it is not semilocally simply connected at $0$.

Check.
$H$ is closed and bounded in $\R^2$, so it is compact.
Each $C_n$ is path-connected and contains $0$, so $H$ is path-connected.
Fix $n$ and let $r_n \colon H \to C_n$ be the identity on $C_n$ and send every other circle to $0$.
This map is continuous, and it is a retraction onto $C_n$.
Let $\gamma_n$ be the loop that goes once around $C_n$.
The map $r_n$ sends it to a generator of the fundamental group $\pi_1(C_n) \cong \Z$, so $\gamma_n$ is not null-homotopic in $H$.
Every neighbourhood of $0$ contains $C_n$ for all large $n$, so it contains loops at $0$ that are not null-homotopic in $H$.

## Remarks

Since $H$ is not semilocally simply connected, it has no universal covering space.
The retractions $r_n$ together give a homomorphism from $\pi_1(H, 0)$ onto the product $\prod_{n \ge 1} \Z$.
It is onto: a loop can run $k_n$ times around $C_n$ during the time interval $[1 - 2^{1-n}, 1 - 2^{-n}]$.
This loop is continuous at time $1$ because the circles shrink.
So $\pi_1(H, 0)$ is uncountable.
The wedge sum of countably many circles, with the CW topology, has a countable free fundamental group and is not homeomorphic to $H$.

## Explanations

### L1 human

The Hawaiian earring is an infinite family of circles in the plane, all touching at one point and getting smaller and smaller.
It looks like a bouquet of circles, but the small circles crowd near the common point.
However close you look at that point, you still see whole circles there that cannot be shrunk away.
This makes its loops far more complicated than those of a finite bouquet.
