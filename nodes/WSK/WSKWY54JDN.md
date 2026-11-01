---
tag: WSKWY54JDN
kind: example
name: Menger sponge
msc: [54F15, 28A80, 54F50]
instance_of: [NJQ196M1WR]
uses: [0TVJZYB6SH, 0V032VWTHD, A3W7RGXXK9, PCM3H6J3EE]
sources:
  - url: https://en.wikipedia.org/wiki/Menger_sponge
same_as:
  wikidata: Q749773
  wikipedia: Menger sponge
---

## Example

Let $M_0 = [0, 1]^3$.
Divide each cube of side $3^{-k}$ in $M_k$ into $27$ equal cubes of side $3^{-k-1}$.
Remove the interiors of the central cube and of the $6$ cubes that share a face with it.
The union of the other $20$ cubes is $M_{k+1}$.
The *Menger sponge* is $M = \bigcap_{k \ge 0} M_k$.

The set $M$ is a [[continuum|NJQ196M1WR]].
Each $M_k$ is a finite union of closed cubes, so it is [[compact|0TVJZYB6SH]].
It is [[connected|0V032VWTHD]]: the $20$ kept cubes in each divided cube are the $12$ edge cubes and $8$ corner cubes, which form a connected frame.
A decreasing intersection of nonempty compact connected sets is nonempty, compact and connected.

## Remarks

The set $M_k$ has volume $(20/27)^k$, so $M$ has volume $0$.
Its Hausdorff dimension is $\log 20 / \log 3 \approx 2.727$.
Its [[Lebesgue covering dimension|A3W7RGXXK9]] is $1$, so topologically it is a curve.
Each face of the cube meets $M$ in a [[Sierpiński carpet|PCM3H6J3EE]].
Menger showed that every compact metric space of dimension at most $1$ embeds in $M$, so $M$ is a universal curve.

## Explanations

### L1 human

Take a cube, cut it into a three by three by three grid, and remove the middle cube and the six cubes in the middle of the faces.
Repeat with each of the twenty small cubes left, and keep going forever.
The result is a sponge with tunnels at every scale.
It has no volume and it is made of curves only, yet every curve one can imagine fits inside it.
