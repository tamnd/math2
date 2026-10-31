---
records:
    - id: 1SB0999M38
      kind: monograph
      title: Harmonic Function Theory
      creators:
        - name: Sheldon Axler
          role: author
        - name: Paul Bourdon
          role: author
        - name: Wade Ramey
          role: author
      date: "1992"
      expressions:
        - key: e1
          kind: edition
          date: "1992"
          ids:
            doi:
                - 10.1007/978-1-4757-8137-3
                - 10.1007/b97238
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2001"
              ids:
                isbn:
                    - "9781441929112"
                    - "9781475781373"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1992"
              ids:
                isbn:
                    - "9781489911865"
                    - "9780387215273"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-8137-3
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/b97238
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
