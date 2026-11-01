---
records:
    - id: RZP28ERRZV
      kind: textbook
      title: An Infinitely Large Napkin
      creators:
        - name: Evan Chen
          role: author
      date: "2026-10-23"
      msc:
        - code: 00-01
          from: napkin
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2026-10-23"
          structure: RZP28ERRZV/e1.json
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: napkin
          snapshot: blake3:4ed6a8681091f1982528026e06219208d001f9656231cf988d38e9d48cb24fc5
          native_id: napkin
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: from deferred to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
