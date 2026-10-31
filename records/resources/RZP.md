---
records:
    - id: RZP28ERRZV
      kind: textbook
      title: An Infinitely Large Napkin
      creators:
        - name: Evan Chen
          role: author
      expressions:
        - key: e1
          kind: edition
          structure: RZP28ERRZV/e1.json
      scope:
        value: deferred
        until: "2027-01-29"
        reason: no test decides the record, and the classifier has no model
        by: m2 v0.6.2 scope/1
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
---
