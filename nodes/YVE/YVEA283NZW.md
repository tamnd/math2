---
tag: YVEA283NZW
kind: object
name: Mersenne Twister
msc: [65C10, 11K45]
instance_of: [C5FG6ARWVV]
sources:
  - url: https://en.wikipedia.org/wiki/Mersenne_Twister
same_as:
  wikidata: Q1196406
  wikipedia: Mersenne Twister
---

## Description

The Mersenne Twister is a [[pseudorandom number generator|C5FG6ARWVV]] designed by Makoto Matsumoto and Takuji Nishimura.
Its standard version, MT19937, works with $32$-bit words.
Its state is an array of $624$ words, that is $19\,968$ bits, of which $19\,937$ bits are effective.
The transition function is linear over the [[field with two elements|0ZXZ82FTX2]] $\F_2$.
It combines three words of the array by shifts, masks and exclusive or, in a twisted generalised feedback shift register recurrence.
The output function applies a fixed invertible linear map, the tempering, to the newest word.
It fits the definition of a generator: the state space is finite, and the transition and output are fixed maps.
The seed determines the initial array.
Its period is $2^{19937} - 1$, which is a [[Mersenne prime|0F3Z22M2GT]]; this is where the name comes from.
Its outputs are $623$-dimensionally equidistributed to $32$-bit accuracy.
That is, over a full period every $623$-tuple of consecutive $32$-bit outputs occurs equally often, except that the all-zero tuple occurs once less.

## Remarks

Because the generator is linear over $\F_2$, $624$ consecutive outputs determine the whole state, so all later outputs can be predicted.
It is therefore not suitable for cryptography.
Linearity also makes it fail some statistical tests based on linear complexity, although these rarely matter in simulation.
The large state means it can take many steps to recover from a seed with mostly zero bits.

## Explanations

### L1 human

The Mersenne Twister is the default random number generator of many programming languages and libraries, for example in Python.
It keeps a large hidden table of bits and stirs it with cheap bit operations at each step.
The sequence repeats only after $2^{19937} - 1$ outputs, a number with about $6000$ decimal digits, so no computation will ever see it repeat.
It is fast and statistically good for simulations, but a clever observer who sees enough outputs can predict the rest.
