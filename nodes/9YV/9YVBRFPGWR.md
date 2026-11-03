---
tag: 9YVBRFPGWR
kind: example
name: Szilard engine
msc: [80A05, 82B30, 94A17]
illustrates: [HABM6R27XZ]
uses: [ZPCGW6FGB0, C9MM7GFRWN, N7R0H2VNDJ, T11MGWEKJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Entropy_in_thermodynamics_and_information_theory
---

## Example

The *Szilard engine* is a thought experiment of Leo Szilard that makes [[Maxwell's demon|HABM6R27XZ]] concrete.
A single gas molecule moves in a box of volume $V$ in contact with a heat bath at temperature $T$.

1. A partition is inserted in the middle, so the molecule is in the left or the right half, each with probability $1/2$.
2. A demon measures which half holds the molecule and records the result as one bit.
3. Using the result, it attaches a load to the correct side. The molecule pushes the partition as a piston in an [[isothermal|C9MM7GFRWN]] expansion from $V/2$ to $V$.
4. The partition is removed, and the box is back in its initial state.

Treat the one molecule as an [[ideal gas|N7R0H2VNDJ]] with $pV = k_B T$.
The work done in step 3 is
$$W = \int_{V/2}^{V} \frac{k_B T}{V'}\, dV' = k_B T \ln 2,$$
and it equals the heat taken from the bath.
So each cycle seems to turn heat from one bath fully into work, against the [[second law|T11MGWEKJ3]].

## Remarks

The cycle is not closed until the demon's one-bit memory is reset.
By [[Landauer's principle|ZPCGW6FGB0]], the reset releases at least $k_B T \ln 2$ of heat to the bath, which cancels the gain of step 3.
So the net work per full cycle is at most $0$, and the second law holds.

## Explanations

### L1 human

Trap one molecule in a box and find out which half it is in.
With that one bit of knowledge, one can let the molecule push a piston and get a little work, $k_B T \ln 2$, from the heat of the surroundings.
Paying back for the bit, by erasing it, costs at least the same amount, so there is no free lunch.
