---
tag: PWSV93XK14
kind: concept
name: Similarity solution for the heat equation
msc: [35C06, 35K05, "80A19"]
specializes: [579J5K9K5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Self-similar_solution
---

## Summary

A similarity solution of the [[heat equation|VP2HN86VAG]] is a solution whose profile keeps its shape in time.
The profile only stretches like $\sqrt{t}$ and changes height like a power of $t$.
Up to a power of $t$, it depends on $x$ and $t$ only through the similarity variable $\eta = x / (2\sqrt{\alpha t})$.
The heat equation then becomes an ordinary differential equation in $\eta$.
The [[heat kernel|KD404MF042]] and the error function profiles of a suddenly heated half-space are the main examples.
It is the case of the heat equation of a general [[similarity solution|579J5K9K5Z]], and it also gives the classical Neumann solution of the [[Stefan problem|3B0HB3DHW1]].
See the [[definition|8BMDZWW2JM]].

## Explanations

### L1 human

When the surface of a cold wall is suddenly heated, the warm layer inside the wall grows thicker over time.
At time $4t$ the warm layer is twice as thick as at time $t$, but it has the same shape.
So one picture of the profile, drawn against $x / \sqrt{t}$, describes the whole history.
This is why the depth reached by heat grows like the square root of time.
For a half-space held at temperature $1$ on its surface and initially at $0$, the profile is $\operatorname{erfc}(x / (2\sqrt{\alpha t}))$.
