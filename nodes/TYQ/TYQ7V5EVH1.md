---
tag: TYQ7V5EVH1
kind: concept
name: Relay channel
msc: [94A40, 94A24, 94A05]
specializes: [B9C5RBFATB]
sources:
  - url: https://en.wikipedia.org/wiki/Relay_channel
same_as:
  wikidata: Q7310895
  wikipedia: Relay channel
---

## Summary

A relay channel is a three-terminal [[channel|B9C5RBFATB]]: a sender, a receiver, and a relay that listens to the sender and transmits to help the receiver.
It is the simplest model of cooperative communication in a network.
Its [[capacity|J7MZ2XQP9M]] is unknown in general, but it is known in special cases such as the physically degraded relay channel.
See the [[definition|E48WEP7RT7]].

## Explanations

### L1 human

Picture a phone far from a cell tower, with a second device halfway between them.
The middle device hears the phone's signal, processes it, and sends its own signal toward the tower to help.
The relay has no message of its own; it only helps the sender's message get through.
The main question is how fast the sender can communicate when the relay helps in the best possible way.
